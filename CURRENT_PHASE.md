# Current phase

- **Phase:** v1.2 Multi-Agent Workflow Integration and Review
- **Status:** IN_PROGRESS
- **Target publication version:** v1.2 (release metadata and public version labels remain separately gated)

## Goal

Mechanically integrate the authoritative approved TASK-001 prose into Chapter 9, verify the rendered reading edition, and present the work for human review. The Authoring Gate has passed; this phase does not authorize additional substantive writing.

## In Scope

- Insert approved §9.5 and the approved chapter-application revision from `drafts/TASK-001-approved.md`.
- Make only necessary mechanical Markdown/Quarto adjustments and minimal cross-reference changes.
- Render and inspect Chapter 9 and relevant site structure; review the diff and release integrity.
- Update TASK-001 and durable phase/handoff state.

## Out of Scope

- New or revised substantive prose outside the approved draft.
- Changes to v1.1 PDF/DOCX, tag, Release, license, or `gh-pages`.
- Public version labels, v1.2 release metadata, merge, or deployment.

## Workstreams

| ID | Workstream | Current state |
| --- | --- | --- |
| A | Approved §9.5 and chapter-application integration | REVIEW |
| B | Quarto render and Chapter 9 structural QA | REVIEW |
| C | Accidental-change and release-integrity check | REVIEW |

## Dependencies

- The Authoring Gate passed, and `drafts/TASK-001-approved.md` is the authoritative text.
- Human review remains required before merge, version-label changes, release, or deployment.

## Deliverables

- `chapters/10-automation.qmd` with approved §9.5 and revised application.
- TASK-001 at `REVIEW`, with concise QA and integration handoff.

## Acceptance Criteria

- The inserted section and application wording match the approved draft; prior Chapter 9 prose remains unchanged.
- `quarto render` passes, and the rendered Chapter 9 has correct headings, anchor, TOC, blockquote, callout, table, and navigation.
- Internal links and release downloads resolve in the local build.
- No frozen asset, tag, `gh-pages`, or public version-label change.

## Constraints

- Preserve v1.1 frozen publication integrity and CC BY 4.0.
- Keep generated `_site/` and temporary QA output ignored; do not commit them.
- Work on `content/v1.2-multi-agent-workflow`; human approval controls merge and deployment.

## Decision Gates

- Human review of the integrated text and QA findings.
- Separate decision on v1.2 site labeling, release metadata, merge, and deployment.

## Escalation Conditions

- Any need to alter the approved substantive wording or change chapter structure beyond the authorized §9.5 insertion.
- Conflicting source material, invalidated acceptance criteria, or a new release/version decision.

## Exit Criteria

- Integration and QA are accepted by the human; required visual viewport review is resolved.
- This phase remains open while TASK-001 is in `REVIEW`.

## Current Status

Approved §9.5 and the application revision are integrated verbatim. Quarto render and static Chapter 9/site checks passed. TASK-001 is `REVIEW`; browser security policy prevented visual local-file and narrow-viewport inspection, which remains for review. Public labels still describe v1.1, as instructed.
