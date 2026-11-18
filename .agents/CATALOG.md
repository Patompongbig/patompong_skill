# Portable skill catalog

Open this detailed catalog for user-requested skill browsing, selection help,
tree details, or catalog maintenance. Normal startup needs no toolkit
selection or catalog read. Use the small [workflow menu](workflows/INDEX.md) when
workflow choices are requested. Reading the catalog does not execute skills.

64 installed instruction skills: four original personal skills, 38 Matt
Pocock skills, six Ponytail skills, 15 Superpowers skills, and one Samber skill. Every local copy is explicit-only; selected skills can follow
relevant dependencies themselves. Status `enabled` means SKILL.md exists, not
automatic invocation or runtime proof. External system/plugin skills are outside
this portable catalog.

Workflows compose these skills: execute uses obra TDD, systematic-debugging,
receiving-code-review, verification-before-completion and Ponytail full;
qa-verify uses ponytail-review, Matt code-review and verification-before-completion;
development-plan uses obra writing-plans and Matt codebase-design;
software-requirement uses Matt domain-modeling and research. See the
[workflow menu](workflows/INDEX.md). Selecting a workflow loads only the skills
its current phase needs.

## Personal skills

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [toolkit-maintain](skills/toolkit-maintain/SKILL.md) | Maintain skills and compose editable workflows | Assigned toolkit/catalog/workflow maintenance | File access; Python for checks; network for imports; explicit-only | Original personal toolkit | enabled |
| [diagnose-bug](skills/diagnose-bug/SKILL.md) | Reproduce and diagnose a concrete software defect | Assigned failure/regression diagnosis | Relevant project runtime and tests; explicit-only | Original personal toolkit | enabled |
| [review-change](skills/review-change/SKILL.md) | Review a diff for actionable correctness defects | Assigned review of a change | File/diff access; project checks as relevant; explicit-only | Original personal toolkit | enabled |
| [market-research](skills/patompong/market-research/SKILL.md) | Stage 2: turn a confirmed intent into the cited "02 — Market Research" document | A new product/feature intent needs competitive landscape and build-vs-buy evidence; skipped for bugfix, refactor, infra, security-patch | samber/deep-research (sub-agents, web); web-search fallback; writes `patompong-docs/docs/research/`; explicit-only | Original personal toolkit; grouped under `skills/patompong/` | enabled |

## Matt Pocock collection

[Pinned provenance and license](skills/mattpocock/PROVENANCE.md);
[host/runtime compatibility](COMPATIBILITY.md); file inventory in `toolkit/IMPORTS.json` (source repository).
All bundled resources are installed; runtime prerequisites remain per target
project and host. Overlapping skills are retained because the user chose the
whole collection; explicit selection resolves which one is used.

### Matt Pocock / Engineering (20)

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [ask-matt](skills/mattpocock/ask-matt/SKILL.md) | Understand which Matt workflow to use. | You want a guide through the installed collection. | Many other Matt skills are mentioned; no task execution itself.; explicit-only | M01; MIT; pinned import | enabled |
| [code-review](skills/mattpocock/code-review/SKILL.md) | Review a fixed Git diff separately against standards and a spec. | Review a branch or changes since a named commit. | Git, two authorized subagents, spec/standards sources; configured issue tracker for tracker specs.; explicit-only | M02; MIT; pinned import | enabled |
| [codebase-design](skills/mattpocock/codebase-design/SKILL.md) | Design a module with useful behavior behind a small interface. | Interface design, testability, or simplifying module structure. | Bundled DEEPENING and DESIGN-IT-TWICE references; subagents only for alternative-design mode.; explicit-only | M03; MIT; pinned import | enabled |
| [diagnosing-bugs](skills/mattpocock/diagnosing-bugs/SKILL.md) | Build a precise failing feedback loop, minimize a defect, test hypotheses, and verify a fix. | A hard bug, flaky failure, or performance regression. | Project test/runtime tools; optional Bash human-reproduction template.; explicit-only | M04; MIT; pinned import | enabled |
| [domain-modeling](skills/mattpocock/domain-modeling/SKILL.md) | Clarify project terminology and record significant design choices. | Resolve overloaded domain terms or maintain a glossary and ADRs. | Bundled glossary/ADR formats and project-owned documentation.; explicit-only | M05; MIT; pinned import | enabled |
| [grill-with-docs](skills/mattpocock/grill-with-docs/SKILL.md) | Interview about a design and capture domain terms and decisions. | A substantial design needs deliberate clarification and written context. | grilling and domain-modeling; project documentation layout.; explicit-only | M06; MIT; pinned import | enabled |
| [implement](skills/mattpocock/implement/SKILL.md) | Build a spec or ticket with test-first work and a closing review. | Implementation of an already agreed scope. | tdd and code-review, Git, project type/test commands; review tracker configuration.; explicit-only | M08; MIT; pinned import | enabled |
| [implement-spec](skills/mattpocock/implement-spec/SKILL.md) | Implement a spec's dependency graph across parallel worktrees and an integration branch. | A large ticketed spec should be built by multiple agents. | tdd, code-review; tracker setup, Git/worktrees, several authorized subagents and project checks.; explicit-only | M07; MIT; pinned import | enabled |
| [improve-codebase-architecture](skills/mattpocock/improve-codebase-architecture/SKILL.md) | Find architectural friction and present candidates in a visual report. | You explicitly want to assess module structure. | codebase-design, grilling, domain-modeling; authorized subagent, browser, CDN access for the report.; explicit-only | M09; MIT; pinned import | enabled |
| [pr](skills/mattpocock/pr/SKILL.md) | Write a clear PR description with a compact visual, before/after evidence, and impact. | Drafting or improving a pull-request body. | File/text access; Git/PR service only if publishing is separately requested; retain CREDITS.md.; explicit-only | M10; MIT; pinned import | enabled |
| [prototype](skills/mattpocock/prototype/SKILL.md) | Build a disposable logic demo or contrasting UI variants to settle a design question. | A design decision needs something runnable or visual. | Bundled LOGIC/UI references; browser/project runner; upstream capture convention uses Git and an issue.; explicit-only | M11; MIT; pinned import | enabled |
| [research](skills/mattpocock/research/SKILL.md) | Investigate a question using primary sources and save cited findings. | Documentation/API facts or comparative research are needed. | Source/network access, file output, upstream requires a background subagent.; explicit-only | M12; MIT; pinned import | enabled |
| [retro](skills/mattpocock/retro/SKILL.md) | Look back at an agent session and suggest improvements to its environment. | A session retrospective is explicitly requested. | writing-for-agents; access to the current session or selected logs and project checks.; explicit-only | M13; MIT; pinned import | enabled |
| [setup-matt-pocock-skills](skills/mattpocock/setup-matt-pocock-skills/SKILL.md) | Set project tracker, triage labels, and domain-document routing. | You select tracker-dependent Matt engineering workflows. | Bundled GitHub/GitLab/local templates; Git optional; gh/glab and account authorization only for remote tracker work.; explicit-only | M14; MIT; pinned import | enabled |
| [tdd](skills/mattpocock/tdd/SKILL.md) | Build behavior in small red-then-green test/implementation slices. | You explicitly want test-first development. | Project test runner; bundled tests/mocking references; codebase-design if the interface needs design.; explicit-only | M15; MIT; pinned import | enabled |
| [to-spec](skills/mattpocock/to-spec/SKILL.md) | Synthesize an existing conversation into a feature spec. | Requirements have already been discussed and need a durable spec. | Configured tracker via setup; project context; gh/glab only for remote publishing.; explicit-only | M16; MIT; pinned import | enabled |
| [to-tickets](skills/mattpocock/to-tickets/SKILL.md) | Split a plan into complete verifiable slices and record blocking relationships. | A larger plan needs manageable implementation tickets. | Configured local or remote tracker; local mode needs no service account.; explicit-only | M17; MIT; pinned import | enabled |
| [triage](skills/mattpocock/triage/SKILL.md) | Classify incoming issues, verify reports, and prepare agent-ready briefs. | You maintain an incoming bug/feature queue. | Tracker/labels setup; grilling and domain-modeling for interviews; gh/glab for remote queues.; explicit-only | M18; MIT; pinned import | enabled |
| [wayfinder](skills/mattpocock/wayfinder/SKILL.md) | Maintain a map of decisions for a project too large to clarify in one session. | A large effort still has important unresolved decisions. | Tracker setup, grilling, domain-modeling; research/prototype for their ticket types; authorized subagents in research flow.; explicit-only | M19; MIT; pinned import | enabled |
| [wizard](skills/mattpocock/wizard/SKILL.md) | Generate an interactive Bash guide for setup steps a human must perform. | A repeatable manual setup/cutover needs a guided procedure. | Bash, bundled template, browser opener; gh and credentials for optional GitHub secret writes; shellcheck optional.; explicit-only | M20; MIT; pinned import | enabled |

