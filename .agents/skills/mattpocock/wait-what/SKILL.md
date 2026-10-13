---
name: wait-what
description: "Stop. That last message did not land: re-pitch it."
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

Wait, I don't understand where you've got to here. Re-pitch that: give me a little bit of context, talk in ASD-STE100 Simplified Technical English, and use the ubiquitous language from `GLOSSARY.md` (follow `GLOSSARY-MAP.md` to the right one if the repo has more than one).
