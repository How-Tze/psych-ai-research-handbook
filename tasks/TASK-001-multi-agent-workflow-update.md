# TASK: Multi-agent research workflow handbook update

- **TASK ID:** TASK-001
- **STATUS:** PLANNED
- **PHASE:** Multi-Agent Workflow Governance and Handbook Update Planning (specification only; execution requires a later approved substantive phase)
- **OWNER / EXECUTOR:** Human and Strategic / Authoring Chat for content approval; execution agent for brief, evidence, and approved integration
- **AUTHORING GATE:** REQUIRES_CHAT_AUTHORING before substantial reader-facing prose

## CONTEXT

The frozen v1.1 handbook uses Project / Harness / Workflow and already discusses fixed work, scripts, Skills, and Agents in [Chapter 9](../chapters/10-automation.qmd). The [project maintenance chapter](../chapters/09-maintenance.qmd) and [verification / responsibility chapter](../chapters/11-safety-recovery.qmd) may support brief cross-references. This task specifies a future version's substantive update; it does not authorize editing v1.1 content now.

## OBJECTIVE

Design and later implement a stable, vendor-neutral section explaining how research workflows change when multiple autonomous agents can execute bounded work.

## IN SCOPE

- Integrate the section primarily into Chapter 9, with only useful lightweight cross-references to project maintenance and verification / responsibility.
- Explain how to match model capability to task risk and cost, rather than defaulting to the strongest model; distinguish model capability from the agent and its harness.
- Explain why project state belongs in the project or repository rather than chat, while keeping sensitive raw research data in appropriate protected locations.
- Explain that parallel agents mainly shorten elapsed time, can increase coordination costs, and do not inherently lower total compute; practical concurrency depends on workload and coupling.
- Show how requiring high-intelligence Chat to mediate every agent step creates a serial bottleneck; distinguish **执行性问题 / 战略性问题** and use phase governance with explicit escalation.
- Treat task specifications as reusable project assets. Include a compact, concrete task-spec example with scope, acceptance criteria, and escalation conditions.
- Define human responsibility for direction, authorization, scientific judgment, and acceptance; assign strategic models to phase design, escalation, and review, and execution agents to routine implementation.
- Prepare a Writing Brief and source/evidence notes before reader-facing drafting, then integrate only an approved draft.

## OUT OF SCOPE

- Any substantive edit to v1.1 chapter files, release PDF/DOCX assets, tag, or GitHub Release in the current phase.
- Current model rankings or prices, subscription tactics, temporary interfaces, detailed API setup, or current ChatGPT / Claude / Gemini / DeepSeek product matrices.
- Claims that a vendor or model is always best for planning or review; a fixed optimum number of parallel agents.
- Dynamic product onboarding, which belongs in the separate Start Guide when appropriate.

## DELIVERABLES

- Writing Brief with exact placement, proposed section outline, target reader, links to existing Project / Harness / Workflow concepts, and evidence or source needs.
- Clearly separated stable claims and optional dated product examples for the Start Guide.
- Substantive draft reviewed and explicitly approved through Strategic / Authoring Chat.
- Future-version handbook section, any justified cross-references, and a compact task-spec example, integrated mechanically from the approved draft.
- Render and QA evidence, plus task, phase, decision, and handoff updates as needed.

## ACCEPTANCE CRITERIA

- The conceptual argument works without vendor-dependent claims and fits Project / Harness / Workflow and the existing Chapter 9 progression.
- Execution versus strategic questions have clear examples and escalation logic; human scientific and publication responsibility remains explicit.
- A reader with psychology or social-science training can follow the section without software engineering background.
- The task-spec example is concrete and compact, and any product-specific example is optional and dated.
- Cross-agent review is described as an additional independent check, not a guarantee of epistemic independence.
- No conflict with the frozen v1.1 release: substantive material enters a separately approved future version; old release assets and tags remain untouched.
- Render, internal links, chapter navigation, and relevant mobile layout checks pass for the future content change.

## CONSTRAINTS

- Prefer **执行性问题 / 战略性问题** over unexplained production jargon.
- Describe high-capability models by function, without assuming a permanent vendor or tier hierarchy.
- Treat useful agent concurrency as workload-dependent; do not present one universal agent count.
- Say “project state / repository as source of truth” without implying sensitive raw data should all be put in Git.
- Execution agents may make only mechanical integration changes to approved prose unless the task explicitly grants further editorial authority.
- Preserve author approval for substantive claims, handbook structure, release/version strategy, merge, and deployment.

## DEPENDENCIES

- Human approval of a later substantive phase, scope, and version strategy; reassign this task to that phase before moving it to `READY`.
- Content integration map and stable/dynamic claim boundary from the current phase.
- Completion of the Authoring Gate before integrating substantial reader-facing prose.

## ESCALATION CONDITIONS

- The proposed section changes the handbook's core framework, chapter structure, scientific claims, or approved scope.
- Evidence contradicts a planned claim, authoritative sources conflict, or acceptance criteria cease to be valid.
- A draft requires substantive rewriting beyond approved editorial authority, or release/version decisions are needed.
- The task would expose sensitive data or depend on moving restricted research material into Git.

## SUBSTANTIVE AUTHORING GATE

1. The execution agent prepares the Writing Brief and marks `REQUIRES_CHAT_AUTHORING`.
2. Mark the task `BLOCKED` if substantive drafting or approval is pending; the marker is not a task status.
3. Strategic / Authoring Chat drafts or reviews the substantial reader-facing prose; the human explicitly approves the draft.
4. The execution agent integrates that approved draft mechanically and runs QA. Further editorial changes require separately granted authority.

## ON COMPLETION

- Record the approved draft and review evidence in the future task handoff; update task status through `REVIEW` to `DONE` only after acceptance.
- Update `CURRENT_PHASE.md`, `DECISIONS.md`, and `HANDOFF.md` only for durable changes.
- Leave merge, release, and deployment to the human-controlled process.
