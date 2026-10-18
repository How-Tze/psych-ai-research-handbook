# HANDOFF — Psych AI Research Handbook

## Active work — 2026-10-18

TASK-015–017 已完成；“作者模式”入口已在两站发布，共用工具 0.1.1 已更新安装。两库 PR #5 已合并；主手册 main `5ad923f`、gh-pages `1168543`，指南 main `09efb70`、gh-pages `4edda02`；Pages 运行 `39095586784` / `39095576252` 成功。收尾记录位于 `codex/author-entry-closeout`，完整证据见 TASK-017。

日常从页面右下角或桌面/开始菜单的“心理学 AI 手册·作者工作台”进入。记录在 `%LOCALAPPDATA%/PsychAI/AuthorWorkbench`，保存为待合并草稿；使用与隐私边界见 `tools/author-workbench/README.md`。

正文 v1.3/v0.12 与冻结下载保持。下一轮获准内容任务先读取 pending、选择范围、冻结批次，保留作者改字，再处理批注并写入候选证据；新修订留待处理。本轮测试不创建真实意见，预存审查文件不动。

18 项测试、58 页两站构建、4,394 处本地引用通过；线上 114 个页面和资源与验收构建一致，历史标签、Release 与附件未变。浏览器工具禁止启动外部应用，正式网页自动浏览曾超时，因此完整网页到应用点击链未自动验收；位置生成、安装版冷启动与定位分别通过。未重启 Windows、未模拟断电。正常浏览器可能要求确认打开应用，也可从“?”复制当前位置后在桌面工作台粘贴。

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
