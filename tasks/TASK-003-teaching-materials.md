# TASK: 三个可检查的教学案例

- **TASK ID:** TASK-003
- **STATUS:** DONE
- **PHASE:** v1.3 capability teaching preparation
- **OWNER / EXECUTOR:** Codex

## CONTEXT
原第6章提到 24 行合成数据、21 对 15 人的筛选差异，仓库缺少对应输入和代码。本轮审查要求从原则进入真实能力练习。

## OBJECTIVE
提供分析规格、实验材料与质性反思三类可供作者深化的教学输入。

## IN SCOPE
新建 examples/v1.3/：A 为新构造的 24 行计分案例，B 为实验列表平衡案例，C 为合成访谈片段与分析立场比较。可写必要教学说明和参考程序。

## OUT OF SCOPE
不修改正式章节，不用真实被试数据，不假定历史缺失材料已被找回，不把模拟结果称为实证结论。

## DELIVERABLES
输入、规格、参考答案/检查标准和离线验证；R 示例若环境不可用应明确未运行。

## ACCEPTANCE CRITERIA
A：24 行，正确规则保留21、错误规则保留15；反向分哨兵及模型公式分别检查。B：每份列表条件均衡、每刺激跨列表换条件。C：区分代码本式整理与反思性解释；不把跨模型一致率作为通用质量标准。

## CONSTRAINTS
新材料标明创建日期及合成属性。临时产物在 .qa/；已发布 release/ 不变。

## DEPENDENCIES
2026-10-13 用户批准的审查方案。

## ESCALATION CONDITIONS
需要真实数据、额外实证主张或公开替换正文时，交 Authoring Gate。

## ON COMPLETION
记录实际验证及限制，进入 REVIEW，交 TASK-004 使用。

## COMPLETION EVIDENCE
2026-10-13：Python 离线检查通过。A 的样本21/15、反向分与公式偏差分别识别；B 两份列表均衡且各刺激跨条件；C 只检查输入结构，解释质量交作者判断。本包不拟合回归，不含未经执行的 R 分析。

2026-10-13：用户批准当前候选及 v1.3 写作方向，本准备任务验收完成；完整作者稿由 TASK-005 接续。
