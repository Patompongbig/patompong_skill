# qa-verify workflow

> Independently verify a code change against its specification and the
> project's engineering standards, and return a severity-ranked verdict.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[engineering standards](references/engineering-standards.md)
Read a reference only when a step needs it.

## Purpose

QA is the independent half of the build–verify loop. It re-runs checks itself,
reads the change in the context of the code around it, and judges it against
the accepted contract, the plan and the engineering standards. It reports; it
never fixes. Its value comes from fresh context and a fixed severity bar: it
does not trust the implementer's claims, and it does not hunt for nits.

It runs inside [execute](execute.md) for every task and at the feature gate,
can be selected on its own to review any change, and verifies a whole roadmap
phase across its features before that phase is called done (release mode).

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **task** | Dispatched by execute with a task packet | Nothing | Verdict returned to the implementer |
| **feature** | Execute's feature gate | Nothing | Two verdicts (spec axis, standards axis) |
| **standalone** (default when selected directly) | The user wants a change reviewed: their own, another agent's, a branch | Nothing; a `log.md` entry only if the user asks | Verdict in chat |
| **release** | All features of a roadmap phase are done; verify the phase as a whole | On `PASS` and user confirmation, one exit line under the phase in `docs/roadmap.md` | Phase verdict |

Standalone mode reads code statically by default. It runs tests and checks only
when the user asks for it. Release mode always runs them.

## Inputs

- **The change.** Task: `git diff -- <files in the task packet>` (new files
  registered with `git add -N`). Feature: `git diff <baseline>` over the whole feature.
  Standalone: the diff, range, branch or paths the user names. Release: the
  phase in `docs/roadmap.md`, its features' dossiers, and the current code.
- **Specification.** The feature contract and its acceptance criteria, the plan
  task, referenced shared contracts, and the protected test list. Standalone
  without a dossier: whatever spec the user names; if none exists, review the
  standards axis only and say so.
- **Standards.** `docs/engineering.md`, the
  [toolkit rubric](references/engineering-standards.md), and project tooling
  rules.
- **Claims.** The task packet. Claims are hypotheses to check, not evidence.

Fail fast: an empty diff, unresolvable range or missing contract is reported
before any review work.

## Outputs

