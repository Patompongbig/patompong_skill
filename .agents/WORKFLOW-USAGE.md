# Using the development workflows

Choose a workflow explicitly. Keep one feature slug and the same target project
through its stages. Existing accepted artifacts let you start later in the sequence.
[Shared handoff rules](workflows/references/development-handoff.md) define acceptance,
ownership and reconciliation; read them with an active development stage.

| Need | Workflow | Result |
| --- | --- | --- |
| Understand something | ask-answer | Read-only chat answer |
| Clarify an idea deeply | interview, alone or combined with a stage | Confirmed understanding |
| Define what should exist | software-requirement-creation | Requirements and system context |
| Define connection behavior and prove expectations | test-and-contract-creation | Contracts, scenarios and Red/passing/blocked tests |
| Decide how to build it | writing-development-plan | Ordered tasks and internal design |
| Build and verify it | execute-development | Green implementation, QA and evidence |
| Use one selected skill | lone-skill | That skill's assigned result |

## A normal feature

1. `Use workflow software-requirement-creation for batch-import. Create requirements
   from my intention and relevant current code. Keep project outputs in patompong-docs.`
2. Review/confirm the requirements. Then: `Switch to test-and-contract-creation for
   batch-import. Define contracts and author tests. Red-only; no production edits.`
3. Review/confirm contracts and tests. Then: `Switch to writing-development-plan for
   batch-import. Consume those requirements/contracts/tests and save the plan.`
4. Review/confirm the reconciled plan. Then: `Switch to execute-development. Implement
   the accepted batch-import plan, preserve approved tests, and loop through Green
   and QA. No push, merge or deploy.`

For a new interface that tests cannot yet call, first define contracts/scenarios,
create a draft development plan for exact interface choices, then return to contract/
test authoring and reconcile the final plan. This is a clarification iteration;
no production stubs or fake integration pass is required to leave the Red stage.

## Existing projects, updates, and review

- Existing accepted requirements/contracts/tests/plan: go directly to execution
  with their paths and acceptance context. Do not recreate them.
- Changed intention: update requirements first. Identify affected contract/tests
  and plan, reconcile each under its selected workflow, then execute the revised scope.
- Review only: `Use writing-development-plan to review this plan. Read-only findings
  in chat; do not edit or execute checks.` For runtime evidence, explicitly request
  the relevant checks; that still does not authorize automatic fixes.
- Deep clarification: `Combine interview with software-requirement-creation for
  export. Interview me, then maintain the confirmed requirements.`
- Small scoped behavior: use concise requirements/contracts/plan; do not create
  every possible document, schema or test level. Explicit minimal-code mode in
  test-and-contract-creation can perform a bounded TDD slice when requested.
- New session or interruption: provide feature, active stage and artifact paths.
  Execution reads progress/QA but validates them against current code and evidence.
- Ordered chain: explicitly name stages and which writing/implementation actions
  you authorize. The agent observes each review/confirmation gate; a chain does
  not grant early implementation, publishing or destructive actions.

## Project artifact layout

```text
patompong-docs/
  docs/
    requirements/<feature>.md
    system/<feature>.md
    contracts/<feature>/contract.md
    GLOSSARY.md
    adr/
    research/
  tests/<feature>/
    test-cases.md
    executable tests and fixtures
    verification.md
  implement-plan/<feature>/
    plan.md
    progress.md
    qa.md
```

Only needed files are created. Production implementation remains in the project's
normal source directories. Existing authoritative documents elsewhere stay intact
and are linked as sources. Workflow output isolation is an instruction boundary,
not a replacement for host filesystem permissions or exclusive directory ownership.

## Before using it in a real project

Copy/merge the complete `.agents` toolkit and activate its routing as described in
[README](README.md). Select the feature scope and inspect existing conventions.
Confirm test runner discovery/imports for `patompong-docs/tests/<feature>/` before
requiring execution; use explicit paths when supported. Identify services, hardware,
credentials and manual gates without putting secrets into these artifacts.

A prepared test is not behavioral Red evidence, and a Green unit test is not real
integration or end-to-end acceptance. Report actual checks and unresolved gates.
These instructions and packaging checks do not prove fresh-host agent behavior;
exercise a small disposable project before relying on a larger implementation.
