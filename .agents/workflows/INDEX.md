# Workflow menu

Select one with "Use workflow <name>". It stays selected until the user switches
or says "return to normal mode".

| Workflow | Purpose | File |
| --- | --- | --- |
| software-requirement | System SRS, roadmap decomposition into phases/features, and engineering standards | [software-requirement.md](software-requirement.md) |
| contract-and-test | Deepen a feature into contract, acceptance criteria and Red tests; owns shared contracts | [contract-and-test.md](contract-and-test.md) |
| development-plan | Ordered, verifiable implementation plan from an accepted contract | [development-plan.md](development-plan.md) |
| execute | Implement an accepted plan task by task, each verified by an independent QA agent | [execute.md](execute.md) |
| qa-verify | Independently verify a change against spec and engineering standards; verdict only | [qa-verify.md](qa-verify.md) |
| doc-reconcile | Audit doc drift and status, migrate legacy docs, apply amendments, compact history | [doc-reconcile.md](doc-reconcile.md) |
| feature-explain | On-demand explanation or snapshot guide of how a feature is implemented | [feature-explain.md](feature-explain.md) |
| interview | Reach a confirmed shared understanding through structured question rounds | [interview.md](interview.md) |
| ask-answer | Read-only investigation and explanation; chat only | [ask-answer.md](ask-answer.md) |
| lone-skill | Use one named skill and the dependencies it needs | [lone-skill.md](lone-skill.md) |

## How the development workflows fit

```text
software-requirement            SRS: what the system is and must do (main guideline)
  └─ decompose                  roadmap: phases → features, REQ coverage
       └─ per feature:
          contract-and-test     contract + acceptance criteria + Red tests
          development-plan      ordered, verifiable tasks
          execute ⇄ qa-verify   task → Green → independent QA → stage → next
          feature gate          full acceptance + parallel spec/standards review
       └─ release (qa-verify)   per phase: all features together, REQ coverage, exit

doc-reconcile    any time: audit drift, migrate legacy docs, amend, compact
feature-explain  on demand: how a feature is actually implemented
interview        combine with any writing stage for structured clarification
ask-answer       read-only, never combined with writing
```

Each stage stops for the user's confirmation; accepting one does not start the
next. Shared rules are in [references/](references/): development handoff,
document model (project layout under `patompong-docs/`), agent roles and models,
engineering standards, glossary.

## Common prompts

- New system: "Combine software-requirement with interview to create the SRS",
  then "software-requirement, standards: take guidance from <projects>", then
  "software-requirement, decompose".
- Per feature: "contract-and-test for FEAT-04" → "development-plan for
  batch-import" → "execute for batch-import". Add "chain" to let a passing
  design review accept the plan and continue without stopping; you still
  accept the contract and the finished feature.
- Requirement changed: "software-requirement, update: <change>"; affected
  features are marked stale.
- Shared contract must change: approve the CR, then "contract-and-test,
  change-request: apply CR-02".
- Docs inconsistent or bloated: "doc-reconcile, audit", then amend or compact.
  Legacy layout: "doc-reconcile, migrate".
- Resume or status: "execute, resume batch-import" · "execute, status".
- Review any change: "qa-verify on <diff> against <contract>".
- Close a roadmap phase: "qa-verify, release PH-2".
- Refactor: small → normal mode, then "qa-verify on my changes, run tests";
  large → "development-plan, refactor <area>" → "execute". The outside-in suite
  must stay green; unit tests may be rewritten or deleted with coverage kept.
- Models: stated in the prompt skip the per-run question, e.g. "implementer
  sonnet, QA opus, high effort".

Workflows never commit. During execute, QA-passed tasks are staged: `git diff`
is unreviewed work, `git diff --staged` is accepted work.
