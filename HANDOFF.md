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

As of 2026-10-16, the active phase is **v1.3 capability chapter authoring**, status REVIEW. TASK-003/004 are DONE; TASK-005 through TASK-011 are in REVIEW. Thirteen candidates (guide plus chapters 1–12) are complete. TASK-011 adds full qualitative research and verification/privacy/recovery chapters under the user's explicit priority. It carries forward TASK-010's natural Chinese, Humanizer-zh and balanced product-example requirements. Start at `drafts/v1.3/README.md`; the branch remains `docs/v1.3-authoring-preparation`, draft PR #3.

The qualitative chapter uses the unchanged six fictional excerpts from two speakers to develop competing readings, a reflexive memo, a provisional interpretation and a paragraph. Its separate retrieval exercise distinguishes codebook use, coding-reliability aims and reflexive analysis. Braun/Clarke (2023), Gale et al. (2013) and author guidance support the method distinctions; AI dialogues and interpretations are authored teaching examples. A completed reading sheet connects source IDs, decisions and next questions.

The safety chapter places checks at the point outputs are used, explains permitted processing environments and indirect identification, and corrects the third risk question. A recovery exercise actually ran the existing report script on a deliberately altered temporary copy (main N=15) and the original confirmed table (N=21). Both runs completed; the restored text matches the prior round-2 report. No refit, model call or change to original inputs occurred. Privacy example and downstream manuscript consequences are fictional. See source notes and the reader exercise for the exact scope.

Literature uses three verified open papers about background music to teach search, comparison and the next reading decision. Design develops a distinct background-speech example, with eight unvalidated texts, sixteen questions, the existing two lists and hypothetical pilot revisions. It explicitly distinguishes item balance, participant allocation and trial order. Source scope is recorded in `drafts/v1.3/source-notes.md`; reader files are under `examples/v1.3/`.

New workflow material lives in `examples/v1.3/workflow/`: a compact project entry, two actually generated numeric reports, a standard-library script and a separate authored interpretation. Both runs use the same existing confirmed CSV; report scope changes, without statistical refitting or model calls. Project situations and Agent exchanges are teaching constructions. Workflow sources were checked on 2026-10-16; Humanizer-zh remains an editorial reference, not a globally installed skill or scientific source.

TASK-010 product examples have official sources checked on 2026-10-16. 千问 and DeepSeek participate in learning and result-table exercises; Doubao and Claude appear in material drafting. 千问办公, Qwen Code and DeepSeek Harness illustrate file handling and execution; the latter is explicitly a preview. Chapter 1 separates these product entry points and puts official sources at the end. D-018 refines D-017: basic chat is the reader baseline, not a single default brand. Carry direct explanation, meaningful research outcomes, contextual definitions and balanced domestic/international examples into remaining chapters. No price or availability catalog is introduced.

Latest validation: all six original excerpts/speakers match; thirty existing teaching files other than the updated index are unchanged. Existing numerical table rows, formulas, figures and code remain. Fourteen-page isolated Quarto preview and 715 local references/image alternatives pass; 17 new source-relative links also pass. Desktop/390px checks cover both new chapters, quotation/recovery tables, the analytic-memo callout and navigation; checked narrow pages have no overflow. Existing invisible zh-CN/Abstract warnings remain. Exact prose awaits Authoring Gate; no chapter is integrated or published.

Published `chapters/`, `release/`, `index.qmd` and `_quarto.yml` are unchanged against main. The pre-existing untracked `docs/project_audit_report.md` remains untouched. The companion Start Guide v0.11 was approved, merged (PR #1/#2), tagged and released on 2026-10-13; all 31 live pages and eight downloads passed checks. Its release does not authorize a handbook v1.3 publication.

## Important future backlog

Complete conclusion, appendices and source/collaboration notes, then edit the book as a whole and integrate approved prose. Apply the beginner-entry and direct-prose standards to remaining work. TASK-011's qualitative chapter is candidate 11 and safety is candidate 12; published numbering and paths remain unchanged. TASK-008's project chapter already includes open-science material preparation. Sharing eligibility remains a researcher/institution decision; no real project uploads are authorized here. Integration/release QA remains necessary for the final publication.
