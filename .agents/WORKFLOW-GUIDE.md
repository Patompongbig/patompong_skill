# Optional workflow guide

This is reference documentation, not a workflow or a required startup read.
Normal Codex behavior is the default: respond to the task under applicable host
and project instructions, with no toolkit preprompt, selection question, or
automatic activation of local skills. Installing this folder does not select
a workflow. Mandatory host/system/plugin instructions still apply.

## Choose a workflow or skill when wanted

- An explicit request such as "Use workflow interview" selects that workflow.
  Read `.agents/workflows/<name>.md`, then its entry skills and relevant
  dependencies as needed. An explicit skill invocation selects that lone skill
  unless the user also assigns a workflow.
- If the user asks for workflow choices, use [the small menu](workflows/INDEX.md).
  Ask for clarification only when their requested selection is ambiguous; do
  not ask for a selection before ordinary tasks.
- Read [the catalog](CATALOG.md) for requested skill browsing, selection help,
  tree details, or catalog maintenance. Read [usage examples](WORKFLOW-USAGE.md)
  when needed for an explicitly chosen development sequence.
- Read [personal preferences](PREFERENCES.md) when relevant to toolkit work;
  they are optional reference guidance, not an extra startup requirement.

## Continue, switch, or return to normal

Keep an explicitly chosen workflow or skill across follow-ups and compaction
until the user changes it. A new session starts in normal mode unless the user
selects a workflow or skill again.

"Return to normal Codex", "use default mode", and "stop using the workflow"
clear the custom selection. Default mode has no workflow file or skill chain.
Previous workflow-specific procedures and restrictions stop applying; explicit
user task constraints and applicable host/project instructions still apply.
The former `workflows/default.md` is retired; do not try to load or recreate it
when returning to default mode. This guide is optional reference documentation.

Respect the active stage's scope for selected combinations. Accepting an artifact
does not automatically select another stage. Read only relevant dependencies;
resolve named skills directly instead of inspecting unrelated bodies.

[Feature-and-architect](workflows/feature-and-architect.md) is an optional living
implementation-guide workflow. Select it alone for documentation, or explicitly
combine it with planning/execution to maintain explanations beside a feature plan.
Its presence on disk does not activate it; the combination ends when switched away
unless explicitly retained. It explains actual code, with missing behavior reported
as gaps, and grants no changes to governing requirements or plan scope.

For a custom workflow, read its exact file. If missing or ambiguous, clarify the
requested name without scanning the full skill tree. Creating or editing a
workflow does not activate it unless the user also requests that switch.

Keep project notes and credentials outside the portable toolkit. Workflow
instructions cannot grant tool permissions or override the user's assignment.
