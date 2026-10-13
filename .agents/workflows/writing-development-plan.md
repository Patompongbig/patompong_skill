# Writing-development-plan workflow

Purpose: create, update, or review an end-to-end feature development plan detailed
enough for a future developer or agent to follow, grounded in agreed requirements
and relevant current project evidence. Produce planning documents only.

Read [shared development handoff](references/development-handoff.md) for feature
identity, artifact ownership, acceptance, reconciliation and stage transitions.

## Inputs and scope

Use the target project, operation, agreed requirements, feature or end-to-end flow,
constraints, and relevant system context. Infer what the prompt already establishes;
ask about consequential gaps. Creating this workflow does not select or execute it.

- Inspect relevant project files and existing evidence without changing code,
  runtime configuration, other agents' instructions, or existing documentation
  outside `patompong-docs/`. Do not run tests, builds, project scripts, installers,
  or implementation commands during planning. Proposed commands belong in the plan.
- Review-only requests are read-only and produce findings in chat. Create/update requests
  authorize writing planning documents in the organized output directory below. Do not
  overwrite unrelated plans or mark planned implementation steps as completed.
- Do not create branches/worktrees, commit, push, publish tickets, or start
  implementation. Proposed future changes may target normal project source paths;
  that does not authorize those changes during this workflow.

## Organized outputs

All paths are relative to the target project root:

- Plan: `patompong-docs/implement-plan/<feature>/plan.md`.
- Preferred requirements reference: `patompong-docs/docs/requirements/<feature>.md`.
- Supporting system context: `patompong-docs/docs/system/<feature>.md`.
- Existing contracts: `patompong-docs/docs/contracts/<feature>/`.
- Existing test scenarios/evidence: `patompong-docs/tests/<feature>/`.

Use a descriptive stable feature slug and reuse its existing plan for updates.
Read relevant requirements, glossary, decisions, and project documentation wherever
already maintained; link to them without moving, modifying, or copying them wholesale.
Existing requirements elsewhere can be used when the user identifies them as the
agreed source. Do not create missing requirements or system files as a side effect;
that belongs to the separately selected requirements workflow. Keep substantial
supporting planning material beside `plan.md` only when it improves usability,
and link it from the main plan. Create no empty scaffolding or private project
artifacts in the portable toolkit.

## Selected skill and adaptations

Read [obra/writing-plans](../skills/obra/writing-plans/SKILL.md) when planning begins.
Use its precise tasks, file/interface mapping, checkable steps, and specification
self-review. Apply these user-selected adaptations to its defaults:

- Use the organized plan path above instead of `docs/superpowers/plans/`.
- Plan behavior-focused tests and suitable test-first steps, respecting existing
  test conventions. Do not impose TDD on every documentation/setup action or
  mandate a commit after every task. Preserve any supplied delivery preference.
- Replace the default header's mandatory execution-skill instruction with a neutral
  handoff: "Planning only. Read this plan and its linked requirements. Implementation
  requires a separately selected execution workflow and user authorization."
- Do not load `executing-plans`, `subagent-driven-development`, worktree, review, or
  other skills merely because the plan mentions future execution. Self-review the
  plan here; independent review or other skills require explicit selection.
- At completion, ask for review of the plan, not an automatic execution choice.
  Remain in planning mode across follow-ups until the user explicitly switches.
- Scale failure-mode coverage to the feature's risks rather than manufacturing a
  fixed number of review-focus items. Capture important uncovered cases and assign
  their checks to the task that owns the behavior.

Also read [codebase-design](../skills/mattpocock/codebase-design/SKILL.md) during
approach selection. Apply its small useful interfaces, focused responsibilities,
dependency strategies and testability guidance within the feature's scope:

- Accepted requirements and existing contracts define behavior; use design to
  choose implementation structure, not to redefine those agreements. Read the
  relevant contract/tests when present and preserve their IDs and expectations.
- Use project domain terms for product concepts and the skill's vocabulary for
  design discussion. Do not rename established project terms to impose its glossary.
- Keep all design proposals in the plan directory. Propose existing-code changes
  without applying them. Interface changes affecting accepted behavior need user
  agreement before dependent steps can become execution-ready.
- Read its DEEPENING reference only for relevant dependency/test-boundary questions.
  Do not automatically consolidate modules or delete existing tests. Replacement
  proposals must show preserved coverage and remain future implementation work.
- Alternative-design exploration and its multi-agent mode are not default. Use
  the relevant reference and delegate only when the user explicitly selects that
  exploration. Avoid introducing indirection solely to manufacture a second adapter.

## Steps

1. **Bound the feature and check requirements.** Read project guidance, the agreed
   requirements, and relevant document indexes. Identify goals, scope, exclusions,
   dependencies, acceptance criteria, and constraints. If the scope is too large
   or requires substantial unrelated context, offer smaller feature/flow slices
   and wait for the user's choice before broad reading. For missing or contradictory
   product decisions, state the gaps and offer `software-requirement-creation`;
   do not silently invoke it or decide the requirements yourself. Continue only
   independent planning while dependent decisions remain open. A blocked partial
   plan is labeled draft, not ready for execution. Missing executable tests do
   not prevent draft planning: propose exact interfaces, link contract/scenario
   decisions, then return to contract/test work before final execution acceptance.

