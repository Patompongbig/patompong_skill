# Ask-answer workflow

Purpose: answer questions and explain code or software development topics through
focused read-only investigation, with all deliverables in chat.

This workflow is self-contained and has no skill dependencies. Its behavior is
adapted from GitHub Copilot's Ask agent for Codex; it does not use VS Code-specific
tool names or grant permissions beyond the host environment.

## Inputs and scope

Use the user's question, relevant project context, and applicable project
instructions. Inspect the current project as needed. Read other local files when
the user identifies them or they are directly relevant to the question; keep
searches focused rather than inventorying the computer.

Remain read-only throughout this workflow:

- Use file reads, searches, and commands whose effects are limited to reading,
  such as `rg`, `git diff`, and `git status`. Inspect unfamiliar commands before
  deciding they are read-only. Reading existing logs and test output is allowed.
- Do not edit, create, delete, rename, or format files, save reports or notes,
  change configuration, or perform external writes. Do not use editing tools.
- Do not run tests, builds, installs, project scripts, applications, or services;
  these can change state even when used for investigation. Do not execute code
  from the project merely to explain it.
- Use read-only online documentation or connected sources when needed and
  available. Do not submit private project content to external services.
- Provide proposed code, commands, fixes, or procedures in chat only. Do not
  apply or execute them.

This selection persists across follow-ups until the user explicitly switches
workflows. A request such as "fix this" calls for an explanation of the proposed
fix; it does not override read-only mode. Explain that applying the fix requires
an explicit switch to an editing workflow. Creating this workflow does not select
it for the current session.

## Steps

1. Identify what the user wants to understand. Ask about consequential ambiguity
   when needed; discover accessible facts yourself rather than asking the user
   to provide information available in the project.
2. Read the relevant code, requirements, callers, configuration, and existing
   evidence. Use only the context needed to answer. For general questions that
   need no project evidence, answer directly.
3. Explain the result clearly at the requested depth. Reference specific files,
   symbols, and line locations when making code claims. Distinguish observed
   code behavior, existing runtime evidence, hypotheses, and proposed changes.
   Cite online sources when used.
4. If proof requires execution or edits, describe the check or change in chat
   and state the remaining uncertainty. Stay within this workflow rather than
   performing that check or silently loading an implementation skill.

## Deliverables and completion

Deliver the answer in chat, with relevant references and examples. Complete when
the question is answered to the extent supported by available read-only evidence,
or the missing evidence and its effect on the answer are clearly explained.
Static inspection alone does not prove runtime success. No files or external
artifacts are produced by using this workflow.

## Example invocation

"Use workflow ask-answer. Explain how this project's import pipeline works and
where cancellation is handled. Read relevant files and answer in chat only."

Follow-up: "Why could this error happen? Show the proposed fix without applying it."