A verdict in the [return format](references/agent-roles.md#return-formats).
QA writes no code, tests or documents. In the execute loop, the implementer
records the verdict in `log.md`.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| QA verifier | opus | Read-only; runs non-mutating checks | Task and standalone verification |
| Spec verifier | opus | Same | Feature gate: conformance to contract and criteria |
| Standards verifier | opus | Same | Feature gate: engineering standards and design quality |
| Release verifier | opus | Same | Release: the phase as a whole, across features |

When dispatched by execute, models were confirmed at the start of that run.
When selected directly, confirm models once per
[agent roles](references/agent-roles.md#model-selection). A main session that
authored the change must delegate the review; one that did not may review
directly.

## Skills

- [verification-before-completion](../skills/obra/verification-before-completion/SKILL.md)
  — what counts as evidence for each claim.
- [ponytail-review](../skills/ponytail/ponytail-review/SKILL.md) — technique for
  tracing callers and data flow beyond the diff, and its "concrete case or no
  finding" rule.
- [code-review](../skills/mattpocock/code-review/SKILL.md) — the two-axis split
  used at the feature gate, and its code-smell baseline as judgement-call input
  to the standards axis.

**Adaptations.** No commits, SHAs or trackers: the change is a working-tree diff
or a user-named range. The verdict format in agent roles replaces each skill's
own output format. Smells are reported only when they reach MAJOR under the
rubric. Ponytail-review's plain-language style applies to finding text.

## Procedure

1. **Pin the target.** Resolve the diff, list changed files including new ones,
   and identify the spec and standards sources. *Exit:* non-empty diff, known
   sources, or a fail-fast report.

2. **Re-run the evidence.** Run the packet's focused checks and the regressions
   the change could affect. Confirm tests were collected and not skipped.
   Confirm protected tests, fixtures and contracts are unchanged (no diff on
   protected paths). For every deleted or rewritten unit test, confirm its
   stated reason and that the behaviour it covered is still tested or was
   deliberately removed; an unexplained loss of coverage is a MAJOR finding.
   Use only non-mutating commands: tests, type checks,
   linters and formatters in check mode. *Exit:* every check has an observed
   result, or is labelled not run with a reason.

3. **Spec axis.** For each criterion the task claims: is it implemented, is it
   correct, does a test actually exercise it? Check contract clauses
   exactly: signatures, data shapes, errors, ordering, cancellation and
   recovery where specified. Flag missing or partial behaviour, and behaviour
   nobody asked for. Quote the clause for every finding.

4. **Standards axis.** Apply `engineering.md`, then the rubric's QA questions.
   Read beyond the diff: callers of every changed symbol, the functions it
   calls, the tests around it. A changed signature or behaviour is checked
   against every caller. Judge scale against the load the requirements state.

5. **Rank and cap.** Keep only findings with a concrete failing case or a
   clearly cited standard. Classify BLOCKER or MAJOR; drop the rest or keep up
   to three as notes. Report at most five findings, most severe first. Mark
   each `reproduced` or `static`. Give a fix *direction*, not code. Decide the
   verdict by the rules in agent roles.

6. **Re-review rounds.** On a resubmission, verify each previous finding and
   review the hunks changed since. Raise a new finding only if it is a BLOCKER
   or was introduced by the fix. Areas that passed are not reopened without new
   cause. This keeps the loop converging.

**Release mode** replaces steps 1–4 with a phase-level check. Feature gates
prove each feature alone; release proves they work together and that the phase
delivers what the roadmap promised.

- **Completeness.** Every feature in the phase has an accepted, non-stale
  contract and plan, all tasks done, and a passed feature gate whose evidence
  still matches the current code. Every REQ the roadmap assigns to the phase
  maps to verified acceptance criteria, or is explicitly deferred.
- **Integration.** Run every feature's outside-in suite together, then the full
  regression suite and the project's build, type and lint checks, on one code
  state. Exercise the end-to-end flows that cross feature boundaries.
- **Shared contracts.** Every consumer is on a supported shape; deprecated
  shapes past their removal condition are flagged; no feature redefines a
  shared interface locally.
- **Docs.** No open CRs, unresolved BLOCKERs or stale artifacts in the phase.

Same verdict format and severity bar; findings name the feature or contract
they belong to. Fixes happen through the owning workflow, then release re-runs.
On `PASS` and the user's confirmation, add under the phase in the roadmap:
`Exit verified: YYYY-MM-DD · <suite command> <counts>`.

## Gates

- **Entry:** target pinned; spec source known, or spec axis explicitly skipped.
- **Exit:** every reported check was run by the verifier; every finding cites
  a clause or standard and carries evidence; verdict follows the rules.

## Boundaries

- Read-only: no edits to code, tests, documents or configuration, and no
  staging. Commands must not mutate the workspace beyond test caches.
- QA cannot introduce requirements. A gap in the specification itself is
  reported as a note for the user, not a finding against the code.
- A reviewer's preference is not a standard. Findings without a cited clause or
  a concrete failing case are not reported.
- QA does not dispatch further agents, except the two axis verifiers at a
  feature gate.
- Release mode's only write is the confirmed exit line in the roadmap.

## Done when

The verdict is returned with observed check results and at most five
evidence-backed findings, and every claim in the packet has been either
confirmed or contradicted.

## Example invocations

- Dispatched by execute: "qa-verify task mode, packet for T-04 attached."
- "Use workflow qa-verify on my uncommitted changes against
  features/export/contract.md. Run the tests too."
- "Use workflow qa-verify to review branch feature/cache against main for
  standards only."
- "Use workflow qa-verify, release PH-2."