#### M01: ask-matt

**Purpose:** Understand which Matt workflow to use.

**Use for:** You want a guide through the installed collection.

**Needs:** Many other Matt skills are mentioned; no task execution itself.

**Overlap:** Overlaps the local catalog and toolkit-maintain routing.

**Compatibility:** Its map assumes almost the whole collection; rewrite to reference only selected skills.

**Example request:** Help me choose a workflow for a multi-session feature.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M02: code-review

**Purpose:** Review a fixed Git diff separately against standards and a spec.

**Use for:** Review a branch or changes since a named commit.

**Needs:** Git, two authorized subagents, spec/standards sources; configured issue tracker for tracker specs.

**Overlap:** Strong overlap with review-change; broader standards/spec review.

**Compatibility:** Requires a fixed base, Git tracker configuration, and parallel reviewers; do not install as a duplicate automatic correctness reviewer.

**Example request:** Review this branch against main and the local feature spec.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M03: codebase-design

**Purpose:** Design a module with useful behavior behind a small interface.

**Use for:** Interface design, testability, or simplifying module structure.

**Needs:** Bundled DEEPENING and DESIGN-IT-TWICE references; subagents only for alternative-design mode.

**Overlap:** Adds architecture vocabulary beyond normal Codex behavior.

**Compatibility:** Requires specific jargon; relax forced terminology for plain-language explanations and make parallel design optional.

**Example request:** Compare two interface designs for this parser.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M04: diagnosing-bugs

**Purpose:** Build a precise failing feedback loop, minimize a defect, test hypotheses, and verify a fix.

**Use for:** A hard bug, flaky failure, or performance regression.

**Needs:** Project test/runtime tools; optional Bash human-reproduction template.

**Overlap:** Strong overlap with diagnose-bug.

**Compatibility:** Rigid no-hypothesis-before-reproduction gates can stall restricted environments; use its useful loop guidance to improve the local skill.

**Example request:** Diagnose this intermittent export failure with a repeatable check.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M05: domain-modeling

**Purpose:** Clarify project terminology and record significant design choices.

**Use for:** Resolve overloaded domain terms or maintain a glossary and ADRs.

**Needs:** Bundled glossary/ADR formats and project-owned documentation.

**Overlap:** Adds persistent project knowledge, not personal toolkit preferences.

**Compatibility:** Writes glossary changes during discussion; agree the project scope and keep outputs outside .agents.

**Example request:** Clarify what job, result, and import mean and record agreed terms.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M06: grill-with-docs

**Purpose:** Interview about a design and capture domain terms and decisions.

**Use for:** A substantial design needs deliberate clarification and written context.

**Needs:** grilling and domain-modeling; project documentation layout.

**Overlap:** Alternative to grill-me with persistent documentation.

**Compatibility:** Wrapper is only skill dispatch; both dependencies are needed. Keep deliberate interviews optional rather than asking exhaustively on routine work.

**Example request:** Stress-test this design and document the terms we agree on.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M08: implement

**Purpose:** Build a spec or ticket with test-first work and a closing review.

**Use for:** Implementation of an already agreed scope.

**Needs:** tdd and code-review, Git, project type/test commands; review tracker configuration.

**Overlap:** Overlaps ordinary implementation work in normal Codex mode.

**Compatibility:** Commits automatically and inherits mandatory checkpoints/subagent assumptions from dependencies; adapt before use.

**Example request:** Implement this approved ticket and verify it.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M07: implement-spec

**Purpose:** Implement a spec's dependency graph across parallel worktrees and an integration branch.

**Use for:** A large ticketed spec should be built by multiple agents.

**Needs:** tdd, code-review; tracker setup, Git/worktrees, several authorized subagents and project checks.

