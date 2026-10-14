# Current phase

- Phase: v1.3 capability chapter authoring
- Status: REVIEW — six complete candidates, including TASK-007 literature exploration and research design
- Approval: 2026-10-13 — human approved the candidate and v1.3 writing direction; 2026-10-14 feedback authorizes draft revision and explicitly prioritizes literature exploration and research design in the same style.
- Target: future v1.3; published edition remains v1.2.
- Branch: docs/v1.3-authoring-preparation.

## Goal, scope and responsibilities

TASK-003/004 preparation is accepted. TASK-005 delivered the first three complete candidates and reproducible examples. TASK-006 refocuses method learning on how to learn with AI, polishes theory and analysis, and adds the writing chapter already specified in the approved authoring package. Strategic / Authoring Chat owns prose; Codex tools handle integration and QA. This is bounded draft authoring authority, not approval of unseen prose for publication.

2026-10-14 follow-up: the human accepts this writing direction and explicitly prioritizes complete literature-exploration and research-design chapters. Execute TASK-007 with detailed examples, natural Chinese and practical AI use throughout; expand the review package to six candidates.

## Deliverables and acceptance

Six complete drafts under drafts/v1.3/, a consolidated review entry and concise editorial requirements for later chapters. Literature exploration includes three real, openly readable papers, concrete searches and follow-ups, comparison and the next reading decision. Research design includes proposal comparison, eight unvalidated teaching texts with sixteen questions, the existing two lists and an error exercise, hypothetical pilot revisions and sample-planning boundaries. Preserve the checked earlier examples and scientific qualifications. Product onboarding stays in the independently released Start Guide.

## Dependencies and constraints

Use the approved teaching materials and briefs. Keep chapters/, release/, index.qmd, _quarto.yml, historical tags/assets and the pre-existing untracked audit file unchanged. No private data, paid API calls or new publication architecture.

## Gates, escalation and exit

TASK-005/006/007 are in REVIEW with complete checked drafts. Human Authoring Gate approves exact prose before mechanical integration; v1.3 release remains a later reviewed gate. Continue remaining authoring work under the approved briefs, next addressing the introduction, first task and project continuity. Escalate scope/version changes or unresolved source conflicts; solve routine editorial and computational questions within the approved briefs.

## Previous phases

The preparation phase completed and was approved on 2026-10-13. The v1.2 Release Gate completed on 2026-09-24; tag v1.2 remains frozen at a8a9326.

## Completion evidence

TASK-007 delivered the two prioritized chapters and reader materials. Primary sources were checked on 2026-10-14; paper findings, authored conversations and unvalidated experiment materials are distinguished. The prose list matches the unchanged CSV; all eight material IDs and sixteen question/answer pairs are present, and the inline S01 matches the download. Existing teaching checks pass; the previous four drafts and their data/scripts are unchanged. Seven-page isolated Quarto preview rendered; 258 local references and image alternatives passed. Desktop and 390px checks covered tables, navigation and expandable answers, with no page overflow observed. Existing non-visible Quarto zh-CN/Abstract translation warnings remain. Published sources and frozen assets are unchanged against main. PR #3 remains a draft; no merge or deployment. Start Guide v0.11 is independently published.
