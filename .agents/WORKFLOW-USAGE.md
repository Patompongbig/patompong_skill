# Using the development workflows

Normal Codex use requires no workflow or preprompt. The sequence below applies
only when you explicitly select these custom workflows. Say "Return to normal
Codex" to clear a selection; see the [optional guide](WORKFLOW-GUIDE.md).

Keep one feature slug and the same target project
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
| Understand and extend the implementation | feature-and-architect | Living architecture, file/function map and detailed use-case guide |
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
- Execution makes only changes necessary for accepted requirements and the plan.
  Small, evidenced factual documentation/status updates and verified plan checkboxes
  are allowed in existing feature-related `patompong-docs/` documents. Requirements
  and acceptance criteria still govern the code; changing their meaning, protected
  tests/contracts or agent instructions needs separate explicit assignment.
  Progress and QA remain the primary task/change/evidence records.
- Ordered chain: explicitly name stages and which writing/implementation actions
  you authorize. The agent observes each review/confirmation gate; a chain does
  not grant early implementation, publishing or destructive actions.

## Project artifact layout

For a living explanation, explicitly select `feature-and-architect`. It can
reconstruct a guide for existing code without running it or changing other files.
Alternatively: `Combine execute-development with feature-and-architect for
batch-import. Implement the accepted plan and maintain its guide after meaningful
slices; preserve governing agreements.` With planning, the guide documents existing
code and links future proposals from the plan. Absent code is recorded as a gap,
not described as implemented. Neither planning nor execution loads it alone.
Use the guide's index as the reading entry point; progress/QA keep execution status
and evidence. The guide supports navigation from use case to function and back;
guide maintenance never authorizes changes to governing requirement or plan scope.

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
    feature-and-architect/       # only when explicitly selected
      index.md
      architecture.md
      use-cases/<use-case>.md
      modules/<module>.md
```

Only needed files are created. Production implementation remains in the project's
normal source directories. Existing authoritative documents elsewhere stay intact
and are linked as sources. Workflow output isolation is an instruction boundary,
not a replacement for host filesystem permissions or exclusive directory ownership.

## Before using it in a real project

Copy/merge the complete `.agents` toolkit and optionally add its entry point as described in
[README](README.md). Select the feature scope and inspect existing conventions.
Confirm test runner discovery/imports for `patompong-docs/tests/<feature>/` before
requiring execution; use explicit paths when supported. Identify services, hardware,
credentials and manual gates without putting secrets into these artifacts.

A prepared test is not behavioral Red evidence, and a Green unit test is not real
integration or end-to-end acceptance. Report actual checks and unresolved gates.
These instructions and packaging checks do not prove fresh-host agent behavior;
exercise a small disposable project before relying on a larger implementation.