**Overlap:** Heavy alternative to the ordinary implementation workflow.

**Compatibility:** Creates branches, merges, can open/ready PRs and close tickets; requires explicit scope and a host with delegation support.

**Example request:** Implement this approved multi-ticket spec on an integration branch.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement-spec/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M09: improve-codebase-architecture

**Purpose:** Find architectural friction and present candidates in a visual report.

**Use for:** You explicitly want to assess module structure.

**Needs:** codebase-design, grilling, domain-modeling; authorized subagent, browser, CDN access for the report.

**Overlap:** Adds an architecture survey beyond review-change.

**Compatibility:** Creates a temp HTML report using remote Tailwind/Mermaid; offer offline output and single-agent execution and keep refactors separately authorized.

**Example request:** Survey this subsystem and show the best simplification candidates.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/improve-codebase-architecture/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M10: pr

**Purpose:** Write a clear PR description with a compact visual, before/after evidence, and impact.

**Use for:** Drafting or improving a pull-request body.

**Needs:** File/text access; Git/PR service only if publishing is separately requested; retain CREDITS.md.

**Overlap:** Complements review-change; does not perform the review.

**Compatibility:** The full template can be heavy for small changes; scale it to change size and retain Dex Horthy/Humanlayer attribution.

**Example request:** Draft a concise PR body for this completed change; do not publish.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/pr/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M11: prototype

**Purpose:** Build a disposable logic demo or contrasting UI variants to settle a design question.

**Use for:** A design decision needs something runnable or visual.

**Needs:** Bundled LOGIC/UI references; browser/project runner; upstream capture convention uses Git and an issue.

**Overlap:** Distinct from production implementation.

**Compatibility:** Upstream commits prototypes to a branch and links tracker issues; make capture fit the project. Omitted hardening applies only to isolated prototypes.

**Example request:** Build a local demo to compare these cancellation states.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M12: research

**Purpose:** Investigate a question using primary sources and save cited findings.

**Use for:** Documentation/API facts or comparative research are needed.

**Needs:** Source/network access, file output, upstream requires a background subagent.

**Overlap:** Overlaps toolkit-maintain only for skill sourcing; otherwise broader research.

**Compatibility:** Use the current agent when delegation is unavailable or unauthorized; no automatic extra agents.

**Example request:** Research this API contract from official sources and write a short cited note.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/research/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M13: retro

**Purpose:** Look back at an agent session and suggest improvements to its environment.

**Use for:** A session retrospective is explicitly requested.

**Needs:** writing-for-agents; access to the current session or selected logs and project checks.

**Overlap:** Useful feedback into toolkit maintenance, with project changes kept separate.

**Compatibility:** Strong preference for deterministic checks can expand scope; recommendations do not authorize edits to global instructions or project tooling.

**Example request:** Review this session and propose the top environment improvements.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M14: setup-matt-pocock-skills

**Purpose:** Set project tracker, triage labels, and domain-document routing.

**Use for:** You select tracker-dependent Matt engineering workflows.

**Needs:** Bundled GitHub/GitLab/local templates; Git optional; gh/glab and account authorization only for remote tracker work.

**Overlap:** Adds project context; not a replacement for portable personal activation.

**Compatibility:** Configure the project after installation; preserve existing guidance. If triage is installed, upstream setup also creates missing labels in GitHub/GitLab. Local Markdown avoids account dependencies.

**Example request:** Prepare local-Markdown tracker configuration for the selected skills.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/setup-matt-pocock-skills/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M15: tdd

**Purpose:** Build behavior in small red-then-green test/implementation slices.

**Use for:** You explicitly want test-first development.

**Needs:** Project test runner; bundled tests/mocking references; codebase-design if the interface needs design.

**Overlap:** Adds a specific testing method beyond proportional checks.

**Compatibility:** Requires user confirmation of test seams before any test and moves refactoring into review; preserve known authorization and project test conventions.

**Example request:** Implement this behavior test-first at the existing public interface.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M16: to-spec

**Purpose:** Synthesize an existing conversation into a feature spec.

**Use for:** Requirements have already been discussed and need a durable spec.

**Needs:** Configured tracker via setup; project context; gh/glab only for remote publishing.

**Overlap:** Planning output, not implementation.

**Compatibility:** Publishes to a tracker and asks about test seams; its extensive user-story template may exceed a small feature's needs.

**Example request:** Turn our agreed requirements into a local spec.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M17: to-tickets

**Purpose:** Split a plan into complete verifiable slices and record blocking relationships.

**Use for:** A larger plan needs manageable implementation tickets.

**Needs:** Configured local or remote tracker; local mode needs no service account.

**Overlap:** Adds task breakdown beyond a short plan.

**Compatibility:** Requires approval of breakdown before publication; avoid mandatory prefactoring unrelated to the approved scope.

**Example request:** Split this spec into local tickets with real dependencies.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M18: triage

**Purpose:** Classify incoming issues, verify reports, and prepare agent-ready briefs.

**Use for:** You maintain an incoming bug/feature queue.

**Needs:** Tracker/labels setup; grilling and domain-modeling for interviews; gh/glab for remote queues.

**Overlap:** Overlaps bug diagnosis only at report verification.

**Compatibility:** Can post comments, change labels, and close issues; meaningful external writes need authorization. More useful for a shared issue queue than a tiny solo toolkit.

**Example request:** Review incoming issues and propose triage outcomes.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/triage/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M19: wayfinder

**Purpose:** Maintain a map of decisions for a project too large to clarify in one session.

**Use for:** A large effort still has important unresolved decisions.

**Needs:** Tracker setup, grilling, domain-modeling; research/prototype for their ticket types; authorized subagents in research flow.

**Overlap:** Heavy planning alternative; not a short task plan.

**Compatibility:** Advanced decision workflow with tracker writes, ticket assignment/closure, and research branch pushes. Keep separate from ordinary feature implementation and select execution scope explicitly.

**Example request:** Map the unresolved decisions for this multi-session product effort.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wayfinder/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M20: wizard

**Purpose:** Generate an interactive Bash guide for setup steps a human must perform.

**Use for:** A repeatable manual setup/cutover needs a guided procedure.

**Needs:** Bash, bundled template, browser opener; gh and credentials for optional GitHub secret writes; shellcheck optional.

