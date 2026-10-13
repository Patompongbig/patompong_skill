# Portable personal agent toolkit

Copy this `.agents` folder into a project root. The instruction-only core needs
no global installation, credentials, symlinks, or runtime. Optional local helpers
use Python 3.9+ and its standard library on Windows or Linux.

## Contents

| File | Use |
| --- | --- |
| [PREFERENCES.md](PREFERENCES.md) | Your revisable working defaults |
| [workflows/default.md](workflows/default.md) | Short implementation workflow |
| [CATALOG.md](CATALOG.md) | Skills, triggers, dependencies, origins, status |
| [STARTUP.md](STARTUP.md) | Prompt for activation without project edits |
| [templates/activation.md](templates/activation.md) | Small root instruction section |
| [skills/](skills/) | Three focused, discoverable skills |
| [scripts/validate.py](scripts/validate.py) | Read-only static checks |
| [scripts/activate.py](scripts/activate.py) | Optional append-only activation |
| [CHANGELOG.md](CHANGELOG.md) | Brief meaningful toolkit changes |

## Copy and activate

1. Copy the complete `.agents` folder, including hidden files, into the project
   root. If the destination already has `.agents`, compare and merge selected
   files; do not overwrite its skills or guidance. Check for same-purpose and
   same-name skills before merging.
2. Append [the activation section](templates/activation.md) to the project's root
   `AGENTS.md`, preserving all existing contents. Or run from that project root:

   ```sh
   python .agents/scripts/activate.py
   python .agents/scripts/validate.py --project-root .
   ```

   On Linux, use `python3` if `python` is unavailable. On Windows, `py -3` is
   another option. These helpers are optional; copying the section by hand works.
   The activator refuses an existing root `AGENTS.override.md`, detects malformed
   markers, preserves existing bytes, and makes no change on repeat activation.
   With overrides or custom instruction filenames, integrate the section into
   the applicable instruction file yourself after inspecting project guidance.
3. Start a fresh Codex session in the project. For a session-only alternative,
   paste [STARTUP.md](STARTUP.md); no root file edit is needed.

For example, run these copy commands from the canonical toolkit project's root
only when the target `.agents` does not yet exist (replace `../my-project`):

```powershell
Copy-Item -LiteralPath .agents -Destination ../my-project/.agents -Recurse
```

```sh
cp -R .agents ../my-project/.agents
```

Copying one folder makes local skills available to a compatible Codex host.
It does **not** activate personal defaults by itself. Root instruction routing
or the startup prompt is the minimal additional step.

## What loads when

| Mechanism | Content | Behavior |
| --- | --- | --- |
| Native discovery | `skills/*/SKILL.md` name and description | Codex scans `.agents/skills` from its working directory to repository root; full skill instructions load when selected |
| Root instruction reference | Preferences and default workflow | Root `AGENTS.md` instructs the agent to read these files; they are not independently auto-loaded |
| Explicit startup prompt | `STARTUP.md` | You paste its text; it is not automatically read |
| On-demand reference | README, catalog, changelog, skill references | Read only when the task needs them |
| Optional helpers | Python scripts | Run explicitly; no hooks or background services |
| External integrations | Imported tool-dependent skills | Require their documented tools, accounts, network access, credentials, or packages |

Project requirements take precedence over these personal defaults. None of the
files override higher-priority agent instructions or grant tool permissions.
Root overrides can hide `AGENTS.md`; nested guidance, custom configuration, and
instruction-size limits can affect loading. Other agents may use different
discovery rules: use the startup prompt and explicitly request a skill file when
native discovery is absent. Tool access and filesystem permissions still apply.

## Everyday use and skill management

Use ordinary task prompts; select relevant skills only. Examples:

- `$toolkit-maintain Add a focused skill for writing migration guides.`
- `$diagnose-bug Find why this test fails and fix the cause.`
- `$review-change Review this diff for correctness; do not edit files.`
- `$toolkit-maintain Find a small selection of documentation skills; compare
  overlap and dependencies before installing anything.`

For creation or edits, check the catalog and installed skill instructions first.
Update an existing same-purpose skill when suitable. Update the catalog and
changelog, include an invocation and completion condition, and validate.
Downloads require actual instruction/script inspection, sources and pinned
revision information, preserved licenses/attribution, and installation
authorization. Install inside this folder, never silently into global locations.
See [maintenance instructions](skills/toolkit-maintain/SKILL.md).

Disable a skill by renaming its `SKILL.md` to `SKILL.md.disabled`, leaving its
resources beside it, and changing its catalog link and status to `disabled`.
Update other links to the renamed manifest as needed.
For example, from the project root:

```powershell
Rename-Item -LiteralPath .agents/skills/review-change/SKILL.md -NewName SKILL.md.disabled
```

```sh
mv .agents/skills/review-change/SKILL.md .agents/skills/review-change/SKILL.md.disabled
```

Re-enable by reversing the rename and restoring `enabled` in the catalog. Restart
Codex after disabling to avoid an already-loaded skill persisting in context.
Without its exact manifest filename, the local copy cannot be discovered as a
skill. Catalog status alone does nothing. Explicitly reading the disabled file
still works; it is ordinary text, not an access restriction. A same-name copy in
another discovery location remains available; inspect the host's skill list.
Remove a skill by deleting only its confirmed folder and catalog row; record the
change. Disable first when you want an easy recovery path.

## Carry improvements back

This checkout is the initial canonical copy; choose another later if useful.
Copies evolve independently. Keep project plans, session notes, credentials, and
private examples outside `.agents`, in project-owned locations.

To return improvements: compare the edited copy against the canonical folder
(an editor diff works; Git is optional), copy only selected reusable changes,
reconcile catalog/changelog and any import attribution, then validate both
copies. Bring selected updates to other projects the same way. Do not copy a
project's `AGENTS.md` back into the toolkit or replace a destination `.agents`
wholesale. No synchronization service is required.

## Validation and limits

```sh
python .agents/scripts/validate.py
python .agents/scripts/validate.py --project-root .
```

The checker finds missing core files, broken local Markdown links, metadata
problems, duplicate local names, catalog/file-state mismatch, symlinks, common
absolute machine paths, and some credential-like files/text. It never executes
skill scripts or contacts the network. `name` and `description` must use nonempty
single-line plain or quoted YAML strings; normalize imported block scalars for
this lightweight checker. Other frontmatter fields are retained but not fully
YAML-validated. Markdown anchor targets, remote links, arbitrary source-code
references, global skill collisions, and complete secret detection are outside
its scope. Review imported files as well.

`--project-root` also checks the standard root activation section and warns about
an override. These are static checks, not proof that a host followed instructions.
In a fresh session, ask: "List the toolkit skills available, read the personal
defaults through the root guidance, and report the paths you actually read."
Then try one relevant invocation and one unrelated request. Do not label discovery
or trigger behavior verified until observed in that host.

Conventions checked on 2026-10-07 against official OpenAI documentation:
[local skill loading](https://learn.chatgpt.com/docs/build-skills) and
[AGENTS.md loading](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Recheck when a host upgrade changes behavior.
