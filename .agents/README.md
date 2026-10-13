# Patompong portable skills and workflows

Copy this complete `.agents` folder into a project. Keep existing project
guidance and merge any existing toolkit files deliberately. Nothing here requires
a global skill installation, symlink, account, background service, or auto-update.

## Navigation

| Location | Purpose |
| --- | --- |
| [PREFERENCES.md](PREFERENCES.md) | Personal session and working defaults |
| [workflows/default.md](workflows/default.md) | Session selection and reading rules |
| [workflows/INDEX.md](workflows/INDEX.md) | Small session menu; seven available workflows |
| [WORKFLOW-USAGE.md](WORKFLOW-USAGE.md) | Development sequence, project layout and example prompts |
| [CATALOG.md](CATALOG.md) | Detailed overall catalog; read when requested |
| [skills/mattpocock/](skills/mattpocock/) | All 38 downloaded Matt skills and their resources |
| [skills/ponytail/](skills/ponytail/) | All six Ponytail skills; explicit-only; benchmark evidence bundled |
| [skills/obra/](skills/obra/) | All 15 Superpowers skills and their supporting resources; explicit-only |
| [templates/workflow.md](templates/workflow.md) | Create a reusable skill combination |
| [COMPATIBILITY.md](COMPATIBILITY.md) | Host/tool requirements and path-based invocation |
| [IMPORTS.json](IMPORTS.json) | Source revision, license, original and installed hashes |
| [scripts/activate.py](scripts/activate.py) | Optional append-only project activation |
| [scripts/validate.py](scripts/validate.py) | Read-only packaging, policy, paths, integrity checks |
| [STARTUP.md](STARTUP.md) | Session prompt when root activation is unavailable |
| [CHANGELOG.md](CHANGELOG.md) | Meaningful changes |
| [VALIDATION.md](VALIDATION.md) | Observed checks and remaining host acceptance tests |

## Folder conventions

Outside collections: `.agents/skills/<author>/<skill>/SKILL.md`.
Matt collection: `.agents/skills/mattpocock/<skill>/SKILL.md`.
Ponytail collection: `.agents/skills/ponytail/<skill>/SKILL.md` (user-selected collection group).
The three original personal skills retain their existing flat paths.
Skill names remain unique locally; authors are navigation groups, not duplicate
wrappers. Supporting resources stay beside their original manifest. MIT license
and additional credits are retained; no upstream executable was run at import.

## Activate in another project

1. Copy the complete `.agents` folder. If one exists, compare and merge without
   replacing unrelated guidance or skills.
2. Append [the activation section](templates/activation.md) to the project's
   AGENTS.md, or run `python .agents/scripts/activate.py` from that project root.
   For an old differing activation section, reconcile it manually; the helper
   preserves bytes and refuses to overwrite it. If a root override exists,
   integrate into the applicable instruction file after inspection.
3. Run `python .agents/scripts/validate.py --project-root .` and start a fresh
   session. On systems without `python`, use an available Python 3.9+ command.

If root instruction routing is unavailable, paste [STARTUP.md](STARTUP.md).
Native nested discovery depends on the host; exact workflow/file paths are the
fallback. Fresh-session discovery and reading behavior remain acceptance checks.

## Session behavior

The agent asks for your workflow once at session start unless you already named
it. It reads only the small menu to ask; it does not read every skill or the full
catalog. It keeps the choice across follow-ups, tasks, and compaction until you
change it. Selected skills can navigate their relevant dependencies and resources.
Ask to browse/select skills or inspect the tree to open the detailed catalog.

Examples: "Use workflow interview for this design", "Use workflow execute-development
for the accepted feature plan", "Use lone-skill mattpocock/handoff", or "Show me the skill catalog".
To switch: "Switch this session to ask-answer." To create: "Use toolkit-maintain to
create my workflow <name> combining <skills>." Keep the small menu in sync.

