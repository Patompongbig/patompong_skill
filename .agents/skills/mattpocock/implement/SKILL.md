---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

## Portable invocation

This toolkit uses explicit session workflow or lone-skill selection. After this
skill is selected, follow its relevant skill dependencies and references as
needed. Named Matt dependencies resolve directly to
`.agents/skills/mattpocock/<name>/SKILL.md` from the target project root; supporting
links resolve from this skill folder. Read each needed file once rather than
loading the collection. A host-specific "Skill tool" instruction means this
file-based lookup in Codex, including instructions inside generated prompts.
If a tool, path convention, or host assumption differs, consult the relevant part
of [portable compatibility](../../../COMPATIBILITY.md). Session scope and the
user's instructions govern any upstream invocation restrictions.

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Read `.agents/skills/mattpocock/tdd/SKILL.md` where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, Read `.agents/skills/mattpocock/code-review/SKILL.md` to review the work.

Commit your work to the current branch.
