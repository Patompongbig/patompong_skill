# Execute-development workflow

Purpose: implement an accepted feature development plan, make its approved tests
pass, and fix verified in-scope defects through a continuous implementation,
verification and QA loop. Execution and QA are coordinated phases of one workflow.

Read [shared development handoff](references/development-handoff.md) for feature
identity, artifact ownership, acceptance, reconciliation and stage transitions.

## Inputs and authorization

For a review-only request, inspect and report without edits or test execution; use
this workflow's QA criteria without entering the fix loop. Running checks or applying
fixes requires a corresponding assignment.

Use an accepted plan, governing requirements, contracts, approved tests, relevant
project architecture/standards, and the user's implementation assignment. Identify
missing or conflicting inputs before dependent work; do not invent accepted scope.
Read source paths and dependencies needed for the feature, not the whole repository.
An overly broad assignment needs smaller agreed feature/flow slices.

- Change only production code, necessary callers, supplementary regression tests,
  and project setup/configuration needed to satisfy the accepted requirements and
  plan. Make the smallest complete change; avoid unrelated cleanup, refactoring,
  formatting, dependency updates, or documentation churn. Preserve other contributors'
  work. A file's presence in the project is not permission to edit it.
- Requirements and acceptance criteria govern the implementation: change the code
  to meet them, never weaken or reinterpret them to match delivered code. Preserve
  accepted behavior, scope, constraints and architectural decisions in requirements,
  design/context documents, glossaries, ADRs and the plan. Changing those agreements
  or their acceptance status requires a separate explicit assignment and agreement;
  pause dependent work until consequential revisions are reconciled.
- Allow small, directly relevant documentation updates: verified plan checkboxes,
  source links, factual implementation/status annotations, and corrections to stale
  file locations or runnable check commands when their meaning/gates stay unchanged.
  Existing explanatory system documentation may be updated to describe current code,
  clearly separating observations from accepted design. Preserve original criteria
  and decision history; report unmet criteria as gaps instead of rewriting them.
  No bulk rewrites, document moves, new specifications or unrelated edits. Preserve
  other authors' notes and existing output-location/ownership restrictions.
  Limit this maintenance to existing feature-related documents in `patompong-docs/`;
  edits elsewhere require explicit assignment. Do not move documents into this
  directory to bypass that boundary.
  The `feature-and-architect/` guide still requires its explicitly selected workflow;
  this maintenance permission does not activate it.
  Log each update and its reason in `progress.md`; put verification evidence and
  discrepancies in `qa.md`. These remain the primary execution records.
- Do not create, edit, delete, or rename `AGENTS.md`, `AGENTS.override.md`,
  `CLAUDE.md`, agent settings, skills, workflows, or other agent instruction files
  as an implementation side effect, even if a plan or included skill suggests it.
  Such changes require a separate explicit assignment. Reading applicable guidance
  remains required; runtime configuration is distinct from agent configuration.
- Approved tests, assertions, expected values, fixtures, scenarios and contracts are
  protected. Record their baseline identity/content and check their integrity at
  gates. Do not modify, delete, skip, weaken or mark them expected-failure to reach
  Green. Add necessary defect regression tests separately without altering them.
  Test artifacts/tooling conflicts require user agreement before protected changes.
  New regression expectations must derive from agreed behavior; record them in QA
  and preserve them through the fix loop. A failing new test may be corrected for
  an evidenced authoring defect, never weakened to match faulty production code.
- Use project standards and accepted architectural decisions, not a new speculative
  enterprise framework. Keep interfaces, caller behavior, validation, security,
  resource ownership, compatibility, and required error handling intact.
- Do not automatically commit, push, merge, deploy, delete worktrees, change other
  agents' settings, or perform destructive migrations. Follow explicit delivery
  instructions and actual tool permissions. Planned external/destructive operations
  still require their corresponding authorization before execution.
- Use safe local test resources. Inspect unfamiliar runners/setup commands for side
  effects. Live user data, paid services and shared environments need explicit scope.

## Organized execution records

Paths are relative to the target project root:

- Read `patompong-docs/implement-plan/<feature>/plan.md` and its linked sources.
- Keep task progress, decisions and resume context in that directory's `progress.md`.
- Keep QA findings, fixes, review scope and verification evidence in its `qa.md`.
- Use these two records as the primary change report: link task/requirement IDs,
  changed paths, reasons, deviations, and observed results. Apply only the bounded
  documentation maintenance allowed above. Plan checkboxes may mirror verified task
  completion; retain detailed status, partial work and blockers in `progress.md`.
  Other product documentation changes need explicit assignment unless covered by
  that bounded maintenance; report the changed sections and supporting evidence.
- Only when explicitly combined with
  [feature-and-architect](feature-and-architect.md), maintain this directory's
  `feature-and-architect/` explanatory guide after meaningful slices and reconcile
  it with final code before completing the combined assignment. This narrow
  explanatory assignment does not permit changes to agreed requirements/design,
  plan scope, protected contracts/tests or agent instructions. Execution alone
  does not load that workflow or require its guide.
