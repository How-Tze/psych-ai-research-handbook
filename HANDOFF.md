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

As of 2026-10-14, the active phase is **v1.3 capability chapter authoring**, status REVIEW. TASK-003/004 are DONE; TASK-005/006/007 are in REVIEW. Following the user's explicit next priority, TASK-007 adds complete literature-exploration and research-design candidates to the four existing drafts. They use natural Chinese, detailed examples and concrete AI questions/follow-ups. Start at `drafts/v1.3/README.md`; the branch remains `docs/v1.3-authoring-preparation`, draft PR #3.

Literature uses three verified open papers about background music to teach search, comparison and the next reading decision. Design develops a distinct background-speech example, with eight unvalidated texts, sixteen questions, the existing two lists and hypothetical pilot revisions. It explicitly distinguishes item balance, participant allocation and trial order. Source scope is recorded in `drafts/v1.3/source-notes.md`; reader files are under `examples/v1.3/`.

Validation: earlier four drafts, teaching data, scripts and calculations are unchanged. Existing case checks pass; the design table matches the CSV, all eight material IDs and sixteen question/answer pairs are present, and the inline excerpt matches its download. Seven-page isolated preview and 258 local references passed. Desktop/390px checks covered navigation, tables and expandable answers, without page overflow. Authoring Gate for exact prose remains before integration; no chapter is integrated or published. Next writing priorities follow the package: introduction, first task and project continuity. Humanizer-zh remains an editorial reference, not a globally installed skill or scientific source.

Published `chapters/`, `release/`, `index.qmd` and `_quarto.yml` are unchanged against main. The pre-existing untracked `docs/project_audit_report.md` remains untouched. The companion Start Guide v0.11 was approved, merged (PR #1/#2), tagged and released on 2026-10-13; all 31 live pages and eight downloads passed checks. Its release does not authorize a handbook v1.3 publication.

## Important future backlog

For a later handbook version, add a section on AI-assisted open-science release workflows: maintain complete local project assets, deliberately select non-sensitive public artifacts, generate/update README/data dictionaries/code/environment metadata, scan for secrets and sensitive content, and maintain public releases when analyses change. Human review remains mandatory for anonymization, consent, and third-party data licensing.
