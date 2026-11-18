# doc-reconcile workflow

> Keep project documentation small, current and consistent: detect drift,
> migrate legacy layouts, apply approved amendments in place, and compact
> accumulated history.

Shared rules: [development handoff](references/development-handoff.md) ·
[document model](references/document-model.md) ·
[agent roles](references/agent-roles.md) ·
[glossary](references/glossary.md)

## Purpose

Documentation overhead grows when changes are recorded as new files instead of
edits, when the same fact lives in several places, and when status drifts
between documents. This workflow is the maintenance counterpart to the
[document model](references/document-model.md): it finds those problems,
restructures existing documents into the model, and applies changes so that
every fact keeps exactly one home.

It changes the *form* and *currency* of documents, never their agreed meaning.
Changes in meaning are decided by the user and applied here (amend) or by the
owning workflow.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **audit** (default) | "Are the docs consistent?", "Where are we?" | Nothing | Drift report and project status overview in chat |
| **migrate** | Move a project's existing docs into the document model | `patompong-docs/` restructured after approval | Migrated layout, merged change notes, obsolete files listed for removal |
| **amend** | Apply an approved change to accepted content | Owning files, `log.md`, dependents' `state.json` | Amended owners, dependents marked stale |
| **compact** | Logs and tables have grown large | `log.md`, Changes tables, superseded sections | Condensed records with open items intact |

Shared contract changes are applied through
[contract-and-test](contract-and-test.md) change-request mode; amend handles
all other owning files.

## Inputs

- The target project's `patompong-docs/`, or its legacy documentation for
  migrate.
- For drift against code: the relevant source, read through researchers.
- For amend: the approved change and the IDs it affects.

## Outputs

Audit writes nothing. Other modes write only inside `patompong-docs/`, and only
after the user approves the proposed change set. Documentation outside
`patompong-docs/` stays read-only.

## Roles and models

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| Reconciler | opus | Writes per mode | Main session: analysis, change set, edits |
| Researcher | sonnet | Read-only | Compares documented interfaces and paths with code |
| Design reviewer | opus | Read-only | Migrate only: checks that no agreed meaning was lost or altered |

Confirm models once at the start of the run per
[agent roles](references/agent-roles.md#model-selection).

## Procedure

1. **Inventory.** List the documents in scope with their status headers,
   `Basis` lines and IDs, and every file that falls outside the document model
   (change notes, addenda, `*-v2`, duplicated specs). *Exit:* inventory.

2. **Detect drift.** Check, in order of cost:
   - **Staleness:** a `Basis` that references upstream content changed since.
   - **Integrity:** dangling or duplicate IDs, broken links, missing headers.
   - **Duplication:** the same requirement, clause or decision stated in more
     than one file, especially with different wording.
   - **Status conflicts:** `state.json`, plan checkboxes and headers disagree.
   - **Code drift** (optional, via researchers): contract interfaces, file maps
     and commands that no longer match the code.

   *Exit:* findings, each with its owning file and owning workflow.

3. **Report** *(audit ends here)*. Group findings by severity: blocks a stage
   (stale inputs, contradictions), misleads (duplicates, wrong status), or
   untidy (broken links, size). For each, propose the action and who performs
   it. Add a status overview per feature from `state.json`: artifact states,
   task progress, verified criteria, stale items.

4. **Propose the change set** *(migrate, amend, compact)*. List every file to
   create, edit, merge or remove, using the
   [legacy mapping](references/document-model.md#legacy-layout-mapping) for
   migrate. Mark where content would be merged and which version wins; any
   conflict in *meaning* is a question for the user, not a reconciler choice.
   *Exit:* user-approved change set.

5. **Apply.**
   - **Migrate:** move content into its owning files, preserving IDs, wording
     of agreed criteria, and acceptance status. Fold change notes into the
     owners and record the folding in `log.md`. Convert progress/QA records to
     `log.md` and `state.json`. Leave obsolete files in place and list them for
     removal; delete only with explicit approval, and only files tracked by git
     or otherwise backed up.
   - **Amend:** follow the [amendment steps](references/document-model.md#amendments).
   - **Compact:** condense `log.md` entries for completed, accepted phases into
     a dated summary block; keep open items, unresolved findings and every CR
     verbatim. Trim Changes tables to the last ten entries. Remove superseded
     sections whose replacement is linked and nothing references them.

   *Exit:* change set applied.

6. **Verify.** Re-run the integrity and duplication checks on the result. For
   migrate, dispatch a design reviewer to compare old and new content for lost
   or altered meaning. Report what changed, what remains, and any dependents now
   stale. *Exit:* clean integrity check and reviewer verdict.

## Gates

- **Entry:** scope known; for amend, an approved change.
- **Exit:** no agreed meaning altered; IDs preserved; every fact has one home;
  dependents of changed content marked stale.

## Boundaries

- Never changes the meaning of requirements, criteria, contract clauses,
  decisions or protected tests. Rewording for structure keeps agreed criteria
  verbatim.
- Accepted status carries over only for unchanged content; merged or reworded
  content returns to draft for the user to re-accept.
- No file deletion without explicit approval of the specific files.

## Done when

The requested mode's output exists: an audit report, or an applied and verified
change set with the remaining work and stale dependents listed.

## Example invocations

- "Use workflow doc-reconcile to audit the docs and give me a status overview."
- "Use workflow doc-reconcile, migrate this project's docs into the new layout."
- "Use workflow doc-reconcile, amend: REQ-IMP-03 timeout changes from 30s to 60s
  (approved)."
- "Use workflow doc-reconcile, compact batch-import's log."
