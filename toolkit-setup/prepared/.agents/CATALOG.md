# Portable skill catalog ? prepared draft

Read this catalog when the user requests skill browsing, selection, or catalog
maintenance. Session workflow selection uses a small workflow menu, not this
catalog. A selected skill may follow its relevant dependencies itself.

All links in this prepared catalog resolve inside its staged .agents folder.
The final catalog will include the three existing personal skills as well.

## Matt Pocock / Engineering

### M01 ? [ask-matt](skills/mattpocock/ask-matt/SKILL.md)

**Purpose:** Understand which Matt workflow to use.

**Use for:** You want a guide through the installed collection.

**Requirements:** Many other Matt skills are mentioned; no task execution itself.

**Overlap:** Overlaps the local catalog and toolkit-maintain routing.

**Compatibility notes:** Its map assumes almost the whole collection; rewrite to reference only selected skills.

**Example:** Help me choose a workflow for a multi-session feature.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M02 ? [code-review](skills/mattpocock/code-review/SKILL.md)

**Purpose:** Review a fixed Git diff separately against standards and a spec.

**Use for:** Review a branch or changes since a named commit.

**Requirements:** Git, two authorized subagents, spec/standards sources; configured issue tracker for tracker specs.

**Overlap:** Strong overlap with review-change; broader standards/spec review.

**Compatibility notes:** Requires a fixed base, Git tracker configuration, and parallel reviewers; do not install as a duplicate automatic correctness reviewer.

**Example:** Review this branch against main and the local feature spec.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M03 ? [codebase-design](skills/mattpocock/codebase-design/SKILL.md)

**Purpose:** Design a module with useful behavior behind a small interface.

**Use for:** Interface design, testability, or simplifying module structure.

**Requirements:** Bundled DEEPENING and DESIGN-IT-TWICE references; subagents only for alternative-design mode.

**Overlap:** Adds architecture vocabulary beyond the default workflow.

**Compatibility notes:** Requires specific jargon; relax forced terminology for plain-language explanations and make parallel design optional.

**Example:** Compare two interface designs for this parser.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M04 ? [diagnosing-bugs](skills/mattpocock/diagnosing-bugs/SKILL.md)

**Purpose:** Build a precise failing feedback loop, minimize a defect, test hypotheses, and verify a fix.

**Use for:** A hard bug, flaky failure, or performance regression.

**Requirements:** Project test/runtime tools; optional Bash human-reproduction template.

**Overlap:** Strong overlap with diagnose-bug.

**Compatibility notes:** Rigid no-hypothesis-before-reproduction gates can stall restricted environments; use its useful loop guidance to improve the local skill.

**Example:** Diagnose this intermittent export failure with a repeatable check.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M05 ? [domain-modeling](skills/mattpocock/domain-modeling/SKILL.md)

**Purpose:** Clarify project terminology and record significant design choices.

**Use for:** Resolve overloaded domain terms or maintain a glossary and ADRs.

**Requirements:** Bundled glossary/ADR formats and project-owned documentation.

**Overlap:** Adds persistent project knowledge, not personal toolkit preferences.

**Compatibility notes:** Writes glossary changes during discussion; agree the project scope and keep outputs outside .agents.

**Example:** Clarify what job, result, and import mean and record agreed terms.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M06 ? [grill-with-docs](skills/mattpocock/grill-with-docs/SKILL.md)

**Purpose:** Interview about a design and capture domain terms and decisions.

**Use for:** A substantial design needs deliberate clarification and written context.

**Requirements:** grilling and domain-modeling; project documentation layout.

**Overlap:** Alternative to grill-me with persistent documentation.

**Compatibility notes:** Wrapper is only skill dispatch; both dependencies are needed. Keep deliberate interviews optional rather than asking exhaustively on routine work.

**Example:** Stress-test this design and document the terms we agree on.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M08 ? [implement](skills/mattpocock/implement/SKILL.md)

**Purpose:** Build a spec or ticket with test-first work and a closing review.

**Use for:** Implementation of an already agreed scope.

**Requirements:** tdd and code-review, Git, project type/test commands; review tracker configuration.

**Overlap:** Overlaps the default workflow.

**Compatibility notes:** Commits automatically and inherits mandatory checkpoints/subagent assumptions from dependencies; adapt before use.

**Example:** Implement this approved ticket and verify it.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M07 ? [implement-spec](skills/mattpocock/implement-spec/SKILL.md)

**Purpose:** Implement a spec's dependency graph across parallel worktrees and an integration branch.

