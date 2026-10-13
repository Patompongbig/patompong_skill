# Software-requirement-creation workflow

Purpose: create, edit, update, or review software requirements and related system
context so the user and future agents understand the agreed scope, current state,
and intended development. Support sustainable growth through relevant constraints
and extension needs. This produces requirements, not an implementation plan.

Read [shared development handoff](references/development-handoff.md) for feature
identity, artifact ownership, acceptance, reconciliation and stage transitions.

## Inputs and scope

Use the target project, requested operation, feature or subsystem, user intention,
and existing project guidance. Infer information already clear in the prompt;
clarify consequential gaps. Creating this workflow does not execute or select it.

- For an existing project, compare relevant code, documents, and available evidence.
  For a new project, capture intentions and constraints without inventing a current
  implementation or demanding nonexistent code.
- Review means findings and proposed revisions in chat unless document edits are
  also requested. Review-only is read-only and chat-only, including glossary/ADR
  proposals. Create/edit/update assignments authorize documentation work
  within the agreed scope after the requirements confirmation below.
- Do not implement features, change runtime code or configuration, install tools,
  create implementation tickets, or run tests/builds merely to establish scope.
  Use existing runtime evidence when available; identify what remains unverified.
- Store all documents created or updated by this workflow under the target
  project's `patompong-docs/` directory, outside the portable `.agents` toolkit.
  Treat existing documents elsewhere as reference sources; do not move, edit,
  replace, or duplicate them wholesale. Describe conflicts and link to those
  sources, preserving their ownership. Changes outside this directory require
  a separate explicit assignment.

## Organized project outputs

Paths are relative to the target project root, not the toolkit checkout:

- `patompong-docs/docs/requirements/<feature>.md`: requirements and scope.
- `patompong-docs/docs/system/<feature>.md`: relevant system context and flows.
- `patompong-docs/docs/GLOSSARY.md`: project domain terms maintained here.
- `patompong-docs/docs/adr/NNNN-<decision>.md`: justified decision records.
- `patompong-docs/docs/research/<topic>.md`: optional approved research findings.
- `patompong-docs/implement-plan/<feature>/`: development-plan output owned by
  the separately selected planning workflow; this workflow does not create plans.

Create only the files needed for the assigned scope. Reuse matching files inside
this directory when updating; preserve existing identifiers and links. For multiple
contexts, keep their glossaries and glossary map inside `patompong-docs/docs/`.
Read relevant external glossaries/maps as sources without modifying them. Explicitly
label proposed or accepted Patompong requirements; their presence does not silently
supersede another project's authoritative documents. Identify the governing source
and any unresolved conflict for future agents.

## Steps

1. **Bound the session before broad reading.** Read project guidance and a small
   document/file index to identify the relevant area. State the operation, feature,
   intended outcome, connected features/flows, and exclusions. If the request spans
   too much of the project, or investigating it would gather substantial unrelated
   context, ask the user to choose a smaller feature, subsystem, or end-to-end flow
   for this session. Offer concrete slices and a recommendation; wait for their
   choice before broad exploration. This also applies to explicitly whole-project
   requests when their scope is too large for a focused session.

2. **Establish relevant current state.** Read only the documents and code needed
   for the chosen scope, tracing affected producers, consumers, interfaces, data
   ownership, user journeys, and failure/recovery flows. Include related features
   when their dependency or interaction matters. State why a boundary needs
   expanding; ask before a substantial expansion and defer unrelated work.
   Distinguish implemented behavior supported by code, documented but unverified
   behavior, available runtime evidence, future intentions, and open questions.
   Surface contradictions rather than treating existing code as the desired spec
   or treating documents as proof of implementation. Name inspection coverage.

3. **Resolve terms and requirements.** Read
   [domain-modeling](../skills/mattpocock/domain-modeling/SKILL.md) and follow its
   relevant glossary/ADR references. Use existing maps as reference sources; write
   only to the organized output paths above, overriding its root glossary/ADR
   defaults. Challenge ambiguous terms, compare definitions with code, and discuss
   concrete scenarios where they affect requirements. Keep terminology separate
   from requirements and implementation details. Capture agreed definitions in
   the discussion, then persist them with the confirmed documentation update in
   step 6; this workflow defers the skill's immediate glossary writes to that
   checkpoint. In review-only mode, propose glossary changes without applying them.
   Offer ADRs only for significant agreed trade-offs that meet the skill's criteria.
   Do not manufacture architecture decisions to fill a document.

   Ask focused questions necessary for the requirement; do not invoke `grill-me`
   or `grilling`. The user may explicitly combine this with the interview workflow
   for a deeper interview. Its confirmation settles the discussion; then perform
   the already-assigned documentation work within this workflow's boundaries.

