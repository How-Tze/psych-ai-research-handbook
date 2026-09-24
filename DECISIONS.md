# Decisions

Durable project decisions. Change a decision through explicit review; do not silently overwrite its rationale.

| ID | Date | Decision | Rationale | Status |
| --- | --- | --- | --- | --- |
| D-001 | 2026-09-23 | Chat history is non-canonical; repository state is canonical. | Agents need a recoverable, reviewable project state. | Adopted |
| D-002 | 2026-09-23 | Govern substantial work by phases rather than Chat-mediated steps. | Approved scope and gates permit routine execution without serial mediation. | Adopted |
| D-003 | 2026-09-23 | Place substantive multi-agent workflow content primarily in the Agent/workflow chapter. | Chapter 9 already covers fixed work, scripts, and Agents. | Planning decision; content gated |
| D-004 | 2026-09-23 | Put changing model tiers, prices, interfaces, and product advice primarily in the dynamic Start Guide. | The handbook should retain stable, vendor-neutral methods. | Adopted |
| D-005 | 2026-09-23 | Keep the v1.1 release frozen; place substantive additions in a future version. | Maintenance must not silently revise the publication snapshot. | Adopted |
| D-006 | 2026-09-23 | The governance phase gate has passed; target the multi-agent workflow update for v1.2 and prepare its Authoring Gate package first. | Pre-authoring review can proceed while substantive prose, release metadata, merge, and deployment remain separately gated. | Adopted |
| D-007 | 2026-09-23 | The TASK-001 Authoring Gate passed; `drafts/TASK-001-approved.md` is the authoritative prose for mechanical v1.2 integration. | Reader-facing wording is controlled by the approved draft; release metadata, public labels, merge, and deployment remain separate decisions. | Adopted |
| D-008 | 2026-09-24 | Apply the human-approved TASK-001 minor editorial review patches without a new Authoring Gate. | The bounded replacements refine the integrated wording and are reflected in the authoritative draft; remaining QA gates still apply. | Adopted |
| D-009 | 2026-09-24 | Enter the v1.2 Release Gate with frozen scope: PR #2 is the primary content range, TASK-001 is done, and the theme is Multi-Agent Workflow / Agent Governance. Use the actual release date; preserve all v1.1 snapshots. | The human approved v1.2 publication and its boundaries. | Adopted |
| D-010 | 2026-09-24 | After an approved phase gate with frozen scope and clear acceptance criteria, Codex executes routine release steps end to end without stepwise approval, including QA, metadata, PR readiness/merge, tag, Release/assets, deployment, smoke tests, and canonical-state updates. Escalate only the conditions in `AGENTS.md`. | Release execution should not become serial Chat-mediated work once strategy and authority are settled. | Adopted |
