# TASK-001 Authoring Packet

For Strategic / Authoring Chat. This packet reproduces current repository sources; it does not contain a draft of §9.5. Source text is verbatim, with line endings normalized to LF and enclosing fences added for separation.

## Source inventory

- `tasks/TASK-001-writing-brief.md`: complete current Writing Brief.
- `chapters/10-automation.qmd`: complete current Chapter 9.
- `chapters/09-maintenance.qmd`: §8.1–§8.3 only.
- `chapters/11-safety-recovery.qmd`: §10.1–§10.4 only.
- `chapters/03-work-environment.qmd`: two terminology excerpts from §2.1 only.

## Exact current Chapter 9 headings and insertion position

The headings and application label below retain their current source wording and order:

~~~~text
# 第9章 固定重复工作：任务说明、脚本与 Agent
## 9.1 一条自然升级路径
## 9.2 什么时候值得进一步封装或自动化
## 9.3 Agent 只在需要跨步骤行动时出现
## 案例A：把“结果—正文一致性检查”固定下来
## 9.4 什么时候不要自动化
本章应用：判断一个重复任务应该停在哪一层
~~~~

Insert the proposed `## 9.5` **between current lines 57 and 59**: after the last §9.4 bullet and before the chapter application. No §9.5 text exists yet. The exact boundary is:

~~~~text
- 维护权限、版本和依赖的成本大于节省的劳动。

本章应用：判断一个重复任务应该停在哪一层

~~~~

## Full current TASK-001 Writing Brief — verbatim

Source: `tasks/TASK-001-writing-brief.md`.

~~~~text
# TASK-001 Writing Brief — v1.2 multi-agent research workflows

**Purpose:** Authoring Gate package for Strategic / Authoring Chat. This is a planning brief, not reader-facing handbook prose. The target version is v1.2; v1.1 chapters, release assets, site labels, and release metadata remain untouched in this phase.

## 1. Precise content integration map

**Primary target:** [Chapter 9, `chapters/10-automation.qmd`](../chapters/10-automation.qmd), a new `## 9.5` section. Insert it **after the final bullet of §9.4** (“维护权限、版本和依赖的成本大于节省的劳动。”) and **before** “本章应用：判断一个重复任务应该停在哪一层” (currently lines 57–59). Retain the existing §9.1–9.4 and Case A order. The new section extends the decision path from one bounded Agent to coordinated agents; it must not make multi-agent use the default endpoint of the automation ladder.

| Location | What the existing text establishes | Planned relationship |
| --- | --- | --- |
| [Chapter 1, §1.1–1.3](../chapters/02-project.qmd) | Research materials, decisions, and versions form a project; the researcher must identify current valid state. | Background only; do not restate six project questions. |
| [Chapter 2, §2.1](../chapters/03-work-environment.qmd) | Model, Tool, Harness, and Agent have distinct functions; permissions and visible material shape behavior. | Use its definitions; distinguish model capability from agent execution, without another full glossary. |
| [Chapter 3, §3.2](../chapters/04-quick-start.qmd) | A one-time task description has goal, input, output, prohibitions, and check basis. | Extend to durable task specifications for repeatable/consequential coordinated work; do not duplicate the five-item prompt lesson. |
| [Chapter 8, §8.1–8.3](../chapters/09-maintenance.qmd) | Project entry, protected originals, decisions, and handoff preserve current state outside chat. | Treat as prerequisite for multi-agent coordination; no second project-folder tutorial. |
| [Chapter 9, §9.1–9.4](../chapters/10-automation.qmd) | Progressive choice of prompt, SOP, script, Skill, Agent; agents require boundaries; automation may be inappropriate. | New §9.5 explains coordination only after this suitability test. |
| [Chapter 10, §10.1–10.4](../chapters/11-safety-recovery.qmd) | Risk-based controls, five quality activities, researcher decisions, and least privilege. | Apply existing safeguards to multiple agents; do not repeat the risk table or decision-rights list. |
| [Appendix B](../chapters/appendix-b.qmd) | Minimal project entry and handoff fields. | Keep the new task-spec example distinct from a project handoff template. |

