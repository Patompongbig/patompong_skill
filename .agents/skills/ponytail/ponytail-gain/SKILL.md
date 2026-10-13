---
name: ponytail-gain
description: "Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, \"what does ponytail save\", \"ponytail impact\"."

---

## Portable invocation

Use this skill only after the user selects it directly or through the session's
chosen workflow. Keep the toolkit's session routing and agreed scope. This copy
does not install plugin hooks, write global mode flags, or activate at startup.
Native slash/plugin commands below are upstream aliases: for this toolkit, read
the corresponding `.agents/skills/ponytail/<skill>/SKILL.md` directly, only when
requested or needed by the selected workflow. Preserve requested explanation
depth and project verification requirements. Use `rg` or a native equivalent
for upstream grep/Bash search examples on Windows.

# Ponytail Gain

Display this scoreboard when invoked. One-shot: do NOT change mode, write flag
files, or persist anything.

The figures are the published agentic benchmark of Ponytail 5: headless Claude
Code (Opus 5.5, default effort) on 39 tasks (feature tickets in a real FastAPI +
React repo, bug fixes, security and privacy cases, small apps), 5 runs each,
against the same agent without the skill. 18 of the tasks have hidden checks
for correctness and safety. Each figure is the geometric mean of the per-task
medians. They are measured, not computed from the current repo.
Source: [bundled benchmark report](benchmark-report.txt) and [upstream README snapshot](upstream-readme.txt). These are author-reported Claude Code results, not independently reproduced here or measured in this Codex session.

## Scoreboard

Render plain ASCII bars. The bar length shows ponytail as a share of the
no-skill baseline; the label carries the exact figure:

```
  ponytail gain           benchmark · 39 tasks × 5 runs · Opus 5.5

  no-skill        ████████████████████  100%
  Lines of code   █████████···········   47%   ▼ 53%
  Output tokens   ███████████·········   55%   ▼ 45%
  Cost            ███████████████·····   74%   ▼ 26%
  Time            ████████████········   59%   ▼ 41%
  Hidden checks passed   97%  (no-skill 96%)
  Tests where the logic needs one   98%  (no-skill 68%)

  This repo:  /ponytail-debt  (shortcuts you deferred)
              /ponytail-audit (what's still cuttable)
```

## Honesty boundary

These are benchmark averages, not this repo. NEVER print a per-repo savings
number ("you saved X lines/tokens here"): the unbuilt version was never
written, so there is no real baseline to subtract from in a live repo. The
only real per-repo figures come from `/ponytail-debt` (a counted ledger), and
this card points there instead of inventing one.

## Boundaries

One-shot display. Edits nothing, changes no mode.
"stop ponytail" or "normal mode": revert.