**Overlap:** A tool-dependent workflow, not instruction-only execution.

**Compatibility:** Generated scripts read/write .env and can change remote secrets; Windows needs Bash or a port. Inspect each generated procedure before execution.

**Example request:** Prepare a guided local setup script for the manual account steps.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wizard/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

### Matt Pocock / Productivity (7)

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [grill-me](skills/mattpocock/grill-me/SKILL.md) | Run a deliberate interview to clarify a plan without saving domain docs. | You specifically request a thorough design interview. | grilling; tool calls must map to the host's skill mechanism.; explicit-only | M21; MIT; pinned import | enabled |
| [grilling](skills/mattpocock/grilling/SKILL.md) | Work through dependent design questions in rounds. | The user asks for a deep stress-test or another selected interview skill calls it. | Authorized subagents for upstream fact-finding; no service account inherently needed.; explicit-only | M22; MIT; pinned import | enabled |
| [handoff](skills/mattpocock/handoff/SKILL.md) | Write portable context so another agent/session can continue. | Changing session, agent, directory, or handing work to someone else. | File access and OS temp location; references to existing artifacts.; explicit-only | M23; MIT; pinned import | enabled |
| [teach](skills/mattpocock/teach/SKILL.md) | Create a stateful learning workspace with lessons, references, and learning records. | Learning a concept over several sessions. | Project-owned teaching directory, source access, HTML/browser support; bundled formats.; explicit-only | M24; MIT; pinned import | enabled |
| [to-questionnaire](skills/mattpocock/to-questionnaire/SKILL.md) | Write a focused questionnaire for a person with missing knowledge. | You need information from a stakeholder before making a decision. | Markdown/file access and recipient/decision context; no sending integration needed.; explicit-only | M25; MIT; pinned import | enabled |
| [wait-what](skills/mattpocock/wait-what/SKILL.md) | Re-explain a message with missing context and plain terminology. | An explanation did not make sense to you. | Conversation context; project glossary optional.; explicit-only | M26; MIT; pinned import | enabled |
| [writing-for-agents](skills/mattpocock/writing-for-agents/SKILL.md) | Improve skills, instruction files, and pointed-to docs using focused triggers and progressive disclosure. | Writing or revising agent-facing instructions. | Bundled SKILL-MECHANICS reference; no external tool inherently required.; explicit-only | M27; MIT; pinned import | enabled |

#### M21: grill-me

**Purpose:** Run a deliberate interview to clarify a plan without saving domain docs.

**Use for:** You specifically request a thorough design interview.

**Needs:** grilling; tool calls must map to the host's skill mechanism.

**Overlap:** Overlaps grill-with-docs; choose the stateless variant when no documentation is needed.

**Compatibility:** Exhaustive interviewing conflicts with routine minimal questions if made always-on; keep it explicitly invoked.

**Example request:** Interview me about this plan before implementation.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grill-me/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M22: grilling

**Purpose:** Work through dependent design questions in rounds.

**Use for:** The user asks for a deep stress-test or another selected interview skill calls it.

**Needs:** Authorized subagents for upstream fact-finding; no service account inherently needed.

**Overlap:** Shared dependency of interview-based Matt skills.

**Compatibility:** Waits until all branches are settled and user confirms understanding; adapt intensity and use direct fact-finding when delegation is unavailable.

**Example request:** Stress-test this architecture's unresolved decisions.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M23: handoff

**Purpose:** Write portable context so another agent/session can continue.

**Use for:** Changing session, agent, directory, or handing work to someone else.

**Needs:** File access and OS temp location; references to existing artifacts.

**Overlap:** Adds continuity without storing project context in the toolkit.

**Compatibility:** Keep project-specific handoffs outside .agents and make durable artifact paths clear. Redact private material.

**Example request:** Write a handoff for continuing this feature in a new session.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/handoff/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M24: teach

**Purpose:** Create a stateful learning workspace with lessons, references, and learning records.

**Use for:** Learning a concept over several sessions.

**Needs:** Project-owned teaching directory, source access, HTML/browser support; bundled formats.

**Overlap:** Separate learning workflow, not development defaults.

**Compatibility:** Creates several workspace files and shared assets; use a separate teaching project rather than the canonical toolkit folder.

**Example request:** Teach me this concept over short practical sessions.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/teach/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M25: to-questionnaire

**Purpose:** Write a focused questionnaire for a person with missing knowledge.

**Use for:** You need information from a stakeholder before making a decision.

**Needs:** Markdown/file access and recipient/decision context; no sending integration needed.

**Overlap:** Complements clarification; does not contact the recipient.

**Compatibility:** Interviews you about recipient and goals, then writes a document; sending it is a separate action.

**Example request:** Draft a questionnaire for the maintainer about these API limits.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/to-questionnaire/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M26: wait-what

**Purpose:** Re-explain a message with missing context and plain terminology.

**Use for:** An explanation did not make sense to you.

**Needs:** Conversation context; project glossary optional.

**Overlap:** Mostly repeats the existing plain-language preference.

**Compatibility:** Very small benefit as a separate skill; can remain a normal prompt.

**Example request:** Re-explain the last point with the missing context.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/wait-what/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M27: writing-for-agents

**Purpose:** Improve skills, instruction files, and pointed-to docs using focused triggers and progressive disclosure.

**Use for:** Writing or revising agent-facing instructions.

**Needs:** Bundled SKILL-MECHANICS reference; no external tool inherently required.

**Overlap:** Overlaps toolkit-maintain and built-in skill-creator, but adds an editorial lens.

**Compatibility:** Its invocation discussion mixes host-specific mechanics; keep current Codex metadata and check observed behavior rather than assuming zero context cost.

**Example request:** Review this skill's trigger and remove unnecessary instruction overhead.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

