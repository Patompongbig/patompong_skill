# lone-skill workflow

> Use one named skill, with the dependencies it needs, without a composed
> workflow.

Shared rules: [development handoff](references/development-handoff.md#baseline-boundaries)
Read a reference only when a step needs it.

## Purpose

For tasks a single skill covers well. The skill governs the work; the toolkit's
baseline boundaries still apply.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **skill** (only mode) | The user names a skill or catalog ID | Whatever the skill and the user's request authorise | The skill's own completion condition |

## Inputs

The skill name (`author/skill`, personal skill name, or catalog ID such as
`M23`) and the task.

## Outputs

As defined by the skill, inside the target project, never inside the portable
toolkit.

## Roles and models

Main session, plus any subagents the skill itself directs (default models per
[agent roles](references/agent-roles.md#roles)). No model prompt unless the
user names models.

## Procedure

1. **Resolve the skill.** Read its manifest directly: personal skills at
   `skills/<name>/SKILL.md`, imported skills at `skills/<author>/<name>/SKILL.md`.
   Read the [catalog](../CATALOG.md) only to look up a catalog ID or when the
   user asks for help choosing. Ask when a name is genuinely ambiguous.
2. **Follow the skill** and the dependencies and references it needs.
3. **Keep the selection** for the session. A newly named skill replaces it. If
   the current skill cannot handle the next task, ask which skill to use rather
   than switching silently.

## Boundaries

The skill cannot widen the [baseline boundaries](references/development-handoff.md#baseline-boundaries):
no commits or pushes, no agent-configuration edits, no installs or external
writes without explicit assignment.

## Done when

The skill's completion condition is met for the user's task.

## Example invocations

- "Use lone-skill mattpocock/handoff to summarise this task for another session."
- "Use lone-skill M13 to run a retro on this session."
