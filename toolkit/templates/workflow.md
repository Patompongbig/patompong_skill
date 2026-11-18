# <workflow-name> workflow

> <One sentence: the repeatable outcome this workflow produces.>

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[glossary](references/glossary.md)

## Purpose

<What problem this stage solves, where it sits in the pipeline, and what it
deliberately does not do. Two to five sentences.>

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| review | <trigger> | Nothing; findings in chat | <exit artifact> |
| create | <trigger> | <owned files> | <exit artifact> |
| update | <trigger> | <owned files> | <exit artifact> |

<Default mode when the request does not name one.>

## Inputs

<Required and optional inputs, with their owning files. State which missing
input blocks the stage and which only limits it.>

## Outputs

<Owned files this workflow may write (target-project-relative), and inputs it
reads but never edits.>

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| <role> | <model> | <read-only / writes owned files> | <one line> |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Procedure

1. **<Phase name>.** <Intent, key obligations and judgement calls. Describe what
   good looks like, not keystrokes.> *Exit:* <observable condition>.
2. **<Phase name>.** <...> *Exit:* <...>.

## Gates

- **Entry:** <conditions that must hold before the first write>.
- **Exit:** <conditions that must hold before the stage reports done>.

## Boundaries

<Only rules specific to this stage. Shared rules live in the references above
and are linked, never restated.>

## Done when

<Observable completion conditions, including what is handed to the next stage.>

## Example invocations

- "Use workflow <workflow-name> to <task>."

<!-- Links are written for the destination. Store as .agents/workflows/<workflow-name>.md and add one row to
workflows/INDEX.md. Use target-project-relative paths for project outputs. -->
