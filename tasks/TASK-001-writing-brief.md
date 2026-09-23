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
