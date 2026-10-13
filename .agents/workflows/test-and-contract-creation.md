# Test-and-contract-creation workflow

Purpose: define agreements between connected systems and author behavior-focused
tests that guide implementation and verify the user's agreed intention. This is
the contract-definition and Red stage of test-driven development by default.

Read [shared development handoff](references/development-handoff.md) for feature
identity, artifact ownership, acceptance, reconciliation and stage transitions.

## Inputs, modes, and authorization

Use the target project, feature/connection/end-to-end flow, agreed requirements,
relevant system context, and existing contracts/tests. Read current code to locate
interfaces and understand constraints, not to derive desired behavior. Resolve
conflicts with the user; do not turn vague "enterprise behavior" into speculative
requirements. Make reliability, compatibility, security, and recovery expectations
explicit where relevant.

- Default: create/update contracts, schemas, test cases, executable tests, fixtures,
  and test helpers; run scoped checks and stop for user review. Do not edit production
  code or runtime configuration. Expected failures are valid outputs of this stage.
- Review-only: inspect and report in chat; no edits, saved reports or test execution
  unless separately requested. An execute-checks assignment does not authorize fixes.
- Minimal-code TDD: only when the user explicitly requests minimal production code,
  establish the exact behavior and allowed code paths, then use the conditional TDD
  skill below. An unbounded "make tests pass" request needs a bounded code scope.
  Do not treat approval of a contract or tests as production-code authorization.
- No automatic installs, shared test-configuration changes, branch/worktree creation,
  commits, deployment, or external writes. Ask before changes outside the organized
  outputs, except production files explicitly assigned in minimal-code mode.
- Inspect test commands and fixtures before execution. Use isolated local test data
  and temporary resources; do not exercise live user data or paid/external systems
  without explicit assignment. Clean up only test-owned resources. Tests may write
  runner caches/temp files; name relevant effects before running unfamiliar tooling.

## Organized outputs

Paths are relative to the target project root, outside the portable `.agents` folder:

- `patompong-docs/docs/contracts/<feature>/contract.md`: behavior and connections.
- Schemas/protocol descriptions beside that contract, in the format appropriate to
  the actual interface; do not impose HTTP tooling on files or in-process calls.
- `patompong-docs/tests/<feature>/test-cases.md`: scenarios and requirement mapping.
- Executable tests, fixtures, and test helpers inside the same test directory.
- `patompong-docs/tests/<feature>/verification.md`: concise observed results,
  commands/environment, coverage, failures, skips and blockers; no sensitive logs.

Create only useful artifacts. Reuse matching feature files on updates. Read existing
project documents and tests elsewhere without editing them. Check runner discovery
and imports for this location. Prefer explicit test paths supported by the existing
runner; ask before changing shared configuration or placing files elsewhere. A
schema here is a contract artifact, not automatically a production dependency.

## Skill entry points

- Read [verification-before-completion](../skills/obra/verification-before-completion/SKILL.md)
  when checking evidence and reporting results. Claims must match the actual checks;
  a finished Red-stage assignment does not mean the feature is passing. Inspect
  relevant existing suite coverage and report unrelated failures when observed;
  do not force unscoped, costly or unavailable execution merely to claim completion.
- In default Red-only mode, read the focused
  [writing-good-tests reference](../skills/obra/test-driven-development/writing-good-tests.md)
  for independent expectations, meaningful assertions and test doubles. Reading
  this reference does not invoke the full TDD skill or authorize production edits.
  Its Green/refactor completion rules do not apply to this intentionally Red-only stage.
- Only for explicitly requested minimal-code mode, read
  [test-driven-development](../skills/obra/test-driven-development/SKILL.md) and use
  small Red-Green-Refactor slices within the assigned code scope. Preserve existing
  work; never delete/rewrite production code to satisfy its upstream reset ritual.
  Tests of existing correct behavior can already pass; do not manufacture a failing
  expectation. Refactoring remains limited to the authorized implementation.
- Do not invoke codebase-design, interview, implementation or other skills by default.
  Interface choices affecting product behavior belong in the contract discussion;
  internal decomposition belongs to writing-development-plan.

## Sequence

1. **Scope and inspect.** Read agreed requirements and relevant connected producers,
   consumers, interfaces, existing tests, and project guidance. If the scope is too
   broad, propose smaller feature/connection/flow slices and wait for the user's
   choice before collecting unrelated context. Distinguish implemented facts,
   desired behavior, existing evidence, assumptions, and unsettled decisions.
   Resolve missing requirements rather than silently designing product policy. For
   new interfaces, read an existing draft plan if available; missing implementation
   does not prevent contract/scenario design. Offer draft planning if exact interface
   design is needed; do not implement production stubs to make Red authoring possible.

