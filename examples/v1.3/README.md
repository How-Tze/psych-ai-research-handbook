# v1.3 教学材料准备包

创建于 2026-10-13；全部数据、情境和访谈均为本轮新构造的合成材料。不是原第6章缺失附件的“恢复”，不是实际研究发现，未纳入当前公开 v1.2。

- A：analysis-spec.md、survey24.csv、check_cases.py。学习识别样本、计分和公式的变化；check_cases.py本身不拟合回归。作者阶段新增的实际分析见下方运行包。
- B：experiment-spec.md、counterbalance.csv。学习把实验设计转成可检查的材料列表。
- C：qualitative-spec.md、synthetic-interviews.csv。学习在不同分析立场下使用 AI，保留歧义和研究者解释责任。

运行：Python 3.10+ 下，在本目录执行 `python check_cases.py`。它只读取文件，输出检查结果，不联网、不修改输入、不写正式分析结果。人工参考检查与可运行断言分开记录，不能把断言通过等同于方法有效。

这批材料服务于 briefs/v1.3-authoring-package.md；正式教学正文需通过 Authoring Gate。TASK-005已为案例 A 补入实际模型比较；案例 B 的平衡检查不证明操纵有效；案例 C 不设唯一正确主题。

## 作者阶段新增的完整分析

[分析运行包](analysis-worked-example.md)包含问卷计分与两种规则的回归、60人×14次合成纵向数据、随机截距模型、诊断及实际参考产物；[首批作者稿](../../drafts/v1.3/README.md)解释这些结果。图和参考结果是明确纳入教材的交付物，临时QA仍只放在.qa/。
