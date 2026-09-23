# Current phase

- **Phase:** Multi-Agent Workflow Governance and Handbook Update Planning
- **Status:** IN_PROGRESS

## Goal

Establish a repository-native phase and task governance system and prepare a future substantive handbook update on multi-agent research workflows. This phase does not authorize substantive handbook editing.

## In Scope

- Establish governance, decision, task, and handoff files.
- Map potential handbook integration points without editing reader-facing prose.
- Separate stable conceptual claims from dynamic product advice.
- Specify the future handbook update and its Authoring Gate.

## Out of Scope

- Editing substantive handbook prose or frozen v1.1 PDF/DOCX assets.
- Changing publication version, license, release tags, or GitHub Release.
- Merging or deploying the site.

## Workstreams

| ID | Workstream | Current state |
| --- | --- | --- |
| A | Repository governance infrastructure | IN_PROGRESS |
| B | Content integration mapping | PLANNED; primary location is Chapter 9 (`chapters/10-automation.qmd`), with possible light cross-references in Chapters 8 and 10 |
| C | Stable-vs-dynamic claim separation | PLANNED; stable method concepts belong in the handbook, changing product guidance in the Start Guide |
| D | Task specification for the future handbook update | PLANNED; see `tasks/TASK-001-multi-agent-workflow-update.md` |

## Dependencies

- Workstream D depends on the content map and stable/dynamic boundary in B and C.
- Substantive authoring depends on human approval of a future phase and the task's Authoring Gate.

## Deliverables

- Updated `AGENTS.md` and compact `HANDOFF.md` pointers.
- `CURRENT_PHASE.md`, `DECISIONS.md`, `tasks/README.md`, and `tasks/TASK_TEMPLATE.md`.
- Planned `tasks/TASK-001-multi-agent-workflow-update.md`.

## Acceptance Criteria

- Governance roles, canonical state, task lifecycle, autonomy, and escalation are clear and consistent with existing release safeguards.
- The future task identifies placement, conceptual scope, exclusions, acceptance checks, and the substantive Authoring Gate.
- No handbook chapter, frozen release asset, tag, or publication branch changes in this phase's governance work.
- Markdown links and repository diff pass review.

## Constraints

- Preserve v1.1 and CC BY 4.0 publication integrity.
- Keep temporary QA under ignored `.audit/` or `.qa/` and keep secrets or restricted data out of Git.
- Use a maintenance branch; human approval controls merge and deployment.

## Decision Gates

- Human approval of a later substantive update phase and any version or release strategy.
- Strategic / Authoring Chat approval of substantial reader-facing prose before integration.

## Escalation Conditions

- Any proposed change to substantive claims, handbook structure, canonical-state design, or release strategy.
- Conflicting authoritative sources, invalidated assumptions or acceptance criteria, or work beyond this phase.

## Exit Criteria

- Governance files and TASK-001 are reviewed and accepted, with no substantive handbook changes.
- Future content work remains separately gated; this phase is closed only after human phase review.

## Current Status

Governance work is underway on `maintenance/phase-governance-2026-09`. TASK-001 is `PLANNED` and is not authorized for content execution in this phase.
