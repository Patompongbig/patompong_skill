# interview workflow

> Reach a shared, explicit understanding of an idea, design or change through
> structured rounds of questions before anything is decided or built.

Shared rules: [development handoff](references/development-handoff.md#combining-and-switching-stages)
Read a reference only when a step needs it.

## Purpose

Interviewing turns an underspecified idea into settled decisions. The agent maps
the decisions as a tree, asks every question whose prerequisites are settled in
each round, recommends an answer for each, and finds facts itself instead of
asking for them. It ends only when nothing is left silently assumed and the user
confirms the shared understanding.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **standalone** (default) | Clarify or stress-test an idea | Nothing | Confirmed summary in chat |
| **combined** | Selected together with a writing stage | Through that stage only | Decisions written to their owning files by that stage |

## Inputs

The user's idea and context; the project's code and documents for facts.

## Outputs

Standalone: a confirmed summary in chat — decisions made, rationale, open items.
Combined: the active stage writes each confirmed decision to its owning file
(requirement, contract clause, plan task, ADR), phrased as a precise engineering
statement of intent rather than a transcript of the exchange, with one log entry
per decision.

## Roles and models

Main session. Fact-finding may use read-only researchers (default sonnet). No
model prompt unless the user names models.

## Skills

- [grill-me](../skills/mattpocock/grill-me/SKILL.md), which follows
  [grilling](../skills/mattpocock/grilling/SKILL.md): design tree, rounds of the
  current frontier, a recommended answer per question, facts found by the agent.

## Procedure

1. **Frame.** Restate the topic and the outcome the interview should reach.
2. **Investigate.** Read what the project already establishes, so questions are
   about decisions, not discoverable facts.
3. **Ask in rounds.** Each round asks the full current frontier with
   recommendations; wait for answers; recompute. Downstream questions wait for
   their prerequisites.
4. **Confirm.** Summarise the shared understanding and open items; continue
   until the user confirms.

## Boundaries

Interviewing grants no write permission. Standalone stays in chat. Combined mode
permits only what the active stage already permits.

## Done when

The decision frontier is empty and the user confirms the summary.

## Example invocations

- "Use workflow interview to clarify the import retry design."
- "Combine software-requirement with interview to create the SRS for the sync
  service."