### Matt Pocock / Specialized tools (4)

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [git-guardrails-claude-code](skills/mattpocock/git-guardrails-claude-code/SKILL.md) | Install a Claude Code hook that blocks matching dangerous Git commands. | You explicitly want Git safety hooks in Claude Code. | Claude Code hook support, Bash, jq, grep; project/global settings scope.; explicit-only | M28; MIT; pinned import | enabled |
| [migrate-to-shoehorn](skills/mattpocock/migrate-to-shoehorn/SKILL.md) | Replace TypeScript test assertions with partial/invalid-data helpers. | You use as-casts in TypeScript tests and want this specific library. | TypeScript, npm/package manager, @total-typescript/shoehorn, type checking.; explicit-only | M29; MIT; pinned import | enabled |
| [scaffold-exercises](skills/mattpocock/scaffold-exercises/SKILL.md) | Generate course exercise folders and starter READMEs. | Building lessons in the author's exercise layout. | pnpm, ai-hero-cli internal lint, TypeScript examples, Git commits.; explicit-only | M30; MIT; pinned import | enabled |
| [setup-pre-commit](skills/mattpocock/setup-pre-commit/SKILL.md) | Configure Husky, lint-staged, formatting, and project checks before commits. | You explicitly want a JavaScript/TypeScript pre-commit setup. | Git, Node/package manager, husky, lint-staged, prettier; project test/type scripts.; explicit-only | M31; MIT; pinned import | enabled |

#### M28: git-guardrails-claude-code

**Purpose:** Install a Claude Code hook that blocks matching dangerous Git commands.

**Use for:** You explicitly want Git safety hooks in Claude Code.

**Needs:** Claude Code hook support, Bash, jq, grep; project/global settings scope.

**Overlap:** Host integration, not a Codex instruction-only skill.

**Compatibility:** Does not protect Codex just by being copied. Pattern matching is not a complete security boundary; use only for its supported host after script review.

**Example request:** Configure project-only Git guardrails for Claude Code.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/git-guardrails-claude-code/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M29: migrate-to-shoehorn

**Purpose:** Replace TypeScript test assertions with partial/invalid-data helpers.

**Use for:** You use as-casts in TypeScript tests and want this specific library.

**Needs:** TypeScript, npm/package manager, @total-typescript/shoehorn, type checking.

**Overlap:** Specialized migration rather than a general testing skill.

**Compatibility:** Adds a dependency; test-only usage. Skip when the project does not need the library.

**Example request:** Migrate these selected test fixtures to shoehorn.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/migrate-to-shoehorn/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M30: scaffold-exercises

**Purpose:** Generate course exercise folders and starter READMEs.

**Use for:** Building lessons in the author's exercise layout.

**Needs:** pnpm, ai-hero-cli internal lint, TypeScript examples, Git commits.

**Overlap:** Specialized course-authoring environment.

**Compatibility:** Requires the author's linter/conventions and commits changes; needs a generic adaptation for other course projects.

**Example request:** Scaffold this section in an ai-hero-cli course project.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/scaffold-exercises/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M31: setup-pre-commit

**Purpose:** Configure Husky, lint-staged, formatting, and project checks before commits.

**Use for:** You explicitly want a JavaScript/TypeScript pre-commit setup.

**Needs:** Git, Node/package manager, husky, lint-staged, prettier; project test/type scripts.

**Overlap:** Integration for a project, not portable preference activation.

**Compatibility:** Installs dependencies, writes config/hooks, formats staged files, and commits; preserve existing tooling and separate commit authorization.

**Example request:** Prepare pre-commit checks matching this project's existing tooling.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/setup-pre-commit/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

### Matt Pocock / Experimental: upstream in-progress (7)

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [chief-of-staff](skills/mattpocock/chief-of-staff/SKILL.md) | Coordinate a long-running goal through subagents and environment improvements. | You want a dedicated orchestration session. | Authorized subagents; optional scheduling/data sources supported by the host.; explicit-only | M32; MIT; pinned import; experimental | enabled |
| [claude-handoff](skills/mattpocock/claude-handoff/SKILL.md) | Launch a fresh Claude background agent with a handoff summary. | You want a Claude-to-Claude background continuation. | Claude CLI supporting --bg; shell invocation and background-agent authorization.; explicit-only | M33; MIT; pinned import; experimental | enabled |
| [loop-me](skills/mattpocock/loop-me/SKILL.md) | Discover recurring personal workflows and write implementable specs. | You want to design repeatable workflows over several sessions. | grilling discipline; project-owned NOTES.md and workflows files.; explicit-only | M34; MIT; pinned import; experimental | enabled |
| [setup-ts-deep-modules](skills/mattpocock/setup-ts-deep-modules/SKILL.md) | Enforce TypeScript package entry-point boundaries with dependency-cruiser. | You choose this package structure and want automated import checks. | TypeScript, Node/package manager, dependency-cruiser, codebase-design; bundled config.; explicit-only | M35; MIT; pinned import; experimental | enabled |
| [writing-beats](skills/mattpocock/writing-beats/SKILL.md) | Build an article as a sequence of selected narrative beats. | You want to shape existing raw material collaboratively. | Input/output Markdown files and repeated user choices.; explicit-only | M36; MIT; pinned import; experimental | enabled |
| [writing-fragments](skills/mattpocock/writing-fragments/SKILL.md) | Collect unstructured writing ideas during an interview. | You want to explore material before choosing an article structure. | Project-owned Markdown output and interview context.; explicit-only | M37; MIT; pinned import; experimental | enabled |
| [writing-shape](skills/mattpocock/writing-shape/SKILL.md) | Turn fixed raw material into an article one agreed block at a time. | You want paragraph-level editorial collaboration. | Read-only raw source and a separate Markdown article file.; explicit-only | M38; MIT; pinned import; experimental | enabled |

#### M32: chief-of-staff

**Purpose:** Coordinate a long-running goal through subagents and environment improvements.

**Use for:** You want a dedicated orchestration session.

**Needs:** Authorized subagents; optional scheduling/data sources supported by the host.

**Overlap:** Much broader than selective delegation or focused implementation.

**Compatibility:** Requires all work in subagents and proactively improves the environment on every message; conflicts with the small, focused toolkit defaults.

**Example request:** Coordinate this explicitly scoped long-running goal.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/chief-of-staff/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M33: claude-handoff

**Purpose:** Launch a fresh Claude background agent with a handoff summary.

**Use for:** You want a Claude-to-Claude background continuation.

**Needs:** Claude CLI supporting --bg; shell invocation and background-agent authorization.

**Overlap:** Duplicates handoff plus a Claude-specific launcher.

**Compatibility:** Experimental and host-specific; the plain handoff skill is more portable.

**Example request:** Continue this task in a named Claude background agent.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/claude-handoff/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M34: loop-me

**Purpose:** Discover recurring personal workflows and write implementable specs.

