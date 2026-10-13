# <workflow-name>

Purpose: <repeatable outcome this combination should produce>.

## Inputs and scope

<Required project/task information; whether this is explanation, planning,
review, or implementation; any actual runtime or tracker prerequisites.>

## Steps

1. Read `.agents/skills/<author>/<skill>/SKILL.md` when this step begins.
   <What to do, the artifact it produces, and how to know the step is complete.>
2. <Next skill entry point, conditional branch, or handoff; include only steps
   needed for this workflow. Skills follow their own relevant dependencies.>

## Deliverables and completion

<Concrete output locations and observable completion conditions.>

## Example invocation

Use workflow <workflow-name> for <task>.

Use target-project-relative paths for project outputs. Supporting resource links
resolve from the skill that owns them. Store this file as
`.agents/workflows/<workflow-name>.md` and add one row to workflows/INDEX.md.
The full catalog is consulted for user-requested discovery, not every execution.
