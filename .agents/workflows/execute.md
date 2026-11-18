# execute workflow

> Implement an accepted feature plan task by task, each task driven to Green and
> independently verified by a fresh-context QA agent before the next begins.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[engineering standards](references/engineering-standards.md)
Read a reference only when a step needs it.

## Purpose

Execution turns an accepted plan into production code that satisfies the
feature contract, passes its protected tests, and meets the project's
engineering standards. This workflow owns the **implementer** side of the
build–verify loop and drives it; the verifier side is
[qa-verify](qa-verify.md), dispatched as a separate agent so no task is
accepted on the implementer's own word.

Execution does not redefine scope, rewrite accepted contracts or tests, or
decide product policy. When the plan cannot be followed without guessing, it
stops and escalates rather than improvising.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **run** (default) | An accepted plan is ready to implement | Code in task scope, unit and regression tests, `log.md`, `state.json`, staging index | All tasks done and feature gate passed, or an escalation |
| **resume** | Continuing a previous run | Same as run | Same as run |
| **status** | "Where are we?" | Nothing | Chat report: task states, stale artifacts, open findings, next task |

**Orchestrator option** (opt-in, with run/resume): the main session dispatches
one implementer subagent per dependency-ready task with a disjoint file set,
integrates results, and runs the QA loop for each. Because several tasks share
the working tree, each task is reviewed, checked and staged by its own file
list (`git diff -- <files>`), never by the whole unstaged diff. Offer it when the plan has
roughly four or more such tasks; never select it implicitly.

## Inputs

| Input | Source | If missing or not accepted |
| --- | --- | --- |
| Plan | `features/<f>/plan.md` | Blocks the run |
| Feature contract | `features/<f>/contract.md` | Blocks dependent tasks |
| Protected tests | `features/<f>/tests/`, listed in `state.json` | Blocks dependent tasks; unaccepted tests are not protected and not a gate |
| Shared contracts | `docs/contracts/` referenced by the contract | Blocks tasks touching them |
| SRS references | `docs/requirements/` IDs in the contract's Basis | Context; conflicts escalate |
| Engineering standards | `docs/engineering.md`, then the toolkit rubric | Rubric alone applies |
| Run state | `features/<f>/state.json`, `log.md` | Created on first run |

A stale input cannot gate execution. Report it and ask whether to reconcile
first (doc-reconcile or the owning stage) or continue with independent tasks.

## Outputs

- **Production code** in the project's normal source paths, limited to files the
  task requires, including necessary callers and configuration.
- **Unit tests** for the internal behaviours each task introduces, written
  test-first, in the project's normal test location (the plan names it).
  Execute owns these: they follow the internal design and may be refactored
  with it, unlike the protected outside-in suite.
- **Regression tests** for defects found during the run, beside the unit tests
  or in `features/<f>/tests/` when they exercise a contract boundary. They
  supplement and never replace protected tests.
- **Records:** `log.md` entries and `state.json` task and criterion status
  (the only record of task status). Bounded factual corrections to the plan
  (moved paths, fixed check commands) are allowed with a log entry; task
  wording and acceptance criteria are not edited.
- **Staging index:** each QA-passed task's files are staged as a checkpoint.

Never written: requirements, contracts, accepted tests and fixtures, ADRs,
roadmap, `engineering.md`, agent instruction files.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Implementer | sonnet | Writes task scope | Main session by default; subagents in orchestrator mode |
| QA verifier | opus | Read-only, runs checks | Per-task verification via [qa-verify](qa-verify.md) |
| QA verifiers ×2 | opus | Read-only, runs checks | Feature gate: spec axis and standards axis in parallel |
| Researcher | sonnet | Read-only | Optional: tracing unfamiliar code before a task |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Skills

Load each when its phase needs it:

- [test-driven-development](../skills/obra/test-driven-development/SKILL.md) —
  observed Red before Green, small steps, refactor under Green.
- [systematic-debugging](../skills/obra/systematic-debugging/SKILL.md) — when a
  failure is not explained by the change just made.
- [receiving-code-review](../skills/obra/receiving-code-review/SKILL.md) — verify
  every QA finding before acting on it or disputing it.
- [verification-before-completion](../skills/obra/verification-before-completion/SKILL.md)
  — at every completion claim.
- [ponytail](../skills/ponytail/ponytail/SKILL.md), **full** mode — the
  "smallest complete change" discipline, applied within the engineering rubric.
- Orchestrator option only:
  [dispatching-parallel-agents](../skills/obra/dispatching-parallel-agents/SKILL.md)
  for disjoint task dispatch.

**Adaptations.** Records use `log.md` and `state.json`, not upstream ledgers or
`.superpowers/` paths. Never commit; upstream steps that commit or use SHAs use
the working-tree diff instead. Never delete existing code to satisfy a TDD reset
rule; if a protected test already passes, record it and implement only what
remains. Ponytail cannot reduce accepted scope, remove required validation,
redesign agreed interfaces or weaken tests; it does not persist after this
workflow ends. Upstream single-pass review limits are replaced by the loop in
agent roles.

