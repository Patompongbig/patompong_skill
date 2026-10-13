"""Apply the confirmed portable toolkit design from the pinned local archive."""
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
TOOLKIT = ROOT / '.agents'
REVISION = '49dd158d1076134a641b33efb035946536778336'
SOURCE = ROOT / 'skill-selection' / 'downloads' / ('mattpocock-' + REVISION) / ('skills-' + REVISION)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8', newline='\n')


def policy(folder, author=None):
    path = folder / 'agents/openai.yaml'
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    if author and 'display_name:' in text:
        text = re.sub(r'(?m)^(  display_name:)\s*"([^"]+)"$', lambda m: m[1] + ' ' + json.dumps(author + ': ' + m[2]), text)
    if re.search(r'(?m)^policy:\s*$', text):
        if re.search(r'(?m)^  allow_implicit_invocation:', text):
            text = re.sub(r'(?m)^  allow_implicit_invocation:.*$', '  allow_implicit_invocation: false', text)
        else:
            text = re.sub(r'(?m)^policy:\s*$', 'policy:\n  allow_implicit_invocation: false', text)
    else:
        text = text.rstrip() + '\npolicy:\n  allow_implicit_invocation: false\n'
    write(path, text.lstrip('\n'))


def adapt_calls(text):
    text = re.sub(r'(?i)call the Skill tool twice, for "([a-z-]+)" and "([a-z-]+)"',
                  lambda m: 'Read `.agents/skills/mattpocock/' + m[1] + '/SKILL.md` and `.agents/skills/mattpocock/' + m[2] + '/SKILL.md`', text)
    text = re.sub(r'(?i)call the Skill tool with ["`]([a-z-]+)["`]',
                  lambda m: 'Read `.agents/skills/mattpocock/' + m[1] + '/SKILL.md`', text)
    text = re.sub(r'(?i)calls the Skill tool with ["`]([a-z-]+)["`]',
                  lambda m: 'reads `.agents/skills/mattpocock/' + m[1] + '/SKILL.md`', text)
    return text


