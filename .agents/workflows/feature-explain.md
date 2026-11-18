# feature-explain workflow

> Explain how a feature is actually implemented — from user behaviour through
> architecture to individual functions — so the owner can understand, debug and
> extend it independently.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[glossary](references/glossary.md)

## Purpose

An on-demand explanation of real code, for the owner to read. It describes what
the code does, including incomplete, unexpected or faulty behaviour, using the
contract and plan only to locate scope and compare intent. It is a snapshot tied
to a code revision, not a continuously maintained document, and no other
workflow updates it.

The explanation is never a source of requirements, design approval or
completion status.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **explain** (default) | A question about how something works | Nothing | Explanation in chat |
| **snapshot** | A durable guide for a feature | `features/<f>/guide/` | Guide tied to a revision |
| **refresh** | The code changed since the last snapshot | `features/<f>/guide/`, edited in place | Guide updated to the current revision |

## Inputs

The feature scope (a dossier, or a named area of code), the relevant source and
tests, and where available the contract, plan and `log.md`. Existing code and a
named scope are enough; the absence of a contract is noted, not filled in.

## Outputs

Snapshot and refresh write only `features/<f>/guide/`:

```text
guide/
  index.md              entry point, reading order, revision, coverage
  architecture.md       components, boundaries, data ownership, file map
  use-cases/<name>.md   step-by-step walkthroughs
  modules/<name>.md     function index and deep explanations
```

A small feature may keep everything in `index.md`. The index records the
revision explained (`HEAD` plus a note of uncommitted changes) so a later reader
can see when it is out of date.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Explainer | sonnet | Writes `guide/` only | Main session: traces code and writes |
| Researcher | sonnet | Read-only | Traces large or unfamiliar areas in parallel |

Confirm models once at the start of a snapshot or refresh run per
[agent roles](references/agent-roles.md#model-selection); explain mode uses
defaults unless the user names models.

## Content standard

Plain language with the project's exact domain terms and symbols, organised from
behaviour to architecture to code, with links both ways: "I want to change this
behaviour" → use case → file and symbol, and "what is this function for?" →
module page → callers and use cases.

1. **Traceability map.** For each use case: goal, linked AC/T IDs, entry points,
   participating files and symbols, tests, and gaps. Planned behaviour absent
   from code is marked *not implemented*; partial behaviour lists the missing
   steps.
2. **Architecture.** Responsibilities, boundaries, dependencies, data ownership
   and lifetime, and connections to other features, as they exist in code. A
   diagram must agree with the detailed flow.
3. **Use-case walkthroughs.** Trigger and inputs, then each step through exact
   functions: validation, transformation, state changes, external calls,
   results. Include an example data trace and the relevant error, cancellation,
   retry and cleanup paths. For asynchronous work, distinguish enqueue,
   processing and completion.
4. **Function index.** Every function that implements or materially supports
   the scoped flows, with file, responsibility and use cases. Trivial helpers
   get one line; dynamic dispatch and library boundaries are named, not
   enumerated.
5. **Deep explanations.** For behaviour-bearing functions: purpose, signature
   with example input and output, callers and callees, branches, side effects,
   errors and invariants. Explain important blocks with short excerpts and
   numbered commentary. Never paste whole files.
6. **Change guidance.** Where a given change would start, what else it touches,
   which invariants and tests protect it.

Label claims by evidence: *observed in code*, *verified by test or log*,
*inferred*, *unknown*. Static reading does not prove a branch runs.

## Procedure

1. **Scope and coverage map.** Identify the use cases in scope and the files and
   symbols involved before writing in depth. *Exit:* coverage map.
2. **Trace.** Read source, callers, registrations, configuration and tests along
   each path; delegate breadth to researchers. Note where code departs from the
   contract or plan. *Exit:* traced paths with evidence labels.
3. **Write.** Produce the explanation at the depth above, in chat (explain) or
   in `guide/` (snapshot). *Exit:* all scoped use cases explained, or the
   remainder listed.
4. **Refresh** *(refresh mode)*. Compare the recorded revision with current code;
   update every affected walkthrough, index entry, diagram and example in
   place; fix renamed or deleted references; keep the owner's own notes and
   flag any that now contradict the code. *Exit:* guide matches current code.
5. **Check.** Every scoped use case and relevant symbol is covered or listed as
   a gap; links, symbols and excerpts match the source. *Exit:* coverage report.

## Boundaries

- Read-only outside `guide/`: no code fixes, no edits to contract, plan or log,
  no running project code.
- Missing implementation is reported as a gap, never described as if it existed.
- Code differing from the contract is explained as it is, with the unmet
  criterion stated separately.

## Done when

The requested explanation exists, grounded in inspected code, with coverage and
evidence limits stated. A partial guide says it is partial.

## Example invocations

- "Use workflow feature-explain: how does batch-import handle cancellation?"
- "Use workflow feature-explain, snapshot batch-import so I can study it."
- "Use workflow feature-explain, refresh the batch-import guide after my changes."
