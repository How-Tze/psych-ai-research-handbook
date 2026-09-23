# Tracked tasks

A tracked task is a repository specification for bounded, reviewable work. Create one when work is repeatable, consequential, spans agents or sessions, or needs explicit acceptance and escalation rules. Small routine fixes can remain in a normal issue or commit.

Use `TASK_TEMPLATE.md`. A task belongs to the phase named in `CURRENT_PHASE.md`; it cannot expand that phase's authority. The phase file tracks the active plan, while each task defines its executable scope and completion evidence.

## Status lifecycle

`PLANNED` → `READY` → `IN_PROGRESS` → `REVIEW` → `DONE`.

Use `BLOCKED` when an escalation condition prevents progress; return to `READY` or `IN_PROGRESS` after resolution. Use `CANCELLED` when the task is withdrawn. `REQUIRES_CHAT_AUTHORING` is an Authoring Gate marker, not a status value. A completed Writing Brief can enter `REVIEW` for the Authoring Gate; the marker and `REVIEW` do not authorize prose drafting or integration. After approval and new authorization, return to `IN_PROGRESS` for the authorized work. Use `BLOCKED` if an unresolved escalation prevents the gate from proceeding.

Agents resolve routine implementation questions against the task acceptance criteria and repository rules. Stop and escalate changes to phase scope, substantive claims, handbook structure, canonical state, release strategy, or invalid assumptions and conflicting authoritative sources. Human approval controls substantive changes, merge, release, and deployment.
