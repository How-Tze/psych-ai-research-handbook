"""Turn the handbook's checked survey results into a small teaching report.

Python standard library only. No model calls, statistical fitting or overwrites.
The main mode is a writing exercise, not a recommendation to omit comparisons.
"""

import argparse
import csv
import hashlib
import io
from decimal import Decimal, InvalidOperation
from pathlib import Path


RULES = {
    "at_least_two": "主规则：每个指标至少两题有效",
    "all_three": "比较规则：每个指标三题全部有效",
}


def read_results(source):
    raw = source.read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    required = {"rule", "n", "Intercept", "stress_mean", "rum_mean"}
    if not required.issubset(reader.fieldnames or []):
        raise ValueError("输入表缺少本例要求的字段。请检查文件，不要猜测列名。")
    rows = {}
    for row in reader:
        rule = row["rule"]
        if rule not in RULES or rule in rows:
            raise ValueError("规则名称未知或重复。请先核对输入表。")
        n = Decimal(row["n"])
        if not n.is_finite() or n <= 0 or n != n.to_integral_value():
            raise ValueError("记录数必须是正整数。")
        numbers = {name: Decimal(row[name]) for name in ("Intercept", "stress_mean", "rum_mean")}
        if not all(value.is_finite() for value in numbers.values()):
            raise ValueError("系数含缺失或非有限数值。")
        rows[rule] = {"n": int(n), **numbers}
    if set(rows) != set(RULES):
        raise ValueError("本教学输入应同时含两种规则，缺少结果时应先核对分析。")
    return rows, hashlib.sha256(raw).hexdigest()


def render(rows, digest, mode):
    selected = ["at_least_two"] if mode == "main" else list(RULES)
    lines = [
        "# 由已核对结果生成的数字稿", "",
        "本文件来自合成教学数据，只整理已有计算，不重新拟合模型，也不生成科学解释。", "",
        "| 计分规则 | 纳入记录数 | 压力系数 | 反刍系数 |",
        "|---|---:|---:|---:|",
    ]
    for rule in selected:
        r = rows[rule]
        lines.append(f"| {RULES[rule]} | {r['n']} | {r['stress_mean']:.3f} | {r['rum_mean']:.3f} |")
    main = rows["at_least_two"]
    lines += ["", "## 可以继续编辑的数字描述", "",
              f"按主规则纳入 {main['n']} 条记录，压力系数为 {main['stress_mean']:.3f}，反刍系数为 {main['rum_mean']:.3f}。"]
    if mode == "compare":
        other = rows["all_three"]
        lines += [f"按三题全部有效的比较规则纳入 {other['n']} 条记录，压力系数为 {other['stress_mean']:.3f}，反刍系数为 {other['rum_mean']:.3f}。"]
    else:
        lines += ["", "这一轮只练习主分析片段。源文件已有比较结果，完整报告还需按研究问题和约定处理相关分析，不能按结果喜好取舍。"]
    lines += ["", "## 本次使用的输入", "",
              "- 来源文件：survey-sensitivity.csv（本手册规定格式）。",
              f"- 报告模式：{mode}。",
              "- 展示精度：系数保留三位小数。",
              f"- 实际读取文件的 SHA-256：{digest}", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--mode", required=True, choices=("main", "compare"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        rows, digest = read_results(args.source)
        content = render(rows, digest, args.mode)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    except FileExistsError:
        parser.exit(2, "输出已存在，请选择新的文件名；本脚本不会覆盖旧稿。\n")
    except (OSError, UnicodeError, ValueError, InvalidOperation, TypeError) as error:
        parser.exit(2, f"未完成报告生成：{error}\n")
    print(f"已生成 {args.output.name}；请继续检查解释和报告范围。")


if __name__ == "__main__":
    main()
