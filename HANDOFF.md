# HANDOFF — Psych AI Research Handbook

## Current state

- Artifact: 《心理学研究的 AI 进阶手册》
- Current published edition: v1.2, 2026-09-24 — Multi-Agent Workflow / Agent Governance
- Historical frozen edition: v1.1, 2026-09-16
- Author: Hao Xie / GitHub: How-Tze
- License: CC BY 4.0 (confirmed 2026-09-16)
- Versioned PDF and DOCX under `release/` are frozen release artifacts; preserve both v1.1 and v1.2.
- `chapters/` contains the current v1.2 Quarto reading edition; the `v1.1` tag preserves the earlier source.
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

As of 2026-10-16, the active phase is **v1.3 capability chapter authoring**, status REVIEW. TASK-003/004 are DONE; TASK-005/006/007/008 are in REVIEW. Following the user's workflow priority and authorization to continue complete writing, TASK-008 adds five candidates: reading guide, work environment, first complete task, project continuity, and repeatable workflows/Agents. There are now eleven candidates (guide plus chapters 1–10), with short bridges across the prior six. Start at `drafts/v1.3/README.md`; the branch remains `docs/v1.3-authoring-preparation`, draft PR #3.

Literature uses three verified open papers about background music to teach search, comparison and the next reading decision. Design develops a distinct background-speech example, with eight unvalidated texts, sixteen questions, the existing two lists and hypothetical pilot revisions. It explicitly distinguishes item balance, participant allocation and trial order. Source scope is recorded in `drafts/v1.3/source-notes.md`; reader files are under `examples/v1.3/`.

New workflow material lives in `examples/v1.3/workflow/`: a compact project entry, two actually generated numeric reports, a standard-library script and a separate authored interpretation. Both runs use the same existing confirmed CSV; report scope changes, without statistical refitting or model calls. Project situations and Agent exchanges are teaching constructions. Workflow sources were checked on 2026-10-16; Humanizer-zh remains an editorial reference, not a globally installed skill or scientific source.

Validation: every earlier chapter line is retained in order; original teaching data, scripts and results are unchanged. Reports reproduce exactly; output protection and malformed-input checks pass, as do existing case checks. Twelve-page isolated Quarto preview, 560 local references/image alternatives and 74 source links pass. New-page desktop/mobile visual QA remains pending because browser URL policy refused access; prior TASK-007 visual QA does not cover the new pages. Existing invisible zh-CN/Abstract warnings remain. Exact prose awaits Authoring Gate; no chapter is integrated or published.

Published `chapters/`, `release/`, `index.qmd` and `_quarto.yml` are unchanged against main. The pre-existing untracked `docs/project_audit_report.md` remains untouched. The companion Start Guide v0.11 was approved, merged (PR #1/#2), tagged and released on 2026-10-13; all 31 live pages and eight downloads passed checks. Its release does not authorize a handbook v1.3 publication.

## Important future backlog

Complete qualitative teaching, verification/privacy/recovery (including the already recorded risk-question correction), conclusion, appendices and source/collaboration notes, then edit the book as a whole and integrate approved prose. TASK-008's project chapter now includes the previously requested open-science material preparation: select shareable assets, prepare explanatory files, check reproducibility and preserve version correspondence. It does not authorize uploading any real project materials; sharing eligibility remains a researcher/institution decision. Complete the pending visual QA before an integration or release gate.
