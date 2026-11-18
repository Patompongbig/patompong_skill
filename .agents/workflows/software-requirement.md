# software-requirement workflow

> Define and maintain the system-level software requirement specification (SRS),
> its decomposition into phases and features, and the project's engineering
> standards.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md)
Read a reference only when a step needs it.

## Purpose

The SRS is the project's main guideline: what the system is, who it serves, what
it must do, and the constraints it must respect, in more depth than `AGENTS.md`.
Every feature contract, test and plan traces back to it.

This workflow owns the system level of the [document model](references/document-model.md):
requirements, the roadmap that splits them into phases and features, the domain
glossary, system-level ADRs, and `engineering.md`. It does not write feature
contracts, tests or plans, and it does not implement.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **review** | Check requirements against intent or code | Nothing | Findings and proposed revisions in chat |
| **create** (default for a new project) | No SRS exists for the scope | `docs/requirements/`, `GLOSSARY.md`, ADRs | Accepted SRS section(s) |
| **update** (default otherwise) | Intent or understanding changed | Same, edited in place | Amended SRS, dependents marked stale |
| **decompose** | Split the SRS into phases and features | `docs/roadmap.md` | Accepted roadmap with full REQ coverage |
| **standards** | Establish or extend project engineering standards, including lessons from reference codebases | `docs/engineering.md` | Accepted standards |

## Inputs

- The user's intent and the scope of this session.
- Existing project guidance and documentation (read-only sources unless inside
  `patompong-docs/`).
- For existing systems: the relevant code, configuration and runtime evidence.
- For decompose: an accepted SRS. For standards: the stack, and any reference
  codebases the user names (local path or public source).

## Outputs

Owned: `docs/requirements/`, `docs/roadmap.md`, `docs/engineering.md`,
`docs/GLOSSARY.md`, `docs/adr/`, `docs/research/` (approved findings only).
Read-only: everything else, including feature dossiers and shared contracts.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Author | opus | Writes owned files | Main session: elicits, drafts and maintains |
| Researcher | sonnet | Read-only | Maps existing code and docs; studies reference codebases |
| Design reviewer | opus | Read-only | Fresh-context consistency and coverage check before user review |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Skills

- [domain-modeling](../skills/mattpocock/domain-modeling/SKILL.md) — challenge
  terms, test them against scenarios, record glossary entries and ADRs.
  *Adaptation:* write to `docs/GLOSSARY.md` and `docs/adr/` under
  `patompong-docs/`, not the repository root, and defer writes to the
  confirmation step instead of writing immediately. Offer ADRs only for
  consequential, agreed trade-offs.
- [research](../skills/mattpocock/research/SKILL.md) — only when a technical
  uncertainty needs dedicated primary-source investigation and the user agrees.
  Findings go to `docs/research/`. If declined, record the uncertainty.

## Procedure

1. **Bound the session.** Read project guidance and a small document index.
   State the operation, the area in scope, connected flows, and exclusions. If
   the request would pull in substantial unrelated context, offer concrete
   smaller slices with a recommendation and wait for the choice.
   *Exit:* agreed scope.

2. **Establish current state.** Read only what the scope needs; delegate wide
   reads to a researcher. Trace producers, consumers, data ownership, user
   journeys and failure flows. Keep four categories distinct: implemented
   (supported by code), documented but unverified, future intent, and open
   question. Code describes what exists, not what is wanted.
   *Exit:* a current-state summary with inspection coverage stated.

3. **Resolve concepts and requirements.** Use domain-modeling to pin down terms
   and test them against concrete scenarios. Ask focused questions for genuine
   gaps; discover facts yourself. Surface contradictions between intent, docs
   and code rather than choosing one silently.
   *Exit:* agreed terms and requirement decisions.

4. **Draft the specification.** Scale the content to the system; omit sections
   that do not apply. Cover where relevant:
   - Purpose, users and actors, goals, scope and explicit exclusions.
   - Domain concepts and their relationships.
   - Functional requirements with stable `REQ-<AREA>-NN` IDs, each verifiable.
   - Quality attributes with measurable targets (labelled *proposed* until agreed):
     performance, reliability, security, privacy, compatibility, operability.
   - System context: components, external systems, data ownership, key flows
     including error, cancellation and recovery paths.
   - Boundary needs between components, summarised; detailed interface
     definitions belong to contracts.
   - Constraints, assumptions, open decisions.
   - Extension needs: what is committed, what is foreseeable, what is deferred.
     Foreseeable growth informs design; it does not authorise building it.

   Keep requirements free of implementation tasks, file-level instructions or
   estimates. *Exit:* a complete draft for the agreed scope.

5. **Decompose** *(decompose mode)*. Split the SRS into phases (`PH-N`, each
   with a goal and an exit condition) and features (`FEAT-NN` with a stable
   slug). Prefer vertical features that deliver verifiable behaviour end to end;
   sequence wide cross-cutting changes as expand → migrate → contract. For each
   feature record: the REQ IDs it covers, the features it depends on, and the
   shared contracts it is likely to need or extend. Include a coverage matrix:
   every in-scope REQ maps to at least one feature, or is explicitly deferred.
   The roadmap carries no live status; that lives in each feature's
   `state.json`. *Exit:* complete coverage and an acyclic dependency order.

6. **Standards** *(standards mode)*. Capture stack, conventions, architecture
   rules and project-specific rules in `docs/engineering.md`, following the
   [shape in the rubric](references/engineering-standards.md#docsengineeringmd-shape).
   For each reference codebase, brief a researcher on the aspects the user
   cares about; distil principles and short illustrative patterns with source
   locations, plus what not to adopt. No verbatim code; respect licenses.
   *Exit:* draft standards ready for review.

7. **Design review.** Dispatch a fresh-context design reviewer over the draft:
   internal contradictions, unverifiable requirements, missing flows, unclear
   ownership, REQ coverage gaps in the roadmap, standards that are not
   checkable. Address confirmed findings.
   *Exit:* reviewer verdict passes, or remaining findings are listed for the user.

8. **Confirm and write.** Present the scope, the changes, open decisions and
   the files to touch. On confirmation, write or amend in place, set status
   headers, update the glossary, and follow the
   [amendment](references/document-model.md#amendments) steps for accepted
   content: affected feature dossiers are marked stale and listed.
   *Exit:* files written and cross-checked (IDs, links, Basis headers).

## Gates

- **Entry:** scope agreed. Decompose requires an accepted SRS for the scope.
- **Exit:** every requirement is verifiable or labelled open; terms are
  consistent with the glossary; status headers are correct; dependents of
  changed requirements are marked stale; the design review has run.

## Boundaries

- Requirements say *what* and *why*, not *how*. Implementation sequencing
  belongs to development-plan; interface detail belongs to contract-and-test.
- Existing documentation outside `patompong-docs/` is a source: link it, report
  conflicts, do not edit or duplicate it.
- No implementation, runtime changes, test runs or ticket creation.

## Done when

The agreed scope is specified clearly enough that a future agent can derive
feature contracts from it without guessing; changed files are written and
consistent; open decisions and deferred areas are explicit; dependents needing
reconciliation are listed. A draft with open decisions is reported as a draft.

## Example invocations

- "Use workflow software-requirement to create the SRS for the sync service.
  Interview me first."
- "Use workflow software-requirement, update: cancellation must now be
  resumable. Show me affected features."
- "Use workflow software-requirement, decompose the SRS into phases and features."
- "Use workflow software-requirement, standards: take guidance from Ollama's and
  codex-cli's module structure and error handling."
- "Use workflow software-requirement to review the requirements against current
  code. Findings only."