**Use for:** A large ticketed spec should be built by multiple agents.

**Requirements:** tdd, code-review; tracker setup, Git/worktrees, several authorized subagents and project checks.

**Overlap:** Heavy alternative to the ordinary implementation workflow.

**Compatibility notes:** Creates branches, merges, can open/ready PRs and close tickets; requires explicit scope and a host with delegation support.

**Example:** Implement this approved multi-ticket spec on an integration branch.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement-spec/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M09 ? [improve-codebase-architecture](skills/mattpocock/improve-codebase-architecture/SKILL.md)

**Purpose:** Find architectural friction and present candidates in a visual report.

**Use for:** You explicitly want to assess module structure.

**Requirements:** codebase-design, grilling, domain-modeling; authorized subagent, browser, CDN access for the report.

**Overlap:** Adds an architecture survey beyond review-change.

**Compatibility notes:** Creates a temp HTML report using remote Tailwind/Mermaid; offer offline output and single-agent execution and keep refactors separately authorized.

**Example:** Survey this subsystem and show the best simplification candidates.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/improve-codebase-architecture/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M10 ? [pr](skills/mattpocock/pr/SKILL.md)

**Purpose:** Write a clear PR description with a compact visual, before/after evidence, and impact.

**Use for:** Drafting or improving a pull-request body.

**Requirements:** File/text access; Git/PR service only if publishing is separately requested; retain CREDITS.md.

**Overlap:** Complements review-change; does not perform the review.

**Compatibility notes:** The full template can be heavy for small changes; scale it to change size and retain Dex Horthy/Humanlayer attribution.

**Example:** Draft a concise PR body for this completed change; do not publish.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/pr/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M11 ? [prototype](skills/mattpocock/prototype/SKILL.md)

**Purpose:** Build a disposable logic demo or contrasting UI variants to settle a design question.

**Use for:** A design decision needs something runnable or visual.

**Requirements:** Bundled LOGIC/UI references; browser/project runner; upstream capture convention uses Git and an issue.

**Overlap:** Distinct from production implementation.

**Compatibility notes:** Upstream commits prototypes to a branch and links tracker issues; make capture fit the project. Omitted hardening applies only to isolated prototypes.

**Example:** Build a local demo to compare these cancellation states.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M12 ? [research](skills/mattpocock/research/SKILL.md)

**Purpose:** Investigate a question using primary sources and save cited findings.

**Use for:** Documentation/API facts or comparative research are needed.

**Requirements:** Source/network access, file output, upstream requires a background subagent.

**Overlap:** Overlaps toolkit-maintain only for skill sourcing; otherwise broader research.

**Compatibility notes:** Use the current agent when delegation is unavailable or unauthorized; no automatic extra agents.

**Example:** Research this API contract from official sources and write a short cited note.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/research/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M13 ? [retro](skills/mattpocock/retro/SKILL.md)

**Purpose:** Look back at an agent session and suggest improvements to its environment.

**Use for:** A session retrospective is explicitly requested.

**Requirements:** writing-for-agents; access to the current session or selected logs and project checks.

**Overlap:** Useful feedback into toolkit maintenance, with project changes kept separate.

**Compatibility notes:** Strong preference for deterministic checks can expand scope; recommendations do not authorize edits to global instructions or project tooling.

**Example:** Review this session and propose the top environment improvements.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M14 ? [setup-matt-pocock-skills](skills/mattpocock/setup-matt-pocock-skills/SKILL.md)

**Purpose:** Set project tracker, triage labels, and domain-document routing.

**Use for:** You select tracker-dependent Matt engineering workflows.

**Requirements:** Bundled GitHub/GitLab/local templates; Git optional; gh/glab and account authorization only for remote tracker work.

**Overlap:** Adds project context; not a replacement for portable personal activation.

**Compatibility notes:** Configure the project after installation; preserve existing guidance. If triage is installed, upstream setup also creates missing labels in GitHub/GitLab. Local Markdown avoids account dependencies.

**Example:** Prepare local-Markdown tracker configuration for the selected skills.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/setup-matt-pocock-skills/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M15 ? [tdd](skills/mattpocock/tdd/SKILL.md)

**Purpose:** Build behavior in small red-then-green test/implementation slices.

**Use for:** You explicitly want test-first development.

**Requirements:** Project test runner; bundled tests/mocking references; codebase-design if the interface needs design.

**Overlap:** Adds a specific testing method beyond proportional checks.

**Compatibility notes:** Requires user confirmation of test seams before any test and moves refactoring into review; preserve known authorization and project test conventions.

