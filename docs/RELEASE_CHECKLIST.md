# Release checklists

## v1.2 Release Gate — 2026-09-24

- [x] Verify approved PR #2 scope and frozen v1.1 asset/tag/Release baselines.
- [x] Update v1.2 date, citation, README, changelog, homepage, and governance state.
- [x] Render and inspect HTML, PDF, and DOCX; check content, layout, navigation, links, and mobile presentation.
- [x] Scan tracked release contents for secrets and restricted material.
- [ ] Mark PR #2 ready, merge to `main`, and verify the merged tree.
- [ ] Create and push the immutable `v1.2` tag; publish GitHub Release with PDF/DOCX assets.
- [ ] Deploy Quarto output to `gh-pages` and smoke-test the public site and downloads.
- [ ] Verify v1.1 historical integrity, record final canonical state, and leave workspaces clean.

The v1.2 DOCX was rendered with Quarto, then finalized in A4 with an updated table of contents. The matching PDF was exported from that DOCX. Print-only mechanical adjustments removed a duplicated homepage title/subtitle and widened two table columns; no chapter source prose changed. The final PDF is 32 A4 pages. The HTML build has 19 pages and 914 local references with no broken file or anchor target. Chapter 9's desktop/mobile preview was accepted by the human before this gate.

## Historical v1.1 public release checklist

## Repository
- [ ] Create public repository `How-Tze/psych-ai-research-handbook`.
- [ ] Review `git status` for secrets/private files before first push.
- [ ] Push source files to `main`.

## Website
- [ ] Run `quarto preview` and inspect desktop + narrow/mobile widths.
- [ ] Confirm all chapter navigation and tables render correctly.
- [ ] Confirm PDF/DOCX download links work.
- [ ] Run `quarto publish gh-pages`.
- [ ] Verify `https://How-Tze.github.io/psych-ai-research-handbook/`.

## Publication metadata
- [x] License confirmed as CC BY 4.0; `LICENSE.md` and metadata added.
- [ ] Decide exact release date.
- [ ] Review `CITATION.cff`.
- [ ] Create GitHub Release `v1.1` and attach frozen PDF + DOCX.
- [ ] Optionally archive on Zenodo and add DOI metadata.

## Communication
- [ ] Prepare a short project description for GitHub/social sharing.
- [ ] Prepare a psychology-community article or collaboration pitch linking to the HTML reading edition.
