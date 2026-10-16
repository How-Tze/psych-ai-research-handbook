# Release checklists

## v1.3 Release Gate — 2026-10-16

- [x] Human accepted the integrated edition at `2271f1c` and authorized formal exports and publication (D-022 / TASK-014).
- [x] Record v1.1/v1.2 tag, Release and four frozen-file baselines; preserve approved candidate source and teaching calculations.
- [x] Update formal version, date, citation, current/historical download entries and lifecycle statements only.
- [x] Generate matching 103-page A4 DOCX/PDF, update contents and page numbers, inspect every final page. Preserve 33 data tables, two figures and 28 native editable equations; 146 internal bookmarks/links and 155 external links pass structural checks.
- [x] Verify 19 chapter sources against the approved input using an explicit status-only change list; print body matches raw DOCX after documented layout transformations.
- [x] Render 22 HTML pages; validate 1,266 local references/resources, 50 material Markdown links, two old routes, 48 old content fragments and three homepage fragments.
- [x] Check desktop and 390px viewport; homepage, navigation, case presentation, wide tables, formulas, images, references and current/historical downloads remain usable.
- [x] Match 34 teaching downloads and ZIP entries to source; run extracted exercises and reproduce both reports without changing original data, analysis programs or results.
- [x] Check tracked source and delivery scope for credentials/private artifacts; no temporary output, review changes, comments or macros in deliverables. The pre-existing untracked audit report is excluded.
- [ ] Merge PR #3 and verify the merged tree; create immutable v1.3 tag.
- [ ] Publish GitHub Release with PDF, DOCX and teaching ZIP; deploy `gh-pages`.
- [ ] Verify public routes/download hashes and historical integrity; record final project state.

Print generation is documented in `publication/README.md`. Word exports the checked DOCX directly to PDF, retaining navigable contents and PDF bookmarks. A second render after title-line balancing changed only seven page images; those were reinspected, and the other 96 images matched the already inspected pages byte for byte. Existing non-visible Quarto zh-CN translation warnings remain; they do not affect the checked Chinese text.

## v1.2 Release Gate — 2026-09-24

- [x] Verify approved PR #2 scope and frozen v1.1 asset/tag/Release baselines.
- [x] Update v1.2 date, citation, README, changelog, homepage, and governance state.
- [x] Render and inspect HTML, PDF, and DOCX; check content, layout, navigation, links, and mobile presentation.
- [x] Scan tracked release contents for secrets and restricted material.
- [x] Mark PR #2 ready, merge to `main`, and verify the merged tree.
- [x] Create and push the immutable `v1.2` tag; publish GitHub Release with PDF/DOCX assets.
- [x] Deploy Quarto output to `gh-pages` and smoke-test the public site and downloads.
- [x] Verify v1.1 historical integrity, record final canonical state, and leave workspaces clean.

The v1.2 DOCX was rendered with Quarto, then finalized in A4 with an updated table of contents. The matching PDF was exported from that DOCX. Print-only mechanical adjustments removed a duplicated homepage title/subtitle and widened two table columns; no chapter source prose changed. The final PDF is 32 A4 pages. The HTML build has 19 pages and 914 local references with no broken file or anchor target. Chapter 9's desktop/mobile preview was accepted by the human before this gate.

PR #2 merged as `a8a9326`, which is the `v1.2` tag target. The v1.2 Release has two uploaded assets, and their public downloads match the repository files by SHA-256. All 19 public HTML routes returned 200; the homepage, Chapter 9, and four v1.1/v1.2 site downloads were checked. The deployed `gh-pages` tree contains only intended current and historical release files, with no `.qa` output. The unchanged v1.1 tag resolves to `175a9b4`; v1.1 PDF/DOCX SHA-256 values remain `8FA5E333C78A2DEAB19FF1DC8DDB1176D588AF153FD86CD174F95A3637C660D3` and `A14965F2B8E5C405C880627837AFD3167D9D2794ADBAA0F08F98E01AA56EF8F3`.

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