**Example:** Implement this behavior test-first at the existing public interface.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M16 ? [to-spec](skills/mattpocock/to-spec/SKILL.md)

**Purpose:** Synthesize an existing conversation into a feature spec.

**Use for:** Requirements have already been discussed and need a durable spec.

**Requirements:** Configured tracker via setup; project context; gh/glab only for remote publishing.

**Overlap:** Planning output, not implementation.

**Compatibility notes:** Publishes to a tracker and asks about test seams; its extensive user-story template may exceed a small feature's needs.

**Example:** Turn our agreed requirements into a local spec.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M17 ? [to-tickets](skills/mattpocock/to-tickets/SKILL.md)

**Purpose:** Split a plan into complete verifiable slices and record blocking relationships.

**Use for:** A larger plan needs manageable implementation tickets.

**Requirements:** Configured local or remote tracker; local mode needs no service account.

**Overlap:** Adds task breakdown beyond a short plan.

**Compatibility notes:** Requires approval of breakdown before publication; avoid mandatory prefactoring unrelated to the approved scope.

**Example:** Split this spec into local tickets with real dependencies.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M18 ? [triage](skills/mattpocock/triage/SKILL.md)

**Purpose:** Classify incoming issues, verify reports, and prepare agent-ready briefs.

**Use for:** You maintain an incoming bug/feature queue.

**Requirements:** Tracker/labels setup; grilling and domain-modeling for interviews; gh/glab for remote queues.

**Overlap:** Overlaps bug diagnosis only at report verification.

**Compatibility notes:** Can post comments, change labels, and close issues; meaningful external writes need authorization. More useful for a shared issue queue than a tiny solo toolkit.

**Example:** Review incoming issues and propose triage outcomes.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/triage/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M19 ? [wayfinder](skills/mattpocock/wayfinder/SKILL.md)

**Purpose:** Maintain a map of decisions for a project too large to clarify in one session.

**Use for:** A large effort still has important unresolved decisions.

**Requirements:** Tracker setup, grilling, domain-modeling; research/prototype for their ticket types; authorized subagents in research flow.

**Overlap:** Heavy planning alternative; not a short task plan.

**Compatibility notes:** Advanced decision workflow with tracker writes, ticket assignment/closure, and research branch pushes. Keep separate from ordinary feature implementation and select execution scope explicitly.

**Example:** Map the unresolved decisions for this multi-session product effort.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wayfinder/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M20 ? [wizard](skills/mattpocock/wizard/SKILL.md)

**Purpose:** Generate an interactive Bash guide for setup steps a human must perform.

**Use for:** A repeatable manual setup/cutover needs a guided procedure.

**Requirements:** Bash, bundled template, browser opener; gh and credentials for optional GitHub secret writes; shellcheck optional.

**Overlap:** A tool-dependent workflow, not instruction-only execution.

**Compatibility notes:** Generated scripts read/write .env and can change remote secrets; Windows needs Bash or a port. Inspect each generated procedure before execution.

**Example:** Prepare a guided local setup script for the manual account steps.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wizard/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

## Matt Pocock / Productivity

### M21 ? [grill-me](skills/mattpocock/grill-me/SKILL.md)

**Purpose:** Run a deliberate interview to clarify a plan without saving domain docs.

**Use for:** You specifically request a thorough design interview.

**Requirements:** grilling; tool calls must map to the host's skill mechanism.

**Overlap:** Overlaps grill-with-docs; choose the stateless variant when no documentation is needed.

**Compatibility notes:** Exhaustive interviewing conflicts with routine minimal questions if made always-on; keep it explicitly invoked.

**Example:** Interview me about this plan before implementation.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grill-me/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M22 ? [grilling](skills/mattpocock/grilling/SKILL.md)

**Purpose:** Work through dependent design questions in rounds.

**Use for:** The user asks for a deep stress-test or another selected interview skill calls it.

**Requirements:** Authorized subagents for upstream fact-finding; no service account inherently needed.

**Overlap:** Shared dependency of interview-based Matt skills.

**Compatibility notes:** Waits until all branches are settled and user confirms understanding; adapt intensity and use direct fact-finding when delegation is unavailable.

**Example:** Stress-test this architecture's unresolved decisions.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M23 ? [handoff](skills/mattpocock/handoff/SKILL.md)

**Purpose:** Write portable context so another agent/session can continue.

**Use for:** Changing session, agent, directory, or handing work to someone else.

**Requirements:** File access and OS temp location; references to existing artifacts.

