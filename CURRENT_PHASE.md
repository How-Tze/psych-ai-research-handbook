# Current phase

- Phase: v1.3 integration preview
- Status: REVIEW — TASK-013 integration and checks complete
- Approval: 2026-10-16 — human accepts the complete candidate and authorizes formal-source integration, unified navigation/cross-references/downloads, legacy-link compatibility and a checked local preview; explicitly no publication.
- Approved input: `db54a0baee935c863290122712bbf1c2db90ae4f`, nineteen candidate QMD files under `drafts/v1.3/` and existing teaching materials.
- Target: integrated v1.3 preview; published edition remains v1.2.
- Branch: docs/v1.3-authoring-preparation; draft PR #3.

## Goal, scope and responsibilities

Integrate the accepted guide, chapters 1–12, conclusion, appendices A/B/C, references and AI disclosure into `chapters/`. Unify navigation, paths, downloads and lifecycle metadata. Keep existing web addresses and content fragments usable. Codex handles mechanical integration, compatibility, packaging, presentation fixes and checks. Substantial prose has passed the Authoring Gate; scientific claims are not independently rewritten. Keep accepted drafts as the baseline. The final mapping and allowed differences are recorded in `docs/v1.3-integration.md`.

## Dependencies, deliverables and acceptance

TASK-003 through TASK-012 are DONE. Use existing teaching cases and checked results; do not refit or replace them. Deliver integrated source, teaching download pack, preserved legacy links and a local preview. Compare prose with approved input, verify local links and downloads, render the full book, and inspect desktop/narrow layouts including navigation, callouts, tables, references and frozen downloads. Exact acceptance criteria are in TASK-013.

## Constraints and gates

This is integration authority, not a release gate. No merge, tag, Release, deployment, new official PDF/DOCX or historical-asset replacement. Preserve `release/`, tags, candidate prose and the pre-existing untracked audit report. Start Guide v0.11 remains independently published. Escalate substantive content/structure/version changes, conflicting approved inputs or an unresolved build/compatibility failure.

## Exit and next step

After implementation and checks, enter REVIEW and deliver the preview for author inspection. A later explicit release gate is required before publication. Update task evidence and HANDOFF; do not treat preview completion as a release.

## Previous phases

v1.3 authoring (TASK-005–012) was accepted on 2026-10-16 at the exact input above. Preparation (TASK-003/004) was accepted on 2026-10-13. v1.2 was published on 2026-09-24; its tag at a8a9326 and all historical assets remain frozen.

## Completion evidence

Twenty book pages plus two legacy entry pages render. Nineteen approved texts match after documented mechanical changes. All 1,262 HTML local references/resources, 50 teaching Markdown links, 48 legacy content fragments and three home fragments pass. All 34 teaching downloads and ZIP entries match source; four historical PDF/DOCX files are unchanged. Extracted exercises pass their stated input/structural checks; both report modes reproduce reference text and input fingerprints. Desktop/390px checks pass, including query-plus-fragment legacy navigation. Existing non-visible Quarto translation warnings remain. No refit, merge, tag, Release or deployment. Preview: http://127.0.0.1:4274/ while its local server runs. See TASK-013 and docs/v1.3-integration.md.
