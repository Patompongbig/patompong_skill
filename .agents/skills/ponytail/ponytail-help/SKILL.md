---
name: ponytail-help
description: "Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, \"ponytail help\", \"how do I use ponytail\"."

---

## Portable invocation

Use this skill only after the user selects it directly or through the session's
chosen workflow. Keep the toolkit's session routing and agreed scope. This copy
does not install plugin hooks, write global mode flags, or activate at startup.
Native slash/plugin commands below are upstream aliases: for this toolkit, read
the corresponding `.agents/skills/ponytail/<skill>/SKILL.md` directly, only when
requested or needed by the selected workflow. Preserve requested explanation
depth and project verification requirements. Use `rg` or a native equivalent
for upstream grep/Bash search examples on Windows.

# Ponytail portable help

Read this reference only when requested or assigned by a selected workflow.

| Skill | Purpose |
| --- | --- |
| [ponytail](../ponytail/SKILL.md) | Smallest complete implementation; lite/full/ultra |
| [ponytail-review](../ponytail-review/SKILL.md) | Evidence-backed review of a change; report only |
| [ponytail-audit](../ponytail-audit/SKILL.md) | Ranked repository/subsystem assessment; report only |
| [ponytail-debt](../ponytail-debt/SKILL.md) | Collect shortcut markers and upgrade triggers |
| [ponytail-gain](../ponytail-gain/SKILL.md) | Display published benchmark evidence, not current-project savings |
| [ponytail-help](SKILL.md) | This reference |

## Selecting a skill and mode

Ask the agent to use `ponytail/ponytail-review`, or assign its exact path in your
workflow. Example: "Use lone-skill ponytail/ponytail in lite mode for this task."
Do not read all six skill bodies just to present this reference.

- Lite: implement the agreed request; mention a smaller option for the user to choose.
- Full: apply the complete simplification ladder after understanding the task.
- Ultra: also question unjustified scope before implementation.

Full is the core skill's default level after explicit activation, not a startup
default. Retain a selected core mode within the session until the user switches
it, says "stop ponytail", or requests normal mode. Turning the modifier off does
not replace the selected session workflow. This installation uses no global
configuration file or lifecycle hook.

## Updates and other hosts

This portable collection is pinned; it does not auto-update. Refresh it only on
the user's request, preserving local adaptations and reviewing source changes.
Native plugin commands, global mode settings and automatic updates belong to a
separate host-plugin installation. See [provenance](../PROVENANCE.md) for the
upstream source and adaptations.