**Overlap:** Adds continuity without storing project context in the toolkit.

**Compatibility notes:** Keep project-specific handoffs outside .agents and make durable artifact paths clear. Redact private material.

**Example:** Write a handoff for continuing this feature in a new session.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/handoff/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M24 ? [teach](skills/mattpocock/teach/SKILL.md)

**Purpose:** Create a stateful learning workspace with lessons, references, and learning records.

**Use for:** Learning a concept over several sessions.

**Requirements:** Project-owned teaching directory, source access, HTML/browser support; bundled formats.

**Overlap:** Separate learning workflow, not development defaults.

**Compatibility notes:** Creates several workspace files and shared assets; use a separate teaching project rather than the canonical toolkit folder.

**Example:** Teach me this concept over short practical sessions.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/teach/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M25 ? [to-questionnaire](skills/mattpocock/to-questionnaire/SKILL.md)

**Purpose:** Write a focused questionnaire for a person with missing knowledge.

**Use for:** You need information from a stakeholder before making a decision.

**Requirements:** Markdown/file access and recipient/decision context; no sending integration needed.

**Overlap:** Complements clarification; does not contact the recipient.

**Compatibility notes:** Interviews you about recipient and goals, then writes a document; sending it is a separate action.

**Example:** Draft a questionnaire for the maintainer about these API limits.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/to-questionnaire/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M26 ? [wait-what](skills/mattpocock/wait-what/SKILL.md)

**Purpose:** Re-explain a message with missing context and plain terminology.

**Use for:** An explanation did not make sense to you.

**Requirements:** Conversation context; project glossary optional.

**Overlap:** Mostly repeats the existing plain-language preference.

**Compatibility notes:** Very small benefit as a separate skill; can remain a normal prompt.

**Example:** Re-explain the last point with the missing context.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/wait-what/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M27 ? [writing-for-agents](skills/mattpocock/writing-for-agents/SKILL.md)

**Purpose:** Improve skills, instruction files, and pointed-to docs using focused triggers and progressive disclosure.

**Use for:** Writing or revising agent-facing instructions.

**Requirements:** Bundled SKILL-MECHANICS reference; no external tool inherently required.

**Overlap:** Overlaps toolkit-maintain and built-in skill-creator, but adds an editorial lens.

**Compatibility notes:** Its invocation discussion mixes host-specific mechanics; keep current Codex metadata and check observed behavior rather than assuming zero context cost.

**Example:** Review this skill's trigger and remove unnecessary instruction overhead.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

## Matt Pocock / Specialized tools

### M28 ? [git-guardrails-claude-code](skills/mattpocock/git-guardrails-claude-code/SKILL.md)

**Purpose:** Install a Claude Code hook that blocks matching dangerous Git commands.

**Use for:** You explicitly want Git safety hooks in Claude Code.

**Requirements:** Claude Code hook support, Bash, jq, grep; project/global settings scope.

**Overlap:** Host integration, not a Codex instruction-only skill.

**Compatibility notes:** Does not protect Codex just by being copied. Pattern matching is not a complete security boundary; use only for its supported host after script review.

**Example:** Configure project-only Git guardrails for Claude Code.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/git-guardrails-claude-code/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M29 ? [migrate-to-shoehorn](skills/mattpocock/migrate-to-shoehorn/SKILL.md)

**Purpose:** Replace TypeScript test assertions with partial/invalid-data helpers.

**Use for:** You use as-casts in TypeScript tests and want this specific library.

**Requirements:** TypeScript, npm/package manager, @total-typescript/shoehorn, type checking.

**Overlap:** Specialized migration rather than a general testing skill.

**Compatibility notes:** Adds a dependency; test-only usage. Skip when the project does not need the library.

**Example:** Migrate these selected test fixtures to shoehorn.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/migrate-to-shoehorn/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M30 ? [scaffold-exercises](skills/mattpocock/scaffold-exercises/SKILL.md)

**Purpose:** Generate course exercise folders and starter READMEs.

**Use for:** Building lessons in the author's exercise layout.

**Requirements:** pnpm, ai-hero-cli internal lint, TypeScript examples, Git commits.

**Overlap:** Specialized course-authoring environment.

**Compatibility notes:** Requires the author's linter/conventions and commits changes; needs a generic adaptation for other course projects.

**Example:** Scaffold this section in an ai-hero-cli course project.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/scaffold-exercises/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M31 ? [setup-pre-commit](skills/mattpocock/setup-pre-commit/SKILL.md)

**Purpose:** Configure Husky, lint-staged, formatting, and project checks before commits.

