# TASK: Publish v1.2 handbook

- **TASK ID:** TASK-002
- **STATUS:** DONE
- **PHASE:** v1.2 Release Gate
- **OWNER / EXECUTOR:** Codex under the human-approved Release Gate

## CONTEXT

TASK-001 is `DONE`; [PR #2](https://github.com/How-Tze/psych-ai-research-handbook/pull/2) contains the frozen primary v1.2 scope. D-009 and D-010 authorize the release workflow and routine end-to-end execution.

## OBJECTIVE

Publish and verify v1.2 — Multi-Agent Workflow / Agent Governance — while preserving v1.1.

## IN SCOPE

- Final QA, version/date and citation metadata, PDF/DOCX build and verification.
- PR readiness and merge, v1.2 tag and GitHub Release with assets.
- GitHub Pages deployment, public smoke tests, and canonical-state updates.

## OUT OF SCOPE

- New substantive prose, scope expansion, version-strategy changes, or modification of v1.1 snapshots.

## DELIVERABLES

- v1.2 source and metadata on `main`, matching PDF/DOCX assets, tag, GitHub Release, and public HTML site.
- Verified links, version labels, historical integrity, and clean workspaces.

## ACCEPTANCE CRITERIA

- Every criterion and exit condition in `CURRENT_PHASE.md` passes.
- Public v1.2 site, downloads, and Release links resolve to the intended edition.
- The v1.1 tag, Release, and asset hashes match their pre-release values.

## CONSTRAINTS

- No new substantive content; use the actual publication date and preserve CC BY 4.0.
- Generated `_site/` and temporary QA output remain untracked on `main`.

## DEPENDENCIES

- Human-approved D-009/D-010 Release Gate; TASK-001 `DONE`; PR #2 ready for release preparation.

## ESCALATION CONDITIONS

- The conditions in `CURRENT_PHASE.md` and `AGENTS.md` for approved release gates.

## ON COMPLETION

- Mark `DONE`; record tag, Release, site, assets, QA, historical integrity, and clean status in `CURRENT_PHASE.md` and `HANDOFF.md`.

Completed 2026-09-24: PR #2 merged as `a8a9326`; `v1.2` tag and GitHub Release published with PDF/DOCX; Pages deployed and all 19 public HTML pages, four current/historical downloads, Release assets, version labels, and v1.1 integrity verified. See `CURRENT_PHASE.md` and `docs/RELEASE_CHECKLIST.md` for the durable QA summary.