- Store useful detailed command output under that directory only as needed, avoiding
  secrets and unnecessary logs. Preserve records for future sessions; no automatic
  deletion of the execution workspace or ledger.
- Production code remains in normal project source paths. New regression tests
  default to `patompong-docs/tests/<feature>/`; ask before another location or shared
  runner configuration changes unless already explicitly assigned.

## Skills and phased loading

Use these seven selected skills. Read each when its phase needs it; retain relevant
instructions across the loop rather than repeatedly loading unrelated collections.

1. [executing-plans](../skills/obra/executing-plans/SKILL.md): task execution and
   progress/resume discipline.
2. [test-driven-development](../skills/obra/test-driven-development/SKILL.md):
   observed Red-to-Green behavior, small changes and verified refactoring.
3. [systematic-debugging](../skills/obra/systematic-debugging/SKILL.md): diagnosis
   when failures or unexpected behavior require investigation.
4. [verification-before-completion](../skills/obra/verification-before-completion/SKILL.md):
   fresh relevant evidence at task and feature completion gates.
5. [requesting-code-review](../skills/obra/requesting-code-review/SKILL.md): independent
   read-only reviews at meaningful risk points and the final feature gate.
6. [receiving-code-review](../skills/obra/receiving-code-review/SKILL.md): verify QA
   findings before fixing them or recording reasoned disagreement.
7. [ponytail](../skills/ponytail/ponytail/SKILL.md), **full** mode: load before
   implementation and apply to implementation/refactoring/fixes throughout this
   workflow. Reuse house code, standard libraries and installed dependencies;
   choose the smallest readable change that completely satisfies the accepted task.

Apply these workflow adaptations to upstream defaults:

- Use the organized records above instead of `.superpowers/sdd/`; native bookkeeping
  is sufficient. Do not run Bash helpers unless inspected and suitable for the host.
- Respect existing workspace isolation. Create a new branch/worktree only when
  assigned or required and authorized by project instructions; otherwise explain
  any unresolved isolation requirement before implementation. Do not invoke extra
  worktree or branch-finishing skills automatically.
- Preserve existing code; never delete/rewrite it solely to satisfy a TDD reset rule.
  Start by running the existing approved tests. If valid tests already pass, record
  that and implement only remaining accepted needs; do not manufacture a failure.
  New regression tests should demonstrate the actual defect before its fix when
  feasible. Import/setup failure is a blocker, not a behavioral Red proof.
- Ordinary implementation decisions are autonomous and recorded when consequential.
  Product-policy changes, conflicting contracts or test expectations need the user;
  the execution skill's autonomous rulings cannot override them.
- Included skills, helper scripts, generated prompts and reviewers inherit the
  change boundaries above. Inspect bookkeeping helpers before use: only bounded
  status/documentation updates are permitted, never changes to governing criteria
  or protected tests/instructions.
- QA has fix-and-recheck cycles, not the execution skill's one-final-fix-pass limit.
  Re-review changed risky areas and unresolved findings when justified; do not repeat
  a whole review for every trivial fix or rerun unchanged checks without a reason.
- Do not inherit automatic model-selection rules from review examples. Use the
  current supported agent tools and session configuration.
- Existing tests remain protected despite any skill suggesting test deletion or
  replacement. Additional tests supplement them. Scope bounds fixes; findings
  outside scope are disclosed, not silently fixed or silently declared irrelevant.

- Ponytail full is a solution modifier, not permission to reduce accepted scope,
  redesign agreed interfaces, weaken protected tests, remove required validation,
  or bypass QA/architecture gates. Its shortcut guidance cannot justify failing
  acceptance criteria. Favor readability and complete behavior over line count.
  Preserve the project's required layers, ownership and lifecycle rules; report
  a consequential simplification proposal rather than silently overriding the plan.
  Its session-persistence rule is bounded by this selected workflow: switching
  workflows does not implicitly carry Ponytail into the next one. Do not load
  ponytail-review or another Ponytail skill automatically.

## Implementation and QA loop

1. **Preflight.** Read plan, requirements, contracts, approved tests and applicable
   standards. Confirm their agreement and dependencies. Record the starting revision,
   existing changes, protected governing-document/instruction/test/contract
   identities and relevant baseline checks. Identify allowed implementation paths
   from the accepted scope, including necessary callers and configuration; identify
   bounded factual documentation updates and any separately assigned edits.
   Distinguish expected feature failures from unrelated failures and environment
   blockers. Establish required acceptance, regression and quality gates from the
   plan/project. Do not call an unavailable gate passed or quietly drop it. An
   accepted Red-stage test blocked solely by a missing production interface can
   enter execution: add that interface within the plan, then collect and run the
   test. Unaccepted tests, conflicting behavior, and unavailable required environments
   remain explicit blockers. Validate accepted artifact versions against current
   contents before freezing their baseline.