**Preceding text:** §9.4 lists six reasons to avoid automation, ending with permissions/version/dependency maintenance costs exceeding saved labor. The new section should begin from that threshold: coordination is justified only where tasks are bounded, separable, checkable, and worth the overhead. This is an outline instruction, not proposed reader-facing wording.

**Following text:** The existing chapter application asks readers to choose a repeated task, specify inputs, outputs, failures, and human checkpoints, and stop at the simplest adequate layer. The new section must lead back to that exercise. Strategic / Authoring Chat should decide whether the application needs a small v1.2 extension to cover coordination; no application edit is authorized in this preparation phase.

## 2. Recommended section structure and length

Target **about 1,000–1,300 Chinese characters** of main text, including a compact five- to seven-line task-spec example, across one `## 9.5` section with at most four short `###` subsections. This keeps Chapter 9 usable as an introductory chapter rather than a multi-agent operations manual.

| Proposed subsection | Coverage | Approximate budget |
| --- | --- | --- |
| `9.5.1 先按任务风险选择模型与执行方式` | Capability versus risk/cost; model versus Agent/Harness; no fixed tier hierarchy. | 180–250 characters |
| `9.5.2 让项目状态和任务规格承载协作` | Canonical project state outside chat; sensitive-data boundary; phase and task specification; compact example. | 300–400 characters |
| `9.5.3 并行执行与升级边界` | Low-coupling parallel work, elapsed time versus total compute, execution versus strategic questions, Chat mediation bottleneck. | 300–400 characters |
| `9.5.4 人的决定权与复核` | Researcher direction and acceptance; strategic review; cross-agent check without false independence claims; return to chapter application. | 180–250 characters |

The four headings and allocations are an authoring outline, not approved prose. If space is tight, combine the last two subsections; preserve the task example and escalation logic.

## 3. Required conceptual decisions

- **Model selection:** Match capability and available controls to error consequences, ambiguity, and review cost. Avoid “always use the strongest” and any permanent vendor tier ordering.
- **Model / Harness / Agent:** A model reasons or generates; the Harness determines tools, context, permissions, records, and stopping; an Agent acts across steps within those boundaries. Multiple agents are a coordination choice, not a new model type.
- **Project state:** Confirmed decisions, current valid inputs/outputs, and unresolved issues need durable project locations. Repository files can be canonical for governance and non-sensitive specifications, while protected data may live elsewhere with controlled references.
- **Parallel work:** Independence and low coupling matter. Parallel agents can reduce elapsed time where tasks overlap in time; they can add compute and coordination cost. Avoid a universal recommended agent count.
- **Governance:** A phase sets goal, scope, acceptance, decision gates, and escalation. A tracked task turns consequential work into a reusable specification. Execution agents resolve routine execution questions; strategic questions return to the human and Strategic / Authoring Chat.
- **Responsibility and review:** Humans retain scientific, ethical, editorial, publication, and acceptance decisions. Cross-agent review can provide an additional check, but shared models, inputs, or assumptions can correlate errors.

The example task specification should use a familiar psychology/social-science activity, such as a **read-only results-to-manuscript consistency check** using confirmed tables and draft text. It should show task objective, allowed inputs, output, acceptance check, prohibited changes, and an escalation trigger. It must not invent new findings or silently turn a check into an automatic manuscript rewrite.

## 4. Duplication and conflict audit

