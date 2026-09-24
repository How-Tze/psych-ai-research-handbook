# AGENTS.md

These instructions apply to the entire repository.

## Mission
Maintain and publish the stable online reading edition of 《心理学研究的 AI 进阶手册》. The repository is a publication project, not a sandbox for adding new AI frameworks or product catalogs.

## Source-of-truth rules
- The existing `release/*_v1.1_*` PDF/DOCX files are frozen v1.1 artifacts. Never modify or replace them. Once a later release is published, its tagged source and assets are likewise frozen.
- `chapters/*.qmd` is the source for the current HTML reading edition; the `v1.1` tag preserves the historical v1.1 text.
- HTML-only transformations are allowed when they preserve wording and meaning (navigation, callouts, responsive tables, accessible link text).
- Substantive edits require a new handbook version or explicit author approval.

### Canonical project state
Chat history is not a project database. Use this hierarchy:

1. Release tags and assets: frozen publication snapshots.
2. `main`: current stable repository state.
3. `CURRENT_PHASE.md`: canonical state of the active phase.
4. `DECISIONS.md`: durable decisions and rationale.
5. `tasks/*.md`: executable task specifications.
6. `HANDOFF.md`: compact project-level recovery summary.

Temporary chats, agent reasoning, audit logs, and local scratch files are non-canonical. Do not move sensitive or restricted research data into Git merely to make it available to agents.

## Phase-governed work

- Organize substantial work into approved phases. Each active phase defines its goal, scope, workstreams, dependencies, deliverables, acceptance criteria, constraints, decision gates, escalation conditions, and exit criteria.
- Agents should execute approved tasks within an approved phase without requesting every next action. They may inspect, implement, test, revise, and update task status, `CURRENT_PHASE.md`, and durable documentation explicitly required by the task.
- Resolve routine execution questions from repository rules and task acceptance criteria: tests, file completeness, specified links, spec conformance, and formatting or maintenance choices.
- Escalate strategic questions: scope or handbook structure changes; substantive claims; schema or canonical-state design; invalidated assumptions or acceptance criteria; conflicting authoritative sources; version or release strategy; or work beyond the approved phase. Stop or mark the task `BLOCKED` at an escalation condition.
- Keep repeatable or consequential prompts as tracked task specifications under `tasks/`, rather than only in chat. Use the fields and status lifecycle in `tasks/README.md` and `tasks/TASK_TEMPLATE.md`.
- Parallel agents should take only sufficiently independent tasks. Use separate branches or worktrees when edits may overlap. Parallelism can reduce elapsed time, but does not imply lower compute use; do not create workstreams merely because concurrency is available.

### Approved release gates

- Once a human has approved a phase gate, frozen scope, and defined acceptance criteria for a routine release, Codex has end-to-end execution authority for that release: final QA, version metadata, PR readiness and merge, tag, GitHub Release and assets, site deployment, smoke tests, and canonical-state updates. Do not request approval for each mechanical step.
- The phase gate or explicit instruction is the human authorization for these actions; it does not transfer scientific, editorial, or strategic judgment to an agent.
- Stop and escalate if substantive content or scope changes; the version strategy must change; approved prose or governing rules conflict; merge, build, deployment, or QA fails without a safe mechanical fix; historical tags, releases, or frozen assets might change; or a new schema, framework, or publication-strategy decision is needed. Fix routine technical problems within the approved scope and continue.

### Responsibilities and authoring gate

- **Human:** owns project direction, approves phase goals and substantive changes, authorizes merge, release, and deployment through a phase gate or explicit decision, and makes final scientific, editorial, and publication judgments.
- **Strategic / Authoring Chat:** handles phase design, conceptual architecture, substantial handbook prose, major editorial rewriting, trade-off analysis, escalation, adversarial review, and phase review. It should not mediate routine execution.
- **Execution agents:** inspect and implement repository work; locate content; prepare writing briefs and source evidence; operate on files; test, render, and run QA; synchronize documentation; and integrate approved prose. They must not autonomously author substantial new handbook prose unless a task explicitly grants that authority.
- Substantial reader-facing prose passes an Authoring Gate: an execution agent prepares a Writing Brief, marks the task `REQUIRES_CHAT_AUTHORING`, obtains an explicitly approved draft through Strategic / Authoring Chat, then makes only mechanical integration changes unless further editorial authority is granted.

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
- Do not merge a branch into `main` without a human-approved release/merge gate or explicit approval.
- Prefer small, coherent commits.

### Content freeze
Within a frozen release scope:
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
- Do not run a production deployment or `quarto publish gh-pages` without a human-approved release gate or explicit instruction. Once authorized, complete deployment and smoke tests under the approved scope.

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