2. **Resume or take the next task.** Reconcile the plan identity, ledger, current
   code and available evidence. Never treat a ledger line or old pass as sufficient
   current proof after code/environment changes. Resume at the first unfinished
   dependency-ready task; do not recreate completed work after compaction. Read
   its exact interfaces, constraints, test cases and completion criteria.

3. **Implement to Green.** Observe the relevant current test result, then make the
   smallest complete implementation satisfying the agreed behavior. Follow the
   accepted decomposition and house patterns; reuse existing code/platform features
   where appropriate. Do not remove accepted functionality to shorten the diff.
   Update required callers/configuration within scope. Diagnose failures using
   systematic-debugging instead of stacking speculative fixes. Run focused checks
   and relevant regressions after meaningful changes. Refactor only within scope
   while retaining Green and protected tests.

4. **Apply risk-based QA.** Review changed interfaces, connected callers, data flow,
   validation, security, error/cancellation/recovery behavior, concurrency/load,
   resource cleanup, compatibility and maintainability where relevant. At significant
   risk points and after final integration, dispatch a read-only reviewer via
   requesting-code-review if supported. Supply governing requirements, contracts,
   standards, task/plan, exact diff or working-tree file scope, known baseline issues,
   and evidence. Judge observed code and check results against agreed criteria;
   distinguish static findings, reproduced defects, unverified assumptions and
   remaining gaps. A progress entry or plan checkbox is not runtime evidence.
   Capture uncommitted changes too; do not commit just to make a diff.
   Reviewers report and do not implement or dispatch additional agents. If delegation
   is unavailable, perform a distinct self-review and clearly label that limitation.

5. **Verify findings and fix.** Use receiving-code-review to verify the concrete
   trigger, impact and compatibility of each finding. Classify blocking correctness,
   security, data-loss, contract or required-standard failures separately from
   optional improvements. Fix confirmed in-scope defects autonomously, adding
   separate regressions where needed. Re-run the failing check and affected
   regression/integration checks. Request focused re-review for consequential fixes
   or disputed unresolved risk. Repeat until the task gates and blocking findings
   are resolved; update progress and QA evidence as work proceeds.

   A reviewer cannot invent new product requirements or weaken approved tests.
   Explain unsupported findings with evidence. Out-of-scope blocking issues require
   a user decision and prevent a complete claim; optional recommendations can be
   explicitly deferred without pretending they are required gates.

6. **Complete the task and continue.** Record delivered behavior, changed paths,
   actual verification commands/results, QA dispositions and justified deviations.
   Mark complete in `progress.md` only when its required criteria hold; then update
   matching plan checkboxes without changing task wording or acceptance criteria.
   Check that edited paths are necessary for the accepted task, documentation edits
   are bounded and evidenced, governing agreements retain their meaning, and
   protected tests/instructions remain unchanged. Continue through all accepted tasks
   without routine permission prompts. Give concise progress updates.

7. **Final feature gate.** Exercise the complete acceptance flow, real integration
   boundaries, required regression suite, and project-defined build/type/lint or
   other quality checks. Use mock evidence only for the claims it supports. Perform
   the final independent feature review, verify protected tests/instructions and
   governing agreements against their baseline, review all permitted documentation
   diffs, and check that every changed file is within scope. Fix blocking findings and
   rerun checks affected by those fixes. Final evidence must correspond to the final
   code state. Report test counts, skips, collection failures,
   unavailable environments and baseline failures, not just a green command.

## Progress and stop conditions

Continue while meaningful in-scope investigation or fixes can advance the feature.
For the same defect after three unsuccessful approaches, stop the speculative fix
loop, reassess root cause and architecture, and record evidence. Continue independent
work; ask the user when the next step needs a behavior decision, changed contract,
scope expansion, authorization, or an external environment change. Follow the
selected debugging skill's architecture-discussion checkpoint before another
architectural fix. Do not turn uncertainty into endless retries or a false success.

Pause dependent work for contradictions, necessary changes to governing agreements,
protected instructions or tests, missing required environments, unauthorized actions,
or a broken plan whose remaining paths would be guesses. State the concrete blocker,
completed work and smallest decision or environment change needed. A blocker is
not feature completion.

## Completion and handoff

Complete only when all accepted tasks, required acceptance/quality gates and blocking
QA findings are satisfied, governing agreements retain their meaning, protected
instructions, contracts and tests remain intact, documentation updates are bounded
and evidence-backed, edits are limited to necessary authorized files, and fresh
evidence supports the final code. If another contributor changes a protected input,
report the drift and reconcile dependent work; do not revert their changes or assume
old acceptance still applies. Unrun/skipped required checks prevent an unconditional
complete claim. Record optional deferred findings and independent-review limits.

Deliver implemented code plus progress/QA records and a concise report of behavior,
verification, deviations and remaining limits. Stop at the authorized delivery state;
feature completion does not automatically merge, publish or deploy.

## Example invocation

"Use workflow execute-development for batch import. Execute the accepted
patompong-docs/implement-plan/batch-import/plan.md, preserve its approved contracts
and tests, and loop through Green verification and QA fixes until its required
gates pass. Keep progress and QA records; do not push, merge or deploy."