| Existing material | Duplication or conflict risk | Authoring instruction |
| --- | --- | --- |
| Chapter 2 §2.1 and Chapter 9 §9.3 | Re-teaching the Model/Tool/Harness/Agent glossary. | Refer briefly to the established distinction; add only the coordination consequence. |
| Chapter 3 §3.2 and Chapter 9 §9.1 | A task spec may sound like a longer one-time Prompt. | Explain durable ownership, acceptance, dependencies, and escalation, using one compact example. |
| Chapter 8 §8.1–8.3 and Appendix B | “Repository as source of truth” may be misread as moving all project material, including restricted data, into Git. | Refer to confirmed state and controlled pointers; preserve protected-original and data-location guidance. |
| Chapter 9 §9.4 and Chapter 2 closing advice | A new multi-agent section may imply more agents are inherently more mature. | Keep the existing suitability and non-automation tests as prerequisites. |
| Chapter 10 §10.1–10.4 and Chapter 7 §7.2 | Repeating risk tables, researcher decision lists, or treating a second agent's agreement as independent evidence. | Give only the escalation/acceptance consequence and distinguish cross-agent review from source-level independent verification. |
| Chapter 9 closing application | Current exercise ends at choosing the simplest layer and may seem to omit phase coordination after a new §9.5. | Connect the new section back to the exercise; consider a small approved application extension at the drafting gate. |
| Site homepage and v1.1 labels | Integrating v1.2 substantive text while the site still labels itself v1.1 would create a publication conflict. | Decide versioned site/source/release presentation before any integration; do not create metadata in this phase. |

No substantive contradiction was found in the existing chapters. The new section should add **coordination and governance**, not replace their existing project, agent, or verification explanations.

## 5. Stable versus dynamic claim map

| Stable handbook material | Dynamic Start Guide material or dated optional example |
| --- | --- |
| Choose capability and oversight according to task risk, ambiguity, cost, and reversibility. | Current model rankings, tier names, benchmark standings, token prices, subscription tactics. |
| Separate model capability from tools, Harness, permissions, and Agent behavior. | Current product UI, API setup, exact context/memory behavior, available agent features. |
| Keep confirmed project state and task acceptance criteria in durable, reviewable locations, with protected data outside inappropriate Git locations. | How a particular vendor's project memory, connectors, workspaces, or file sync work today. |
| Parallelism is conditional on task separability and may trade latency for coordination/compute. | Current service concurrency limits, quotas, pricing, or claims that a specific platform is fastest. |
| Phase governance separates routine execution from strategic escalation; humans retain consequential decisions. | Current orchestration products, buttons, subscription workarounds, or vendor-specific role matrices. |
| Independent verification returns to distinct evidence or methods; another agent can be a useful extra check. | Claims that a named model pairing has a measured review advantage without dated evidence. |

Any optional product illustration must be dated, sourced to current official documentation, clearly dispensable from the argument, and preferably maintained in the Start Guide.

## 6. Claims needing factual verification before drafting or publication

| Potential claim | Required check or safer treatment |
| --- | --- |
| Quantified time, quality, or cost gains from multi-agent work | Require study or reproducible benchmark with task type, setup, denominator, and date; otherwise frame as a conditional workflow trade-off. |
| One model class is cheaper, better at planning, or safer than another | Verify dated prices/capabilities and scope; omit from the stable section where possible. |
| Current tools support parallel agents, shared context, memory, or specific permission controls | Check official product documentation at publication time; move operational details to the Start Guide. |
| Cross-agent review is independent or improves scientific validity | Check evidence and reviewer/input overlap; describe an additional check, not guaranteed epistemic independence. |
| A fixed number of agents is optimal | Needs workload-specific evidence; do not state a universal optimum. |
| Git or any named platform is suitable for all research data | Check institutional, consent, ethics, security, and licensing rules for the actual project; retain a protected-data boundary. |
| A current journal or institution requires a particular AI disclosure or human sign-off | Recheck the applicable current policy if such a claim is introduced; no new policy claim is needed for this section. |

The structural argument about serial mediation and parallel scheduling may be explained as a conditional inference. Do not present it as a measured universal effect without evidence.

## 7. Terminology, wording risks, and reader background

