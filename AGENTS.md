<!-- personal-toolkit:begin -->
## Agent toolkit (opt-in)

Default: normal agent behavior. Do not open or read anything under `.agents/`
unless the user explicitly selects a workflow or skill.
- "Use workflow <name>": read `.agents/workflows/<name>.md`, then only what it links.
- "Use skill <author>/<name>" or a catalog ID: read `.agents/README.md` for where to look.
- "What workflows are there?": read `.agents/workflows/INDEX.md`.
The selection lasts until the user says "return to normal mode".
<!-- personal-toolkit:end -->
