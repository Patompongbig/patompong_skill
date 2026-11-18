# ask-answer workflow

> Answer questions about code and software engineering through focused,
> read-only investigation, with every deliverable in chat.

## Purpose

A safe mode for understanding. The agent investigates and explains; it never
changes anything. Proposed fixes, commands and code are shown, not applied. The
selection persists across follow-ups until the user switches workflows; "fix
this" yields an explained proposal and a note that applying it needs an editing
workflow.

## Modes

| Mode | Use when | Writes | Ends with |
| --- | --- | --- | --- |
| **answer** (only mode) | Any question | Nothing | Answer in chat |

## Inputs

The question, the current project, files the user names, and read-only online
documentation when needed.

## Outputs

Chat only: the answer with file and line references, examples, and proposed
changes clearly labelled as proposals.

## Roles and models

Main session. Wide investigations may dispatch read-only researchers (default
sonnet). No model prompt unless the user names models.

## Procedure

1. **Understand the question.** Ask only about consequential ambiguity; find
   facts yourself.
2. **Investigate.** Read the relevant code, callers, configuration, documents
   and existing logs or test output. Delegate breadth to researchers. General
   questions that need no project evidence are answered directly.
3. **Answer.** At the requested depth, citing `path:line` for code claims and
   sources for online facts. Distinguish observed behaviour, existing runtime
   evidence, inference, and proposals.
4. **Name the limits.** If proof needs execution or edits, describe the check
   and the remaining uncertainty instead of performing it.

## Boundaries

- Read-only: file reads, searches and commands whose only effect is reading
  (`rg`, `git diff`, `git log`, `git status`). Inspect unfamiliar commands first.
- No edits, saved notes, configuration changes or external writes.
- No tests, builds, installs, scripts or services, even to investigate.
- No private project content sent to external services.
- Never combined with a writing stage; switching requires an explicit request.

## Done when

The question is answered as far as read-only evidence allows, and any missing
evidence and its effect on the answer are stated.

## Example invocations

- "Use workflow ask-answer. Explain how the import pipeline handles cancellation."
- "Why could this error happen? Show the fix without applying it."
