# Feature-and-architect workflow

Purpose: create, update, or review a living feature implementation and architecture
guide that lets the owner understand, debug, maintain, and extend the software
independently. Explain what the current code actually does, connecting every scoped
feature/use case to its files, functions, important code blocks, data, and tests.
Use the plan to locate scope and compare intention; source code establishes the
implementation account, including incomplete, unexpected or faulty behavior.

This is an explicitly selected, self-contained documentation workflow with no
skill dependencies. It is not automatically added to planning or execution.
Read [shared development handoff](references/development-handoff.md) for source
ownership, evidence, and composition boundaries. Creating this workflow does not
activate it.

## Inputs and boundaries

Use the target project, feature/plan identity, create/update/review operation,
requirements, plan, progress/QA records, existing explanations, and relevant source
code/tests. Infer known context; ask only about consequential gaps. Existing code
and a named scope are sufficient to reconstruct a guide when no plan exists;
identify that limitation instead of inventing requirements or acceptance.

- Standalone create/update writes explanatory Markdown only inside the output
  directory below. Read requirements, plans, progress/QA, source, configuration,
  and tests without changing them. Do not fix defects, implement features, change
  agent instructions, install tools, run project code/tests/builds, or publish.
  Use available verification evidence and disclose what has not been exercised.
- Review-only produces findings and proposed corrections in chat without writing
  files or running project code. An explicitly requested combination retains the
  active planning/execution stage's permissions; this workflow adds no execution
  permissions itself and cannot bypass ask-answer's read-only boundary.
- The guide explains the software; it does not become a new source of requirements,
  architecture approval, implementation status, or QA acceptance. Link governing
  documents and report disagreements. Do not rewrite them to make the story agree.
  If code differs from a requirement, explain the actual path and the unmet criterion
  separately. Code is evidence of implementation, not authority to change the goal.
  Derive function/flow claims from inspected code; cite tests and QA for observed
  runtime results. Do not claim a branch ran merely because source contains it.
- Scope includes all use cases assigned by the selected plan, affected existing
  behavior, and connected producers/consumers needed to understand them. Do not
  silently reduce a large plan to one example. Work in manageable slices, track
  remaining coverage, and label partial results explicitly. Substantial expansion
  beyond that scope requires agreement; unrelated repository audits stay outside it.

## Organized outputs

Use target-project-relative paths beside the existing feature plan:

```text
patompong-docs/implement-plan/<feature>/
  plan.md
  progress.md
  qa.md
  feature-and-architect/
    index.md
    architecture.md
    use-cases/<use-case>.md
    modules/<module>.md
```

Reuse the stable plan/feature slug. Several features in one plan may share this
directory with distinct use-case/module pages. Create only needed pages; a small
guide may keep its architecture and tables in the index. Do not create missing
plan/progress/QA files merely to fill the layout. Keep project artifacts outside
the portable toolkit. Link authoritative guides elsewhere instead of copying them.

The index is the entry point and reading order. Include source paths, reviewed
revision when available, relevant uncommitted scope and review date; a commit alone
does not identify a dirty working tree. Record coverage and stale/unreviewed areas
per page or section so an index refresh does not imply every page was refreshed.
Give the owner navigation in both directions: "I want to understand/change this
behavior" -> use case -> file/symbol, and "what is this function for?" -> module
explanation -> callers/use cases. Include a short suggested reading path from a
real entry point through the main flow to its relevant tests.

## Content and depth

Use plain English with the project's exact domain terms and code symbols. Explain
technical concepts where the reader first needs them. Organize from user behavior
to architecture to implementation detail, with cross-links in both directions.

1. **Feature and traceability map.** For every in-scope use case, identify the goal,
   requirement/task references, documented implementation state, entry points,
   participating files/symbols, tests/evidence, explanation links, and open gaps.
   Describe observed state without overriding the progress/QA owners' status.
   Mark planned-but-absent behavior as not implemented, and partially implemented
   behavior with its exact missing steps. Do not manufacture function details for it.
2. **Architecture and file map.** Explain component responsibilities, boundaries,
   dependencies, data ownership/lifetime, interfaces, and connections to existing
   features as they exist in code, even when they differ from the planned design.
   Identify files created, modified, and reused only when supported by
   a relevant diff/history; otherwise label provenance unknown. Explain what each
   file contributes and why it is involved. Use compact diagrams when they clarify
   actual relationships; a diagram must agree with the detailed flow.
3. **Step-by-step use cases.** Start with actor/trigger, prerequisites and concrete
   input. Follow each meaningful step through exact functions/files, validation,
   transformations, state/storage changes, external calls and returned/displayed
   results. Include an example data/state trace. Explain relevant alternate/error,
   cancellation, retry, timeout, recovery and cleanup paths. For asynchronous work,
   distinguish enqueue from processing, concurrent work, and completion signals;
   do not present a conceptual diagram as a guaranteed call order.
4. **Complete relevant function index.** Inventory functions, methods, handlers and
   callbacks that implement or materially support the scoped flows, including
   relevant reused code. Map each to its file, responsibility, use cases and detail
   page. Give trivial forwarding/accessor helpers short entries. Identify dynamic
   dispatch or external/generated/library boundaries and unresolved targets; do not
   enumerate dependency internals or claim an unknown call graph is complete.
