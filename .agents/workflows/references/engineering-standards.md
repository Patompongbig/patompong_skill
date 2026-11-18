# Engineering standards

The shared rubric the implementer writes against and the QA verifier grades
against. It states principles, not a style guide.

## Precedence

1. The target project's own rules: `AGENTS.md`, linters, formatters, existing
   conventions in the code being changed.
2. `patompong-docs/docs/engineering.md`: project standards and the lessons
   distilled from reference codebases.
3. This rubric.

When a higher source is silent, use the lower. When the codebase consistently
does something this rubric discourages, follow the codebase inside existing
modules and raise the conflict instead of mixing styles.

## Rubric

Each area lists the principle and the question QA asks.

**Architecture and boundaries.** Respect the project's layers and dependency
direction. Domain logic does not depend on transport, storage or UI details.
New dependencies point inward, toward stable abstractions.
*QA: Does any new import cross a boundary the architecture forbids?*

**Module design.** Prefer deep modules: substantial behaviour behind a small,
stable interface. One clear responsibility per module. Split a module when it
mixes reasons to change, not when it reaches an arbitrary length.
*QA: Could a caller use this without knowing its internals?*

**Naming and readability.** Names state intent in the project's domain terms.
Functions do one thing at one level of abstraction. Control flow is shallow;
guard clauses over nested conditionals. Comments explain *why*, not *what*.
*QA: Would a new maintainer understand this without the conversation?*

**Interfaces and compatibility.** Public signatures, data shapes and error
contracts match the accepted contract exactly. Changes to shared interfaces are
compatible by default; breaking changes follow the
[shared contract protocol](document-model.md#shared-contracts-and-compatibility).
*QA: Does any existing caller break or silently change behaviour?*

**Errors and resilience.** Validate at boundaries; trust internal invariants.
Errors carry enough context to diagnose. No swallowed exceptions, no catch-all
recovery that hides defects. Cancellation, timeout, retry and cleanup paths are
handled where the contract requires them.
*QA: What happens on the failure paths the contract names?*

**State, concurrency and resources.** Ownership and lifetime of state are
explicit. Shared mutable state is avoided or guarded. Resources are released on
every path. Asynchronous work distinguishes enqueue, execution and completion.
*QA: Is there a leak, race or ordering assumption under concurrent use?*

**Performance and scalability.** Choose data structures and algorithms that fit
expected load from the requirements. Avoid N+1 access, unbounded growth and
blocking work on hot paths. Do not optimise without a stated need.
*QA: Does this degrade badly at ten times the expected input?*

**Security and privacy.** No secrets in code, logs or fixtures. Untrusted input
is validated and encoded for its sink. Least privilege for files, processes and
credentials.
*QA: Can untrusted input reach a sensitive sink unvalidated?*

**Testing.** Tests assert observable behaviour through public interfaces, derive
expected values independently of the code under test, and name the defect they
would catch. Doubles only at true boundaries. No sleeps where a condition can be
awaited.
*QA: Would this test fail if the behaviour regressed?*

**Simplicity.** Build the smallest complete change: reuse existing project code,
the standard library and installed dependencies before adding new machinery. No
speculative abstraction, unused parameters, dead code or premature
configurability. Simplicity never removes required validation, error handling
or accepted scope. (Ponytail *full* mode applies this principle during execution.)
*QA: Is there code here that the accepted task did not require?*

**Change hygiene.** The diff contains only what the task needs. No drive-by
reformatting, unrelated refactors or dependency changes. Generated files are
regenerated, not hand-edited.
*QA: Does every changed line trace to the task?*

## Reference codebases

Users may name open-source projects whose engineering approach this project
should learn from (for example, "take guidance from Ollama and codex-cli").
These are **sources of principles, not code to copy.**

The software-requirement workflow's *standards* mode handles this:

1. A researcher subagent studies the named codebase from a local path or public
   source, focused on the aspects the user cares about.
2. It condenses observations into principles and short illustrative patterns,
   each tied to the reference location that shows it.
3. The user approves; the result is written to `docs/engineering.md`.

Copy no code verbatim and respect the reference's license. Adapt each lesson to
this project's language, scale and constraints. Record what *not* to adopt when
the reference's context differs.

### `docs/engineering.md` shape

```markdown
Status: accepted · Updated: YYYY-MM-DD

# Engineering standards — <project>

## Stack and conventions
Language/runtime versions, formatter, linter, test runner, commands.

## Architecture
Layers, allowed dependency directions, module ownership.

## Project rules
Rules that override or extend the toolkit rubric, each checkable.

## Reference codebases
### <name> (<source>, studied YYYY-MM-DD)
Adopt:
- <principle> — e.g. "one package per domain capability; the CLI layer only parses
  and dispatches" (ref: <path>).
Avoid:
- <aspect that does not fit this project, and why>.
```

Implementer and QA read this file first, then this rubric.