- Use **执行性问题 / 战略性问题**, with plain examples. Define escalation through a change in research scope, methods, claims, or acceptance criteria; do not use unexplained production jargon.
- Preserve **项目（Project）/ 运行框架（Harness）/ 工作流（Workflow）** as distinct levels. Chapter 2 also uses `Project/Workspace` for a product environment; avoid treating that vendor-style workspace as the canonical scientific project.
- Use **研究者** for scientific judgment and acceptance; **Agent** for bounded action; **模型** for reasoning capability. Describe high-capability models functionally.
- Use **任务说明** for a one-off request and **任务规格** or **可追踪任务说明** for a durable, reviewable task asset; explain the added fields once.
- Avoid implying that all prompts belong in Git, that every task needs an agent, that parallelism saves total compute, or that model agreement equals evidence.
- Avoid a software-team-only vocabulary (for example sprint, ticket, CI, orchestrator) unless it is explained through a research example.
- Expected reader: psychology/social-science students, research assistants, and supervisors who have read Chapters 1–3 and 8–9; no Git, programming, or agent orchestration experience is assumed.

## 8. Recommended cross-references and gate handoff

1. **Primary text:** New Chapter 9 §9.5 may refer back once to Chapter 2 §2.1 for Harness and Chapter 8 §8.1–8.3 for confirmed state. Avoid repeated citations in every subsection.
2. **Optional Chapter 8 link:** A single pointer near §8.3 or its application could direct readers who coordinate several agents to Chapter 9 §9.5; add only if the author approves the cross-reference.
3. **Optional Chapter 10 link:** A single pointer near §10.2–10.3 could connect multi-agent review to independent evidence and researcher decision rights; keep the existing risk guidance intact.
4. **No new Chapter 1, Chapter 2, or Appendix B subsection** is recommended. Existing definitions and templates are sufficient.

**Authoring Gate request:** Strategic / Authoring Chat should review this map, settle the section/application boundary and any cross-references, then draft or review the substantial Chinese prose. The human must explicitly approve the draft. Only then may an execution agent mechanically integrate it in an authorized future phase and run Quarto/site QA. Version labels and release presentation need a separate decision before that integration.
~~~~

## Complete current Chapter 9 — verbatim

Source: `chapters/10-automation.qmd`.

~~~~text
# 第9章 固定重复工作：任务说明、脚本与 Agent

本章问题：什么时候应该继续人工协作，什么时候才值得把重复任务固定或自动化？

工作流通常先从真实任务开始。第一次用清楚的任务说明完成；第二、第三次发现输入、输出和检查方式都很相似，再把不变部分保存下来。

## 9.1 一条自然升级路径

一次人工完成 → 保存有效任务说明（Prompt）→ 多次使用后形成模板或 SOP → 确定性规则交给脚本 → 边界稳定的 AI 方法可以封装为 Skill → 只有确实需要根据中间状态跨步骤行动时才使用 Agent。

| **形式**           | **适合解决什么**                           | **不适合承担什么**         |
|--------------------|--------------------------------------------|----------------------------|
| 任务说明（Prompt） | 当前一次任务的目标、输入、输出和限制       | 整个项目的长期状态         |
| 模板 / SOP         | 重复任务中人与工具的协作顺序、交接和确认点 | 代替实际执行和研究证据     |
| 脚本               | 规则已经明确、每次都应一致执行的转换       | 规则未定时自行选择研究方法 |
| Skill              | 输入输出和检查方式较稳定的可复用 AI 方法   | 因为被封装就自动变得正确   |
| Agent              | 需要根据中间状态在文件或工具之间选择下一步 | 自行扩大权限或改变研究问题 |

## 9.2 什么时候值得进一步封装或自动化

1\. 任务已经真实重复出现；

2\. 方法和边界相对稳定；

3\. 输入和输出能够清楚描述；

4\. 常见失败和“不知道”能够表示；

5\. 可以设置检查方式和人工确认点；

6\. 复用确实减少不一致，而不是掩盖项目差异。

