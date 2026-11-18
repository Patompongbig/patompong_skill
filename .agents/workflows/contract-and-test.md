# contract-and-test workflow

> Deepen one roadmap feature into a precise contract — scope, acceptance
> criteria and interfaces — and author the tests that prove it, stopping at Red.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[engineering standards](references/engineering-standards.md)
Read a reference only when a step needs it.

## Purpose

This is where a feature from the roadmap becomes concrete and testable. The
contract states exactly what the feature must do and how it connects to the
rest of the system; the tests make every acceptance criterion executable. Both
are written against the SRS and the shared contracts, so features deepened at
different times stay aligned.

This workflow also owns the shared contract registry: it creates shared
contracts and applies approved change requests to them. It does not decide
internal decomposition (development-plan) or write production code, except in
the explicitly requested minimal-code mode.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **review** | Check a contract or tests against the SRS and code | Nothing | Findings in chat |
| **create / update** (default) | Deepen a feature or revise its contract | `features/<f>/contract.md`, `tests/`, `log.md`, `state.json`; new shared contracts | Accepted contract and tests, observed Red |
| **change-request** | Apply an approved CR to a shared contract | `docs/contracts/`, consumer `state.json` staleness | Amended shared contract, consumers marked stale |
| **minimal-code** | User explicitly authorises bounded production code | Above, plus the named production paths | Named behaviour Green via TDD |

## Inputs

- The roadmap entry for the feature (`FEAT-NN`), its REQ IDs and dependencies.
- The SRS sections those REQs belong to.
- Shared contracts the feature uses or extends.
- Relevant current code: to locate interfaces and constraints, not to derive
  desired behaviour.
- A draft plan, when the exact interface shape is still being proposed.

A missing roadmap entry or unaccepted SRS for the scope limits the work to a
draft and is reported.

## Outputs

Owned: `features/<f>/contract.md`, `features/<f>/tests/` (`test-cases.md`,
executable tests, fixtures, helpers), new files in `docs/contracts/`, amendments
to existing shared contracts via approved CRs. Appends to `log.md`; maintains
its entries in `state.json`.

**Contract shape** (`contract.md`):

```markdown
Status: draft · Updated: YYYY-MM-DD · Basis: REQ-IMP-01..04, CT-ORDER
# FEAT-04 batch-import — contract
## Scope            in / out, linked REQs
## Acceptance       AC-NN: Given … When … Then …  (→ REQ)
## Interfaces       feature-owned clauses C-NN; shared contracts referenced by ID
## Behaviour rules  validation, state transitions, errors, timeouts, retries,
                    idempotency, cancellation, recovery — only where relevant
## Examples         valid and invalid, with expected outcomes
## Open decisions
```

**Test cases** (`test-cases.md`): scenarios `S-NN`, each with linked AC/C IDs,
level (schema, contract, integration, end-to-end), setup, input, expected
observable outcome, and the defect it is meant to catch. Unit-level tests are
owned by execute.

Test evidence is recorded in `log.md`, not a separate verification file.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Author | opus | Writes owned files | Main session: contract, scenarios, tests |
| Researcher | sonnet | Read-only | Locates interfaces, producers and consumers |
| Design reviewer | opus | Read-only | Fresh-context check: contract ↔ SRS and shared contracts, tests ↔ criteria |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Skills

- [writing-good-tests](../skills/obra/test-driven-development/writing-good-tests.md)
  — independent expectations, meaningful assertions, doubles at boundaries.
  Reading this reference does not invoke the full TDD skill.
- [verification-before-completion](../skills/obra/verification-before-completion/SKILL.md)
  — classifying observed results honestly.
- [test-driven-development](../skills/obra/test-driven-development/SKILL.md) —
  **minimal-code mode only**, within the named production paths. Existing code
  is never deleted to satisfy a reset rule.

## Procedure

