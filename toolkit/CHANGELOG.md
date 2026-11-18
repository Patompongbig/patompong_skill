# Toolkit changes

- 2026-11-18: Review fixes. Task packets scope QA to the task's file list, so the
  orchestrator option no longer mixes parallel tasks in one diff. Verdict rules made
  consistent (MAJOR fails unless marked deferrable; deferred MAJORs reported at the
  feature gate). Removed plan checkboxes: state.json is the only task-status record.
  Workflow headers drop the glossary and say to read references only when needed.

- 2026-11-18: Added test economy to the engineering rubric (one test per rule,
  table-driven cases, deletion when behaviour is removed or covered, migration chain
  testing and squashing). Task packets list removed tests with coverage; qa-verify
  treats unexplained coverage loss as MAJOR. Documented refactor plans and the
  small/large refactor path.

- 2026-11-18: Clarified test ownership: contract-and-test writes the outside-in suite
  (schema, contract, integration, end-to-end); execute writes unit tests test-first
  against the plan's internal design. Renamed execute's final check to "feature gate"
  and added qa-verify release mode for phase-level verification across features
  (REQ coverage, combined suites, shared-contract consumers), recorded as one exit
  line in the roadmap. Added guided/chain autonomy: user owns what and done, agents
  own how; under chain a passing design review accepts the plan. Parked security/ops
  and pilot-run items in toolkit/BACKLOG.md.

- 2026-11-18: Slimmed the portable folder. `.agents/` now holds only README.md (single
  entry point and activation block), CATALOG.md, COMPATIBILITY.md, workflows/ and
  skills/. Moved CHANGELOG, VALIDATION, IMPORTS.json, PREFERENCES, the workflow
  template and both scripts to a new repo-root `toolkit/` folder that is never copied.
  Merged and removed WORKFLOW-GUIDE, WORKFLOW-USAGE and STARTUP (content now in
  README.md and workflows/INDEX.md). The activation block is defined once in
  README.md and tells agents not to read `.agents/` unless a workflow or skill is
  selected. Validator and activator updated for the new layout.

- 2026-11-18: Restructured the development workflows around a system SRS, per-feature
  dossiers and an independent build–verify loop. Added shared references (glossary,
  document model, agent roles, engineering standards) and rewrote the development
  handoff so workflows link rules instead of restating them. Renamed
  software-requirement-creation → software-requirement (+ decompose and standards
  modes), test-and-contract-creation → contract-and-test (+ alignment preflight,
  shared-contract registry, change-request mode), writing-development-plan →
  development-plan, feature-and-architect → feature-explain (on-demand snapshot).
  Split execute-development into execute (implementer) and qa-verify (fresh-context
  verifier, verdict with at most five BLOCKER/MAJOR findings, three-round cap).
  Added doc-reconcile (audit, migrate, amend, compact) to reduce documentation
  overhead: one owning file per fact, edit in place, `log.md` + `state.json`
  replace progress/QA/verification files, compatible-by-default contracts with
  expand → migrate → contract for breaking changes. Per-run model selection by
  role with host mapping (Claude, ChatGPT, Gemini). Execution never commits;
  QA-passed tasks are staged as checkpoints. Rewrote the workflow template to one
  fixed structure. Removed the old workflow files without aliases. Made toolkit
  docs host-neutral ("normal agent behavior"). No imported skill files changed.

- 2026-10-31: Allowed bounded factual execution-documentation updates and verified
  plan checkboxes, retaining progress/QA as the primary records. Governing criteria
  and accepted decisions cannot be weakened to fit code; tests/contracts and agent
  instructions remain protected. Feature-and-architect now prioritizes actual code,
  explicit implementation gaps and two-way human navigation; planning proposals
  stay in the plan. Synchronized handoff, planning, guide, README and usage guidance.

- 2026-10-31: Added the explicit-only feature-and-architect workflow for living,
  source-grounded implementation guides beside feature plans. Covers all scoped
  use cases, relevant function indexes, deep behavior/code-block explanations,
  architecture and extension guidance; preserves proposed/observed/verified states.
  Added narrow opt-in planning/execution integration for its explanatory directory
  while protecting governing inputs and keeping execution reports in progress/QA.
  Updated menu, guide, catalog navigation, README and usage. No skills or imported
  resources changed; creating the workflow does not select it.

- 2026-10-31: Tightened execute-development to minimal necessary implementation
  edits, with requirements, design/context documents, the accepted plan and agent
  instructions protected from incidental changes. Progress and QA records own
  task status, deviations and change reports; plan checkboxes stay unchanged.
  Added preflight/final scope checks and synchronized shared handoff/usage/README.
  Clarified retired default.md routing and stale active-guidance wording; historical
  setup scripts/snapshots remain historical. No skills added or imported files edited.