**Use for:** You want to design repeatable workflows over several sessions.

**Needs:** grilling discipline; project-owned NOTES.md and workflows files.

**Overlap:** Potentially useful later for toolkit growth.

**Compatibility:** Captures personal context and can create/edit/delete specs; keep it outside portable files and keep interview scope bounded.

**Example request:** Help me specify a recurring documentation workflow.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/loop-me/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M35: setup-ts-deep-modules

**Purpose:** Enforce TypeScript package entry-point boundaries with dependency-cruiser.

**Use for:** You choose this package structure and want automated import checks.

**Needs:** TypeScript, Node/package manager, dependency-cruiser, codebase-design; bundled config.

**Overlap:** Tool-enforced architecture, not generic module advice.

**Compatibility:** Installs tooling, adds scripts/example package, writes instruction pointers, and enforces a strong folder convention.

**Example request:** Set up agreed TypeScript package-boundary checks.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/setup-ts-deep-modules/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M36: writing-beats

**Purpose:** Build an article as a sequence of selected narrative beats.

**Use for:** You want to shape existing raw material collaboratively.

**Needs:** Input/output Markdown files and repeated user choices.

**Overlap:** Overlaps writing-shape; choose one article-shaping workflow.

**Compatibility:** Slow interactive writing workflow, not technical implementation; preserves user edits but needs frequent decisions.

**Example request:** Shape these notes into an article one beat at a time.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-beats/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M37: writing-fragments

**Purpose:** Collect unstructured writing ideas during an interview.

**Use for:** You want to explore material before choosing an article structure.

**Needs:** Project-owned Markdown output and interview context.

**Overlap:** Feeds writing-beats or writing-shape rather than replacing either.

**Compatibility:** Appends material as it emerges; personal notes must remain outside the portable toolkit.

**Example request:** Explore these ideas and collect useful article fragments.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-fragments/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

#### M38: writing-shape

**Purpose:** Turn fixed raw material into an article one agreed block at a time.

**Use for:** You want paragraph-level editorial collaboration.

**Needs:** Read-only raw source and a separate Markdown article file.

**Overlap:** Alternative to writing-beats; installing both may be unnecessary.

**Compatibility:** Requires frequent choices and format discussion; not a concise automatic writing workflow.

**Example request:** Shape this raw material into a separate article.

**Source:** [Pinned upstream](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-shape/SKILL.md). All files in its skill folder
are retained; see installed inventory for original/installed hashes.

## Choosing combinations

- Interview: grill-me follows grilling; grill-with-docs also follows domain-modeling.
- Build: implement follows tdd and code-review; implement-spec adds parallel task orchestration.
- Architecture: codebase-design provides design principles; improve-codebase-architecture surveys candidates.
- Continuity: handoff writes portable session context; teach maintains a separate learning workspace.
- Planning: target-project setup chooses local tasks or a tracker; to-spec and to-tickets write the artifacts.

Use workflow <name> to select a composition, or name one author/skill directly.
For example: "Use lone-skill mattpocock/handoff" or
"Use toolkit-maintain to create a workflow combining mattpocock/prototype and review-change."

## Ponytail collection (6)

[Pinned provenance and license](skills/ponytail/PROVENANCE.md); [compatibility](COMPATIBILITY.md).
All six are installed as explicit-only instruction skills. Select them independently
or compose them in a workflow later; no automatic startup hooks are installed.

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [ponytail](skills/ponytail/ponytail/SKILL.md) | Build the smallest complete solution using existing code and platform features | Explicitly selected implementation modifier; lite/full/ultra | Relevant code, callers and project checks; explicit-only | P01; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |
| [ponytail-review](skills/ponytail/ponytail-review/SKILL.md) | Review changes for concrete defects, safety, load, tests, speed and complexity | Assigned diff, staged, branch, PR or file review; report only | File/diff access; Git or PR access when applicable; explicit-only | P02; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |
| [ponytail-audit](skills/ponytail/ponytail-audit/SKILL.md) | Map a repository or subsystem and rank quality and maintenance findings | Explicitly scoped repository/folder audit; report only | Repository access; expected load; runtime checks only when run; explicit-only | P03; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |
| [ponytail-debt](skills/ponytail/ponytail-debt/SKILL.md) | Collect deliberate shortcut markers and their upgrade triggers | Assigned shortcut-debt ledger; writes only if requested | rg or equivalent; optional Git blame; marker convention; explicit-only | P04; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |
| [ponytail-gain](skills/ponytail/ponytail-gain/SKILL.md) | Explain published benchmark results without inventing project savings | User asks about Ponytail benchmark impact | Bundled benchmark report and README; no live measurement; explicit-only | P05; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |
| [ponytail-help](skills/ponytail/ponytail-help/SKILL.md) | Explain portable skill selection, modes and paths | User requests a Ponytail usage reference | No plugin, hook or global config required; explicit-only | P06; Dietrich Gebert; MIT; pinned 5.1.0 | enabled |

### Benefits, overlap, and selection

- **ponytail:** reuse existing code before creating new machinery. Lite keeps scope
  alternatives under user control; full applies the ladder; ultra challenges need.
  Example: reuse the project's input component rather than build a custom calendar.
  Complements an implementation workflow; preserve its project checks and requested
  explanation depth. The mode persists only after selection, within that session.
- **ponytail-review:** checks connected callers as well as the diff, reporting
  correctness, safety, load, tests, speed, and unnecessary complexity. Example:
  catch a consumer outside a field-rename diff. Overlaps review-change and Matt's
  code-review; choose a primary reviewer instead of running all by default.
- **ponytail-audit:** maps entry points and data flow and ranks up to 20 findings.
  Example: assess the importer before a reliability project. Requires an explicit
  audit scope. Overlaps architecture surveys but covers broader operational risks;
  disclose unread code and distinguish static findings from runtime proof.
- **ponytail-debt:** collects shortcut markers, limits, and upgrade triggers. Example:
  list importer shortcuts lacking revisit conditions. Useful only where markers
  exist; the core mode is not required. Report only unless a ledger is requested.
- **ponytail-gain:** displays published benchmark methodology and averages, not
  project savings. Its bundled Claude Code evidence has not been reproduced here.
- **ponytail-help:** explains these skills, mode selection, exact path invocation,
  and user-requested updates. It does not activate a mode or load every skill body.

