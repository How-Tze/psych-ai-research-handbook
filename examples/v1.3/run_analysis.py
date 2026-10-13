"""Reproduce the v1.3 teaching results; all inputs are synthetic.

Usage: python run_analysis.py --output ./analysis-output
Requires requirements-analysis.txt. Writes only under the requested output folder.
"""
import argparse
import json
import platform
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
import statsmodels
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parent
SEED = 20261013


def score_survey(min_items):
    raw = pd.read_csv(ROOT / "survey24.csv")
    scored = raw[["id"]].copy()
    for scale in ("stress", "rum", "sleep"):
        items = raw[[f"{scale}{j}" for j in (1, 2, 3)]].copy()
        if scale == "rum":
            items["rum3"] = 6 - items["rum3"]
        scored[f"{scale}_mean"] = items.mean(axis=1).where(
            items.notna().sum(axis=1) >= min_items
        )
    return scored.dropna().reset_index(drop=True)


def survey_analysis():
    main = score_survey(2)
    complete = score_survey(3)
    assert main.id.tolist() == [f"S{i:02}" for i in range(1, 22)]
    assert complete.id.tolist() == [f"S{i:02}" for i in range(1, 16)]
    assert np.isclose(main.loc[0, "rum_mean"], 10 / 3)
    rows = []
    for label, data in (("at_least_two", main), ("all_three", complete)):
        fitted = smf.ols("sleep_mean ~ stress_mean + rum_mean", data=data).fit()
        # Independent linear-algebra check of the formula-based implementation.
        design = np.column_stack([np.ones(len(data)), data.stress_mean, data.rum_mean])
        assert np.linalg.matrix_rank(design) == 3
        reference = np.linalg.lstsq(design, data.sleep_mean, rcond=None)[0]
        assert np.allclose(reference, fitted.params.values)
        rows.append({"rule": label, "n": len(data), **fitted.params.to_dict()})
    return main, pd.DataFrame(rows)


def generate_diary():
    rng = np.random.default_rng(SEED)
    rows = []
    for person in range(1, 61):
        mu = rng.normal(5, 1.5)
        intercept = rng.normal(0, 0.8)
        within = rng.normal(0, 1, 14)
        within -= within.mean()
        error = rng.normal(0, 0.7, 14)
        for day in range(14):
            rows.append({
                "id": f"P{person:02}", "day": day + 1,
                "stress_index": mu + within[day],
                "sleep_index": 6 + 0.8 * (mu - 5) - 0.6 * within[day]
                + intercept + error[day],
            })
    data = pd.DataFrame(rows)
    data["stress_mean"] = data.groupby("id").stress_index.transform("mean")
    data["stress_within"] = data.stress_index - data.stress_mean
    data["stress_between"] = data.stress_mean - 5
    return data


def diary_analysis(data):
    assert len(data) == 840 and data.id.nunique() == 60
    assert data.groupby("id").size().eq(14).all()
    assert np.allclose(data.groupby("id").stress_within.mean(), 0, atol=1e-12)
    pooled = smf.ols("sleep_index ~ stress_index", data=data).fit()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        mixed = smf.mixedlm(
            "sleep_index ~ stress_within + stress_between", data=data,
            groups=data["id"], re_formula="1"
        ).fit(reml=True, method="lbfgs")
    if not mixed.converged:
        raise RuntimeError("Mixed model did not converge; do not publish reference values.")
    # Balanced data: a person-demeaned OLS slope provides an independent check
    # of the within-person fixed slope in this random-intercept model.
    centered_y = data.sleep_index - data.groupby("id").sleep_index.transform("mean")
    within_reference = np.dot(data.stress_within, centered_y) / np.dot(
        data.stress_within, data.stress_within
    )
    assert np.isclose(mixed.fe_params["stress_within"], within_reference, atol=1e-7)
    ci = mixed.conf_int()
    coefficients = [{"model": "pooled_OLS", "term": "stress_index",
                     "estimate": float(pooled.params["stress_index"]),
                     "ci_low": None, "ci_high": None}]
    for term in mixed.fe_params.index:
        coefficients.append({"model": "random_intercept_REML", "term": term,
            "estimate": float(mixed.fe_params[term]),
            "ci_low": float(ci.loc[term, 0]), "ci_high": float(ci.loc[term, 1])})
    diagnostics = data[["id", "day", "stress_within", "stress_between"]].copy()
    diagnostics["fitted_conditional"] = mixed.fittedvalues
    diagnostics["residual_conditional"] = mixed.resid
    previous = diagnostics.groupby("id").residual_conditional.shift(1)
    valid = previous.notna()
    summary = {
        "n_observations": len(data), "n_people": int(data.id.nunique()),
        "days_each": 14, "converged": bool(mixed.converged),
        "random_intercept_variance": float(mixed.cov_re.iloc[0, 0]),
        "residual_variance": float(mixed.scale),
        "conditional_rmse": float(np.sqrt(np.mean(mixed.resid ** 2))),
        "pooled_lag1_residual_correlation": float(np.corrcoef(
            previous[valid], diagnostics.loc[valid, "residual_conditional"])[0, 1]),
        "warnings": [str(w.message) for w in caught],
        "interval_method": "pointwise asymptotic normal 95% Wald intervals",
        "estimation": "REML, random intercept, common within-person slope",
    }
    return pd.DataFrame(coefficients), diagnostics, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    scored, sensitivity = survey_analysis()
    diary = generate_diary()
    coefficients, diagnostics, summary = diary_analysis(diary)
    for name, frame in (("survey-scored", scored), ("survey-sensitivity", sensitivity),
                        ("diary-synthetic", diary), ("diary-coefficients", coefficients),
                        ("diary-diagnostics", diagnostics)):
        frame.to_csv(args.output / f"{name}.csv", index=False, float_format="%.10f")
    metadata = {
        "purpose": "Synthetic worked example; one realization, not a power simulation or empirical finding",
        "seed": SEED, "generator": "numpy default_rng / PCG64",
        "generation": {"people": 60, "days": 14, "person_mean_mean": 5,
                       "person_mean_sd": 1.5, "intercept": 6, "between_slope": 0.8,
                       "within_slope": -0.6, "random_intercept_sd": 0.8,
                       "error_sd": 0.7, "within_raw_sd": 1,
                       "within_centered_per_person": True, "missing": False,
                       "time_trend": False, "serially_correlated_errors": False},
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "pandas": pd.__version__, "scipy": scipy.__version__,
                     "statsmodels": statsmodels.__version__},
        "diary_model": summary,
    }
    (args.output / "analysis-metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(sensitivity.to_string(index=False))
    print(coefficients.to_string(index=False))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
