# Toolkit backlog

Ideas parked for later review. Not part of the portable `.agents/` folder.

## Open

- **Security and operations depth** (2026-11-18). QA reviews security statically
  through the engineering rubric, but nothing prompts for threat modelling in the
  SRS, and there is no runbook or observability guidance for deployed services.
  Consider: a threat-model subsection in software-requirement's quality
  attributes; an optional operations section (deployment, monitoring, rollback,
  runbook) for projects that run as services. Only worth adding if a project
  needs it.
- **Pilot run** (2026-11-18). The restructured workflows have not been exercised
  end to end. Run one small real feature through software-requirement →
  contract-and-test → development-plan → execute, then fix what the run shows
  (ignored rules, annoying gates, context cost, model prompt behaviour).

## Decided against

- **Retro loop promoting recurring QA findings into rules** (2026-11-18). Skipped
  to keep overhead and context growth down; QA already runs on every task.
- **Separate fast-lane workflow for small changes** (2026-11-18). Normal mode
  covers small fixes.
