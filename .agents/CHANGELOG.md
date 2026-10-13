# Toolkit changes

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
