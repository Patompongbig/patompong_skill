# development-plan workflow

> Turn one feature's accepted contract and tests into an ordered, verifiable
> implementation plan that an implementer can follow without guessing.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[engineering standards](references/engineering-standards.md)
Read a reference only when a step needs it.

## Purpose

The plan decides *how* to build what the contract specifies: the internal
structure, the files involved, the order of work, and the checks that prove
each step. It is the cheapest place to catch a wrong approach — a reviewed plan
prevents confidently building the wrong thing.

The plan consumes the contract and tests; it never redefines them. It does not
write code, run project commands, or start execution.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **review** | Check a plan against its contract and the code | Nothing | Findings in chat |
| **create** (default without a plan) | Plan a feature | `features/<f>/plan.md`, `log.md`, `state.json` | Accepted plan |
| **update** (default with a plan) | Contract changed, or plan is stale or wrong | Same, edited in place | Reconciled, re-accepted plan |

## Inputs

- Accepted feature contract and tests, with the protected list.
- Referenced shared contracts and SRS sections.
- `docs/engineering.md` and the toolkit rubric.
- Relevant current code, tests and configuration.

**Refactor plans** change structure, not behaviour: the existing accepted
contract stays as is, and its outside-in suite plus the feature gate prove
behaviour is preserved. Tasks name the unit tests to rewrite, merge or delete.

A contract that is still draft permits a **draft plan** only: proposed
interfaces are marked as proposals and handed back to contract-and-test for
acceptance before the plan can be accepted.

## Outputs

Owned: `features/<f>/plan.md`. Appends to `log.md`; maintains plan status in
`state.json`. Supporting material beside `plan.md` only when it materially aids
use, linked from the plan.

**Plan shape:**

```markdown
Status: draft · Updated: YYYY-MM-DD · Basis: contract.md, CT-ORDER, REQ-IMP-01..04
# FEAT-04 batch-import — plan
## Approach         how the feature passes through the system's layers, and why
## File map         path — responsibility — existing | proposed
## Tasks
### T-01 <title>    Delivers · Implements AC-.. · Depends on T-.. · Files
                    Interfaces consumed/produced (exact names, signatures, types)
                    Steps (checkable)  · Checks (command, cwd, expected result)
## Parallel sets    groups of dependency-ready tasks with disjoint files
## Coverage         AC → tasks → tests
## Feature gate       acceptance flow, regression suite, quality checks
## Risks · Open questions · Deferred
```

The plan header states: "Planning only. Implementation requires the execute
workflow and the user's authorisation."

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Planner | opus | Writes owned files | Main session: approach, decomposition, plan |
| Researcher | sonnet | Read-only | Maps affected code, callers, conventions and commands |
| Design reviewer | opus | Read-only | Fresh-context check: plan ↔ contract, tests and standards |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Skills

- [writing-plans](../skills/obra/writing-plans/SKILL.md) — precise tasks,
  file and interface mapping, checkable steps, self-review. *Adaptations:* plan
  path and header as above; test-first steps where they fit, without forcing TDD
  on documentation or setup steps; no commit steps; do not load execution,
  worktree or review skills because the plan mentions them.
- [codebase-design](../skills/mattpocock/codebase-design/SKILL.md) — deep
  modules, small interfaces, dependency strategy, testability. *Adaptations:*
  design chooses structure, never behaviour; keep project domain terms; read
  its DEEPENING reference only for dependency or test-boundary questions;
  alternative-design exploration and its multi-agent mode run only when the
  user selects them.

## Procedure

1. **Alignment preflight.** Run the
   [preflight](references/development-handoff.md#alignment-preflight) against
   the contract, shared contracts and SRS. If the contract is draft or stale,
   say so and limit the output to a draft plan. *Exit:* `aligned` or conflicts.

2. **Map current state.** Brief researchers on the affected areas: existing
   modules and responsibilities, callers, conventions, test layout and runnable
   commands. Distinguish inspected facts from assumptions. Do not invent
   baseline results. *Exit:* a factual map of what the feature touches.

3. **Choose the approach.** Describe how the feature passes through the real
   layers and connects to existing behaviour. Apply codebase-design and
   `engineering.md` to internal decomposition. Resolve consequential choices
   with the user; make routine ones by project convention. Include data
   evolution, configuration, security or rollback only where the feature needs
   them. No speculative infrastructure or unrelated refactors.
   *Exit:* agreed approach.

4. **Write the plan.** Decompose into tasks that each deliver verifiable
   behaviour, fit one fresh context, and preferably cut vertically through the
   layers. Give each task exact interfaces, linked ACs, files, checkable steps
   and checks with expected results; leave routine implementation bodies to the
   implementer. Map existing protected tests to tasks instead of recreating
   them. For each task, name the unit-level behaviours its internal design
   introduces, so execute writes their unit tests test-first; give their
   location by project convention. Identify parallel sets so execution can
   offer the orchestrator option. Label every command as planned. Record real
   blockers explicitly — no step may hide a decision behind "TBD" or "handle
   edge cases". *Exit:* complete draft plan.

5. **Design review.** Dispatch a fresh-context design reviewer: every AC is
   covered by a task and a check; interfaces match the contract exactly;
   dependency order is acyclic and correct; parallel sets really share no files;
   the approach respects the engineering standards; no task requires guessing.
   Address confirmed findings. *Exit:* verdict passes, or findings listed.

6. **Confirm and hand off.** Present the plan, key decisions, risks and open
   questions. On acceptance, set the status header and `state.json`. Under
   [chain autonomy](references/development-handoff.md#autonomy), a passing
   design review with no open questions accepts the plan and the chain
   continues to execute. Report the
   handoff for execute: contract and test paths, protected list, required
   environments, the feature-gate checks. *Exit:* accepted plan or labelled draft.

## Gates

- **Entry:** preflight run; the contract exists (accepted for a final plan).
- **Exit:** full AC coverage; interfaces consistent with the contract; every
  check has a command or a stated prerequisite; the design review has run.

## Boundaries

- No code, no project commands, no tests run. Proposed changes to existing code
  stay proposals.
- Interface changes that affect accepted behaviour go back to contract-and-test;
  the plan does not change them.
- Plans may propose branch, migration or deployment steps for the future; none
  are authorised by the plan itself.

## Done when

The plan is written, reviewed and either accepted or reported as a draft with
its blockers; execute can start from it without guessing. A plan is not a
passing test, and a finished plan is not a finished feature.

## Example invocations

- "Use workflow development-plan for FEAT-04 batch-import from its accepted
  contract."
- "Use workflow development-plan, update the export plan after CT-ORDER v3."
- "Use workflow development-plan to review the import plan against its contract.
  Findings only."
