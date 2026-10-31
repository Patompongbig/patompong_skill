# Setup validation: 2026-10-11

## Bounded updates and code-grounded explanations: 2026-10-31

Execution now permits small, evidenced factual documentation updates and verified
plan checkboxes while preserving governing requirements, acceptance criteria and
accepted decisions. Progress/QA remain the primary records. Static scenario review
covered verified task completion, a stale source link, an implementation failing
an agreed criterion, an absent implementation during planning, and guide navigation
between use cases, files and symbols. Code explains current behavior; requirements
remain the criteria against which that behavior is judged. No target-project guide
or execution session was run, so these are instruction checks only.

Observed: `git diff --check` passed. The toolkit validator reported the same 23
previously identified imported-resource hash mismatches and no other errors.
Full static validation remains unsuccessful because of those existing mismatches.

## Feature-and-architect workflow checks: 2026-10-31

Added an eighth menu workflow, with no new skill or imported-resource changes.
Static scenario review covered standalone reconstruction from existing code,
planning-only proposed interfaces, explicitly combined execution with incremental
guide updates, review-only chat findings, missing plans/runtime evidence, changed
or deleted symbols, preservation of owner notes, partial large-plan coverage, and
switching away without implicit guide maintenance. These are instruction checks,
not observed agent execution or a generated target-project guide.

Observed: `git diff --check` passed. The toolkit validator's before/after output
was identical: the same 23 pre-existing imported-resource hash mismatches and no
additional errors. Current menu coverage, local links and workflow paths introduced
no reported failures. Full static validation remains unsuccessful because of those
existing mismatches. Live documentation quality, source-trace accuracy and combined
planning/execution behavior remain acceptance checks in a target project.

## Execution boundaries and retired default workflow: 2026-10-31

Static review checked minimal implementation scope, protected governing documents
and agent instructions, progress/QA ownership of task status and change reports,
and inheritance of these boundaries by skills, helpers and reviewers. Shared
handoff, README and usage guidance were synchronized without changing other stages'
ownership. No new QA workflow or skill was added.

No active workflow depends on the retired `workflows/default.md`. The optional
guide explicitly identifies it as retired; stale wording in the catalog and import
guidance now refers to normal Codex behavior. Historical setup scripts and snapshots
still describe the old installation and were preserved, not run.

Observed: `git diff --check` passed. Before and after the edits,
`python3 -B .agents/scripts/validate.py --project-root .` reported the same 23
imported-resource hash mismatches documented below, with no additional errors.
Full static validation therefore remains unsuccessful. Instruction compliance in
a real execution session remains a runtime acceptance check.

## Normal Codex default checks: 2026-10-26

Normal Codex is now the default; the former default workflow is an optional
WORKFLOW-GUIDE.md. Static review covered ordinary tasks without toolkit routing,
explicit workflow selection, persistence, and returning to normal mode. Historical
setup scripts/snapshots describe older installations and were not reapplied.

Observed checks: `git diff --check` passed. An isolated relocated copy produced
the same validator result as the live toolkit. Negative cases detected a missing
guide and an unlisted default.md workflow. Activation preserved existing project
guidance and was byte-idempotent on a repeated call.

Full validation remains unsuccessful because of 23 pre-existing imported-resource
hash mismatches. The affected files match committed HEAD. Restoring the previous
tracked toolkit files in a temporary copy reproduced exactly the same 23 errors;
these changes introduced no additional validator failures. The deliberately
edited Superpowers router has a refreshed installed hash and retained upstream
hash. Fresh-host startup and selection behavior still need runtime acceptance.

## Observed results

- 47 local skills: 38 Matt skills, six Ponytail skills, and three preserved personal skills.
- All local manifests have explicit-only invocation policy; existing UI metadata retained.
- All 103 upstream Matt resources accounted for against the pinned archive.
- Bundled shell/config templates are byte-identical to upstream and were inspected
  statically; none was executed as part of installation.
- Catalog/manifest state, grouped names, local links, dependency entry paths,
  workflow entry paths, licenses, and imported-file hashes passed validation.
- Copying the complete toolkit to a different temporary project passed validation.
- Activation preserved existing project instructions, was byte-idempotent on
  repeat, and refused a conflicting root override.
