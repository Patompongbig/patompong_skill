---
name: review-change
description: "Review an existing diff, patch, or proposed code change for actionable correctness defects and regressions. Use when review is requested; not ordinary implementation, debugging a reported failure, or unsolicited broad audits."
---

# Review a change

Establish the review scope and intended behavior. Read the changed code plus
relevant callers and project requirements. Identify concrete failure scenarios;
separate demonstrated defects from questions, assumptions, and style preferences.

Review without editing unless edits are separately requested. Use relevant checks
when they clarify a finding; inspect what those checks execute before running
them. Avoid broad refactoring suggestions unrelated to the change.

For each actionable finding, give its location, triggering condition, practical
impact, and evidence or a reproducible check. Order by impact. If none are found,
say so and name meaningful coverage gaps; a clean review is not runtime proof.

Example: `$review-change Review the current diff for regressions without editing files.`

Complete when findings or the absence of findings are reported with scope,
observed validation, and remaining uncertainty.
