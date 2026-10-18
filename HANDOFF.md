# HANDOFF — Psych AI Research Handbook

## Active work — 2026-10-18

TASK-015 已批准并 DONE；TASK-016 的私人作者工作台 0.1.0 已实现、安装，处于 REVIEW，等待作者试用。两库工作分支为 `codex/author-workbench`。桌面和开始菜单入口名为“心理学 AI 手册·作者工作台”，私人记录在 `%LOCALAPPDATA%/PsychAI/AuthorWorkbench`，程序与记录分开存放。

实现及使用说明见 `tools/author-workbench/README.md`，实际检查与边界见 `docs/author-workbench-trial.md`。两站共用同一工具。开始下一轮获准内容任务时读取 pending、选择范围、冻结批次，先保留作者改字，再处理批注；仅凭聊天生成稿不能标为已整合。新修订留待处理。

正文、下载、历史标签、main 和公开网站未变；没有推送、合并或部署。AW-07 公开入口仍需独立授权。测试记录在忽略的 `.qa/task016/`，不混入真实私人意见箱；预存审查文件未动。

## Current state

- Artifact: 《心理学研究的 AI 进阶手册》
- Current published edition: v1.3, 2026-10-16 — complete AI research workflows and teaching materials
- Historical frozen editions: v1.1 (2026-09-16), v1.2 (2026-09-24)
- Author: Hao Xie / GitHub: How-Tze
- License: CC BY 4.0 (confirmed 2026-09-16)
- Versioned PDF and DOCX under `release/` are frozen release artifacts; preserve v1.1, v1.2 and v1.3.
- `chapters/` is the published v1.3 source; all historical snapshots remain in their release tags. Historical source remains in v1.1/v1.2 tags.
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

## Completed v1.3 release phase

As of 2026-10-16, TASK-014 is DONE under the human-approved v1.3 Release Gate. The integrated edition at `2271f1c` is accepted; TASK-003–014 are DONE. Authorization covers matching HTML/PDF/DOCX, final QA, PR #3 readiness and merge, tag, Release assets, Pages deployment and public verification. Do not ask for repeated mechanical approvals. Substantial text is frozen. PR #3 merged as `029e414`, also the v1.3 tag target. Release `415120365` carries PDF/DOCX/ZIP; gh-pages `014e79d` deployed successfully (run `38926095603`). Public checks passed for 63 site pages/files and all three Release downloads. See `docs/RELEASE_CHECKLIST.md` for hashes, historical integrity and the bounded browser-check limitation.

The nineteen texts and 34 teaching files are integrated. Preserve two legacy routes, 48 content anchors and three home anchors; see `docs/v1.3-integration.md`. The ZIP contains the 34 files, an entry README and license. Explicit Quarto resources avoid copying temporary outputs. Data, scripts, figures and numerical results are unchanged.

The print workflow is documented in `publication/README.md`. Quarto produces DOCX; print-only formatting retains native equations and internal bookmarks; a separate invisible Word instance updates the TOC and exports matching PDF. Both are new v1.3 files; historical v1.1/v1.2 assets remain frozen. Release checks and final public evidence belong in `docs/RELEASE_CHECKLIST.md`.

The accepted Chinese style, contextual terminology, detailed AI research teaching and connected workflows remain intact. Draft QMD inputs and source notes preserve authoring evidence. No new scientific claims, model results or product facts are added during release.

Temporary exports, page images and check output remain under ignored `.qa/task014/`. The pre-existing untracked `docs/project_audit_report.md` remains untouched. Start Guide was unchanged by this handbook release and subsequently completed its own v0.12 release. The completed release gate grants no authority for later phases; current design/governance scope is recorded above.