1. **Alignment preflight.** Run the
   [preflight](references/development-handoff.md#alignment-preflight): the
   feature traces to its REQs and roadmap entry; the shared contracts it needs
   fit as they are, need a compatible extension, or need a CR; its upstream
   artifacts are accepted and not stale. *Exit:* `aligned` or a conflict list.

2. **Inspect.** Read the relevant producers, consumers, interfaces and existing
   tests; delegate wide reads to a researcher. Distinguish implemented facts,
   desired behaviour, assumptions and open decisions. If the feature is too
   broad for one session, propose smaller slices and wait.
   *Exit:* a scoped view of what the contract must govern.

3. **Agree observable behaviour.** Present normal and important failure
   scenarios with independently derived expected outcomes. Confirm
   consequential interface and boundary choices. Specify observable behaviour,
   not internal structure or incidental call order, unless that order is a
   genuine obligation. *Exit:* agreed scenarios.

4. **Define the contract.** Write scope, acceptance criteria and feature-owned
   interface clauses. Apply the ownership rule: an interface used by two or
   more features belongs in `docs/contracts/`; reference it rather than
   restating it. A needed change to an accepted shared contract becomes a
   [change request](references/document-model.md#shared-contracts-and-compatibility)
   in `log.md`, classified compatible or breaking; dependent clauses stay draft
   until it is decided. Use schemas or types for structure and written rules for
   behaviour; schema validity alone does not prove interaction.
   *Exit:* draft contract, CRs raised where needed.

5. **Map scenarios to checks.** Tests here are **outside-in**: they exercise
   the feature through its agreed boundaries, so they survive any internal
   design the plan later chooses. Choose the smallest mix that proves each
   criterion: schema/type checks, contract tests (consumer and provider),
   integration tests for real connections, end-to-end checks for the user
   outcome. Unit tests are not written here — they depend on internal structure
   that development-plan decides, and are authored during execute. Every AC has
   at least one scenario; include failure, cancellation, recovery and
   regression scenarios where the contract names them.
   *Exit:* complete `test-cases.md`.

6. **Author tests.** Exercise agreed public interfaces. Derive expected values
   from the contract's examples, never from production helpers. Use doubles only
   at true boundaries; a consumer test against a double is not provider
   verification — test the provider separately or label the gap. Never write a
   fake implementation that makes the system look integrated. Check that the
   runner discovers tests in this location; ask before changing shared runner
   configuration. *Exit:* executable tests for the mapped scenarios.

7. **Run and classify.** Run the scoped tests and classify each: Red,
   already passing (legitimate; do not invert it), blocked (missing interface,
   import, fixture or environment), or not run. Zero collected tests is not
   evidence. Record results in `log.md`. *Exit:* every test classified.

8. **Design review.** Dispatch a fresh-context design reviewer: every AC traces
   to a REQ; no clause contradicts the SRS or a shared contract; every AC has a
   test that would fail if the behaviour regressed; no test asserts incidental
   implementation. Address confirmed findings. *Exit:* verdict passes, or
   findings listed for the user.

9. **Confirm and accept.** Present the contract, scenarios, test results and
   open CRs. On the user's acceptance, set status headers, record the protected
   test list in `state.json`, and mark the plan stale if one exists and the
   contract changed. *Exit:* accepted artifacts, or a labelled draft.

**Change-request mode.** Apply an approved CR to the shared contract in place:
compatible changes without a version bump; breaking changes through expand →
migrate → contract with a version bump and a deprecation note. Update the
Changes table and the consumer list, and mark each consumer's dossier stale.

**Minimal-code mode.** Only on explicit request naming the production paths.
After the contract is accepted, implement the named behaviour in small
Red → Green slices; stop when a failing test needs work outside those paths.

## Gates

- **Entry:** preflight run; the feature exists in the roadmap or the user has
  explicitly scoped it.
- **Exit:** every AC traces to a REQ and has at least one scenario and test;
  every test is classified with observed evidence; shared-contract changes are
  CRs, not silent edits; the design review has run.

## Boundaries

- No production code outside minimal-code mode. Accepting a contract or tests
  is not authorisation to implement.
- Existing project tests outside `features/<f>/tests/` are read-only.
- Use isolated local test data; no live user data or paid services without
  explicit scope.
- Do not weaken expectations to fit current code; a mismatch is a conflict.

## Done when

The contract and tests are written, run and classified, reviewed, and either
accepted (with the protected list recorded) or reported as a draft with its
open decisions. The feature may be entirely Red; that is the expected outcome.

## Example invocations

- "Use workflow contract-and-test for FEAT-04 batch-import. Define the contract
  and Red tests from the SRS; stop for my review."
- "Use workflow contract-and-test, change-request: apply approved CR-02 to
  CT-ORDER."
- "Use workflow contract-and-test, minimal-code for request validation in
  src/import/validator.py only."
- "Use workflow contract-and-test to review the export contract against the SRS."