2. **Map relevant current state.** Inspect the affected code, interfaces, tests,
   configuration, and connected feature flows. Identify exact existing paths and
   responsibilities, constraints, and applicable project commands. Distinguish
   inspected facts, existing runtime evidence, assumptions, and proposed new code.
   Plan new paths explicitly as proposed. Do not invent successful baseline results.
   Ask before a substantial scope expansion; defer unrelated improvements.

3. **Choose the end-to-end approach.** Describe how the feature passes through its
   actual layers and connects to existing behavior. Apply codebase-design to
   internal decomposition and testability. Consume accepted interface/data contracts
   and authored tests when available; propose missing details explicitly instead of
   silently changing agreed behavior. Set compatibility expectations and meaningful
   task dependencies. Resolve consequential implementation choices with the user; make routine choices using project patterns.
   Include schema/data evolution, setup, security, packaging, deployment, or rollback
   only when the feature needs them. Avoid speculative infrastructure and unrelated
   refactors. Split at meaningful independently verifiable deliverables, preferably
   complete vertical slices; explain any task needing later integration to be usable.

4. **Write the ordered plan.** Include a short header with goal, plan status,
   requirements/source links, approach, relevant stack, evidence coverage, global
   constraints, and the neutral execution handoff above. Then include:
   - A file/responsibility map distinguishing existing and proposed paths.
   - Stable task IDs, dependency edges, and an explicit execution order; identify
     independent tasks without dispatching agents.
   - Per task: delivered behavior, linked requirement/acceptance IDs or anchors,
     exact files, consumed/produced interfaces, and checkable steps.
   - Exact names, signatures, types, values, and decisions needed to avoid guessing.
     Use focused test assertions/examples and algorithm guidance where helpful;
     leave routine implementation bodies to the future implementer.
   - Existing approved tests mapped to tasks, not copied/recreated by plan steps.
     New tests may be proposed, clearly separated from already protected artifacts.
   - Verification commands with working directory, environment prerequisites,
     expected pass/failure meaning, and stop conditions. Clearly label commands as
     planned and unexecuted. If a command cannot be established from evidence,
     identify the prerequisite rather than inventing a runnable instruction.
   - Normal and relevant failure, cancellation, recovery, compatibility, and
     connected-feature regression checks tied to the tasks owning those behaviors.
   - Final integration and acceptance checks proving the complete user flow; include
     manual validation, deployment/migration and recovery steps where applicable.
   - A requirement-to-task/check mapping, risks, unresolved questions, and deferred
     work. Use unchecked implementation checkboxes for future progress tracking.

   No plan step may hide an unresolved choice behind "TBD" or "handle edge cases."
   Record real blockers separately. Do not prescribe branch operations, external
   writes, destructive migrations, or production deployment as automatically
   authorized; state their future authorization and recovery prerequisites.

5. **Self-review against the requirements.** Check every in-scope requirement has
   tasks and acceptance evidence. Check paths, interfaces, dependency order, shared
   names/types, command prerequisites, relevant edge cases, and connected flows.
   Verify that steps are unambiguous without reproducing the entire implementation.
   Correct plan defects; surface requirement/contract conflicts rather than changing
   requirements or weakening existing tests. Reuse relevant authored tests and link
   their evidence; a previous test report does not prove the future implementation.
   Check contracts/tests and final proposed signatures agree. If interface choices
   are awaiting contract review, keep dependent tasks in draft. Keep findings concrete
   and disclose inspection limits.

6. **Save and hand off for review.** For create/update, save the draft or revised
   plan inside its feature directory and check its local links and consistency.
   Link the result in chat, summarize important decisions and blockers, and ask
   whether it captures the user's intention. Record agreed revisions in the plan;
   label accepted only when the user confirms it. For review-only, report findings
   without saving. Do not start execution, even after plan acceptance, without an
   explicit switch and implementation assignment. Hand off the final requirements,
   contract/test paths, accepted versions, protected files, pending checks and
   required environments so execution can start without guessing.

## Deliverables and completion

A create/update assignment produces the organized plan, requirement traceability,
ordered verifiable tasks, and an explicit future handoff. A review assignment
produces findings and coverage in chat. Plan preparation is complete when it has
been written and self-reviewed with remaining issues disclosed; acceptance remains
pending until user confirmation. A plan is ready for execution only when accepted
and material dependent decisions are settled. Planned tests are not passing tests,
and a completed plan is not a completed feature.

## Example invocations

"Use workflow writing-development-plan. Plan batch import end to end from
patompong-docs/docs/requirements/batch-import.md, including cancellation, result
integration, recovery, and acceptance checks. Save the plan; do not implement."

"Use workflow writing-development-plan to update the existing export plan for
our revised requirements. Keep outputs under patompong-docs/implement-plan/export/."

"Use workflow writing-development-plan to review the import plan against its
requirements and relevant code. Report gaps only; do not edit."
