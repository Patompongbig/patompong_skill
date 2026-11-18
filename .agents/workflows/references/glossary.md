# Workflow glossary

Every workflow uses these terms with exactly these meanings. Project domain terms
live in the target project's `patompong-docs/docs/GLOSSARY.md`, not here.

## Artifact states

| Term | Meaning |
| --- | --- |
| **Draft** | Written but not confirmed by the user. Never gates downstream work. |
| **Accepted** | The user confirmed this content (or, under chain autonomy, a passing design review accepted an agent-owned artifact). Recorded in the file header and `state.json`. Acceptance belongs to content, not a filename: a material edit returns the artifact to draft. |
| **Stale** | Was accepted, but an upstream artifact it depends on changed afterwards. Must be reconciled before it can gate execution or QA. |
| **Superseded** | Replaced by another artifact or section; kept only when history matters and linked to its replacement. |

## Ownership and change

| Term | Meaning |
| --- | --- |
| **Owning file** | The single file where a fact is defined. Every other file links to it by ID. See the [document model](document-model.md#ownership). |
| **Owning workflow** | The only workflow allowed to change an owning file's meaning. Others may read it or apply bounded factual updates. |
| **Protected artifact** | Accepted contract, test, fixture, expected value or governing requirement that a downstream stage must not modify to make its own work pass. |
| **Amendment** | An approved change applied in place to the owning file, with one log entry and staleness propagated to dependents. |
| **Change request (CR)** | A proposal to change an accepted shared contract or governing requirement, raised by a stage that does not own it. Applied only after user approval. |
| **Compatible change** | A change existing consumers can ignore: additive, optional, or relaxing an input constraint. No version bump. |
| **Breaking change** | A change that can invalidate an existing consumer: removal, rename, type or semantic change, tightened validation, new required element. Bumps the version and follows expand → migrate → contract. |
| **Deprecated** | Still valid, scheduled for removal once its listed consumers have migrated. |

## Verification

| Term | Meaning |
| --- | --- |
| **Red** | A test runs, reaches the target behavior, and fails because that behavior is absent or wrong. |
| **Blocked** | A check cannot run meaningfully: missing interface, import, fixture, environment or permission. Not Red and not passing. |
| **Green** | The relevant checks ran against the current code and passed, with non-zero collected tests and no masking skips. |
| **Verified** | An acceptance criterion has fresh Green evidence at the level it requires (unit, contract, integration or end-to-end). |
| **Evidence** | A reproducible observation (command, working directory, result) tied to the code state it describes. A ledger line, checkbox or agent claim is not evidence. |
| **Static finding** | A defect identified by reading code, not yet reproduced. Labelled as such until reproduced. |

## Agent coordination

| Term | Meaning |
| --- | --- |
| **Role** | A responsibility with fixed access rights (researcher, author, design reviewer, implementer, QA verifier, explainer). See [agent roles](agent-roles.md). |
| **Fresh context** | A subagent started with only an explicit brief, without the conversation history. Required for independent review. |
| **Brief** | The written assignment given to a subagent: objective, scope, inputs, constraints, output format, stop condition. |
| **Task packet** | What the implementer hands to QA for one task: scope, diff, commands run, claims. |
| **Verdict** | QA or design-review result: `PASS`, `PASS_WITH_NOTES` or `FAIL`, with severity-ranked findings. |
| **Severity** | `BLOCKER` (violates acceptance, contract, protected test, correctness, security or data integrity), `MAJOR` (real maintenance, scalability or reliability cost; missing required test or error path), `MINOR` (notes only). |
| **Checkpoint** | Staging (`git add`) a task's files after QA passes so unstaged changes are only unreviewed work. Never a commit. |

## Stage mechanics

| Term | Meaning |
| --- | --- |
| **Alignment preflight** | A short check, before deep writing, that new work agrees with the SRS, roadmap and the shared contracts it touches. Output: `aligned` or a list of conflicts. |
| **Gate** | A condition that must hold before a stage may write (entry) or report done (exit). |
| **Feature gate** | The final verification after all tasks of a feature: full acceptance run plus parallel spec and standards review. |
| **Release** | Phase-level verification across all features of a roadmap phase (qa-verify release mode). Phase exit requires it. |
| **Autonomy** | `guided` (every stage waits for the user) or `chain` (agent-owned artifacts auto-accepted on a passing design review). See the [development handoff](development-handoff.md#autonomy). |
| **Escalation** | Stopping a loop and asking the user for a decision, with the evidence and the smallest decision needed. |
