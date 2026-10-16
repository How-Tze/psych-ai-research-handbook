# Current phase

- Phase: v1.3 Release Gate
- Status: IN_PROGRESS — TASK-014
- Approval: 2026-10-16 — human approves the complete integrated edition and authorizes PDF/DOCX generation and inspection, final QA, publication of v1.3, historical preservation and legacy-link compatibility.
- Frozen content input: `2271f1cbf9a122b56894edb63c9d01fbf63b237a`; PR #3.
- Target: v1.3 HTML, PDF, DOCX and teaching materials; public edition remains v1.2 until deployment completes.
- Branch: docs/v1.3-authoring-preparation.

## Goal, scope and responsibilities

TASK-013 is accepted. Codex executes TASK-014 end to end under the approved release gate: final metadata, print exports and inspection, final checks, PR readiness/merge, tag, Release/assets, gh-pages deployment, public smoke tests and recovery documentation. Substantial prose is frozen; no new scientific content or product facts.

## Dependencies and deliverables

Use the nineteen integrated texts and 34 teaching resources from the frozen commit. Deliver matching HTML/PDF/DOCX, teaching ZIP, immutable v1.3 tag and Release, working current and historical downloads and legacy entries. Preserve original source data, programs, numerical results, candidate files, CC BY 4.0 and the pre-existing untracked audit report.

## Acceptance and constraints

Follow TASK-014. Verify print content, native equations, navigation, tables, figures, pagination and final page images; full HTML build, local links, resources and narrow layout; clean tracked scope; public downloads and Release asset hashes. Baseline v1.1/v1.2 tags, Release metadata and frozen file hashes before mutation. Use actual publication date. Temporary files remain ignored. No changes to Start Guide.

## Gates, escalation and exit

Human release authorization is complete; do not request approval for routine release actions. Escalate scientific/scope/version changes, conflicting authority, risks to historical snapshots or unfixable technical failures. Mark DONE only after merge, tag, Release, deployment and public verification, then record final evidence and leave a recoverable clean state.

## Previous phases

TASK-003–013 are DONE. v1.3 authoring was accepted at db54a0b and integration at 2271f1c on 2026-10-16. v1.2 was released on 2026-09-24 at a8a9326; historical snapshots remain frozen.
