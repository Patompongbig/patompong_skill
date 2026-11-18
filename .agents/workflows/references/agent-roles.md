# Agent roles and coordination

How workflows divide work between the main session and subagents, how models
are chosen, and the formats agents use to hand work to each other. Terms are
defined in the [glossary](glossary.md).

## Coordination levels

Use the lightest level that fits. Each step up costs tokens and review attention.

| Level | Shape | Use when |
| --- | --- | --- |
| **Single session** (default) | Main session does the stage's work; spawns read-only subagents for research and independent review | Almost all work |
| **Orchestrator** (opt-in) | Main session plans, dispatches one implementer subagent per task, integrates, and runs QA; it writes little code itself | Plan has roughly 4+ dependency-ready tasks with disjoint file sets, and the user selects it |

Agent teams, background/cloud agents and parallel worktrees are not used unless
the user explicitly assigns them. If the host cannot delegate, run the role
serially in the main session, as a distinct pass, and label the result
`self-review (no independent context)`.

## Roles

| Role | Default model | Access | Responsibility |
| --- | --- | --- | --- |
| **Researcher** | sonnet | Read-only | Wide reading of code, docs, logs or reference codebases; returns a condensed answer with paths |
| **Author** | opus | Writes the stage's owned files | Requirements, contracts, tests and plans; usually the main session |
| **Design reviewer** | opus | Read-only | Fresh-context check of a draft artifact against its upstream sources before user review |
| **Implementer** | sonnet | Writes code within task scope | Implements one task to Green against the plan, contract and engineering standards |
| **QA verifier** | opus | Read-only; may run checks | Independently re-runs checks and reviews the task diff; returns a verdict |
| **Explainer** | sonnet | Writes `guide/` only | Produces on-demand implementation explanations |

Roles keep their boundaries: an implementer does not reinterpret requirements, a
reviewer does not rewrite code, a researcher does not decide.

## Model selection

At the **start of each workflow run**, ask once, in a single prompt, which model
each role used by that run should take. Offer, per role:

`Default (<role default>) · haiku · sonnet · opus · fable`

- Each name means the newest model of that family available on the host.
- Translate names to the current host's model names using the
  [compatibility table](../../COMPATIBILITY.md#agent-roles-and-model-selection).
- Reasoning effort is **medium** unless the user specifies otherwise.
- Choices persist for the rest of the run and across follow-ups until changed.
- Skip the prompt when the invocation already states the models.
- Chat-only workflows (ask-answer, interview, lone-skill) and feature-explain's
  explain mode skip the prompt and use defaults unless the user names models.
- The main session cannot change its own model. If the user picks a different
  model for a main-session role, say so and suggest switching the session model;
  continue with the current one if they prefer.
- If the host cannot set a subagent's model, report that once and use the
  session model.

## Writing a brief

Subagents do not inherit the conversation. Every brief states:

1. **Objective** — the single question to answer or task to complete.
2. **Scope** — exact paths, IDs or diff range; what is out of scope.
3. **Inputs** — links to owning files; quote only the clauses that matter.
4. **Constraints** — access rights, protected artifacts, standards to apply.
5. **Output format** — one of the formats below.
6. **Stop condition** — when to return, including when blocked.

Keep briefs self-sufficient but short. Pass references, not pasted documents.

## Return formats

**Researcher.**

```text
ANSWER: 5–10 lines.
EVIDENCE: path:line — what it shows (one per line).
OPEN: unresolved questions or unread areas.
```

**Design reviewer and QA verifier.**

```text
VERDICT: PASS | PASS_WITH_NOTES | FAIL
CHECKS: command — result (only for QA; re-run by the verifier, not copied).
FINDINGS (max 5, BLOCKER/MAJOR only, most severe first):
  [BLOCKER] path:line — defect. Violates: AC-03 / C-02 / engineering.md §Errors.
            Evidence: reproduced | static. Fix direction: one or two lines.
NOTES (optional, max 3, MINOR): one line each.
```

`FAIL` requires at least one BLOCKER, or a MAJOR the verifier judges must be
fixed before the task can be built upon. Findings cite the violated clause; a
reviewer cannot introduce new requirements.

## Task packet

What the implementer hands to QA for one task:

```text
TASK: T-04 — <title>. Implements: AC-02, AC-05. Basis: contract.md, plan.md#T-04.
SCOPE: files changed (unstaged diff = this task only).
CHECKS RUN: command — result.
CLAIMS: behaviors now satisfied; known limits; deviations from plan with reason.
```

## Build–verify loop

1. Implementer completes a task and sends the task packet.
2. QA verifier runs in fresh context, re-runs checks, reviews the diff against
   contract, plan and engineering standards, and inspects connected callers
   outside the diff.
3. `PASS` / `PASS_WITH_NOTES` → the task's files are staged (checkpoint), the
   log and `state.json` are updated, the next task starts.
4. `FAIL` → the implementer verifies each finding before acting, fixes confirmed
   ones, may dispute a finding with evidence, and sends a new packet.
5. **Maximum three QA rounds per task.** After the third `FAIL`, or on a dispute
   neither side can settle with evidence, escalate to the user.

Trivial tasks (documentation, configuration, renames) may be batched into the
next task's QA round.

## Feature gate

After all tasks of a feature: run the full acceptance flow and required
quality checks, then dispatch two QA verifiers in parallel — one for spec and
contract conformance, one for engineering standards — over the whole feature
diff. Same verdict format, same loop rules.
