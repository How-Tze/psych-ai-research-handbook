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

## Repository maintenance

### Git workflow
- Never perform substantial multi-file maintenance directly on `main`.
- Create a dedicated branch for audits, frontend changes, refactors, or automated fixes. Use prefixes such as `maintenance/`, `fix/`, or `docs/`.
- Never modify, move, delete, or recreate existing release tags without explicit user approval.
- Never alter the published v1.1 frozen PDF/DOCX release assets as part of website maintenance.
- Do not merge a maintenance branch into `main` without explicit human approval.
- Prefer small, coherent commits.

### Content freeze
For the current maintenance cycle:
- Do not expand substantive handbook content.
- Do not introduce new tools, frameworks, examples, arguments, or references.
- Do not silently rewrite prose or change methodological or factual claims.
- Presentation-only transformations are allowed where necessary to fix HTML rendering.
- If a rendering defect appears to require changing substantive wording, leave it unresolved and report it.

### Temporary audit and QA artifacts
- Treat automation-generated technical artifacts as disposable by default.
- Store temporary material under `.audit/` or `.qa/`; these directories must remain gitignored.
- Do not commit automated audit reports, raw validator output, QA screenshots, render/debug logs, temporary diffs, crawl output, pixel comparisons, test caches, generated `_site/`, secrets, or API keys.
- Record only durable conclusions in tracked files such as `HANDOFF.md`, `CHANGELOG.md`, or stable documentation under `docs/`.

### Publication integrity
- `main` represents the current maintainable public source.
- The existing `v1.1` tag and GitHub Release are a frozen historical publication snapshot.
- Website maintenance does not automatically create a new handbook version.
- CSS, HTML, navigation, accessibility, and repository-presentation fixes do not constitute v1.2.
- Handle future substantive content changes separately.

### Deployment
- Do not run a production deployment or `quarto publish gh-pages` unless explicitly instructed by the user.

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