These entries can be lone skills or future workflow components. Installation does
not add them to the session workflow menu or select a workflow on your behalf.

## Samber collection (1)

[Pinned provenance and license](skills/samber/PROVENANCE.md); [compatibility](COMPATIBILITY.md).

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [deep-research](skills/samber/deep-research/SKILL.md) | Multi-source research with parallel sub-agent tracks, confidence tracking and a cited report | A thorough sourced report is the deliverable (market, competitive, technical, academic, legal, trend and more) | Web search and fetch; sub-agents for parallel tracks; optional pandoc or md-to-pdf; explicit-only | S01; Samuel Berthe / samber; MIT; pinned 1.3.0 | enabled |

#### S01: deep-research

**Benefit:** Parallel research tracks with per-claim citations, source tiers and a confidence ladder; a separate report-writer sub-agent keeps the coordinator's context clean.

**Example:** "Research the AI coding assistant market and write a cited report."

**Overlap:** Matt research (M12) for single cited notes from primary sources; deep-research is broader and multi-track. Used by personal market-research.

**Cost/scope:** standard depth spawns many sub-agents across three fan-out steps; callers such as market-research narrow it to one fan-out. Default output goes to `./research/` unless a caller overrides it.

## Superpowers collection / obra (15)

Version 7.0.0, pinned import. [Provenance and MIT license](skills/obra/PROVENANCE.md);
[compatibility and runtime requirements](skills/obra/COMPATIBILITY.md).
All entries are explicit-only. Upstream automatic startup is adapted to your
selected workflow; installation adds no workflow or implicit activation.

### Superpowers / Design and requirements

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [brainstorming](skills/obra/brainstorming/SKILL.md) | Clarify intent, constraints, choices and scope before building | A substantial new idea needs a design conversation | File/source access; optional browser companion requires Node.js and Bash; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [writing-plans](skills/obra/writing-plans/SKILL.md) | Turn an agreed specification into testable implementation tasks | A multi-step task needs exact files, interfaces, tests and commands | Agreed spec; project conventions; execution method chosen at handoff; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |

#### brainstorming

**Benefit:** Turn a feature idea into a design whose assumptions you can review.

**Example:** "Clarify what a batch importer should do before planning its implementation."

**Overlap:** Matt grill-me/grilling; Ponytail lite scope discussion.

**Requirements:** File/source access; optional browser companion requires Node.js and Bash.

**Workflow behavior:** design/plan review gates can pause before implementation. Existing user authorization and the selected execution method are preserved; this is an explicit process choice, not a prerequisite for every task.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/brainstorming/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### writing-plans

**Benefit:** Leave enough detail for another agent to implement without guessing.

**Example:** "Plan the importer with exact validation tests and task interfaces."

**Overlap:** Matt write-spec and spec-to-issues; different task granularity.

**Requirements:** Agreed spec; project conventions; execution method chosen at handoff.

**Workflow behavior:** design/plan review gates can pause before implementation. Existing user authorization and the selected execution method are preserved; this is an explicit process choice, not a prerequisite for every task.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-plans/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

### Superpowers / Implementation

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [executing-plans](skills/obra/executing-plans/SKILL.md) | Implement an agreed plan inline with a durable progress ledger | You choose the current agent as implementer instead of per-task subagents | Git; project test tools; Bash helpers or documented manual equivalents; final reviewer if supported; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [subagent-driven-development](skills/obra/subagent-driven-development/SKILL.md) | Execute planned tasks with independent implementers and review gates | You explicitly select an agent-driven execution method for a scoped plan | Multi-agent tools; Git; project tests; Bash helpers or manual equivalents; more review contexts; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [test-driven-development](skills/obra/test-driven-development/SKILL.md) | Write a failing behavior test before code, then pass and refactor | You select test-first feature or bug-fix implementation | Runnable project tests; writing-good-tests.md reference; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |

#### executing-plans

**Benefit:** Resume long work reliably while avoiding a new implementer context per task.

**Example:** "Execute an approved plan here and report verification and recorded rulings."

**Overlap:** Matt implement; single implementer with ledger rather than per-task delegation.

**Requirements:** Git; project test tools; Bash helpers or documented manual equivalents; final reviewer if supported.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/executing-plans/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### subagent-driven-development

**Benefit:** Separate implementation from review and retain evidence across compaction.

**Example:** "Implement an approved plan with a fresh worker and reviewer per meaningful task."

**Overlap:** Matt implement-spec; Superpowers emphasizes task briefs, ledger and bounded review loops.

**Requirements:** Multi-agent tools; Git; project tests; Bash helpers or manual equivalents; more review contexts.

**Cost/scope:** multiple fresh agent contexts can increase cost. Select this when independent checks or transcript dimensions justify it; installed does not mean behavioral tests have been run.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### test-driven-development

**Benefit:** Prove tests detect missing behavior before relying on a green run.

**Example:** "Add a failing test for a malformed import row before implementing validation."

**Overlap:** Matt tdd; this version is particularly strict about red-green evidence.

**Requirements:** Runnable project tests; writing-good-tests.md reference.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

### Superpowers / Debugging and evidence

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [systematic-debugging](skills/obra/systematic-debugging/SKILL.md) | Reproduce, trace, hypothesize and test the root cause before fixing | A bug, regression, build failure or unexpected behavior needs investigation | Relevant logs/runtime/tests; bundled tracing and waiting techniques; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [verification-before-completion](skills/obra/verification-before-completion/SKILL.md) | Require fresh relevant evidence before reporting success | A selected task is about to be called complete, fixed or passing | The commands that actually prove the specific claim; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [diagnosing-superpowers](skills/obra/diagnosing-superpowers/SKILL.md) | Investigate a failed agent session from transcripts with cited evidence | You ask why Superpowers repeated work, ignored a plan or used excessive time | Authorized local transcripts; analyst agents; optional issue tools and separately requested scrubbed export; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |

#### systematic-debugging

**Benefit:** Replace repeated guesses with evidence about where the failure starts.

**Example:** "Trace an importer failure through parser and caller before changing code."

**Overlap:** Personal diagnose-bug and Matt diagnosing-bugs.

**Requirements:** Relevant logs/runtime/tests; bundled tracing and waiting techniques.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### verification-before-completion

