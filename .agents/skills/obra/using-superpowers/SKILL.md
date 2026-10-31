---
name: using-superpowers
description: "Use when the user explicitly selects Superpowers routing or asks how its installed skills fit a chosen task."
---

## Portable scope and invocation

This local copy runs only after explicit user selection or as a relevant
dependency of the selected workflow/skill. Installation does not activate it.
Read named dependencies directly at their recorded manifest paths; read no
unrelated skills. The selected workflow and user/project instructions control
scope and authorization, including any already-approved implementation.
Upstream mandatory language applies within the assigned skill's scope, not
as global session routing. Preserve proportional checks for low-impact edits;
do not delete existing work to satisfy a test-first ritual. Use Bash helpers
only in Bash, after inspection; native equivalents may implement the same
documented ledger/diff behavior. Keep all task artifacts in the target project.
Read `[collection compatibility](../COMPATIBILITY.md)` when a platform/resource
requirement is relevant. No startup hooks or global configuration are installed.

# Using Superpowers in the portable toolkit

This collection is explicit-only. Normal Codex sessions require no toolkit
preprompt, workflow selection question, or automatic activation of this collection.
Offer the small workflow menu only when the user asks for workflow choices.

After the user selects a workflow or lone skill, read its assigned entry point.
Read only relevant dependencies as the selected skill reaches them. Keep the
session selection until the user changes it. Returning to normal/default Codex
clears the selection. Installation itself selects nothing.

For user-requested selection help, use the Superpowers section of the overall
catalog. Explain the tradeoff between inline execution with a final review and
per-task implementation/review agents. Follow the user's chosen method.

Resolve a Superpowers dependency directly as
`.agents/skills/obra/<skill>/SKILL.md`; do not scan unrelated skill bodies.
For Codex tool adaptation, read [the portable reference](references/codex-tools.md)
only if that task needs it. Other platform references are bundled for use on
those hosts, not automatic dependencies in a Codex session.

Applicable user/project instructions and higher-priority rules control scope,
permissions, verification, model selection and reading. Original upstream's
automatic startup and 1-percent relevance mandate are intentionally replaced
in this local copy by explicit selection and normal Codex behavior by default.
