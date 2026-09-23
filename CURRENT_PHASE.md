# Current phase

- **Phase:** v1.2 Multi-Agent Workflow Authoring Preparation
- **Status:** IN_PROGRESS
- **Target publication version:** v1.2 (no release metadata or assets authorized yet)

## Goal

Prepare TASK-001's Authoring Gate package from the existing handbook, so Strategic / Authoring Chat can draft a bounded v1.2 section after review. This phase authorizes pre-authoring analysis only.

## In Scope

- Map the exact Chapter 9 insertion point and limited cross-references.
- Prepare a Writing Brief, stable/dynamic claim map, duplication/conflict audit, structure, length estimate, and factual verification list.
- Update TASK-001 and durable project state for gate review.

## Out of Scope

- Reader-facing substantive prose, chapter edits, or authoring approval by implication.
- Changes to v1.1 PDF/DOCX, tag, Release, license, or `gh-pages`.
- v1.2 release metadata, merge, or deployment.

## Workstreams

| ID | Workstream | Current state |
| --- | --- | --- |
| A | Content integration and cross-reference map | REVIEW |
| B | Stable-vs-dynamic claim and verification map | REVIEW |
| C | Duplication/conflict audit | REVIEW |
| D | TASK-001 Writing Brief and Authoring Gate package | REVIEW |

## Dependencies

- The governance phase gate has passed; TASK-001 may enter `READY` for pre-authoring work.
- The existing v1.1 chapters and Project / Harness / Workflow framing are the baseline.
- Substantive drafting and mechanical integration depend on a separately reviewed Authoring Gate and explicitly approved draft.

## Deliverables

- Durable `tasks/TASK-001-writing-brief.md` with the integration map, audit, claim boundary, verification needs, and structure.
- Updated TASK-001 status and concise handoff/decision records.

## Acceptance Criteria

- The brief identifies the precise insertion point, adjacent text, concepts, repetition risks, terminology, reader background, and estimated length.
- Stable method concepts and dynamic product facts are clearly separated; any claims requiring verification are listed.
- No handbook chapter, release asset, tag, or publication output changes.
- TASK-001 reaches `REVIEW` for the Authoring Gate, without reader-facing prose drafted.

## Constraints

- Preserve v1.1 and CC BY 4.0 publication integrity.
- Keep sensitive research data out of Git; keep temporary audit material under ignored `.audit/` or `.qa/`.
- Work on `content/v1.2-multi-agent-workflow`; human approval controls merge and deployment.

## Decision Gates

- Strategic / Authoring Chat and human review of the Writing Brief before substantive drafting.
- Explicit human approval of the substantive draft before mechanical integration.
- Separate decisions for any v1.2 release metadata, merge, and deployment.

## Escalation Conditions

- Proposed changes to the approved scope, handbook structure, scientific claims, canonical-state design, or v1.2 target.
- Conflicting authoritative sources, invalidated assumptions or acceptance criteria, or a need to expose restricted research material.

## Exit Criteria

- The Authoring Gate package is reviewed, with scope and wording risks resolved by the human and Strategic / Authoring Chat.
- The phase does not close merely because the brief is ready for review.

## Current Status

TASK-001 is `REVIEW` for the Authoring Gate package in `tasks/TASK-001-writing-brief.md`. The phase remains `IN_PROGRESS` until gate review. No handbook prose, release asset, or site file was modified.
