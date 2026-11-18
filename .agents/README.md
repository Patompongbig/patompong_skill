# Patompong agent toolkit

Opt-in workflows and skills for coding agents (Claude Code, Codex, Gemini). Copy
this whole `.agents` folder into a project. Nothing here is active until the user
selects it.

## For agents

**Default is normal agent behavior.** Do not read files under `.agents/` unless
the user explicitly selects a workflow or skill. When they do:

| User says | Read |
| --- | --- |
| "Use workflow `<name>`" | `workflows/<name>.md`, then only what it links, when needed |
| "Use skill `<author>/<name>`" or "lone-skill …" | `skills/<author>/<name>/SKILL.md` (personal skills: `skills/<name>/SKILL.md`) |
| A catalog ID such as `M23`, or "help me pick a skill" | The matching entry in [CATALOG.md](CATALOG.md) |
| "What workflows are there?" | [workflows/INDEX.md](workflows/INDEX.md) |

The selection lasts across follow-ups and compaction until the user switches or
says "return to normal mode", which clears every workflow-specific rule. A new
session starts in normal mode. Selecting or creating a workflow never grants tool
permissions beyond the host's.

## Contents

```text
.agents/
  README.md          this file — the only entry point
  workflows/         INDEX.md (menu) · one file per workflow · references/ (shared rules)
  skills/            personal skills, plus mattpocock/, obra/, ponytail/ collections
  CATALOG.md         every skill: purpose, needs, overlap — read on demand
  COMPATIBILITY.md   host requirements and model-name mapping per host
```

## Activate in a project

Copy `.agents/` into the project root, then add this block to the project's
`AGENTS.md` (create it if missing; keep existing content). On a host that does
not read `AGENTS.md`, paste the same text as your first message instead.

```markdown
<!-- personal-toolkit:begin -->
## Agent toolkit (opt-in)

Default: normal agent behavior. Do not open or read anything under `.agents/`
unless the user explicitly selects a workflow or skill.
- "Use workflow <name>": read `.agents/workflows/<name>.md`, then only what it links.
- "Use skill <author>/<name>" or a catalog ID: read `.agents/README.md` for where to look.
- "What workflows are there?": read `.agents/workflows/INDEX.md`.
The selection lasts until the user says "return to normal mode".
<!-- personal-toolkit:end -->
```

Project documents produced by the workflows live in `patompong-docs/` at the
project root, never inside `.agents/`.
