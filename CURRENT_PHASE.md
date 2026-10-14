# Current phase

- Phase: v1.3 capability chapter authoring
- Status: REVIEW — four author candidates revised for Chinese clarity and practical AI use
- Approval: 2026-10-13 — human approved the candidate and v1.3 writing direction; 2026-10-14 feedback authorizes revising the drafts and extending their teaching depth to other chapters.
- Target: future v1.3; published edition remains v1.2.
- Branch: docs/v1.3-authoring-preparation.

## Goal, scope and responsibilities

TASK-003/004 preparation is accepted. TASK-005 delivered the first three complete candidates and reproducible examples. TASK-006 refocuses method learning on how to learn with AI, polishes theory and analysis, and adds the writing chapter already specified in the approved authoring package. Strategic / Authoring Chat owns prose; Codex tools handle integration and QA. This is bounded draft authoring authority, not approval of unseen prose for publication.

## Deliverables and acceptance

Four complete drafts under drafts/v1.3/, a consolidated review entry and concise editorial requirements for later chapters. Preserve the checked teaching examples and scientific qualifications. Method learning must show concrete questions, follow-ups and practice; writing must demonstrate paragraphs, revision and reviewer replies. Product onboarding stays in the independently released Start Guide.

## Dependencies and constraints

Use the approved teaching materials and briefs. Keep chapters/, release/, index.qmd, _quarto.yml, historical tags/assets and the pre-existing untracked audit file unchanged. No private data, paid API calls or new publication architecture.

## Gates, escalation and exit

TASK-005/006 are in REVIEW with complete checked drafts. Human Authoring Gate approves exact prose before mechanical integration; v1.3 release remains a later reviewed gate. Continue remaining authoring work under the approved briefs, prioritizing literature exploration and research design. Escalate scope/version changes or unresolved source conflicts; solve routine editorial and computational questions within the approved briefs.

## Previous phases

The preparation phase completed and was approved on 2026-10-13. The v1.2 Release Gate completed on 2026-09-24; tag v1.2 remains frozen at a8a9326.

## Completion evidence

TASK-006 delivered four candidates and updated the review entry. Original numeric tables, display equations and figures are preserved; the writing examples match the reference CSV. Five-page isolated Quarto preview rendered; 162 local references and image alternatives passed. Desktop and 390px checks passed, including expandable exercises and generation details; no page overflow or math errors observed. Existing non-visible Quarto zh-CN/Abstract translation warnings remain. Published sources and frozen assets are unchanged against main; teaching data/scripts are unchanged from TASK-005. PR #3 remains a draft. Start Guide v0.11 is independently published.
