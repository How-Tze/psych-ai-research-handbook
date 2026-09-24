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

The **v1.2 Release Gate** is complete: `v1.2 RELEASED / DEPLOYED / VERIFIED` on 2026-09-24. [`CURRENT_PHASE.md`](CURRENT_PHASE.md) records the gate and QA summary; [`DECISIONS.md`](DECISIONS.md) records the approved scope and end-to-end execution authority; [`tasks/`](tasks/README.md) holds task specifications. Agents execute approved phase tasks and escalate strategic questions under [`AGENTS.md`](AGENTS.md).

[`TASK-001`](tasks/TASK-001-multi-agent-workflow-update.md) and [`TASK-002`](tasks/TASK-002-v1.2-release.md) are `DONE`. [PR #2](https://github.com/How-Tze/psych-ai-research-handbook/pull/2) merged as `a8a9326`; the [`v1.2` tag](https://github.com/How-Tze/psych-ai-research-handbook/tree/v1.2) points to that commit. The [v1.2 GitHub Release](https://github.com/How-Tze/psych-ai-research-handbook/releases/tag/v1.2) has PDF/DOCX assets, and the [public site](https://How-Tze.github.io/psych-ai-research-handbook/) serves v1.2. The approved §9.5 was previously accepted by the human on desktop and mobile. Release smoke tests passed for all 19 public HTML pages, current and historical downloads, and Release assets; hashes and historical integrity are recorded in the [release checklist](docs/RELEASE_CHECKLIST.md). Two post-tag site-resource fixes on `main` preserve v1.1 download URLs and exclude temporary QA files from `gh-pages`; no substantive prose or v1.2 asset changed. The next phase needs a new approved goal and scope.

## Important future backlog

For a later handbook version, add a section on AI-assisted open-science release workflows: maintain complete local project assets, deliberately select non-sensitive public artifacts, generate/update README/data dictionaries/code/environment metadata, scan for secrets and sensitive content, and maintain public releases when analyses change. Human review remains mandatory for anonymization, consent, and third-party data licensing.
