# HANDOFF — Psych AI Research Handbook

## Current state

- Artifact: 《心理学研究的 AI 进阶手册》
- Frozen edition: v1.1, 2026-09
- Author: Hao Xie / GitHub: How-Tze
- License: CC BY 4.0 (confirmed 2026-09-16)
- PDF and DOCX under `release/` are frozen release artifacts.
- `chapters/` contains an HTML reading edition derived from the frozen DOCX.
- The manually authored DOCX table of contents was removed from HTML because Quarto supplies navigation.
- One-cell case/example tables from Word were converted to Quarto callouts for web readability; wording is preserved.

## Editorial boundary

Do not silently change v1.1 arguments, claims, methods, or references while doing deployment work. Layout-only HTML fixes, broken links, typo corrections, and accessibility improvements are acceptable if recorded. Substantive content changes belong to a later version.

## 2026-09 website maintenance

- The public site audit found repeated book-title labels in chapter navigation, duplicate Quarto/authored numbering, one literal Markdown heading on the homepage, and one remaining one-cell conversion table.
- The maintenance branch adds explicit navigation labels, disables Quarto's redundant automatic section numbers, repairs the homepage heading boundary, and converts the non-tabular example task to a callout without changing its wording.
- Web presentation now includes clearer release/changelog entry points, a wider tablet reading column, long-link wrapping, and an explicit keyboard focus indicator.
- QA covered desktop, tablet, and mobile layouts; generated internal links and anchors, downloads, navigation, callouts, tables, references, and the homepage were rechecked. `quarto render` passes.
- The frozen v1.1 PDF/DOCX files and substantive handbook prose were not changed.
- Unresolved: the current Quarto installation emits non-visible `zh-CN` translation warnings for “Abstract”; monitor upstream/tooling changes unless this becomes reader-visible.
- This maintenance branch has not been merged or deployed. Human review is required before either action.

## Immediate tasks

1. Run local `quarto preview`.
2. Inspect case callouts, long tables, reference links, mobile width, and download buttons.
3. Fix HTML-only presentation issues without modifying the frozen PDF/DOCX.
4. Decide the exact public release date.
5. Publish GitHub Pages, then create GitHub Release v1.1.

## Important future backlog

For a later handbook version, add a section on AI-assisted open-science release workflows: maintain complete local project assets, deliberately select non-sensitive public artifacts, generate/update README/data dictionaries/code/environment metadata, scan for secrets and sensitive content, and maintain public releases when analyses change. Human review remains mandatory for anonymization, consent, and third-party data licensing.
