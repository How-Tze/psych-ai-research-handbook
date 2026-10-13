# v1.3 教学材料准备包

创建于 2026-10-13；全部数据、情境和访谈均为本轮新构造的合成材料。不是原第6章缺失附件的“恢复”，不是实际研究发现，未纳入当前公开 v1.2。

- A：analysis-spec.md、survey24.csv、check_cases.py。学习识别样本、计分和公式的变化；程序不拟合回归，也不报告虚构推断统计。
- B：experiment-spec.md、counterbalance.csv。学习把实验设计转成可检查的材料列表。
- C：qualitative-spec.md、synthetic-interviews.csv。学习在不同分析立场下使用 AI，保留歧义和研究者解释责任。

运行：Python 3.10+ 下，在本目录执行 `python check_cases.py`。它只读取文件，输出检查结果，不联网、不修改输入、不写正式分析结果。人工参考检查与可运行断言分开记录，不能把断言通过等同于方法有效。

这批材料服务于 briefs/v1.3-authoring-package.md；正式教学正文需通过 Authoring Gate。案例 A 在纠错之外，应由作者补入“AI 帮助比较分析选择”的正面示范；案例 B 的平衡检查不证明操纵有效；案例 C 不设唯一正确主题。
