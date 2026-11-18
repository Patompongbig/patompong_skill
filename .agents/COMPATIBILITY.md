# Portable skill compatibility

Read the relevant section when a selected skill meets a host/tool mismatch.
The installed catalog also gives per-skill requirements and overlap.

## Invocation and paths

- All local skills use `agents/openai.yaml` with
  `policy.allow_implicit_invocation: false`. Full bodies are read by explicit
  assignment or as relevant dependencies of the selected workflow/skill.
- Native discovery of names/metadata is host behavior. Normal startup needs
  no toolkit preprompt, selection question, or guide/menu/catalog/skill-body read.
  Native selectors and nested author
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
- For optional toolkit discovery, put the activation block in the applicable AGENTS.md; a
  CLAUDE.md-only block is not read by hosts that only load AGENTS.md. Preserve existing files
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

## Agent roles and model selection

Workflows name models by family; translate to the current host. Each name means
the newest model of that family the host offers. Reasoning effort defaults to
medium. Role defaults and the selection prompt are defined in
[agent roles](workflows/references/agent-roles.md#model-selection).

| Family | Claude Code | ChatGPT / Codex | Gemini |
| --- | --- | --- | --- |
| haiku | haiku | Luna | — (use Hydrogen) |
| sonnet | sonnet | Terra | Hydrogen |
| opus | opus | Sol | Argon |
| fable | fable | Astra | Carbon |

Setting a subagent's model uses the host's own mechanism (for example, the
`model` option on Claude Code subagents, or a custom agent definition in Codex).
Where a host cannot set it, workflows report that once and use the session model.

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
`toolkit/IMPORTS.json` in the source repository, and rerun validation. Session configuration changes only through
user-requested edits. Domain documentation evolves when its relevant skill is used.

## Ponytail portable installation

All six skills live under `skills/ponytail/` with explicit-only policy. Use exact
manifest paths via a lone-skill assignment or a selected workflow. Native plugin
namespace/slash commands are not registered by this file-based installation.
No lifecycle hooks, global mode flags, startup injection, or auto-update were
installed. Full is the core skill's default after selection; it is not automatic
at session start. Lite/full/ultra can be chosen in the user request.

Review and audit report only; debt persists a ledger only when requested. Use rg
or native Windows search in place of Bash grep. Gain includes the referenced
benchmark report and README as text snapshots; results concern the author's
Claude Code benchmark, not measured savings or runtime proof in this toolkit.
Help documents the portable behavior rather than native plugin configuration.
At the Ponytail import, workflow/menu files were unchanged. User-created workflows
now select individual Ponytail skills explicitly; see the [workflow menu](workflows/INDEX.md).

## Superpowers / obra

All 15 skills and per-skill resources are installed under `skills/obra/`.
See [collection compatibility](skills/obra/COMPATIBILITY.md) for Bash/Node.js,
optional visual companion, delegation and explicit-only activation.
No startup hooks, global settings or automatic updater were installed.