规则完全确定时，优先用脚本。若仍需要模型按一套稳定方法处理不同材料，可以考虑 Skill；任务需要根据中间结果选择下一步、跨文件或工具行动时，再考虑 Agent。“Skill”目前被多家 AI 平台用于指代可复用工作流或能力包，但具体格式、安装方式和可用范围并不相同；本书把它作为便于讨论的统称。封装能减少重复劳动，但不会自动增加方法效度。

## 9.3 Agent 只在需要跨步骤行动时出现

Agent 的区别不在于 Prompt 更长，而在于它会根据中间结果继续行动。只有当可见材料、权限、停止点和人工确认都能写清时，这种执行方式才值得采用。具体能力仍取决于第2章介绍的运行框架（Harness），权限按任务需要逐步增加。

::: {.callout-note appearance="simple" icon=false}
## 案例A：把“结果—正文一致性检查”固定下来

两轮修改都需要核对样本量、模型名称、系数、表图编号和因果措辞。研究者先保存一份检查任务说明，再形成固定表格模板。只有当项目能稳定提供结构化结果表和正文位置后，才考虑封装为可复用 Skill；它仍只标记问题，不自动改写正式结论。
:::

## 9.4 什么时候不要自动化

- 方法规则仍在争议；

- 无法定义什么算关键错误；

- 输入高度不稳定，每次都需要重新解释；

- 一次失败可能无痕覆盖正式状态；

- 人工复核能力跟不上自动处理规模；

- 维护权限、版本和依赖的成本大于节省的劳动。

本章应用：判断一个重复任务应该停在哪一层

从你最近一个月重复至少两次的任务中选一个。先写清不变输入、不变步骤、输出、失败状态和人工检查点，再决定它应该停在哪一层。能用简单形式可靠完成，就不要为了“高级”继续升级。
~~~~

## Chapter 8 cross-reference context — verbatim §8.1–§8.3

Source: `chapters/09-maintenance.qmd`; ends before its chapter application.

~~~~text
## 8.1 最小项目结构只需五类材料

| **材料**           | **它回答什么**                       |
|--------------------|--------------------------------------|
| 项目入口           | 这是什么研究，从哪里开始看           |
| 受保护原件         | 哪些数据、材料和外部原文默认不覆盖   |
| 工作材料与当前成果 | 哪些正在修改，哪些已经可以进入下一步 |
| 决定与变化记录     | 重要方法或状态为什么改变             |
| 当前状态 / 交接页  | 现在什么有效、卡在哪里、下一步是什么 |

这五类内容不一定对应五个文件。小项目可以把它们合并在一两页说明中；项目变复杂以后，再拆分版本记录、来源记录或团队规则。先保证别人能够找到入口、原件、当前成果、重要决定和下一步。

## 8.2 适合交给 AI 的项目维护劳动

- 扫描项目文件并生成文件地图；

- 比较版本，提取新增、删除和实质变化；

- 把研究者确认过的组会或聊天决定整理进决定记录；

- 根据研究者确认的输出更新当前状态；

- 在数据、模型或材料改变后，列出可能需要重做的表图与正文位置；

- 生成交接页草稿，并标出无法从现有材料确认的事项。

AI 只根据已经确认的事实整理关系，不替研究者宣布哪份文件“最终有效”。它可以降低维护成本，最终解释权仍由研究者掌握。

::: {.callout-note appearance="simple" icon=false}
## 案例A：项目第一次真正可交接

项目入口现在能定位原始问卷导出、当前变量字典、分析规格、当前脚本、研究者确认的输出和正文。交接页只写当前状态与未决问题。新成员不需要重读几十轮旧聊天，就能知道下一步是“核对两条文献主张并重跑当前稳健性规格”，而不是重新猜测全部历史。
:::

## 8.3 课题组先统一最低接口

如果课题组里的项目在理论、设计和分析上差异很大，不必先统一整套研究流水线。可以先统一几个最低接口：原始数据不可覆盖；每个项目有一个入口；明确当前有效版本；重要方法变化留下理由；正文数字能够返回输出；交接时提供当前状态和未决事项。具体工具、目录和自动化程度由各项目决定。
~~~~