## Procedure

1. **Preflight.** Confirm models. Read the plan, contract, protected tests,
   referenced shared contracts and engineering standards; confirm they are
   accepted, mutually consistent and not stale. Record the git baseline: `HEAD`
   revision and any pre-existing staged or unstaged changes. If pre-existing
   changes exist, ask how to treat them, because they would mix with task
   checkpoints. Run the baseline checks the plan names and classify each result:
   expected Red, already passing, unrelated failure, or blocked by environment.
   Identify required gates and environments; an unavailable required gate is
   reported now, not discovered at the end.
   *Exit:* inputs accepted, baseline recorded in `log.md`, gates known.

2. **Select the task.** Take the first dependency-ready task that is not done in
   `state.json`. On resume, reconcile state with the current code and log;
   never treat an old pass as current evidence after code or environment
   changed. Read the task's interfaces, linked criteria, tests and checks.
   *Exit:* one task in progress, with its criteria and file scope known.

3. **Implement to Green.** Work inside-out against the outside-in suite: for
   each unit-level behaviour the task introduces, write its unit test first
   and observe it fail; observe the relevant protected tests failing for the
   right reason. Make the smallest complete change that satisfies the criteria,
   following the plan's decomposition, the project's patterns and the
   engineering rubric. Register new files with `git add -N` so they appear in
   the task diff. Add a regression test for any defect found along the way.
   Diagnose unexpected failures systematically rather than stacking guesses.
   Run focused checks and the regressions the change could affect; refactor
   only within the task while staying Green.
   *Exit:* focused checks Green, protected tests untouched, task packet written.

4. **Verify.** Dispatch [qa-verify](qa-verify.md) in task mode with the task
   packet ([format](references/agent-roles.md#task-packet)). Act on the verdict
   using the [build–verify loop](references/agent-roles.md#buildverify-loop):
   verify each finding, fix confirmed ones, dispute unsupported ones with
   evidence, resubmit. Three `FAIL` rounds on one task escalate to the user.
   *Exit:* `PASS` or `PASS_WITH_NOTES`, or an escalation.

5. **Checkpoint and record.** Stage exactly the task's files. Append a `QA`
   entry to `log.md` (changed paths, checks and results, deviations, notes
   deferred), update `state.json`. Continue to the next
   task without asking for routine permission; give a one-line progress update.
   *Exit:* none of this task's files remain unstaged.

6. **Feature gate.** When all tasks are done: run the complete acceptance flow,
   the required regression suite and the project's build, type and lint checks.
   Confirm protected tests, contracts and governing documents are unchanged
   since the baseline. Dispatch the two parallel feature-gate verifiers over the
   whole feature diff (`git diff <baseline>`). Fix blocking findings through the
   same loop and re-run every check those fixes affect. Final evidence must
   describe the final code state.
   *Exit:* gate checks Green, both verdicts pass, criteria marked verified.

## Gates

- **Entry:** plan, contract and tests accepted and not stale; git baseline
  recorded; required environments available or explicitly flagged.
- **Task exit:** focused and affected checks Green on current code; QA verdict
  passes; files staged; records updated.
- **Feature exit:** every task done; every criterion verified at its required
  level; feature-gate verdicts pass; no unresolved BLOCKER; protected artifacts
  intact; every changed file traces to a task.

## Boundaries

- Requirements and acceptance criteria govern: change the code to meet them,
  never reinterpret them to match the code.
- Protected tests, fixtures, expected values and contracts are never modified,
  skipped, weakened or marked expected-failure. A genuine defect in one is a
  conflict for the user, not a fix.
- Routine implementation choices are autonomous and logged when consequential.
  A product-policy question, contract conflict or scope expansion escalates.
- **Stop rule.** After three unsuccessful approaches to the same defect, stop
  fixing; reassess root cause and design using systematic-debugging, record the
  evidence, and escalate if the answer changes architecture or scope.
- **Pause** dependent work for contradictions between governing artifacts, a
  stale input, a missing required environment, or an action outside
  authorization. State the blocker, the work completed, and the smallest
  decision that unblocks it. Continue independent tasks meanwhile.

## Done when

All accepted tasks are done; the feature gate has passed on the final code;
blocking findings are resolved; deferred MAJORs and notes are logged and listed
in the report; records
are current; and the staged diff contains the complete, verified feature. The
report states behaviour delivered, evidence (with test counts, skips and any
unavailable gates), deviations, and remaining limits. The user commits when
satisfied; execution never does.

## Example invocations

- "Use workflow execute for batch-import. Implement the accepted plan and loop
  through QA until the feature gate passes."
- "Use workflow execute, resume batch-import from where the last session stopped."
- "Use workflow execute for export with the orchestrator option; implementer
  sonnet, QA opus."
- "Use workflow execute, status for batch-import."
