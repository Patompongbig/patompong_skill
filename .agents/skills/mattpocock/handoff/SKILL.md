---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
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

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
