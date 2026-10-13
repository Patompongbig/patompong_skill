# Shared development handoff

Read this when using requirements, contract/test, planning, or execution workflows.
It defines their common artifact ownership and transition rules, not a new workflow
or an instruction to load every stage's skills.

## Feature identity and sources

Use one stable feature slug across `patompong-docs/docs/requirements/<feature>.md`,
`patompong-docs/docs/contracts/<feature>/`, `patompong-docs/tests/<feature>/`, and
`patompong-docs/implement-plan/<feature>/`. Reuse existing equivalents and link them;
do not duplicate a project's authoritative documents merely to populate folders.
Confirm the target project root before writing; paths describe that project, not
the portable toolkit checkout. Create only artifacts needed for the assigned scope.

Put concise handoff metadata in the documents already being maintained:
- Feature/scope and status: draft, accepted, or superseded.
- Governing requirements, contract/test paths and relevant source revision or date.
- Acceptance evidence: the user's confirmation of this artifact/version, or pending.
- Important decisions, blockers, deferred work, and the next needed stage/action.

Stable requirement, contract, scenario and task IDs should link the same behavior.
Separate document acceptance from test results. A draft is not accepted; accepted
contracts can have Red or blocked tests. A previously verified feature can become
unverified after relevant code, tests, dependencies or environment change.
Do not create a separate status database or write chat-only review results to disk
unless the assignment authorizes a document update. Conversation confirmation is
valid; capture its substance in the next authorized artifact update, not fake quotes.

## Ownership and consistency

| Stage | Owns changes | Reads as input |
| --- | --- | --- |
| Requirements | Goals, scope, acceptance criteria, terminology, justified system context | Intention, current evidence, project guidance |
| Contract/test | Observable interface agreement, scenarios, schemas and executable tests | Accepted requirements, relevant design proposals and code |
| Development plan | Internal decomposition, task order, proposed source paths, check commands | Requirements, contracts, scenarios/tests, current code |
| Execution | Assigned production code, supplementary regressions, progress and QA evidence | Accepted requirements, contracts/tests and plan |

Project instructions and user-confirmed intent govern. Requirements state what must
happen; accepted contracts make connection behavior precise; tests exercise it;
plans explain how to build it. If these disagree, surface the exact conflict rather
than silently choosing the convenient document. Existing code describes current
state, not desired behavior. A test is not authority to contradict an agreed
requirement. Execution cannot rewrite accepted contracts/tests to reach Green.

Requirements may summarize boundary needs and link contracts, but detailed testable
protocol artifacts belong to contract/test work. Planning may propose missing
interfaces, but acceptance and contract/test alignment are required before dependent
execution. No stage edits another stage's protected artifacts solely to unblock
itself. Routine implementation detail may change with a recorded reason; a change
to accepted behavior or a consequential architectural agreement needs user decision.

After an accepted upstream change, identify affected contracts/tests/plans and mark
or report them as needing reconciliation. Update only artifacts inside the assigned
operation's ownership; list dependent artifacts that require a later selected stage.
Do not rewrite history, silently carry old acceptance to changed content, or mark
implementation complete using stale verification.

## Practical order without a circular dependency

Normally: requirements -> contract/scenario agreement and focused Red tests ->
final development plan -> execution with Green and QA.

For a new interface: requirements -> initial contract/scenarios -> draft plan that
proposes exact interfaces -> contract/test review and executable tests -> reconcile
and accept the final plan -> execution. Draft planning does not require preexisting
executable tests, and tests can be authored against proposed interfaces without
adding production stubs. Missing imports/interfaces are blocked evidence, not a
behavioral Red pass. Execution can implement accepted missing interfaces; an
unavailable required environment must still be restored before its final gate.

Use existing accepted artifacts to enter at a later stage. Do not force a project
to recreate documents or repeat approvals already supplied for unchanged content.
For small work, keep documents/tasks short; do not drop necessary contracts or
acceptance checks simply to shorten the process.

## Stage switching and combined workflows

Selecting or accepting one stage does not automatically select or authorize the
next. Explicitly requested multi-stage chains can advance through their named
stages, preserving each stage's confirmation and editing boundaries. Explain which
stage is active. A chain's later editing assignment does not permit early edits.

Interview is a clarification method that can be combined with one active stage.
It supplies questions and confirmation, not extra edit permissions. After confirmed
understanding, perform the already-authorized active stage. Ask-answer remains
chat-only/read-only: do not combine it with a writing stage to bypass its boundary;
ask for an explicit switch. Review-only inside any workflow permits inspection and
chat findings only; executing tests, saving a report, or applying fixes requires a
corresponding assignment. Offer the smallest useful change of scope when needed.

Workflow-specific adaptations govern included skills; imported dependencies cannot
expand the active operation, its output paths, protected artifacts, delegation scope,
or external actions. Load only the phase/dependency actually needed.

## Gate and handoff evidence

Provide links to the stage's outputs, their acceptance status, inspected coverage,
remaining decisions, next stage inputs, and executed versus proposed commands.
For tests record working directory, runner/discovery path, dependencies, fixture and
service requirements, isolation/cleanup, expected result and actual result when run.
Flag commands unavailable on the target host rather than inventing successful runs.

Different claims require different evidence: document consistency, behavioral Red,
unit/contract checks, actual integration, end-to-end acceptance, and independent QA
are distinct. Zero collected, skipped, expected-failure or environment-blocked checks
do not count as passing acceptance. Required external/hardware/manual gates stay
explicit and incomplete until observed or the user deliberately changes the criterion.
