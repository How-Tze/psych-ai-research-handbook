"""Create the two handbook teaching figures from explicit CSV inputs.

Run after run_analysis.py --output reference.
Requires requirements-analysis.txt and matplotlib==3.11.2.
Use --input to select an analysis output directory; defaults to reference/.
"""
import argparse
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd
from scipy.special import ndtri

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=ROOT / "reference")
    parser.add_argument("--output", type=Path, default=ROOT / "figures")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    available = {f.name for f in font_manager.fontManager.ttflist}
    font = next((name for name in ("Microsoft YaHei", "Noto Sans CJK SC", "SimHei")
                 if name in available), None)
    if font is None:
        raise RuntimeError("Install a Chinese font: Microsoft YaHei, Noto Sans CJK SC, or SimHei")
    six = pd.read_csv(ROOT / "method-six-rows.csv")
    diagnostic_path = args.input / "diary-diagnostics.csv"
    diagnostic = pd.read_csv(diagnostic_path)
    assert len(six) == 6 and len(diagnostic) == 840
    style = {"font.family": font, "font.size": 10, "axes.titlesize": 11,
             "axes.spines.top": False, "axes.spines.right": False,
             "axes.unicode_minus": False, "figure.facecolor": "white",
             "axes.facecolor": "white", "text.color": "#222222",
             "axes.labelcolor": "#222222", "savefig.facecolor": "white"}
    with plt.rc_context(style):
        fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.5), layout="constrained")
        means = []
        for person, color, marker in (("A", "#006699", "o"), ("B", "#A64B00", "^")):
            part = six[six.id == person]
            axes[0].plot(part.stress, part.sleep_difficulty, marker=marker,
                         color=color, label=f"{person}：3天", linewidth=1.6, markersize=6)
            mx, my = part.stress.mean(), part.sleep_difficulty.mean()
            means.append((mx, my))
            axes[1].scatter(mx, my, marker=marker, color=color, s=60)
            axes[1].annotate(person, (mx, my), xytext=(8, -1), textcoords="offset points")
        axes[1].plot(*zip(*means), color="#555555", linestyle="--", linewidth=1.3, zorder=0)
        axes[0].set_title("A  同一个人的变化")
        axes[1].set_title("B  两个人的均值")
        axes[0].legend(frameon=False, loc="upper left")
        for ax in axes:
            ax.set(xlim=(0.5, 6.5), ylim=(1.5, 7.5), xlabel="压力（教学单位）",
                   ylabel="睡眠困难（教学单位）")
            ax.set_aspect("equal")
        fig.savefig(args.output / "within-between.png", dpi=300)
        plt.close(fig)

        fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.5), layout="constrained")
        residual = diagnostic.residual_conditional.to_numpy()
        axes[0].scatter(diagnostic.fitted_conditional, residual, s=8,
                        color="#006699", alpha=0.85, edgecolors="none")
        axes[0].axhline(0, color="#333333", linewidth=1, linestyle="--")
        axes[0].set(title="A  条件残差与拟合值", xlabel="条件拟合值", ylabel="条件残差")
        theoretical = ndtri((np.arange(1, len(residual) + 1) - 0.5) / len(residual))
        ordered = np.sort(residual)
        axes[1].scatter(theoretical, ordered, s=8, color="#006699", alpha=0.85, edgecolors="none")
        rq1, rq3 = np.quantile(residual, [0.25, 0.75])
        tq1, tq3 = ndtri([0.25, 0.75])
        slope = (rq3 - rq1) / (tq3 - tq1)
        intercept = rq1 - slope * tq1
        axes[1].plot(theoretical[[0, -1]], intercept + slope * theoretical[[0, -1]],
                     color="#333333", linewidth=1, linestyle="--")
        axes[1].set(title="B  正态分位数图", xlabel="标准正态理论分位数", ylabel="条件残差分位数")
        fig.savefig(args.output / "diary-diagnostics.png", dpi=300)
        plt.close(fig)
    manifest = {
        "purpose": "Chinese handbook web teaching figures; no journal submission target",
        "matplotlib": matplotlib.__version__, "font": font, "dpi": 300,
        "within_between": {"source": "method-six-rows.csv", "rows": 6, "people": 2,
            "transformation": "raw points and arithmetic person means; no uncertainty inference",
            "excluded": 0, "missing": 0, "size_inches": [7.2, 3.5]},
        "diagnostics": {"source": "reference/diary-diagnostics.csv", "rows": 840, "people": 60,
            "transformation": "conditional residuals; normal quantiles (rank-.5)/n; quartile reference line",
            "excluded": 0, "missing": 0, "uncertainty": "none shown", "size_inches": [7.6, 3.5]},
        "input_sha256": {"method-six-rows.csv": hashlib.sha256((ROOT / "method-six-rows.csv").read_bytes()).hexdigest(),
                         "diary-diagnostics.csv": hashlib.sha256(diagnostic_path.read_bytes()).hexdigest()},
    }
    (args.output / "provenance.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("Two figures generated; no rows removed; provenance saved.")


if __name__ == "__main__":
    main()
