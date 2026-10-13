# Patompong portable setup: historical proposal

Applied after Q4 and Q5 were confirmed. See APPLIED.md and VALIDATION.md.
The remaining-choice section below is retained as proposal history.

## Confirmed by the user

- Downloaded collections use `.agents/skills/<author>/<skill>/SKILL.md`.
- Matt skills use `.agents/skills/mattpocock/<skill>/SKILL.md`.
- Ask for a workflow at the start of each new session; retain it through that
  session unless the user changes it. A workflow named in the opening request
  counts as the selection; do not ask for the same selection again.
- Keep session startup small: preferences, session routing, and a small workflow
  menu. Do not open the complete catalog or scan skill bodies to offer choices.
- After selection, read the chosen workflow and skills it directs the agent to.
  Skills can follow relevant skill dependencies and supporting references
  themselves; there is no closed workflow whitelist and no extra approval for
  following an ordinary dependency.
- A detailed overall CATALOG.md provides names, purposes, use cases, paths,
  dependencies, overlap, compatibility, source/attribution, and examples.
  Read it when the user asks to browse/select skills or inspect the skill tree.
- Preserve existing personal skills and third-party licenses/resources.

## Prepared download

38 unchanged skill folders are staged under `prepared/.agents/skills/mattpocock/`.
Every bundled file was copied and SHA-256 compared with the downloaded archive.
See source-verification.json. A detailed catalog draft is in
`prepared/.agents/CATALOG.md`. Neither draft activation nor runtime setup has
been applied to the active toolkit.

## Proposed implementation

1. Keep current personal skill paths; place outside collections in author folders.
2. Set explicit-only policy on toolkit skills using agents/openai.yaml and
   document this as a local adaptation. Host discovery of names/metadata and
   agent reading of full instructions are different; loading behavior needs a
   fresh-session check rather than an absolute no-reading guarantee.
3. Add a portable session routing rule and update root activation, STARTUP.md,
   preferences, and README together. Scope rules cannot override system rules.
4. Provide editable workflow files with goal, ordered steps, skill entry paths,
   deliverables, completion criteria, and relevant project prerequisites.
   A workflow selects entry points; dependency navigation remains skill-driven.
5. Support a session choice of a lone skill as well as a composed workflow.
   Resolve a supplied author/name directly; consult the catalog only when the
   user requests discovery help. Change workflow only at the user's request.
6. Adapt unsupported Skill-tool wording to path-based dependency lookup; retain
   the pristine archive and record local changes. Check bundled relative links.
7. Extend the existing validator for author groups, catalog matching, policy,
   and workflow entry paths; verify preservation, resources, and portable copying.

## Still to settle in the interview

- Initial named workflows: template only, or a small approved example set?
- Host-specific skills: preserve and label Claude/Bash/tool prerequisites, or
  also prepare specific Codex replacements? Downloaded files alone cannot provide
  Claude-only hooks, credentials, external services, or each project's runtime.

## Completion evidence

Final setup must distinguish downloaded, installed/adapted, statically checked,
and runtime-tested. No third-party script is run solely because it was downloaded.
Session-wide workflow behavior will need a fresh-session acceptance check.