For chat-only explanation, select "Use workflow ask-answer." This self-contained
workflow reads relevant context without editing files or running tests, builds,
or applications. It has no skill dependencies and stays read-only until you
explicitly switch workflows. See [ask-answer](workflows/ask-answer.md).

For requirements work, select "Use workflow software-requirement-creation."
It scopes inspection to a relevant feature and connected flows, uses domain-modeling,
and offers research only for user selection. Review produces findings; confirmed
create/update assignments maintain requirements and related system context without
an implementation plan. Outputs stay in the target project's `patompong-docs/docs/`;
existing documents elsewhere are reference sources. Development plans belong in
`patompong-docs/implement-plan/` when a planning workflow is selected. See
[software-requirement-creation](workflows/software-requirement-creation.md).

For implementation planning, select "Use workflow writing-development-plan."
It uses obra/writing-plans and mattpocock/codebase-design to turn agreed requirements,
existing contracts/tests and relevant current code
into ordered, checkable end-to-end tasks. Plans stay in the target project's
`patompong-docs/implement-plan/<feature>/plan.md`. It writes planning documents
only and does not start implementation or select execution skills. See
[writing-development-plan](workflows/writing-development-plan.md).

For contracts and executable tests, select "Use workflow test-and-contract-creation."
It defaults to contract definition, test authoring and Red verification for user
review, using verification-before-completion and focused test-writing guidance.
Full test-driven-development is selected only when you explicitly request minimal
production code for a bounded behavior. Contracts live in
`patompong-docs/docs/contracts/<feature>/`; tests and evidence live in
`patompong-docs/tests/<feature>/`. See
[test-and-contract-creation](workflows/test-and-contract-creation.md).

For feature implementation, select "Use workflow execute-development."
It executes an accepted plan with protected contracts/tests, Green verification,
root-cause debugging and iterative risk-based QA. Seven skills load by phase,
including Ponytail full for the smallest complete implementation within the accepted
design; execution and review remain coordinated in one workflow. Progress and QA records stay beside
`patompong-docs/implement-plan/<feature>/plan.md`. Completion requires fresh required
gates and resolved blocking findings; delivery actions remain explicitly scoped.
See [execute-development](workflows/execute-development.md).

## Runtime scope and updates

62 instruction skills are installed, including seven experimental Matt skills.
Project runtimes, tracker credentials, Bash/Node utilities, Claude-only hooks,
and subagent availability are separate prerequisites in [compatibility](COMPATIBILITY.md).
Downloading the collection does not run M14 target-project setup. Local task
files avoid tracker accounts. Project notes, glossaries, plans, and secrets remain
outside `.agents`. Higher-priority mandatory system/plugin skill rules still apply.

All local copies use explicit-only metadata. Host loading of names/metadata and
agent reading of instruction bodies are different. This setup cannot override
host/system loading behavior or remove global/plugin skills elsewhere.

Updates are manual: request a pinned import review, preserve local adaptations,
licenses and resources, refresh the file hashes, and validate. When editing an
imported file deliberately, refresh its installed_sha256 in IMPORTS.json after
review; preserve upstream_sha256. Integrity failures detect unrecorded changes.
Disable a skill by renaming SKILL.md to SKILL.md.disabled and updating its catalog
link/status and relevant workflows/import manifest path. Start a fresh session.

## Development handoffs

See [workflow usage](WORKFLOW-USAGE.md) for the normal sequence and the new-interface
iteration. Each active development stage reads the shared handoff convention;
accepted requirements, contracts/tests and plans keep separate status from runtime
verification. Review-only stays read-only. User-selected combinations preserve
stage boundaries and do not automatically authorize later implementation.

## Verification

The validator checks grouped paths, metadata, explicit policy, catalog state,
bundled file integrity, local links, and workflow entry paths. It does not execute
upstream scripts or prove skill quality. Test behavior in a fresh session:
start without a workflow and expect one selection question; name interview and
expect only that workflow, grill-me, and its grilling dependency to be needed;
continue without another workflow question; request the catalog to browse skills.