- The validator rejected missing resources/manifests, broken workflow paths and
  Markdown links, accidental implicit invocation, and unrecorded imported edits.
- Historical catalog/source-integrity checks passed; The historical review remains preserved; all six Ponytail skills are now installed.
- A toolkit-local .gitattributes pins text to LF to preserve resource hashes when
  this folder is committed and checked out on Windows or Linux.

Commands run from this setup checkout:

```sh
python -B .agents/scripts/validate.py --project-root .
python -B toolkit-setup/check_setup.py
python -B skill-selection/review_tools/validate_catalog.py
```

## Acceptance checks still needing a fresh host session

Native author-group discovery, selector labels, explicit invocation, normal-mode
startup, and skill quality are not runtime-proven here. The workflow/menu and
direct paths provide the portable invocation route. Verify in a fresh session:
an ordinary task proceeds without a selection question or toolkit-body reading;
explicitly select interview; permit grill-me to follow grilling; continue without
a new selection question; return to normal Codex and verify interview restrictions
stop applying; explicitly request the catalog to browse skills. These checks
supersede the historical once-per-session startup question.

Claude-only hooks/background agents, each project's tests/GPU/runtime, external
tracker accounts, Bash wizard operation, and optional package integrations were
not installed or runtime-tested. See COMPATIBILITY.md for their requirements.

## Ponytail installation checks: 2026-10-11

All six pinned main manifests match their reviewed source after normalizing Git
Windows newline conversion. All 47 installed skills passed the toolkit validator,
including explicit-only policy, catalog coverage, local links, license existence,
and recorded resource hashes. The historical review/choices validator also passed.
Copying the complete toolkit to another temporary project passed validation.
The updated v0.3.0 portable ZIP was verified byte-for-byte against this folder,
and its extracted toolkit passed validation. No workflow/menu was edited.
Native host discovery and skill behavior remain fresh-session acceptance checks;
no third-party hook or task-specific runtime was executed for installation.

## Superpowers installation checks: 2026-10-13

The toolkit now contains 62 skills: 38 Matt, six Ponytail, 15 Superpowers and
three original personal skills. All 74 upstream Superpowers per-skill files
are preserved; executable resources are byte-identical to the pinned source.
All 62 manifests, explicit invocation policies, catalog entries, local links,
license references and resource hashes passed static validation. Historical
review integrity/choices checks passed. Copying to another temporary project
passed validation. Negative checks rejected a modified executable and removed
its platform-literal exemption; enabling implicit router invocation was rejected.
All existing workflow files were checked byte-identical during installation.
The updated ZIP was checked against every packaged file and validated after
extraction. No upstream executable, visual companion, hooks or global settings
were run or installed. Host discovery and skill behavior remain runtime checks.


## Development workflow consistency checks: 2026-10-13

The seven available workflows now have matching menu entries. Three entries for
absent historical example workflows were removed rather than recreating them.
The validator checks current menu targets, duplicate names and workflow coverage.

Observed: `python -B .agents/scripts/validate.py --project-root .` passed with 62
skills. An isolated temporary copy also passed, with relative links preserved.
Nine packaging checks covered the live and relocated toolkit, rejection of a
missing listed workflow, duplicate menu selection, wrong existing menu target,
unlisted existing workflow, empty selections, and unlisted new workflow, plus
acceptance of a correctly listed additional custom workflow. All passed; temporary
mutations were confined to the copy. Import inventory/hash checks still passed.

Static scenario review covered a new feature with missing interfaces, direct entry
from existing accepted artifacts, changed requirements invalidating dependent
contracts/tests/plans, read-only reviews, interview plus documentation work,
execution interruption/resume, and unavailable required runtime gates. Shared
handoff rules now describe these transitions and distinguish artifact acceptance
from Red/Green/integration evidence. This is instruction review, not observed
agent execution of those scenarios.

Native discovery, real test-runner integration in a target project, independent QA
delegation and complete feature execution remain fresh-host acceptance checks.
No imported skill body, host settings or target-project implementation was changed.
Historical setup reports and archived packages do not certify this revised version.
