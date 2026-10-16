# HANDOFF — Psych AI Research Handbook

## Current state

- Artifact: 《心理学研究的 AI 进阶手册》
- Current published edition: v1.2, 2026-09-24 — Multi-Agent Workflow / Agent Governance
- Historical frozen edition: v1.1, 2026-09-16
- Author: Hao Xie / GitHub: How-Tze
- License: CC BY 4.0 (confirmed 2026-09-16)
- Versioned PDF and DOCX under `release/` are frozen release artifacts; preserve both v1.1 and v1.2.
- This branch integrates the approved v1.3 preview in `chapters/`; published main/site and frozen v1.2 assets are unchanged. Historical source remains in v1.1/v1.2 tags.
- The manually authored DOCX table of contents was removed from HTML because Quarto supplies navigation.
- One-cell case/example tables from Word were converted to Quarto callouts for web readability; wording is preserved.

## Editorial boundary

Do not silently change frozen v1.1 or v1.2 arguments, claims, methods, or references while doing deployment work. Layout-only HTML fixes, broken links, typo corrections, and accessibility improvements are acceptable if recorded. Substantive content changes belong to a later version.

## 2026-09 website maintenance

- The public site audit found repeated book-title labels in chapter navigation, duplicate Quarto/authored numbering, one literal Markdown heading on the homepage, and one remaining one-cell conversion table.
- The maintenance branch adds explicit navigation labels, disables Quarto's redundant automatic section numbers, repairs the homepage heading boundary, and converts the non-tabular example task to a callout without changing its wording.
- Web presentation now includes clearer release/changelog entry points, a wider tablet reading column, long-link wrapping, and an explicit keyboard focus indicator.
- QA covered desktop, tablet, and mobile layouts; generated internal links and anchors, downloads, navigation, callouts, tables, references, and the homepage were rechecked. `quarto render` passes.
- The frozen v1.1 PDF/DOCX files and substantive handbook prose were not changed.
- Unresolved: the current Quarto installation emits non-visible `zh-CN` translation warnings for “Abstract”; monitor upstream/tooling changes unless this becomes reader-visible.
- The website maintenance branch was merged into `main` as `78646c7`. Later merges and deployments require an approved release gate or explicit human authorization.

## Current phase

As of 2026-10-16, **v1.3 integration preview** is in REVIEW under TASK-013. Human acceptance of the complete candidate at `db54a0baee935c863290122712bbf1c2db90ae4f` passes the Authoring Gate; TASK-003–012 are DONE. The human requested integration, checks and a preview without publication. Branch: `docs/v1.3-authoring-preparation`; PR #3 remains draft.

All nineteen accepted texts are in `chapters/`: guide, chapters 1–12, conclusion, three appendices, references and AI disclosure. Quarto supplies the approved order and display numbers while retaining most historical filenames. See `docs/v1.3-integration.md` for the full mapping and mechanical changes. Draft QMD inputs and historical release assets remain unchanged. Substantive expansion or scientific correction still requires author judgment.

Old usage and project-maintenance URLs redirect to the guide and project chapter via two static HTML resources, preserving query strings and fragments and providing clickable fallback links. All 48 old content fragments and three home fragments are retained. Keep their `legacy-anchor` elements during heading maintenance.

The homepage and appendix A link the same ZIP containing 34 teaching files, an entry README and license. Resources are explicit to avoid copying local outputs. After material updates, track new delivery files, update the Quarto resource list and run `python scripts/package-materials.py` before rendering. Seven teaching Markdown files received chapter-path/lifecycle corrections; data, programs, images, calculations and reference results are unchanged. Three templates are in `examples/v1.3/templates/`.

Continue the accepted natural Chinese, detailed AI research teaching, connected workflows, contextual term explanations and balanced product examples. Humanizer-zh was used during approved authoring; this integration does not rewrite substantial prose. Reading boundaries remain in `drafts/v1.3/source-notes.md`. Product facts retain prior verification dates; no new product assertions were added.

Validation: full Quarto build (20 book pages plus two legacy entries); 19-text comparison; 1,262 HTML local references/resources and 50 Markdown links; old fragments; byte matching of all rendered downloads and ZIP teaching entries; unchanged four historical PDF/DOCX files. Extracted input/structural exercises pass, and both report modes reproduce reference text including source fingerprints. No statistical refit or model run. Desktop/390px checks show no page overflow on checked pages; cases, tables, formulas, images, templates and sources checked. Legacy query-plus-fragment navigation works. Existing invisible zh-CN/Abstract warnings remain.

Local preview: http://127.0.0.1:4274/ , served from `_site/` while its server runs. Recreate with `quarto preview` if needed. Temporary checks, unpacked files and outputs stay in `.qa/task013/`. The pre-existing untracked `docs/project_audit_report.md` remains untouched. Start Guide v0.11 stays independently published and unchanged in this task.

## Important future backlog

Review the integrated preview as a reading edition: navigation, chapter transitions, download entry and old-link behavior. Approved prose is integrated; differences are bounded mechanical and lifecycle changes. No merge, tag, Release, formal v1.3 PDF/DOCX or production deployment has occurred. A later explicit release gate must freeze scope and authorize publication, including final metadata and any new publication assets. Historical tags and assets remain frozen.
