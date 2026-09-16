# AGENTS.md

These instructions apply to the entire repository.

## Mission
Maintain and publish the stable online reading edition of 《心理学研究的 AI 进阶手册》. The repository is a publication project, not a sandbox for adding new AI frameworks or product catalogs.

## Source-of-truth rules
- `release/*.pdf` and `release/*.docx` are frozen v1.1 artifacts. Do not modify them.
- `chapters/*.qmd` is the HTML reading representation of the frozen v1.1 text.
- HTML-only transformations are allowed when they preserve wording and meaning (navigation, callouts, responsive tables, accessible link text).
- Substantive edits require a new handbook version or explicit author approval.

## Safety and privacy
- Never commit API keys, `.env`, private research data, unpublished third-party manuscripts, account screenshots, or local credential files.
- Before any public release, inspect `git status` and repository contents for secrets and private artifacts.

## Publishing
- The public license is fixed as **CC BY 4.0** for v1.1. Do not change or remove the license without explicit author approval.
- Keep `main` as source.
- Use Quarto for HTML build.
- Use `gh-pages` for rendered GitHub Pages output.
- Do not commit `_site/` to `main` unless the publication strategy is deliberately changed.

## Style
- Chinese is the primary reader language.
- Prefer stable method language over fast-changing product-specific claims.
- Preserve the distinction between researcher judgment and AI structural/execution labor.
- Avoid turning the book into a generic AI product manual; dynamic product onboarding belongs in the separate Start Guide project.

## QA
After meaningful site changes:
1. run `quarto render`;
2. inspect the homepage, chapter navigation, case callouts, wide tables, references, and release-download links;
3. check at least one narrow/mobile viewport;
4. ensure no broken internal links.