2. **Agree observable behavior.** Present normal and important failure scenarios
   with independently derived expected outcomes. Confirm consequential interface
   choices and test boundaries not already agreed. State what each proposed test
   boundary catches and misses. Do not force internal structures or incidental
   call ordering unless those are genuine contractual obligations.

3. **Define the contract.** Capture participating systems and responsibilities,
   transport/call/file interfaces, inputs/outputs, validation, state transitions,
   ownership, identifiers, ordering, errors, timeouts, retries/idempotency,
   cancellation, recovery, and version compatibility where relevant. Link to the
   governing requirements. Include meaningful valid/invalid examples and measurable
   invariants. Use schemas/types for structure and written rules for behavior;
   schema validation alone does not verify system interaction. Label proposed and
   accepted decisions; surface conflicts instead of changing requirements elsewhere.

4. **Map scenarios to checks.** Choose the smallest useful mix:
   - Schema/type checks for message validity.
   - Contract tests for consumer expectations and actual provider conformance.
   - Unit tests for important isolated rules.
   - Integration tests for real connected components and transport/state behavior.
   - End-to-end acceptance checks for the complete intended user outcome.

   Add relevant failure, cancellation, recovery, compatibility, and connected-feature
   regressions. Give scenarios stable IDs, linked requirements/contract clauses,
   setup, inputs, expected observable outcomes, test level, and evidence limits.
   Write the overall contract/scenario map first, then author runnable tests in
   manageable slices. Avoid speculative bulk unit tests and coverage quotas.

5. **Author executable tests.** Exercise agreed public interfaces; derive expected
   results from confirmed examples/requirements, not production helpers computing
   both sides. For each test, name the realistic defect it should detect. Prefer
   real components for integration checks. Use doubles only at appropriate boundaries;
   assert contractual arguments/order when required, not incidental implementation.
   A consumer test against a double is not provider verification: test the actual
   provider separately or label the gap. Never write a fake implementation that
   makes the system appear integrated. Keep helpers in test utilities.

6. **Run and classify evidence.** Execute available scoped checks and record:
   - Expected Red: the test reaches the behavior and detects its absence/violation.
   - Passing existing behavior: legitimate evidence; do not weaken or invert tests.
   - Blocked: missing interface/import/environment/fixture prevents meaningful execution.
   - Skipped/not run: no runtime proof, with reason.
   - Mocked versus actual integration: state what was really exercised.

   When useful, demonstrate important tests detect wrong behavior with controlled
   invalid inputs, negative fixtures, or an isolated fault/mutation experiment.
   Do not alter production files for such experiments in default mode. A mental
   mutation check is design reasoning, not observed failure evidence. Check test
   collection and report zero collected tests as no proof. Missing capabilities
   must not be hidden by skips, broad expected-failure markers, or permissive assertions.

7. **Stop for review, or perform the authorized minimal loop.** In default mode,
   hand the user the contract, scenarios, tests, observed Red/passing/blocked status,
   and implementation needs. Ask the user to confirm the contract/scenario/test
   artifact set and record its accepted versions/protected file list in the existing
   contract or test-case document when writing is assigned. Proposed tests remain
   draft until reviewed; accepted tests can be Red or blocked. Wait for review;
   acceptance does not start Green.
   In explicit minimal-code mode, confirm contracts before dependent implementation
   unless already accepted, load the TDD skill, and implement only the assigned
   behavior in small Red-Green slices. Run relevant regression/integration checks
   and report suite scope. Do not change the agreed contract to accommodate a bug.
   Stop when a failing test needs work outside the authorized scope.

8. **Hand off consistently.** Link artifacts and map requirements to contract clauses,
   tests, and observed results. Identify runner discovery, imports, fixtures and
   environment setup needed at execution, including blockers caused only by absent
   production interfaces. Supply reproducible commands/prerequisites and known
   gaps. The future development plan must consume these contracts and tests; proposed
   changes to accepted behavior require discussion and corresponding revisions, not
   silently weaker expectations. Do not automatically execute another workflow.

## Deliverables and completion

Default completion: contracts and focused tests are authored, inspected and checked
where possible, with results and blockers disclosed for user review. The feature
can remain Red. Review-only completion is the scoped findings report. Minimal-code
completion additionally requires fresh evidence for the specific implemented claims.
Distinguish "prepared", "contract accepted", "expected failure observed", and
"behavior verified". Never infer whole-system success from unit/schema/contract
checks alone; report the real integration and acceptance coverage.

## Example invocations

"Use workflow test-and-contract-creation for batch import cancellation. Define
contracts and author/run tests from the agreed requirements. Stop in Red-only
mode for my review; do not edit production code."

"Use workflow test-and-contract-creation. I approve minimal production code for
request validation in src/import/validator.py only. Use the accepted contract and
TDD for that behavior; report unrelated implementation gaps without fixing them."
