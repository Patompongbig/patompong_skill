# Session workflow routing

This file routes a session; it is not an automatically selected build workflow.

1. Read applicable project instructions and personal preferences.
2. If this session has no selected workflow or lone skill, use the small menu
   in [INDEX.md](INDEX.md) to ask which to use, then wait. Read no full catalog or
   skill bodies to compose that question. A choice in the opening user prompt
   already answers the question. An explicit skill invocation is a lone-skill
   selection unless the user also assigns a workflow.
3. Read the selected workflow file, then its skill entry points as each step
   needs them. The paths in the workflow fix those entry points. Skills follow
   relevant dependencies themselves; this is not a closed allowlist. Resolve a
   named dependency directly in its author group rather than inspecting unrelated
   skills. Supporting resources are loaded only for the current task/branch.
4. Respect the selected workflow's conditional dependencies and scope adaptations;
   a skill dependency does not override review-only mode or authorize extra effects.
   For an explicitly requested combination or ordered chain, identify the active
   stage and apply its boundaries. Interview can clarify that stage; ask-answer
   cannot authorize writes. No automatic stage switch follows artifact acceptance.
   Keep the selection across messages, new tasks within this session, and
   compaction. Change it when the user asks; do not ask again for every task.
5. When the user names a lone skill, read its manifest directly. If they ask for
   help choosing a skill or details of the tree, read [the catalog](../CATALOG.md)
   and only the skill detail needed for that request. Catalog reading is not a
   routine prerequisite for task execution or session workflow selection.
6. Maintain the assignment's scope and appropriate verification. Report actual
   changes, checks, and unresolved runtime prerequisites. A workflow cannot turn
   an explanation into edits or provide permissions absent from the user's task.

For a known custom workflow, read `.agents/workflows/<name>.md` directly. If the
path is missing or a name is ambiguous, ask for the intended file/name instead
of loading the whole skill tree. Host-mandated system/plugin skills remain subject
to higher-priority instructions; portable rules control this toolkit's copies.
