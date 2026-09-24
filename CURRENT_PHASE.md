# Current phase

- **Phase:** v1.2 Release Gate
- **Status:** IN_PROGRESS
- **Target publication version:** v1.2 — Multi-Agent Workflow / Agent Governance
- **Release date:** actual publication date

## Goal

Publish the approved v1.2 handbook source, PDF/DOCX assets, GitHub Release, and public HTML site; verify every published route and preserve the frozen v1.1 snapshot.

## In Scope

- Final release QA of PR #2 and its approved Chapter 9 prose.
- Version/date metadata, README, CHANGELOG, citation, homepage, and release-state updates.
- Generate and verify versioned PDF/DOCX assets; advance, merge, tag, and release PR #2.
- Deploy the rendered site to GitHub Pages and smoke-test pages, downloads, and labels.
- Record the result in canonical project state.

## Out of Scope

- New substantive handbook content or a change to TASK-001's approved prose.
- Rewriting the v1.1 tag, GitHub Release, PDF/DOCX, or historical site snapshot.
- A new schema, framework, publication strategy, or version target.

## Workstreams

| ID | Workstream | Current state |
| --- | --- | --- |
| A | Release metadata, governance, and source QA | DONE |
| B | Versioned PDF/DOCX build and visual/content QA | DONE |
| C | PR #2 readiness, merge, v1.2 tag and GitHub Release | READY |
| D | Pages deployment and public smoke test | READY |
| E | Final canonical-state and clean-workspace check | READY |

## Dependencies

- TASK-001 is `DONE`; its approved text and human desktop/mobile preview review are recorded.
- PR #2 contains the frozen primary v1.2 content range.
- The human approved end-to-end execution of this Release Gate in D-009 and D-010.

## Deliverables

- Updated v1.2 source, metadata, governance, and release checklist on `main`.
- `release/psych-ai-research-handbook_v1.2_zh-CN.pdf` and `.docx` attached to the v1.2 GitHub Release.
- Immutable `v1.2` tag and an updated public GitHub Pages reading edition.
- Verified public links and a concise release report.

## Acceptance Criteria

- The frozen TASK-001 prose and other substantive chapters are unchanged by release preparation.
- Quarto HTML and DOCX renders pass; a matching PDF is exported from the finalized DOCX; layout, headings, tables, links, downloads, and mobile presentation are checked.
- v1.2 metadata, publication date, citation, README, homepage, assets, tag, and Release agree.
- PR #2 is merged to `main`; the tag resolves to the intended release commit; Pages serves that version.
- v1.1 tag, historical Release, and frozen asset hashes remain unchanged.
- Final local workspaces are clean and release state is recorded.

## Constraints

- Use `main` as source and `gh-pages` only for rendered output; keep `_site/` ignored on `main`.
- Preserve CC BY 4.0 and do not commit secrets or restricted research data.
- Follow `AGENTS.md` approved-release autonomy and escalation rules.

## Decision Gates

- The human has approved this Release Gate, frozen scope, version target, merge, tag, assets, Release, and deployment. Routine steps require no additional approval.
- New strategic or substantive decisions require escalation under `AGENTS.md`.

## Escalation Conditions

- Substantive content or scope changes, an invalid version strategy, or conflict with approved prose/governance.
- Merge, build, deployment, or QA failure that cannot be safely resolved mechanically.
- Risk to historical release assets/tags or need for a new schema, framework, or publication-strategy decision.

## Exit Criteria

- v1.2 is RELEASED / DEPLOYED / VERIFIED, with public smoke tests and canonical-state updates complete.

## Current Status

Release metadata and versioned assets are ready on `content/v1.2-multi-agent-workflow`. Quarto HTML/DOCX render, 32-page A4 PDF export, print layout, Chapter 9, 19-page internal-link scan, asset-copy hashes, and secret-pattern scan passed. No v1.2 tag, GitHub Release, or production deployment has been made yet.
