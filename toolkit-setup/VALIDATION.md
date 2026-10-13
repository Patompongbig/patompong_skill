# Setup validation: 2026-10-11

## Observed results

- 41 local skills: 38 author-grouped Matt skills and three preserved personal skills.
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
- Historical catalog/source-integrity checks passed; Ponytail remains review-only.
- A toolkit-local .gitattributes pins text to LF to preserve resource hashes when
  this folder is committed and checked out on Windows or Linux.

Commands run from this setup checkout:

```sh
python -B .agents/scripts/validate.py --project-root .
python -B toolkit-setup/check_setup.py
python -B skill-selection/review_tools/validate_catalog.py
```

## Acceptance checks still needing a fresh host session

Native author-group discovery, selector labels, explicit invocation, the actual
once-per-session question, and skill quality are not runtime-proven here. The
workflow/menu and direct paths provide the portable invocation route. Verify in a
fresh session: one workflow question before skill-body/catalog reading; select
interview; permit grill-me to follow grilling; continue without a new workflow
question; explicitly request the catalog to browse skills.

Claude-only hooks/background agents, each project's tests/GPU/runtime, external
tracker accounts, Bash wizard operation, and optional package integrations were
not installed or runtime-tested. See COMPATIBILITY.md for their requirements.