def main():
    source_manifests = sorted((SOURCE / 'skills').glob('*/*/SKILL.md'))
    if len(source_manifests) != 38:
        raise RuntimeError('Pinned archive must contain 38 skills')
    destination = TOOLKIT / 'skills/mattpocock'
    if destination.exists():
        raise RuntimeError('Author group already exists; inspect before updating')
    backup = ROOT / 'toolkit-setup/before-apply'
    backup.mkdir(parents=True, exist_ok=True)
    for relative in ['AGENTS.md', '.agents/PREFERENCES.md', '.agents/workflows/default.md', '.agents/CATALOG.md', '.agents/README.md', '.agents/STARTUP.md', '.agents/templates/activation.md', '.agents/skills/toolkit-maintain/SKILL.md', '.agents/CHANGELOG.md', '.agents/scripts/validate.py']:
        original = ROOT / relative
        if original.exists():
            target = backup / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if target.read_bytes() != original.read_bytes():
                    raise RuntimeError('Existing backup differs; inspect before applying: ' + relative)
            else:
                shutil.copy2(original, target)
    destination.mkdir(parents=True)
    shutil.copy2(SOURCE / 'LICENSE', destination / 'LICENSE')
    candidates = json.loads((ROOT / 'skill-selection/candidates.json').read_text(encoding='utf-8'))['candidates']
    assessments = {x['name']: x for x in candidates if x['repository'] == 'mattpocock/skills'}
    imports = []
    portable_note = '''## Portable invocation

This toolkit uses explicit session workflow or lone-skill selection. After this
skill is selected, follow its relevant skill dependencies and references as
needed. Named Matt dependencies resolve directly to
`.agents/skills/mattpocock/<name>/SKILL.md` from the target project root; supporting
links resolve from this skill folder. Read each needed file once rather than
loading the collection. A host-specific "Skill tool" instruction means this
file-based lookup in Codex, including instructions inside generated prompts.
If a tool, path convention, or host assumption differs, consult the relevant part
of [portable compatibility](../../../COMPATIBILITY.md). Session scope and the
user's instructions govern any upstream invocation restrictions.

'''
    for original in source_manifests:
        folder = destination / original.parent.name
        shutil.copytree(original.parent, folder)
        original_files = []
        changed = []
        for src in sorted(original.parent.rglob('*')):
            if not src.is_file():
                continue
            local = folder / src.relative_to(original.parent)
            original_files.append({'path': local.relative_to(TOOLKIT).as_posix(), 'source_path': src.relative_to(SOURCE).as_posix(), 'upstream_sha256': hashlib.sha256(src.read_bytes()).hexdigest()})
            if local.suffix == '.md':
                old = local.read_text(encoding='utf-8')
                new = adapt_calls(old)
                if local.name == 'SKILL.md':
                    end = new.index('\n---', 4) + 4
                    new = new[:end] + '\n\n' + portable_note + new[end:].lstrip('\n')
                if new != old:
                    changed.append(local.name)
                    write(local, new)
        policy(folder, 'Matt Pocock')
        original_files_by_path = {r['path']: r for r in original_files}
        for local in sorted(folder.rglob('*')):
            if not local.is_file():
                continue
            rel = local.relative_to(TOOLKIT).as_posix()
            installed_hash = hashlib.sha256(local.read_bytes()).hexdigest()
            if rel not in original_files_by_path:
                original_files.append({'path': rel, 'source_path': None, 'upstream_sha256': None})
                original_files_by_path[rel] = original_files[-1]
            original_files_by_path[rel]['installed_sha256'] = installed_hash
        record = {'name': folder.name, 'category': original.parent.parent.name, 'manifest': (folder / 'SKILL.md').relative_to(TOOLKIT).as_posix(), 'source_url': f'https://github.com/mattpocock/skills/blob/{REVISION}/{original.relative_to(SOURCE).as_posix()}', 'revision': REVISION, 'license': 'skills/mattpocock/LICENSE', 'adaptations': ['Explicit-only agents/openai.yaml policy; author-prefixed UI title', 'Portable invocation note and direct named skill paths'], 'files': original_files}
        imports.append(record)
    for name in ['toolkit-maintain', 'diagnose-bug', 'review-change']:
        policy(TOOLKIT / 'skills' / name)

    write(destination / 'PROVENANCE.md', f'''# Matt Pocock import provenance

- Source: [mattpocock/skills](https://github.com/mattpocock/skills/tree/{REVISION}).
- Pinned revision: `{REVISION}`; downloaded during setup on 2026-10-11.
- Collection: 38 skill folders; all 103 upstream files retained.
- License: [MIT](LICENSE). Additional [PR credits](pr/CREDITS.md) retained.
- Local changes: explicit-only policy on every skill, author-prefixed UI labels,
  portable invocation note, and direct paths for ordinary named Skill-tool calls.
- Executable resources are preserved unchanged, not executed on installation.
- Original source archive remains in the setup checkout outside the portable
  folder; its executable files are not automatically activated.
- [Installed inventory](../../IMPORTS.json) records original and installed hashes.
- [Compatibility](../../COMPATIBILITY.md) identifies host/runtime requirements.

These are installed instruction packages, not runtime proof for every skill.
No global configuration, account credentials, hooks, packages, or project tracker
configuration were created as part of the import. Updates are explicit and pinned.
''')
    write(TOOLKIT / 'IMPORTS.json', json.dumps({'revision': REVISION, 'acquisition_date': '2026-10-11', 'imports': imports}, indent=2) + '\n')
    write(TOOLKIT / 'PREFERENCES.md', '''# Personal working preferences

- Use English unless requested otherwise.
- At the beginning of each new session, ask which workflow or lone skill to use.
  An opening request that already names one counts as the selection. Keep that
  choice throughout the session until the user changes it; compaction and
  follow-up tasks do not start another selection round.
- Read only the selected workflow's entry skills and their relevant dependencies
  and supporting references. Skills navigate their dependencies themselves.
- Read the full skill catalog only when the user requests skill browsing,
  selection help, tree details, or catalog maintenance. Opening a session and
  offering workflow choices does not require reading the catalog or skill bodies.
- Understand the outcome, ask about consequential uncertainties, and complete
  the authorized work with proportionate verification and concise updates.
- Preserve explain/review scope; edits require an editing assignment.
- Keep unrelated refactoring, credentials, and private project notes outside
  the portable toolkit. Keep changes focused and explain material tradeoffs.
- Use delegation when supported and directed by the selected workflow or skill.
- Project requirements and higher-priority instructions take precedence; explain
  material conflicts. These defaults do not grant extra tool permissions.
''')
    write(TOOLKIT / 'workflows/default.md', '''# Session workflow routing

This file routes a session; it is not an automatically selected build workflow.

1. Read applicable project instructions and personal preferences.
2. If this session has no selected workflow or lone skill, use the small menu
   in [INDEX.md](INDEX.md) to ask which to use, then wait. Read no full catalog or
   skill bodies to compose that question. A choice in the opening user prompt
   already answers the question. An explicit skill invocation is a lone-skill
   selection unless the user also assigns a workflow.
3. Read the selected workflow file, then its skill entry points as each step
   needs them. The paths in the workflow fix those entry points. Skills follow
   relevant dependencies themselves; this is not a closed allowlist. Resolve a
   named dependency directly in its author group rather than inspecting unrelated
   skills. Supporting resources are loaded only for the current task/branch.
4. Keep the selection across messages, new tasks within this session, and
   compaction. Change it when the user asks; do not ask again for every task.
5. When the user names a lone skill, read its manifest directly. If they ask for
   help choosing a skill or details of the tree, read [the catalog](../CATALOG.md)
   and only the skill detail needed for that request. Catalog reading is not a
   routine prerequisite for task execution or session workflow selection.
6. Maintain the assignment's scope and appropriate verification. Report actual
   changes, checks, and unresolved runtime prerequisites. A workflow cannot turn
   an explanation into edits or provide permissions absent from the user's task.

For a known custom workflow, read `.agents/workflows/<name>.md` directly. If the
path is missing or a name is ambiguous, ask for the intended file/name instead
of loading the whole skill tree. Host-mandated system/plugin skills remain subject
to higher-priority instructions; portable rules control this toolkit's copies.
''')
    write(TOOLKIT / 'workflows/INDEX.md', '''# Session workflow menu

Read only this small menu to offer session choices. The full skill catalog is
separate and is opened when the user asks to browse or choose individual skills.

| Workflow | Purpose | File |
| --- | --- | --- |
| interview | Clarify and stress-test an idea | [interview.md](interview.md) |
| planning | Clarify a feature, write a spec, and split it into tasks | [planning.md](planning.md) |
| build-review | Implement an agreed task with tests and closing review | [build-review.md](build-review.md) |
| review | Review a change against its standards and specification | [review.md](review.md) |
| lone-skill | Use one named skill and the dependencies it needs | [lone-skill.md](lone-skill.md) |

These are editable starting examples, not automatic task classifiers. Ask which
one the user wants at session start unless they have already named it. Preserve
their choice for the session. The user can name a custom workflow file directly.

Create a custom workflow by copying [the template](../templates/workflow.md), or
ask: "Use toolkit-maintain to create workflow <name> combining <skills>."
When adding a workflow, add one concise row here; keep detailed skill descriptions
in the full catalog. This menu does not authorize opening every linked file.
''')
    workflows = {
        'interview': '''# Interview workflow

Purpose: sharpen an idea through questions before deciding or building.

1. Read [grill-me](../skills/mattpocock/grill-me/SKILL.md).
2. It follows grilling itself; ask rounds of unresolved decisions and wait for
   answers. Investigate facts rather than asking the user to supply discoverable
   information.
3. Finish with the shared understanding and remaining decisions, using the
   skill's confirmation rule. An interview alone does not authorize implementation.

Deliverable: a clear agreed design or plan. Completion: the user confirms the
shared understanding. Example: "Use interview to clarify this import workflow."
''',
        'planning': '''# Planning workflow

Purpose: turn a feature discussion into a specification and verifiable tasks.

1. Establish the target project and where its tasks and design notes belong.
   If tracker conventions are missing, read
   [setup-matt-pocock-skills](../skills/mattpocock/setup-matt-pocock-skills/SKILL.md)
   and perform the relevant per-project setup. Local Markdown is supported.
2. Read [grill-with-docs](../skills/mattpocock/grill-with-docs/SKILL.md) to clarify
   the design; let it follow its interview and domain-modeling dependencies.
3. Once the design is agreed, read [to-spec](../skills/mattpocock/to-spec/SKILL.md)
   to synthesize the discussion and agree testing boundaries.
4. Read [to-tickets](../skills/mattpocock/to-tickets/SKILL.md) to propose complete
   slices and publish the approved breakdown to the configured tracker.

Deliverables: agreed terminology/decisions, a spec, and tasks with dependencies.
Completion: the approved spec and tasks exist at the configured destinations.
This workflow produces planning artifacts; implementing them is a separate task.
Example: "Use planning for an editable-parts import feature; use local tasks."
''',
        'build-review': '''# Build and review workflow

Purpose: implement an agreed task with feedback from tests and a closing review.

1. Read the user-assigned spec/ticket and establish the authorized editing scope.
   Agree test boundaries already covered by that scope and identify the review
   base. If the tracker conventions are missing, follow the relevant setup skill.
2. Read [implement](../skills/mattpocock/implement/SKILL.md). It follows tdd and
   code-review itself as needed. Do not eagerly read both dependency bodies at
   session startup.
3. Run the project's relevant checks, report the review findings, and resolve
   defects within scope. Upstream implement ends with a local commit; honor the
   user's commit instructions and preserve unrelated work. It does not imply a
   remote push or release.

Requirements: a project runtime/test runner; Git for diff review/committing;
subagents for upstream two-axis review when the host supports them.
Deliverable: verified implementation and closing review. Completion: assigned
behavior is implemented and appropriate checks pass, or a concrete external
prerequisite is documented. Example: "Use build-review to implement ticket 03."
''',
        'review': '''# Review workflow

Purpose: review an existing change separately against standards and its spec.

1. Read [code-review](../skills/mattpocock/code-review/SKILL.md).
2. Establish the Git comparison base, originating spec, and relevant standards.
   The skill runs its reviewers and follows relevant tracker setup when needed.
3. Report findings and evidence. Keep review read-only unless the user requests
   fixes. Where no subagent support exists, report that the upstream isolation
   cannot be reproduced; do not claim parallel review occurred.

Deliverable: actionable standards/spec findings. Completion: the comparison and
both applicable axes are reported. Example: "Use review against main and spec.md."
''',
        'lone-skill': '''# Lone-skill session

Purpose: use a named skill without requiring a composed workflow.

1. If the user already named an author/skill or an explicit skill invocation,
   resolve that manifest directly and read it. Matt skills live at
   `.agents/skills/mattpocock/<name>/SKILL.md`; the three existing personal skills
   remain at `.agents/skills/<name>/SKILL.md`. Outside downloads use author groups.
2. If the user asks for selection help or tree details, read
   [CATALOG.md](../CATALOG.md) to explain appropriate choices. Naming a known
   skill does not require catalog reading. Ask to resolve genuinely ambiguous names.
3. Follow the chosen skill and relevant dependencies/references. The skills can
   navigate their dependencies themselves; no workflow whitelist is required.
4. Retain lone-skill mode for the session. A later explicitly named skill updates
   the skill choice. If the existing choice cannot handle the next task, ask
   which skill they want, rather than silently selecting an unrelated one.

Deliverable and completion follow the assigned skill and task. Example:
"Use lone-skill: mattpocock/handoff; summarize this task for another session."
'''
    }
    for name, text in workflows.items():
        write(TOOLKIT / 'workflows' / (name + '.md'), text)
    write(TOOLKIT / 'templates/workflow.md', '''# <workflow-name>

Purpose: <repeatable outcome this combination should produce>.

## Inputs and scope

<Required project/task information; whether this is explanation, planning,
review, or implementation; any actual runtime or tracker prerequisites.>

## Steps

1. Read `.agents/skills/<author>/<skill>/SKILL.md` when this step begins.
   <What to do, the artifact it produces, and how to know the step is complete.>
2. <Next skill entry point, conditional branch, or handoff; include only steps
   needed for this workflow. Skills follow their own relevant dependencies.>

## Deliverables and completion

<Concrete output locations and observable completion conditions.>

## Example invocation

Use workflow <workflow-name> for <task>.

Use target-project-relative paths for project outputs. Supporting resource links
resolve from the skill that owns them. Store this file as
`.agents/workflows/<workflow-name>.md` and add one row to workflows/INDEX.md.
The full catalog is consulted for user-requested discovery, not every execution.
''')
    activation = '''<!-- personal-toolkit:begin -->
## Patompong portable workflow defaults

Read [.agents/PREFERENCES.md](.agents/PREFERENCES.md) and
[.agents/workflows/default.md](.agents/workflows/default.md).
At each new session, ask which workflow or lone skill to use unless the opening
request already names one. Keep that selection throughout the session until the
user changes it. Use only [the small workflow menu](.agents/workflows/INDEX.md)
to offer choices; read no full catalog or skill bodies for that question.
After selection, read the selected workflow and the skills/references it needs;
skills follow their relevant dependencies themselves. Read
[the full catalog](.agents/CATALOG.md) only for user-requested skill browsing,
selection help, tree details, or catalog maintenance.
Follow applicable project requirements and higher-priority instructions; explain
material conflicts. Keep project notes and credentials outside the portable folder.
<!-- personal-toolkit:end -->
'''
    write(TOOLKIT / 'templates/activation.md', activation)
    root_guidance = ROOT / 'AGENTS.md'
    old = root_guidance.read_text(encoding='utf-8') if root_guidance.exists() else ''
    if old.count('<!-- personal-toolkit:begin -->') != 1 or old.count('<!-- personal-toolkit:end -->') != 1:
        raise RuntimeError('Inspect nonstandard root activation before replacing')
    new = re.sub(r'<!-- personal-toolkit:begin -->.*?<!-- personal-toolkit:end -->', activation.rstrip(), old, flags=re.S)
    write(root_guidance, new)
    write(TOOLKIT / 'STARTUP.md', '''Read the applicable project instructions, `.agents/PREFERENCES.md`, and
`.agents/workflows/default.md`. At the beginning of this session ask which
workflow or lone skill I want, using only `.agents/workflows/INDEX.md` for choices.
If my opening request already names one, it is my selection. Keep the selection
through the session until I change it.

Read only the selected workflow's entry skills and their relevant dependencies
and resources. Skills follow those dependencies themselves. Read the full
`.agents/CATALOG.md` only when I ask to browse/choose skills, inspect the tree,
or maintain the catalog. Keep private/project context outside the portable folder.
Project requirements and higher-priority instructions apply; this grants no
additional tool permissions.

My workflow or lone skill: [choose one, or ask me]
My task: [desired outcome and constraints]
''')
    write(TOOLKIT / 'COMPATIBILITY.md', '''# Portable skill compatibility

Read the relevant section when a selected skill meets a host/tool mismatch.
The installed catalog also gives per-skill requirements and overlap.

## Invocation and paths

- All local skills use `agents/openai.yaml` with
  `policy.allow_implicit_invocation: false`. Full bodies are read by explicit
  assignment or as relevant dependencies of the selected workflow/skill.
- Native discovery of names/metadata is host behavior; the no-catalog/no-body
  startup rule governs agent file reads. Native selectors and nested author
  discovery need a fresh-session check. Direct file paths remain the portable
  fallback; no symlinks or flat duplicate wrappers are required.
- Ordinary named upstream Skill-tool calls are adapted to project-root paths.
  Other Skill-tool instructions, including generated subagent prompts, mean
  reading the corresponding manifest. Resolve a named Matt dependency directly
  in its author group. Read references only when their branch is relevant.
- `/clear`, `/compact`, and temporary filesystem paths are host conventions,
  not skill names. Use available host equivalents and the OS temporary directory.
- Upstream writing-for-agents mechanics describe another host's invocation rules.
  Here the user allows selected skills to follow dependencies, including explicit
  skill copies. This local policy governs those invocation mechanics.

## Target project configuration

- M14 setup runs per target project; downloading the collection does not run it.
  Local Markdown tasks need no tracker account. GitHub/GitLab modes need their
  CLI or a compatible authorized integration and account access.
- For Codex, put the setup's routing block in the applicable AGENTS.md; a
  CLAUDE.md-only block does not activate Codex guidance. Preserve existing files
  and integrate into the active instruction file rather than replacing it.
- Project glossaries, ADRs, task files, teaching records, and generated artifacts
  live outside this portable folder. The skill's example generated-project links
  are examples, not missing bundled resources.

## Platform-specific skills

| Skill | Requirement / supported boundary |
| --- | --- |
| git-guardrails-claude-code | Claude Code PreToolUse hooks plus Bash and jq; copied script retained, no Codex hook claim |
| claude-handoff | Claude CLI background-agent support; use handoff for a portable summary |
| wizard | Bash, gh for GitHub secrets, browser-opening utilities, and authorized target-project credentials |
| diagnosing-bugs | Project test/runtime tools; Bash only for its optional human-reproduction template |
| setup-pre-commit | Node/package manager, Husky, lint-staged, Prettier, and project check commands |
| migrate-to-shoehorn | TypeScript tests and @total-typescript/shoehorn in the target project |
| setup-ts-deep-modules | TypeScript project, dependency-cruiser, bundled .cjs configuration |
| scaffold-exercises | AI Hero course conventions and pnpm ai-hero-cli; adapt for other course layouts |
| prototype | Project UI/runtime tools; HTML logic prototypes can be standalone |
| improve-codebase-architecture | HTML report preview; upstream report template may need network/CDN access |

## Subagents and execution

code-review, research, implement-spec, chief-of-staff, and some design/interview
branches require or direct subagents. Use the host's supported delegation when
the selected skill directs it. If unavailable, identify the unsupported behavior
and discuss a suitable serial alternative; do not claim parallel isolation.
The seven upstream in-progress skills remain labeled experimental in the catalog.

Bundled shell/config resources are preserved unchanged. Inspect any executable
before running it. Installing this instruction collection does not install every
project runtime, configure global hooks, create accounts, or authorize remote
messages, publishing, or secret writes. Setup those components in the target
project when the user assigns the corresponding operation.

## Updates

There is no automatic upstream update or background process. To update, explicitly
request a new pinned source review, preserve local edits and licenses, refresh
IMPORTS.json, and rerun validation. Session configuration changes only through
user-requested edits. Domain documentation evolves when its relevant skill is used.
''')
    maintenance = TOOLKIT / 'skills/toolkit-maintain/SKILL.md'
    text = maintenance.read_text(encoding='utf-8')
    text = text.replace("Read [the catalog](../../CATALOG.md) and the relevant\nexisting instructions before creating another skill with the same purpose.", "Read relevant existing instructions for the assigned maintenance operation.\nRead [the catalog](../../CATALOG.md) only when the user asks for skill browsing,\nselection help, tree details, or catalog maintenance; routine session workflow\nselection does not authorize catalog reading.")
    text += '''\n## Compose or edit a workflow\n\nWhen the user assigns workflow creation or editing, read\n[workflow composition](references/workflows.md) and the specifically named skills.\nExisting personal skills stay flat; outside imports use\n`skills/<author>/<skill>/SKILL.md`. Preserve author grouping when importing.\n'''
    write(maintenance, text)
    write(maintenance.parent / 'references/workflows.md', '''# Create an editable workflow

1. Establish the repeatable outcome, scope, and ordered skill combination from
   the user's request. Read the skills they named directly; follow relevant
   dependencies as needed. Read the complete catalog only if they request skill
   selection help, tree browsing, or catalog maintenance.
2. Use [the workflow template](../../../templates/workflow.md). Write the file
   to the toolkit's workflows/<name>.md with concrete entry skill paths, required
   inputs, conditional steps, deliverables, and completion criteria. The workflow
   chooses entry points; each skill still navigates relevant dependencies itself.
3. Add a concise row to [the session menu](../../../workflows/INDEX.md). Keep the
   detailed skills catalog separate; avoid copying entire skill instructions.
4. Update the changelog and relevant docs; run the toolkit validator. Check that
   all entry paths exist and the sequence produces the requested deliverable.

Example: "Use toolkit-maintain to create design-review combining
mattpocock/codebase-design and review-change; finish with written recommendations."

Complete when the editable file/menu entry exist, paths validate, and invocation
is explained. Creating a workflow does not execute it or change the session's
selected workflow unless the user requests that switch.
''')
    catalog = ['# Portable skill catalog\n\n', 'Open this detailed catalog for user-requested skill browsing, selection help,\ntree details, or catalog maintenance. Session startup uses only the small\n[workflow menu](workflows/INDEX.md). Reading the catalog does not execute skills.\n\n', '41 installed instruction skills: three original personal skills and 38 Matt\nPocock skills. Every local copy is explicit-only; selected skills can follow\nrelevant dependencies themselves. Status `enabled` means SKILL.md exists, not\nautomatic invocation or runtime proof. External system/plugin skills are outside\nthis portable catalog.\n\n', '## Personal skills\n\n', '| Name | Purpose | Use when | Requirements | Origin / notes | Status |\n| --- | --- | --- | --- | --- | --- |\n']
    originals = [('toolkit-maintain', 'Maintain skills and compose editable workflows', 'Assigned toolkit/catalog/workflow maintenance', 'File access; Python for checks; network for imports'), ('diagnose-bug', 'Reproduce and diagnose a concrete software defect', 'Assigned failure/regression diagnosis', 'Relevant project runtime and tests'), ('review-change', 'Review a diff for actionable correctness defects', 'Assigned review of a change', 'File/diff access; project checks as relevant')]
    for name, purpose, trigger, requirements in originals:
        catalog.append(f'| [{name}](skills/{name}/SKILL.md) | {purpose} | {trigger} | {requirements}; explicit-only | Original personal toolkit | enabled |\n')
    catalog += ['\n## Matt Pocock collection\n\n', '[Pinned provenance and license](skills/mattpocock/PROVENANCE.md);\n[host/runtime compatibility](COMPATIBILITY.md); [file inventory](IMPORTS.json).\nAll bundled resources are installed; runtime prerequisites remain per target\nproject and host. Overlapping skills are retained because the user chose the\nwhole collection; explicit selection resolves which one is used.\n\n']
    for category, label in [('engineering', 'Engineering'), ('productivity', 'Productivity'), ('misc', 'Specialized tools'), ('in-progress', 'Experimental: upstream in-progress')]:
        subset = [r for r in imports if r['category'] == category]
        catalog += [f'### Matt Pocock / {label} ({len(subset)})\n\n', '| Name | Purpose | Use when | Requirements | Origin / notes | Status |\n| --- | --- | --- | --- | --- | --- |\n']
        for rec in subset:
            x = assessments[rec['name']]
            values = [f"[{rec['name']}]({rec['manifest']})", x['purpose'], x['trigger'], x['dependencies'] + '; explicit-only', f"{x['id']}; MIT; pinned import" + ('; experimental' if category == 'in-progress' else ''), 'enabled']
            catalog.append('| ' + ' | '.join(v.replace('|', '/') for v in values) + ' |\n')
        catalog += ['\n']
        for rec in subset:
            x = assessments[rec['name']]
            catalog += [f"#### {x['id']}: {rec['name']}\n\n", f"**Purpose:** {x['purpose']}\n\n", f"**Use for:** {x['trigger']}\n\n", f"**Needs:** {x['dependencies']}\n\n", f"**Overlap:** {x['overlap']}\n\n", f"**Compatibility:** {x['adaptation']}\n\n", f"**Example request:** {x['example']}\n\n", f"**Source:** [Pinned upstream]({rec['source_url']}). All files in its skill folder\nare retained; see installed inventory for original/installed hashes.\n\n"]
    catalog += ['## Choosing combinations\n\n', '- Interview: grill-me follows grilling; grill-with-docs also follows domain-modeling.\n- Build: implement follows tdd and code-review; implement-spec adds parallel task orchestration.\n- Architecture: codebase-design provides design principles; improve-codebase-architecture surveys candidates.\n- Continuity: handoff writes portable session context; teach maintains a separate learning workspace.\n- Planning: target-project setup chooses local tasks or a tracker; to-spec and to-tickets write the artifacts.\n\n', 'Use workflow <name> to select a composition, or name one author/skill directly.\nFor example: "Use lone-skill mattpocock/handoff" or\n"Use toolkit-maintain to create a workflow combining mattpocock/prototype and review-change."\n']
    write(TOOLKIT / 'CATALOG.md', ''.join(catalog))
    write(TOOLKIT / 'README.md', '''# Patompong portable skills and workflows

Copy this complete `.agents` folder into a project. Keep existing project
guidance and merge any existing toolkit files deliberately. Nothing here requires
a global skill installation, symlink, account, background service, or auto-update.

## Navigation

| Location | Purpose |
| --- | --- |
| [PREFERENCES.md](PREFERENCES.md) | Personal session and working defaults |
| [workflows/default.md](workflows/default.md) | Session selection and reading rules |
| [workflows/INDEX.md](workflows/INDEX.md) | Small session menu; five editable examples |
| [CATALOG.md](CATALOG.md) | Detailed overall catalog; read when requested |
| [skills/mattpocock/](skills/mattpocock/) | All 38 downloaded Matt skills and their resources |
| [templates/workflow.md](templates/workflow.md) | Create a reusable skill combination |
| [COMPATIBILITY.md](COMPATIBILITY.md) | Host/tool requirements and path-based invocation |
| [IMPORTS.json](IMPORTS.json) | Source revision, license, original and installed hashes |
| [scripts/activate.py](scripts/activate.py) | Optional append-only project activation |
| [scripts/validate.py](scripts/validate.py) | Read-only packaging, policy, paths, integrity checks |
| [STARTUP.md](STARTUP.md) | Session prompt when root activation is unavailable |
| [CHANGELOG.md](CHANGELOG.md) | Meaningful changes |

## Folder conventions

Outside collections: `.agents/skills/<author>/<skill>/SKILL.md`.
Matt collection: `.agents/skills/mattpocock/<skill>/SKILL.md`.
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

Examples: "Use workflow interview for this design", "Use workflow build-review
for ticket 03", "Use lone-skill mattpocock/handoff", or "Show me the skill catalog".
To switch: "Switch this session to review." To create: "Use toolkit-maintain to
create my workflow <name> combining <skills>." Keep the small menu in sync.

## Runtime scope and updates

41 instruction skills are installed, including seven experimental Matt skills.
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

## Verification

The validator checks grouped paths, metadata, explicit policy, catalog state,
bundled file integrity, local links, and workflow entry paths. It does not execute
upstream scripts or prove skill quality. Test behavior in a fresh session:
start without a workflow and expect one selection question; name interview and
expect only that workflow, grill-me, and its grilling dependency to be needed;
continue without another workflow question; request the catalog to browse skills.
''')
    changelog = TOOLKIT / 'CHANGELOG.md'
    old_changes = changelog.read_text(encoding='utf-8')
    entry = '''
- 2026-10-11 / 0.2.0: Installed all 38 Matt Pocock skills in author-grouped paths,
  preserving all 103 upstream resources and licensing. Applied explicit-only
  invocation and ordinary named skill-call adaptations. Added a detailed overall
  catalog, five editable workflow examples, composition template and instructions,
  once-per-session routing, compatibility notes, and pinned file inventory.
  Preserved three original personal skills. No upstream runtime/hook executed.
'''
    write(changelog, old_changes.replace('# Toolkit changes\n', '# Toolkit changes\n' + entry, 1))
    write(ROOT / 'toolkit-setup/APPLIED.md', '''# Applied setup

The confirmed setup is now in the active .agents folder, including root routing.
The prepared draft is historical staging, not the active installation.
Backups of changed pre-existing files are in before-apply; source files and
licenses are in the pinned download. See the active README/CATALOG/IMPORTS.json.
Final validation evidence is recorded separately in VALIDATION.md.
''')
    print('APPLIED: 38 grouped Matt skills, three personal skills, explicit policy, detailed catalog, five workflows, template, routing, provenance and compatibility.')


if __name__ == '__main__':
    main()
