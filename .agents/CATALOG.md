# Skill catalog

Paths are relative to this file. Status must match the manifest filename:
`enabled` uses `SKILL.md`; `disabled` uses `SKILL.md.disabled`. Status alone does
not change discovery. Each folder is named after its unique skill name.

| Name | Purpose | Trigger | Dependencies | Origin / version | Status |
| --- | --- | --- | --- | --- | --- |
| [toolkit-maintain](skills/toolkit-maintain/SKILL.md) | Maintain this toolkit; find and evaluate third-party skills | Find, compare, create, edit, import, disable, remove, or validate toolkit skills | Core: file access; optional validation: Python 3.9+; search/import: network and source access | Original for this toolkit / 0.1.1; no upstream code copied | enabled |
| [diagnose-bug](skills/diagnose-bug/SKILL.md) | Reproduce and trace a reported defect | A reported failure, regression, or incorrect behavior requiring diagnosis | Project runtime and relevant test tools when available | Original for this toolkit / 0.1.0; no upstream code copied | enabled |
| [review-change](skills/review-change/SKILL.md) | Review an existing change for actionable defects | Explicit review of a diff, patch, or proposed change | File/diff access; Git optional; project checks optional | Original for this toolkit / 0.1.0; no upstream code copied | enabled |

New imported rows must link to source and record a pinned revision or release,
license/attribution location, adaptations, overlap, and required integrations.
Use a supporting provenance file when the row would become unwieldy. Initial
skills need no account, service, or globally installed skill package.