5. **Deep function and block explanations.** For behavior-bearing symbols, explain
   purpose, signature and meaningful input/output examples, actual callers/callees,
   preconditions, branches/algorithm, data transformations, side effects, mutations,
   resource ownership, errors and invariants. Cover security, transaction,
   concurrency and performance constraints where relevant. Link exact source paths
   and symbols with current line locations when useful. Explain important blocks
   with focused source excerpts and numbered commentary; label pseudocode and
   proposed code explicitly. Do not paste entire files or create a second codebase.
6. **Maintenance and extension guidance.** Explain where a concrete behavior change
   would start, connected files/callers/contracts affected, invariants to preserve,
   and relevant tests/commands. Mark unexecuted commands as proposed and state known
   prerequisites. Separate extension options from agreed work. Explain design
   rationale only when supported by decisions/history; label inferences or unknowns.

Each meaningful function explanation has one home, linked from all relevant flows.
Depth follows behavior and risk, not line count. Index all relevant symbols even
when their explanation is brief; do not substitute a file list for the walkthrough.

## Working sequence

1. **Establish identity and coverage.** Read project guidance, the selected plan
   and its linked requirements/contracts, existing guide and progress/QA. Determine
   intended scope, available implementation and the revision being explained. Build
   the use-case/file/symbol coverage map before deep writing. Use the plan and diff
   as discovery aids, not proof that every task was implemented or every new file
   was planned. Include relevant implementation deviations without legitimizing them.
2. **Trace the actual implementation.** Read source, callers, dependencies, tests
   and configuration along each scoped path. Check registrations, routes, jobs and
   event handlers as needed. Reconcile claimed behavior with code. Distinguish
   planned, observed in code, runtime-verified, inferred and unknown behavior.
   Link existing test evidence to the state it actually verified; static inspection
   cannot prove runtime success. Surface missing paths and contradictions.
3. **Write connected explanations.** Populate the index, architecture, use cases
   and module details at the depth above. Include meaningful input/output examples
   and code-block explanations grounded in inspected source. Cross-link task and
   requirement IDs where available. Keep proposed interfaces visibly separate from
   existing ones. Omit irrelevant template sections instead of inventing content.
4. **Maintain incrementally.** On later requests, compare the recorded sources with
   current code and the relevant diff. Refresh changed symbol explanations and all
   affected flow steps, file/function indexes, diagrams, examples and extension
   guidance. Check deletions/renames and fix obsolete references. Preserve the
   owner's notes and edits; flag contradictory notes for resolution. Replace stale
   technical descriptions rather than appending conflicting accounts. Link shared
   modules across feature guides and flag other affected guides without editing
   them outside the assigned scope. If history is unavailable, re-inspect the
   affected code rather than assuming an old guide is current.
5. **Check and hand off.** Reconcile every scoped use case with the coverage map,
   every relevant symbol with its explanation, and each walkthrough with actual
   calls, state changes and outcomes. Check links, identifiers, source locations,
   excerpts and diagrams. Report documented coverage, unresolved conflicts, stale
   sections, runtime evidence limits and the next useful reading path. Do not call
   incomplete coverage complete or mark the implementation accepted.

## Explicit combinations with planning and execution

- With `writing-development-plan`, document the current code and use the plan only
  as context for scope and identified gaps. Keep future architecture/interfaces in
  the plan and link them as proposals; do not populate the implementation guide
  with imaginary function walkthroughs. If no code exists, produce only an initial
  scope/source index that clearly says implementation is absent. The deep guide
  grows when code exists. Only the assigned planning operation may edit the plan.
- With `execute-development`, update this explanatory directory after meaningful
  completed slices and reconcile it with final code before the combined assignment
  is complete. This explicitly assigns maintenance of the guide directory;
  execution's bounded factual documentation/status updates remain permitted.
  Neither permission changes governing requirements, accepted decisions or scope,
  protected tests/contracts or agent instructions. Progress and QA remain the
  primary change/evidence records; link them rather than duplicating their logs here.
- A later switch to another workflow or normal mode ends this combination unless
  the user explicitly retains it. Existing guide files do not implicitly select
  this workflow or impose guide updates on ordinary implementation sessions.

## Deliverables and completion

Create/update delivers a navigable, source-grounded guide in the feature directory
with all agreed use cases mapped, relevant functions indexed, meaningful behavior
explained deeply, maintenance guidance, and explicit evidence/coverage limits.
Preparation is complete when those documents exist and their consistency has been
checked against the inspected source. Missing implementation is a gap, not fabricated
detail. When no implementation exists, report only an initial index prepared and
the deep explanation pending; do not claim a complete implementation guide.
Review-only delivers chat findings. No new skill, tracker, teaching workspace, or
service account is required.

## Example invocations

"Use workflow feature-and-architect to document the implemented batch-import plan.
Explain every use case, index its functions, and trace meaningful functions and
code blocks deeply. Save a linked guide beside the plan; do not change code."

"Combine writing-development-plan with feature-and-architect for export. Write
the plan and document the existing implementation. Link future proposals from the
plan; mark absent code instead of inventing function walkthroughs."

"Combine execute-development with feature-and-architect for the accepted import
plan. Implement it and maintain its explanatory guide after meaningful slices.
Preserve governing requirements and agent instructions; limit plan updates to
verified status and factual references."

"Use workflow feature-and-architect to update the cancellation explanation after
my code changes. Preserve my notes, refresh affected flows and function references,
and report gaps without fixing production code."
