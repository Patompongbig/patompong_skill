# Toolkit maintenance

Source-repository files for maintaining `.agents/`. Never copied into projects;
agents using the toolkit never need them.

| Path | Purpose |
| --- | --- |
| `CHANGELOG.md` | Meaningful toolkit changes |
| `BACKLOG.md` | Parked ideas and decisions not taken |
| `VALIDATION.md` | Historical record of observed checks |
| `IMPORTS.json` | Imported skills: source revisions, licenses, upstream and installed hashes |
| `PREFERENCES.md` | Personal preferences for toolkit work |
| `templates/workflow.md` | Fixed structure for new workflows |
| `scripts/validate.py` | Read-only static checks of `.agents/` (metadata, links, integrity, menu) |
| `scripts/activate.py` | Append the activation block from `.agents/README.md` to a project's `AGENTS.md` |

```sh
python toolkit/scripts/validate.py                                   # this repo's .agents
python toolkit/scripts/validate.py --project-root .                  # also check AGENTS.md activation
python toolkit/scripts/validate.py --agents /proj/.agents --project-root /proj
python toolkit/scripts/activate.py --project-root /proj              # after copying .agents into /proj
```

When an imported skill file is edited deliberately, refresh its `installed_sha256`
in `IMPORTS.json` after review and keep `upstream_sha256`. Workflow and skill
maintenance uses the `toolkit-maintain` skill in `.agents/skills/`.