**Benefit:** Prevent claims based on a diff, old test result or worker summary alone.

**Example:** "Verify the reproduction and relevant tests before saying the bug is fixed."

**Overlap:** Existing reporting defaults and review workflows; small verification gate.

**Requirements:** The commands that actually prove the specific claim.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### diagnosing-superpowers

**Benefit:** Distinguish observed session behavior from speculation about the skill.

**Example:** "Explain repeated task execution in a specified session without modifying its logs."

**Overlap:** Matt retro; focuses on transcript evidence and maintainer reports.

**Requirements:** Authorized local transcripts; analyst agents; optional issue tools and separately requested scrubbed export.

**Cost/scope:** multiple fresh agent contexts can increase cost. Select this when independent checks or transcript dimensions justify it; installed does not mean behavioral tests have been run.

**Boundaries:** transcript analysis is read-only; report findings with file/line evidence. A scrubbed bundle or GitHub issue is a separately requested action with review gates.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/diagnosing-superpowers/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

### Superpowers / Review and delivery

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [requesting-code-review](skills/obra/requesting-code-review/SKILL.md) | Request an independent review against requirements and an exact diff range | You select a review gate for a feature, task or pre-merge check | Git diff range; code-reviewer.md; a supported authorized reviewer agent; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [receiving-code-review](skills/obra/receiving-code-review/SKILL.md) | Verify review feedback before applying it or pushing back | You assign assessment or implementation of review comments | Feedback, code and relevant tests; posting replies only when authorized; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [finishing-a-development-branch](skills/obra/finishing-a-development-branch/SKILL.md) | Verify a branch and prepare the chosen integration or handoff | Implementation is ready and you need to merge, open a PR or keep the branch | Git; passing project checks; forge access for a requested push/PR; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |

#### requesting-code-review

**Benefit:** Give a reviewer bounded evidence instead of your full conversation history.

**Example:** "Review this feature branch against the approved importer specification."

**Overlap:** Personal review-change, Matt code-review and Ponytail review.

**Requirements:** Git diff range; code-reviewer.md; a supported authorized reviewer agent.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/requesting-code-review/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### receiving-code-review

**Benefit:** Avoid blindly accepting an incorrect or incompatible suggestion.

**Example:** "Check whether a suggested API change breaks current callers before applying it."

**Overlap:** Complements all reviewers instead of replacing them.

**Requirements:** Feedback, code and relevant tests; posting replies only when authorized.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/receiving-code-review/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### finishing-a-development-branch

**Benefit:** Make the delivery decision and workspace ownership explicit.

**Example:** "Verify a feature branch and keep it for later, or prepare a requested PR."

**Overlap:** Matt pr covers descriptions; this skill covers integration and worktree lifecycle.

**Requirements:** Git; passing project checks; forge access for a requested push/PR.

**Boundaries:** presenting merge/PR/keep options is not permission to push, merge or discard work; use the user-selected option and actual authorization.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/finishing-a-development-branch/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

### Superpowers / Coordination and tooling

| Name | Purpose | Use when | Requirements | Origin / notes | Status |
| --- | --- | --- | --- | --- | --- |
| [using-git-worktrees](skills/obra/using-git-worktrees/SKILL.md) | Detect isolation and create or reuse an appropriate worktree | Feature work or a plan needs an isolated checkout | Git or native worktree tools; project setup and baseline tests; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [dispatching-parallel-agents](skills/obra/dispatching-parallel-agents/SKILL.md) | Split independent problems into isolated agent assignments | You select parallel investigation or implementation of independent tasks | Multi-agent tools; disjoint write scopes; integration verification; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [using-superpowers](skills/obra/using-superpowers/SKILL.md) | Navigate the selected Superpowers workflow and its needed dependencies | You explicitly ask how to use Superpowers or select its routing skill | Direct file access; only relevant platform reference loaded; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |
| [writing-skills](skills/obra/writing-skills/SKILL.md) | Create and improve reusable skill instructions using behavioral scenarios | You select creation or testing of a reusable skill | Bundled authoring references; behavioral tests require agent support; optional Node.js and Graphviz; explicit-only | Jesse Vincent / obra; MIT; 7.0.0 | enabled |

#### using-git-worktrees

**Benefit:** Keep unrelated work isolated and avoid nesting harness-managed worktrees.

**Example:** "Check existing isolation before setting up a feature worktree."

**Overlap:** Supports both Superpowers execution methods and Matt worktree-based implementation.

**Requirements:** Git or native worktree tools; project setup and baseline tests.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/using-git-worktrees/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### dispatching-parallel-agents

**Benefit:** Investigate unrelated failures concurrently without sharing unnecessary context.

**Example:** "Investigate three independent subsystem failures with separate assignments."

**Overlap:** Matt research/implement-spec also delegate; this is a general dispatch pattern.

**Requirements:** Multi-agent tools; disjoint write scopes; integration verification.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/dispatching-parallel-agents/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### using-superpowers

**Benefit:** Explain the collection without making it a mandatory global startup process.

**Example:** "Explain which Superpowers execution method fits this agreed plan."

**Overlap:** Matt ask-matt and your small workflow router; adapted to explicit selection.

**Requirements:** Direct file access; only relevant platform reference loaded.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/using-superpowers/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

#### writing-skills

**Benefit:** Check whether instructions change agent behavior rather than only looking well written.

**Example:** "Create a reusable importer review skill and compare behavior with and without it."

**Overlap:** toolkit-maintain and Matt writing-for-agents; adds pressure testing.

**Requirements:** Bundled authoring references; behavioral tests require agent support; optional Node.js and Graphviz.

**Cost/scope:** multiple fresh agent contexts can increase cost. Select this when independent checks or transcript dimensions justify it; installed does not mean behavioral tests have been run.

**Source:** [Pinned upstream](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-skills/SKILL.md). All per-skill resources retained; local adaptations recorded in the inventory.

### Choosing among installed collections

Use one principal design/planning/review method per task rather than stacking
equivalent methods. Superpowers is strongest when you want an explicit design →
plan → test-first execution → review → delivery process with progress ledgers.
Matt's collection offers domain/specification and architecture workflows;
Ponytail adds simplification, readable quality reports and shortcut tracking.
Personal diagnosis/review skills remain available for smaller focused jobs.
No combined workflow is created here; choose its exact skills when you build one.
