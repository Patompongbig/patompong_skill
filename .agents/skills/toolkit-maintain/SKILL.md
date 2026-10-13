---
name: toolkit-maintain
description: "Maintain this portable personal .agents toolkit: find and evaluate third-party skills, create or edit reusable instructions, and import, disable, remove, or validate toolkit skills. Use for personal toolkit management, not ordinary project implementation or unrelated global agent configuration."
---

# Maintain the personal toolkit

Locate this toolkit using this skill's file location: its root is two directories
above this skill folder. Read relevant existing instructions for the assigned maintenance operation.
Read [the catalog](../../CATALOG.md) only when the user asks for skill browsing,
selection help, tree details, or catalog maintenance; routine session workflow
selection does not authorize catalog reading.
Read [the README](../../README.md) when changing layout, activation, or portability.

For creation and updates:

1. Establish the repeatable job, appropriate trigger, and completion condition.
   Extend a suitable existing skill rather than adding an overlapping entry.
2. Keep the entrypoint focused, with standard `name` and `description` frontmatter.
   Bundle relative resources only when needed. Preserve user intent; do not turn
   a one-off example into a personal preference. Keep project context elsewhere.
3. Include an example invocation, exclusions that prevent likely misrouting, and
   a clear completion condition. Inspect any executable resource before running it.
4. Keep catalog, relevant docs, and [changelog](../../CHANGELOG.md) consistent.
   Use [the validator](../../scripts/validate.py) when Python is available; otherwise
   inspect metadata, names, links, file states, and portability manually and say so.
5. Compare one intended trigger and one unrelated request against the description.
   Label this a static review unless actual host behavior was tested. Run changed
   scripts with meaningful cases and report observed results and limitations.

For finding or importing skills, read
[import guidance](references/imports.md) only when needed. Installing into this
toolkit does not authorize global configuration changes or account actions.

To disable, rename the target `SKILL.md` to `SKILL.md.disabled` in the same folder
and update its catalog link, status, and other links to that manifest. Ensure the
original filename is gone.
Reverse both changes to re-enable; use a fresh session after disabling. For removal,
confirm the precise skill folder, remove its row and obsolete references, and
record the change. Do not remove unrelated same-name skills from other locations.

Example: `$toolkit-maintain Disable review-change and validate the toolkit.`

Evaluation example: `$toolkit-maintain Find and evaluate a few third-party skills
for writing technical documentation. Read their instructions and recommend which
to reuse, adapt, or skip; do not install yet.`

Complete when requested changes exist, catalog/docs match the file state,
appropriate checks have run or their unavailable prerequisites are reported,
and the outcome plus any activation/restart requirement is explained.

## Compose or edit a workflow

When the user assigns workflow creation or editing, read
[workflow composition](references/workflows.md) and the specifically named skills.
Existing personal skills stay flat; outside imports use
`skills/<author>/<skill>/SKILL.md`. Preserve author grouping when importing.
