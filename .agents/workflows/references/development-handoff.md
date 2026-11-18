# Development handoff

Shared operating rules for the development workflows: the pipeline, authority
between artifacts, modes, baseline boundaries, evidence and stage transitions.
Document layout and ownership are in the [document model](document-model.md);
roles and loops in [agent roles](agent-roles.md); terms in the [glossary](glossary.md).
Workflows link here instead of restating these rules.

## Pipeline

```text
software-requirement ──► roadmap (decompose) ──► per feature:
   (SRS, system level)                            contract-and-test ──► development-plan
                                                  ──► execute ⇄ qa-verify ──► feature gate
                                               per phase: qa-verify release ──► phase exit
doc-reconcile: any time (audit / migrate / amend)
feature-explain: on demand, after code exists
interview: combinable with any writing stage
ask-answer: read-only, never combined with a writing stage
```

The SRS defines the system as a whole. Decompose turns it into phases and
features. Each feature is then deepened through its contract and tests, planned,
and implemented under independent QA.

**Entering later.** Start at any stage whose inputs already exist and are
accepted. Do not recreate artifacts or repeat approvals for unchanged content.

**New interfaces.** When the exact interface is not yet known, a draft plan may
propose it; contract-and-test then reviews and accepts it, and the plan is
reconciled before execution. Tests may be written against proposed interfaces
without production stubs; the resulting import failures are *blocked*, not Red.

## Authority

When artifacts disagree, the higher one governs:

1. User-confirmed intent in the current conversation
2. SRS (`docs/requirements/`) and accepted ADRs
3. Shared contracts (`docs/contracts/`)
4. Feature contract (`features/<f>/contract.md`)
5. Accepted tests
6. Plan
7. Existing code — evidence of *current* state, never authority for desired behaviour

Surface every conflict with the exact clauses involved. Never resolve it by
editing the lower artifact to match convenience, or the higher one to match code.
Changing an accepted higher artifact goes through its owning workflow or a change
request.

## Alignment preflight

Contract-and-test and development-plan begin with a preflight before deep writing:

- Every in-scope item traces to SRS requirements and its roadmap feature.
- Referenced shared contracts are current, and the new work fits them as-is or
  needs a compatible extension or a CR.
- Upstream artifacts the stage depends on are accepted and not stale.

Output `aligned`, or a numbered conflict list with a proposed resolution for each.
Independent work continues; dependent work waits for the user's decision.

## Modes

Every workflow interprets modes the same way:

| Mode | Writes | Notes |
| --- | --- | --- |
| **review** | Nothing | Findings in chat. No saved reports, no test execution unless also assigned. |
| **create / update** | The workflow's owned files | Propose the change, obtain confirmation, then write. Already-confirmed content needs no second confirmation. |
| Workflow-specific modes | As defined by that workflow | e.g. decompose, standards, audit, migrate, amend. |

Default mode is stated by each workflow.

## Baseline boundaries

These apply to every workflow, every included skill, and every subagent.

- **Version control.** Never commit, push, merge, rebase, open PRs or delete
  branches/worktrees. The only permitted git write is staging task files as a
  checkpoint during execution.
- **Agent configuration.** Do not create or edit `AGENTS.md`, `CLAUDE.md`, agent
  settings, skills or workflows as a side effect of project work.
- **Environment.** No installs, global configuration changes, deployments,
  destructive migrations or external writes without an explicit assignment.
- **Data.** Use isolated local test data. Live user data, paid services and
  shared environments need explicit scope. Inspect unfamiliar commands before
  running them.
- **Protected artifacts.** A stage never modifies another stage's accepted
  artifacts to unblock itself. Downstream stages consume them; disagreements
  become conflicts or CRs.
- **Scope.** If a request needs substantial unrelated context, propose smaller
  feature or flow slices and wait for the user's choice before broad reading.
- **Included skills.** Workflow adaptations override a skill's defaults. A skill
  cannot widen output paths, write access, delegation or external actions.

## Autonomy

The user owns *what* is built and whether it is done; agents own *how*, under
independent review.

| Artifact or decision | Accepted by |
| --- | --- |
| SRS, roadmap, `engineering.md`, ADRs | User |
| Feature contract and its outside-in tests | User |
| Shared-contract change requests | User |
| Plan | User (guided) · design review (chain) |
| Unit tests and code | QA verdict, task by task |
| Feature done, phase exit | User, on the feature-gate or release report |

Two levels, chosen per request:

- **guided** (default): every stage stops for the user's confirmation.
- **chain**: the user names a sequence and says "chain", e.g. "contract-and-test →
  development-plan → execute for batch-import, chain". User-owned artifacts
  still stop for acceptance. An agent-owned artifact is accepted automatically
  when its design review returns `PASS` or `PASS_WITH_NOTES` and it has no open
  decisions, conflicts or CRs; the chain then continues. The status header
  records `accepted (auto: design review PASS)` and the log notes it, so the
  user can review it later. Any `FAIL`, open decision or escalation stops the
  chain and returns to the user.

Execution's task loop is autonomous at both levels; it stops only for the
escalations defined in [execute](../execute.md).

## Acceptance and staleness

- The user accepts, except agent-owned artifacts under chain autonomy (above). Record acceptance in the file's status header and in
  `state.json`; capture the substance of the confirmation, never invented quotes.
- Document acceptance and test results are separate facts: an accepted contract
  can have Red or blocked tests.
- After an accepted upstream change, the changing stage marks dependents stale
  (see [amendments](document-model.md#amendments)) and lists them. A stale
  artifact cannot gate execution or a completion claim until reconciled.
- Previously verified behaviour becomes unverified when relevant code, tests,
  dependencies or environment change.

## Evidence

Claims require matching evidence:

| Claim | Evidence required |
| --- | --- |
| Documents consistent | Cross-check of IDs, links, Basis headers |
| Behavioural Red | Test collected, executed, failed on the target behaviour |
| Unit / contract behaviour | Fresh Green run of those tests |
| Integration | Real connected components exercised, not doubles |
| End-to-end acceptance | Complete user flow observed |
| Independent QA | Fresh-context verifier verdict on the final code state |

Zero collected tests, skips, expected-failure markers and environment-blocked
checks are not passes. Required manual, hardware or external gates stay open
until observed or the user changes the criterion. Record for every executed
check: working directory, command, result; for unexecuted ones, label them
`proposed`.

## Combining and switching stages

- Selecting or accepting one stage does not start the next. An explicitly
  requested chain advances through its named stages, each keeping its own
  confirmation and write boundaries. Always state which stage is active.
- **Interview** supplies structured questioning and confirmation to the active
  writing stage. Confirmed decisions are written to their owning files, phrased
  as engineering statements of intent, with one log entry each. Interview alone
  is chat-only.
- **Ask-answer** stays read-only; switching to a writing stage requires an
  explicit request.
- Review-only inside any workflow permits inspection and chat findings only.

## Stage handoff

Each stage ends by reporting, in chat:

- Outputs written (links) and their status.
- Alignment result and any open conflicts or CRs.
- Dependents marked stale.
- Commands executed versus proposed, with results.
- Inputs the next stage needs, and the decisions still open.