4. **Offer research when needed.** If a technical uncertainty requires dedicated
   investigation, ask whether the user wants to use
   [research](../skills/mattpocock/research/SKILL.md), describing the question,
   expected output, and relevant tool/delegation prerequisites. Do not load or
   execute that skill until the user selects it. Route its findings to the research
   output above rather than another project location. Their answer applies to the agreed
   research scope; ask again only for a materially different scope. Continue
   independent requirements work while awaiting the answer. If declined or
   unavailable, record the uncertainty rather than inventing a conclusion. An
   unanswered offer is not approval. Mandatory host source-verification rules
   still apply; they do not automatically select this optional skill.

5. **Draft and review the specification.** Read existing requirements as sources,
   reuse matching files inside `patompong-docs/`, and identify which documents own
   which facts. Scale content to the
   feature rather than imposing a large template. Include where relevant:
   - Goals, users, scope, exclusions, and current-state gaps.
   - Functional behavior, connected feature interactions, data/interface contracts,
     and normal, error, cancellation, and recovery flows.
   - Quality requirements, compatibility, security/privacy, performance, deployment,
     maintenance, and other actual constraints, with measurable criteria where
     meaningful. Label proposed targets instead of inventing agreed metrics.
   - Priorities, acceptance criteria, assumptions, and unresolved decisions.
   - Foreseeable extension needs and limits that matter to this feature. Separate
     committed scope, future possibilities, and deferred work; avoid speculative
     infrastructure or treating possible growth as authorization to build it.

   Provide stable requirement identifiers when they help references and updates;
   preserve existing identifiers. Link requirement claims to relevant documents,
   code locations, or source evidence without reproducing unrelated project code.
   Review for contradictions, missing flows, unclear ownership, unverifiable
   acceptance criteria, and effects on connected features. Report concrete gaps.
   Do not turn this into implementation tasks, file-by-file coding instructions,
   ticket breakdowns, execution sequences, or estimates.

6. **Confirm and maintain the agreed documents.** Present the concrete proposed
   scope, requirements changes, remaining decisions, and files to create/update.
   Wait for user confirmation before applying the documentation changes unless
   the user has already confirmed that exact content and scope. Keep review-only
   work in chat. For create/edit/update work, revise the relevant requirements and
   glossary plus justified system-context documents, such as scope, architecture
   overview, flow descriptions, boundary requirements, or ADRs. Link detailed
   protocols and executable specifications owned by test-and-contract-creation
   rather than editing those accepted artifacts here. Create new files only for a
   clear purpose. Maintain cross-links and distinguish proposed from accepted
   decisions. Preserve unrelated content and reconcile obsolete statements rather
   than accumulating contradictory specifications. Agent instruction/configuration
   changes require explicit assignment; documenting scope does not authorize them.

7. **Verify the documentation result.** Check changed documents for consistent
   terms, requirement status, scope, links, identifiers, acceptance criteria, and
   alignment with the inspected evidence and confirmed intention. Report the
   changes, coverage, deferred areas, unresolved decisions, and verification
   limits. Identify dependent contracts/tests/plans needing reconciliation after
   changed requirements; do not silently carry their old acceptance forward.
   Documentation checks are not runtime or implementation proof.

## Deliverables and completion

For review: findings, proposed corrections, and coverage/uncertainty in chat.
For create/edit/update: the agreed specification and relevant system-context
files under the target project's `patompong-docs/docs/`; glossary and ADRs
only as justified. Do not create an implementation plan.

Complete when the agreed session scope is covered, the requirements and related
context are understandable to the user and a future agent, requested document
changes exist and are checked, and unknowns/deferred areas are explicit. A draft
with unresolved decisions is labeled as such rather than called implementation-ready.
No tracker, service account, or mandatory research is required.

## Example invocations

"Use workflow software-requirement-creation. Update requirements for batch import
using current code and my intended cancellation behavior. Include related result
and recovery flows; keep this to requirements and supporting system documents."

"Use workflow software-requirement-creation to review export requirements against
current project evidence. Report gaps only; do not edit documents."

"Combine software-requirement-creation with interview to clarify the scope of a
new project before creating its requirements."
