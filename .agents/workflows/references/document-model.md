# Document model

How project documents are laid out, who owns each fact, and how changes are
applied without multiplying files. Read this before any workflow writes to
`patompong-docs/`. Terms are defined in the [glossary](glossary.md).

## Principles

1. **The software requirement specification (SRS) is the main guideline.** It
   describes what the system is and must do, in more depth than `AGENTS.md`.
   Every feature traces back to it.
2. **One fact, one home.** Each fact has exactly one owning file. Other files
   reference it by ID and do not restate it.
3. **Edit in place.** Never create `plan-v2.md`, addendum, change-note or
   "update" files. Replace superseded text in the owning file; record *why* in
   the log, the contract's Changes table, or an ADR.
4. **Status lives in data, explanation lives in prose.** Machine-tracked status
   is in `state.json`; prose documents carry only a one-line status header.
5. **Size is a cost.** Link evidence instead of pasting it. No transcripts, raw
   logs, or duplicated code in documents.

## Layout

All paths are relative to the target project root, never the portable toolkit.

```text
patompong-docs/
  docs/                              # SYSTEM level
    requirements/                    # SRS: concepts, REQ-IDs, system context, constraints
    roadmap.md                       # phases → features, dependencies, REQ coverage
    contracts/<CT-ID>-<slug>.md      # shared contracts (used by 2+ features)
    engineering.md                   # project engineering standards and reference codebases
    GLOSSARY.md                      # project domain terms
    adr/NNNN-<slug>.md               # consequential decisions
    research/<topic>.md              # approved research findings
  features/<feature>/                # FEATURE level dossier
    contract.md                      # scope, acceptance criteria, feature-owned interfaces
    tests/                           # outside-in suite: test-cases.md, tests, fixtures
    plan.md                          # tasks, dependencies, checks
    log.md                           # append-only decisions, progress, QA verdicts, CRs
    state.json                       # machine-readable status
    guide/                           # optional feature-explain snapshot
```

Create only what the current scope needs. Small projects may keep the SRS in a
single `requirements/README.md`. Existing project documentation outside
`patompong-docs/` is a read-only source: link it, do not move or duplicate it.

## Identifiers

| Kind | Format | Defined in |
| --- | --- | --- |
| Requirement | `REQ-<AREA>-NN` | `docs/requirements/` |
| Phase | `PH-N` | `docs/roadmap.md` |
| Feature | `FEAT-NN` plus a stable slug | `docs/roadmap.md` |
| Shared contract | `CT-<NAME>` | `docs/contracts/` |
| Acceptance criterion | `AC-NN` | `features/<f>/contract.md` |
| Feature contract clause | `C-NN` | `features/<f>/contract.md` |
| Test scenario | `S-NN` | `features/<f>/tests/test-cases.md` |
| Task | `T-NN` | `features/<f>/plan.md` |
| Change request | `CR-NN` | the raising feature's `log.md` |

IDs are never reused or renumbered. Feature-local IDs are referenced from other
features as `<feature>/AC-03`. Removed items keep their ID with a `removed` note
when anything still links to them.

## Ownership

| Fact | Owning file | Owning workflow |
| --- | --- | --- |
| System purpose, concepts, requirements, constraints, system context | `docs/requirements/` | software-requirement |
| Phases, features, dependencies, REQ coverage | `docs/roadmap.md` | software-requirement (decompose) |
| Project engineering standards, reference codebases | `docs/engineering.md` | software-requirement (standards) |
| Domain terms | `docs/GLOSSARY.md` | software-requirement |
| Consequential decisions | `docs/adr/` | the stage that made the decision |
| Shared interface (2+ consumers) | `docs/contracts/` | contract-and-test |
| Feature scope, acceptance criteria, feature-owned interfaces | `features/<f>/contract.md` | contract-and-test |
| Outside-in tests (schema, contract, integration, end-to-end) | `features/<f>/tests/` | contract-and-test |
| Unit and regression tests | project test location named in the plan | execute |
| Phase exit verification | one line under the phase in `docs/roadmap.md` | qa-verify (release) |
| Decomposition, task order, proposed paths, check commands | `features/<f>/plan.md` | development-plan |
| Progress, decisions, QA verdicts, CRs | `features/<f>/log.md` | any stage (append only) |
| Machine status | `features/<f>/state.json` | any stage, within its own entries |
| Implementation explanation | `features/<f>/guide/` | feature-explain |

A stage may apply **bounded factual updates** outside its ownership — ticking a
verified plan checkbox, correcting a moved file path — but never changes the
meaning of a requirement, criterion, contract clause, protected test or decision.

## File conventions

**Status header.** Every prose document starts with one line:
`Status: draft | accepted | stale | superseded · Updated: YYYY-MM-DD · Basis: <IDs>`
`Basis` lists the upstream artifacts the content was written against
(for example `REQ-IMP-01..04, CT-ORDER v2`), so staleness is detectable.

