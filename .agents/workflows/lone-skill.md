# Lone-skill session

Purpose: use a named skill without requiring a composed workflow.

1. If the user already named an author/skill or an explicit skill invocation,
   resolve that manifest directly and read it. Matt skills live at
   `.agents/skills/mattpocock/<name>/SKILL.md`; the three existing personal skills
   remain at `.agents/skills/<name>/SKILL.md`. Outside downloads use author groups.
2. If the user asks for selection help or tree details, read
   [CATALOG.md](../CATALOG.md) to explain appropriate choices. Naming a known
   skill does not require catalog reading. A request naming a catalog ID such as
   M14 authorizes looking up that matching catalog entry; it does not require
   reading every entry. Ask to resolve genuinely ambiguous names.
3. Follow the chosen skill and relevant dependencies/references. The skills can
   navigate their dependencies themselves; no workflow whitelist is required.
4. Retain lone-skill mode for the session. A later explicitly named skill updates
   the skill choice. If the existing choice cannot handle the next task, ask
   which skill they want, rather than silently selecting an unrelated one.

Deliverable and completion follow the assigned skill and task. Example:
"Use lone-skill: mattpocock/handoff; summarize this task for another session."
