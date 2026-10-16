"""Read-only specification checks for synthetic teaching materials."""
import csv
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
FORMULA = "sleep_mean ~ stress_mean + rum_mean"


def load(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def score(rows, complete_only=False, reverse_top=6):
    scored = {}
    for row in rows:
        items = [row[f"{scale}{j}"] for scale in ("stress", "rum", "sleep")
                 for j in range(1, 4)]
        if complete_only and not all(items):
            continue
        scales = {}
        for scale in ("stress", "rum", "sleep"):
            values = []
            for j in range(1, 4):
                raw = row[f"{scale}{j}"]
                if raw:
                    value = float(raw)
                    if scale == "rum" and j == 3:
                        value = reverse_top - value
                    values.append(value)
            if len(values) >= 2:
                scales[scale + "_mean"] = mean(values)
        if len(scales) == 3:
            scored[row["id"]] = scales
    return scored


def violations(scored, formula):
    errors = []
    if set(scored) != {f"S{i:02}" for i in range(1, 22)}:
        errors.append("sample")
    if abs(scored.get("S01", {}).get("rum_mean", -999) - 10 / 3) > 1e-10:
        errors.append("reverse_score")
    if formula != FORMULA:
        errors.append("formula")
    return errors


def main():
    survey = load("survey24.csv")
    assert len(survey) == 24 and len({r["id"] for r in survey}) == 24
    correct = score(survey)
    faulty = score(survey, complete_only=True, reverse_top=5)
    assert len(correct) == 21 and len(faulty) == 15
    assert violations(correct, FORMULA) == []
    assert violations(faulty, FORMULA + " + age") == ["sample", "reverse_score", "formula"]
    assert violations(score(survey, complete_only=True), FORMULA) == ["sample"]
    assert violations(score(survey, reverse_top=5), FORMULA) == ["reverse_score"]
    assert violations(correct, FORMULA + " + age") == ["formula"]
    print("A PASS: 24 inputs; correct N=21; faulty N=15; three deviations detected independently.")
    experiment = load("counterbalance.csv")
    assert len(experiment) == 16
    for name in ("L1", "L2"):
        group = [r for r in experiment if r["list"] == name]
        assert len(group) == 8
        assert {int(r["trial"]) for r in group} == set(range(1, 9))
        assert len({r["stimulus"] for r in group}) == 8
        assert sum(r["condition"] == "quiet" for r in group) == 4
        assert sum(r["condition"] == "noise" for r in group) == 4
    for stimulus in {r["stimulus"] for r in experiment}:
        assert {r["condition"] for r in experiment if r["stimulus"] == stimulus} == {"quiet", "noise"}
    print("B PASS: two lists, eight unique stimuli each; 4/4 conditions; every stimulus crosses conditions.")
    excerpts = load("synthetic-interviews.csv")
    assert len(excerpts) == 6 and len({r["id"] for r in excerpts}) == 6
    assert {r["speaker"] for r in excerpts} == {"P1", "P2"}
    print("C INPUT CHECK ONLY: six synthetic excerpts; interpretation requires human review.")


if __name__ == "__main__":
    main()
