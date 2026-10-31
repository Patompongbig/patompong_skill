# Optional explicit-use prompt

Normal Codex use needs no startup prompt. Use this template only when you want
to select a toolkit workflow or skill on a host without instruction routing.
Replace the placeholders before sending it.

```text
Use .agents/workflows/<workflow-name>.md for this task, or use the named
.agents/skills/<author>/<skill>/SKILL.md as a lone skill. Read the selected
entry point and its relevant dependencies only. Keep this selection until I
change it; "return to normal Codex" clears it. Applicable project and host
instructions still apply.

My task: <desired outcome and constraints>
```