## Chapter 10 cross-reference context — verbatim §10.1–§10.4

Source: `chapters/11-safety-recovery.qmd`; ends before §10.5.

~~~~text
## 10.1 按失败后果分配风险控制

| **大致风险** | **典型任务**                                           | **最低做法**                                   |
|--------------|--------------------------------------------------------|------------------------------------------------|
| 较低         | 不含结果的措辞润色、格式整理、想法发散                 | 快速人工比较，保留原意                         |
| 中等         | 文献概括、代码修改、结果段候选、批量提取               | 按来源、字段或规则核验，配合抽查并保留输入输出 |
| 较高         | 样本排除、变量定义、模型变化、伦理、因果结论、正式提交 | 明确规格、独立证据/方法判断、人工确认与回退    |

这里的三级风险只是本手册用于快速分流任务的简化框架，并非 NIST 或其他机构发布的统一风险等级。它借鉴一般风险管理思路：根据使用情境、后果、可发现性、可恢复性和现有控制来调整治理强度（NIST, 2023；Autio et al., 2024）。判断时重点看五件事：任务是否进入正式证据、是否改变方法或伦理、错误是否难发现、能否完整恢复、后果是否会扩散到其他文件和决策。

## 10.2 分清五种质量活动

| **活动** | **回答的问题**                             |
|----------|--------------------------------------------|
| 生成     | 能产生什么候选                             |
| 验证     | 是否满足已知规格、数字、来源或字段要求     |
| 独立审计 | 还有什么遗漏、过强推断或系统性错误         |
| 人工复核 | 是否采纳、修改、拒绝或升级                 |
| 复现     | 从规定输入、版本和环境能否重新得到预期产物 |

结构合法不等于内容正确；代码运行不等于符合研究规格；两个模型意见一致不等于获得独立证据；能够重跑也不等于研究设计有效。

## 10.3 应由研究者保留的决定权

- 研究问题与理论贡献；

- 构念界定与关键测量选择；

- 样本纳排和重要数据处理规则；

- 模型与分析地位；

- 因果和机制解释；

- 研究伦理与敏感数据处理；

- 正式结论与提交。

## 10.4 最小权限：先只读，再逐步增加

> 1\. 只读审查：列文件、风险和所需信息；
>
> 2\. 计划与候选补丁：说明拟改内容和影响，由人决定是否应用；
>
> 3\. 有限写入：只修改指定副本或目录；
>
> 4\. 确认后执行：运行已确认的脚本和测试，并在关键节点暂停；
>
> 5\. 有界自动执行：仅用于规则稳定、错误可发现、结果可回退的重复任务。
~~~~

## Terminology and exact wording to preserve

These quotations point to the source wording and do not replace the full passages above.

- **Chapter 2 §2.1:** “本手册把这一层称为“运行框架（Harness）”。”
- **Chapter 2 §2.1:** “Harness 是当前 agent 工程中常用的概念之一，但不是跨厂商统一的产品分类。”
- **Chapter 9 §9.1:** “任务说明（Prompt）”
- **Chapter 9 §9.3:** “Agent 的区别不在于 Prompt 更长，而在于它会根据中间结果继续行动。”
- **Chapter 8 §8.2:** “AI 只根据已经确认的事实整理关系，不替研究者宣布哪份文件“最终有效”。”
- **Chapter 10 §10.2:** “两个模型意见一致不等于获得独立证据”
- **Writing Brief §7:** “执行性问题 / 战略性问题”
- **Writing Brief §7:** “项目（Project）/ 运行框架（Harness）/ 工作流（Workflow）”
- **Writing Brief §7:** “任务规格”
- **Writing Brief §7:** “可追踪任务说明”

## Authoring boundary

Use the Writing Brief to review scope and wording. Drafting and approval of substantive reader-facing prose occur outside this packet; handbook chapters and v1.1 release assets remain unchanged.
