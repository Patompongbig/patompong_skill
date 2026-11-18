---
name: market-research
description: "Stage 2: turn a confirmed product intent into the cited \"02 — Market Research\" document (competitive landscape, build vs buy, market gaps, recommendation). Use after Stage 1 intent for new products or features; not for bugfix, refactor, infra or security-patch work, or single-fact lookups."
---

# Market research (Stage 2)

Turn a confirmed **intent** into the document **"02 — Market Research"**: the
evidence for whether to build, buy or partner, and why.

**Input:** the Stage 1 intent (problem, target users, region, project type),
from the conversation or the project's intent document. Ask for any missing
field before starting.

**Skip gate:** when the project type is bugfix, refactor, infra or
security-patch, write "Stage 2 skipped: <type>", emit the Carry-Forward with
that line, and stop.

## Steps

1. **Scope.** Pick a topic slug and fix the region and the decision this
   research serves. Done when the assumptions fit one line:
   `type=market, region=<region>, decision=<build/buy/partner for what>`.

2. **Research with deep-research.** Read
   `.agents/skills/samber/deep-research/SKILL.md` and run it with these overrides:
   - **Depth:** its Step 1 auto-scoped from the assumptions line (no interview),
     then Steps 2, 5 and 6. Skip Steps 3, 4 and 7.
   - **Step 2 axes**, one sub-agent each:
     1. *Local landscape*: players in the region, positioning, pricing,
        strengths and weaknesses.
     2. *Global benchmarks*: leading solutions and practices elsewhere.
     3. *Build vs buy*: products, vendors, APIs and open source to adopt;
        partnership feasibility, integration effort, lock-in.
     4. *Economics*: pricing models, cost to build and run versus license cost,
        willingness to pay.
     5. Optional: one axis the intent specifically needs.
   - **Paths:** report `patompong-docs/docs/research/market-<slug>.md`; notes
     in `patompong-docs/docs/research/market-<slug>/`.
   - **Report body:** the [document template](#document-template) below.

   Done when the report writer has saved the report.

   **Fallback**, when sub-agents are unavailable: research the same four axes
   yourself with web search, one after another, under the same quality bar, and
   write the same document. With no web access at all, stop and tell the user.

3. **Validate** against the [quality bar](#quality-bar). Done when every item
   passes or each failing item is recorded under Gaps.

4. **Present** the document for approval and edit it in place on feedback.
   Then emit the [Carry-Forward](#carry-forward-stage-12).

## Document template

Title `02 — Market Research`; one header line with date, assumptions and method
(deep-research or web-search fallback).

- **Competitive Landscape**: local and global players, with a comparison table
  (player, segment, differentiator, pricing, strengths, weaknesses).
- **Build vs Buy**: each path (build, buy or license, partner, adopt open
  source) with pros, cons, cost signals and lock-in.
- **Market Gaps**: underserved segments, missing features, pricing or regional
  whitespace.
- **Recommendation**: the direction, its rationale, and confidence
  (High, Medium or Low).
- **Gaps**: what could not be found or confirmed.
- **Sources**: numbered, cited inline as `[n]`.

## Quality bar

- Every claim cites a source; numbers (size, price, share) have two
  independent sources or carry confidence Low.
- Competitive Landscape and Build vs Buy are both present and evidence-backed.
- Conflicting sources are named side by side.
- Thin evidence becomes a Gaps entry and the stage proceeds with what exists.

## Carry-Forward (Stage 1.2)

End the stage with this block, the hand-off to the next stage:

```markdown
### Carry-Forward (Stage 1.2)
- Intent: <one line>
- Recommendation: <direction> (confidence: <High|Medium|Low>)
- Key findings: <up to three, each with source [n]>
- Build vs buy: <chosen path, or open with the deciding question>
- Gaps and open questions: <list, or none>
- Document: <path>
```

Example: `Use skill patompong/market-research for the intent above: a Thai SME
invoicing app.`

Complete when the approved document passes the quality bar, or its failures are
listed under Gaps, and the Carry-Forward is emitted.
