# Initial toolkit validation

Validated on Windows on 2026-10-07. Project-local evidence belongs here, outside
the portable `.agents` folder.

Inspection found an empty workspace with no existing root or ancestor instruction
files, root override, or project-local skills/configuration. The relevant global
configuration search found no custom skill-discovery or project-document settings.
Only system skills were present in the inspected global skill directory. No global
files were modified. Discovery conventions were checked against
[official skill documentation](https://learn.chatgpt.com/docs/build-skills) and
[official instruction documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Commands completed:

```sh
python -B .agents/scripts/validate.py --project-root .
python -B -m unittest discover -s tests -v
```

Static validation passed for all three skills and this project's root activation.
All 13 packaging tests passed. Each test copied the toolkit into a newly created
temporary sample project whose path contained a space. Checks covered preservation
of UTF-8/BOM and CRLF project guidance, idempotent activation, copied helpers run
from a different working directory, rejection of overrides/foreign targets/changed
markers, disable and re-enable file states, status-only disabling failure, broken
and escaping links, missing metadata/manifests, duplicate names, unsupported scalar
metadata, machine paths, and private-key-like text. Temporary projects were cleaned
up after the tests.

Static trigger review:

| Skill | Intended example | Unrelated example excluded by description |
| --- | --- | --- |
| toolkit-maintain | Disable a portable toolkit skill | Implement a project API endpoint |
| toolkit-maintain (evaluation) | Compare third-party documentation skills without installing | Recommend an unrelated consumer product |
| diagnose-bug | Investigate a reproducible parser failure | Plan an unrelated new feature |
| review-change | Review an existing diff without editing | Diagnose a reported test failure |

These cases are a description/instruction review, not observed model routing.
Native skill discovery, actual trigger behavior, and instruction following have
not been tested in a fresh Codex session. Linux execution has not been tested.
The optional helpers use platform-independent Python standard-library APIs.

The bundled skill-creator `quick_validate.py` was attempted but could not complete
because its PyYAML dependency is absent. No dependency was installed. The toolkit's
own standard-library metadata/reference validator completed successfully; its
documented limitations still apply.