**log.md.** Append-only, newest last, one short entry per event:

```markdown
### 2026-11-18 · T-03 · QA PASS
Changed: src/import/parser.py, tests/test_parser.py. Evidence: `pytest tests/test_parser.py` 12 passed.
```

Entry types: `DECISION`, `PROGRESS`, `QA <verdict>`, `CR-NN`, `AMEND`, `BLOCKED`,
`DEVIATION`. Keep each entry to a few lines. When the log grows past roughly 300
lines, doc-reconcile may condense entries for accepted, completed phases into a
summary block, keeping open items and all CRs verbatim.

**state.json.** Minimal, machine-edited, never narrative:

```json
{
  "feature": "batch-import",
  "id": "FEAT-04",
  "phase": "PH-2",
  "updated": "2026-11-18",
  "artifacts": {
    "contract": { "status": "accepted", "basis": ["REQ-IMP-01", "CT-ORDER v2"] },
    "tests":    { "status": "accepted", "protected": ["tests/test_cancel.py"] },
    "plan":     { "status": "accepted" }
  },
  "tasks":    { "T-01": { "status": "done", "qa": "PASS" } },
  "criteria": { "AC-01": { "status": "verified", "evidence": "tests/test_cancel.py::test_cancel_mid_batch" } },
  "stale":    [ { "artifact": "plan", "cause": "CT-ORDER v3", "since": "2026-11-20" } ]
}
```

Allowed values — artifact: `draft | accepted | stale | superseded`; task:
`todo | in_progress | blocked | done`; criterion: `unverified | red | blocked | verified`.
Plan checkboxes mirror task status; `state.json` wins when they disagree.

## Amendments

Any change to accepted content follows the same short path:

1. **Locate the owner** of the fact being changed. If the current stage does not
   own it, raise a CR instead of editing.
2. **Edit in place** and set the status header back to `draft` if the change is
   material; the user re-accepts it.
3. **Log once**: an `AMEND` entry naming the IDs changed and the reason.
4. **Propagate staleness**: add a `stale` entry to every dependent artifact's
   `state.json` whose `Basis` includes the changed IDs.
5. **Report** the dependents that a later stage must reconcile. Do not edit them
   from the current stage.

## Shared contracts and compatibility

Shared contracts change rarely if they are compatible by default. The scheme is
deliberately light.

**Header.**
`# CT-ORDER: Order record` then
`Version: 2 · Status: accepted · Consumers: FEAT-03, FEAT-05 · Updated: YYYY-MM-DD`

**Rules.**

- The contract is a living document edited in place; git is the full history.
- A single integer version bumps **only on breaking changes**. Compatible changes
  edit the document without a bump.
- Consumers are listed once, in the header. Features reference `CT-ORDER` without
  a version unless they intentionally remain on a deprecated shape.
- A short **Changes** table at the end keeps the last ~10 entries:
  `| Date | Change | Class | Affected |`.

**Breaking change protocol — expand → migrate → contract.**

1. **Expand.** Add the new shape alongside the old one. Mark the old one
   `deprecated — remove when: FEAT-03, FEAT-05 migrated`. Bump the version.
2. **Migrate.** Each consumer moves to the new shape through its own feature
   work. Its dossier is marked stale until reconciled.
3. **Contract.** When no consumer remains on the old shape, remove it and log it
   in the Changes table.

This keeps old and new consumers working throughout and removes the need for a
coordinated re-alignment of every feature.

**Change requests.** A feature that needs a shared contract to change appends to
its own `log.md`:

```markdown
### 2026-11-18 · CR-02 · CT-ORDER
Need: batch import must record partial failure per row.
Change: add optional `rowErrors[]` to OrderResult.  Class: compatible.
Affected: none (optional field).  Decision: pending
```

The user decides. On approval, contract-and-test (or doc-reconcile amend) applies
it to the registry and propagates staleness to the listed consumers.

## Legacy layout mapping

Used by doc-reconcile *migrate* to move older projects into this model.

| Legacy path | New home |
| --- | --- |
| `docs/requirements/<feature>.md` | System-level content → `docs/requirements/`; feature acceptance → `features/<f>/contract.md` |
| `docs/system/<feature>.md` | System context section of `docs/requirements/` |
| `docs/contracts/<feature>/` | Feature-owned clauses → `features/<f>/contract.md`; interfaces with 2+ consumers → `docs/contracts/` |
| `tests/<feature>/` | `features/<f>/tests/` (`verification.md` evidence → `log.md`) |
| `implement-plan/<feature>/plan.md` | `features/<f>/plan.md` |
| `implement-plan/<feature>/progress.md`, `qa.md` | `features/<f>/log.md` + `state.json` |
| `implement-plan/<feature>/feature-and-architect/` | `features/<f>/guide/` |
| Scattered change notes, addenda, `*-v2` files | Merged into their owning files; obsolete files removed after user approval |