**Use for:** You explicitly want a JavaScript/TypeScript pre-commit setup.

**Requirements:** Git, Node/package manager, husky, lint-staged, prettier; project test/type scripts.

**Overlap:** Integration for a project, not portable preference activation.

**Compatibility notes:** Installs dependencies, writes config/hooks, formats staged files, and commits; preserve existing tooling and separate commit authorization.

**Example:** Prepare pre-commit checks matching this project's existing tooling.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/setup-pre-commit/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

## Matt Pocock / Experimental

### M32 ? [chief-of-staff](skills/mattpocock/chief-of-staff/SKILL.md)

**Purpose:** Coordinate a long-running goal through subagents and environment improvements.

**Use for:** You want a dedicated orchestration session.

**Requirements:** Authorized subagents; optional scheduling/data sources supported by the host.

**Overlap:** Much broader than selective delegation or focused implementation.

**Compatibility notes:** Requires all work in subagents and proactively improves the environment on every message; conflicts with the small, focused toolkit defaults.

**Example:** Coordinate this explicitly scoped long-running goal.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/chief-of-staff/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M33 ? [claude-handoff](skills/mattpocock/claude-handoff/SKILL.md)

**Purpose:** Launch a fresh Claude background agent with a handoff summary.

**Use for:** You want a Claude-to-Claude background continuation.

**Requirements:** Claude CLI supporting --bg; shell invocation and background-agent authorization.

**Overlap:** Duplicates handoff plus a Claude-specific launcher.

**Compatibility notes:** Experimental and host-specific; the plain handoff skill is more portable.

**Example:** Continue this task in a named Claude background agent.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/claude-handoff/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M34 ? [loop-me](skills/mattpocock/loop-me/SKILL.md)

**Purpose:** Discover recurring personal workflows and write implementable specs.

**Use for:** You want to design repeatable workflows over several sessions.

**Requirements:** grilling discipline; project-owned NOTES.md and workflows files.

**Overlap:** Potentially useful later for toolkit growth.

**Compatibility notes:** Captures personal context and can create/edit/delete specs; keep it outside portable files and keep interview scope bounded.

**Example:** Help me specify a recurring documentation workflow.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/loop-me/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M35 ? [setup-ts-deep-modules](skills/mattpocock/setup-ts-deep-modules/SKILL.md)

**Purpose:** Enforce TypeScript package entry-point boundaries with dependency-cruiser.

**Use for:** You choose this package structure and want automated import checks.

**Requirements:** TypeScript, Node/package manager, dependency-cruiser, codebase-design; bundled config.

**Overlap:** Tool-enforced architecture, not generic module advice.

**Compatibility notes:** Installs tooling, adds scripts/example package, writes instruction pointers, and enforces a strong folder convention.

**Example:** Set up agreed TypeScript package-boundary checks.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/setup-ts-deep-modules/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M36 ? [writing-beats](skills/mattpocock/writing-beats/SKILL.md)

**Purpose:** Build an article as a sequence of selected narrative beats.

**Use for:** You want to shape existing raw material collaboratively.

**Requirements:** Input/output Markdown files and repeated user choices.

**Overlap:** Overlaps writing-shape; choose one article-shaping workflow.

**Compatibility notes:** Slow interactive writing workflow, not technical implementation; preserves user edits but needs frequent decisions.

**Example:** Shape these notes into an article one beat at a time.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-beats/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M37 ? [writing-fragments](skills/mattpocock/writing-fragments/SKILL.md)

**Purpose:** Collect unstructured writing ideas during an interview.

**Use for:** You want to explore material before choosing an article structure.

**Requirements:** Project-owned Markdown output and interview context.

**Overlap:** Feeds writing-beats or writing-shape rather than replacing either.

**Compatibility notes:** Appends material as it emerges; personal notes must remain outside the portable toolkit.

**Example:** Explore these ideas and collect useful article fragments.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-fragments/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

### M38 ? [writing-shape](skills/mattpocock/writing-shape/SKILL.md)

**Purpose:** Turn fixed raw material into an article one agreed block at a time.

**Use for:** You want paragraph-level editorial collaboration.

**Requirements:** Read-only raw source and a separate Markdown article file.

**Overlap:** Alternative to writing-beats; installing both may be unnecessary.

**Compatibility notes:** Requires frequent choices and format discussion; not a concise automatic writing workflow.

**Example:** Shape this raw material into a separate article.

**Source:** [Pinned source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-shape/SKILL.md); bundled files preserved. Behavior is not runtime-tested.