- 2026-10-25: Made normal Codex behavior the default with no toolkit preprompt,
  startup selection question or automatic local skill use. Replaced the former
  default workflow with an optional WORKFLOW-GUIDE.md; synchronized root activation,
  preferences, startup template, menu, catalog introduction, usage and compatibility
  docs. Explicit selections persist until changed; returning to normal clears them.
  Updated the validator and Superpowers router, preserving its upstream hash and
  refreshing the installed hash. Historical setup snapshots remain historical.

- 2026-10-13: Reviewed and reconciled the custom development workflow chain. Added
  shared artifact ownership/status/handoff rules and real-use prompts; resolved
  draft-plan/new-interface Red-stage ordering, protected-input acceptance, review-only
  and interview-composition boundaries, and dependent-artifact reconciliation.
  Removed three menu entries for absent historical examples. Validator now checks
  actual menu coverage/targets instead of requiring obsolete example filenames.
  Imported skill contents and hashes remain unchanged.

- 2026-10-13: Added Ponytail full as execute-development's implementation modifier.
  Reuse and minimal complete changes remain constrained by accepted scope/design,
  protected contracts/tests and QA gates; mode does not leak into other workflows.
  Updated usage docs. No Ponytail reviewer or imported-skill edits added.

- 2026-10-13: Added execute-development with six selected execution/TDD/debugging/
  verification/review skills loaded by phase, protected approved tests/contracts,
  iterative in-scope QA fixes, independent risk/final reviews and explicit blockers.
  Organized progress/QA records beside the feature plan; no automatic delivery or
  workspace deletion. Updated menu and usage docs. Ponytail remains unselected.

- 2026-10-13: Added test-and-contract-creation with Red-only default, organized
  contract/test/evidence outputs, verification-before-completion, and conditional
  TDD only for explicitly requested minimal production code. Added codebase-design
  to writing-development-plan with accepted-contract/test alignment, scoped design
  proposals and no automatic edits, test deletion or alternative-design delegation.
  Updated menu and usage docs; no imported skills changed and no model requirement.

- 2026-10-13: Added writing-development-plan using obra/writing-plans with
  user-selected patompong-docs/implement-plan/<feature>/plan.md output, suitable
  test-first planning, no per-task commit mandate, and a neutral execution handoff.
  Added requirements traceability, focused scope, review/update modes and plan-only
  boundaries. Updated menu and usage docs; no imported skills changed or added.

- 2026-10-13: Confined software-requirement-creation outputs to the target project's
  patompong-docs/docs/ for requirements, system context, glossaries, ADRs and approved
  research. Existing documents elsewhere remain reference sources. Reserved
  patompong-docs/implement-plan/ for separately selected development planning.

- 2026-10-13: Added software-requirement-creation for focused requirements and
  related system-context creation, updates and review. Uses domain-modeling with
  documentation confirmation before writes; offers research by user choice.
  Broad scopes require a smaller session scope. No implementation planning or
  new skills added. Updated the workflow menu and usage documentation.

- 2026-10-13: Added the self-contained ask-answer workflow, adapted from Copilot
  Ask behavior for focused read-only investigation and chat-only answers. Added
  its menu entry and usage documentation. No skills added; skill count remains 62.
  Static checks found missing existing planning, build-review and review files;
  ask-answer behavior still needs a fresh-session check.

- 2026-10-13 / 0.4.0: Imported all 15 Superpowers 7.0.0 skills in skills/obra/,
  preserving per-skill resources and MIT licensing. Added explicit invocation,
  selection-first router and capability-based Codex adaptations; catalog benefit
  notes and overlaps. Recorded hash-protected Unix fallback/path-comment
  exceptions for four unchanged upstream scripts. Workflow menu unchanged.

- 2026-10-11 / 0.3.0: Installed all six Ponytail skills under skills/ponytail/
  at pinned version 5.1.0, with MIT attribution, explicit-only policy, portable
  invocation/help adaptations, and bundled benchmark evidence. Updated the
  catalog and provenance. Retained existing workflows; no startup hooks enabled.

- 2026-10-11 / 0.2.0: Installed all 38 Matt Pocock skills in author-grouped paths,
  preserving all 103 upstream resources and licensing. Applied explicit-only
  invocation and ordinary named skill-call adaptations. Added a detailed overall
  catalog, five editable workflow examples, composition template and instructions,
  once-per-session routing, compatibility notes, and pinned file inventory.
  Preserved three original personal skills. No upstream runtime/hook executed.

- 2026-10-08: Added Matt Pocock task-group navigation for 38 selection candidates.
  Refreshed the review source snapshot while preserving choice IDs and decisions.
  No third-party skills enabled; imports follow the user's selection.

- 2026-10-07 / 0.1.1: Recorded the user's English-language preference. Extended
  toolkit-maintain with a focused third-party evaluation rubric and invocation;
  reused the existing skill to avoid overlap. No third-party skills installed.

- 2026-10-07 / 0.1.0: Created portable preferences, default workflow, activation
  template and startup prompt, three focused original skills, catalog, and
  optional standard-library activation and validation helpers. Added a portable
  manifest-rename procedure for disabling skills. No upstream skills imported.
