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

As of 2026-10-13, the active phase is **v1.3 capability chapter authoring**, status REVIEW. The human approved the preparation candidate and writing direction. TASK-003/004 are DONE; TASK-005 delivers complete method-learning, theory-development and data-analysis candidates under `drafts/v1.3/`, with one review entry, source notes, executable synthetic analyses, reference outputs and two figures. The branch remains `docs/v1.3-authoring-preparation`.

Validation: the original teaching checks pass; the questionnaire regressions and 60-person × 14-day random-intercept example ran, with independent numerical checks, convergence and no warnings. Four-page isolated Quarto preview, 124 local references and desktop/390px layout checks passed. A long equation was split to remove mobile overflow. Authoring Gate for these exact new drafts is next; no new chapter prose is integrated or published.

Published `chapters/`, `release/`, `index.qmd` and `_quarto.yml` are unchanged against main. The pre-existing untracked `docs/project_audit_report.md` remains untouched. The companion Start Guide v0.11 was approved, merged (PR #1/#2), tagged and released on 2026-10-13; all 31 live pages and eight downloads passed checks. Its release does not authorize a handbook v1.3 publication.

## Important future backlog

For a later handbook version, add a section on AI-assisted open-science release workflows: maintain complete local project assets, deliberately select non-sensitive public artifacts, generate/update README/data dictionaries/code/environment metadata, scan for secrets and sensitive content, and maintain public releases when analyses change. Human review remains mandatory for anonymization, consent, and third-party data licensing.
