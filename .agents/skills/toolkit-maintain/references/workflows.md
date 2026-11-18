# Create an editable workflow

1. Establish the repeatable outcome, scope, and ordered skill combination from
   the user's request. Read the skills they named directly; follow relevant
   dependencies as needed. Read the complete catalog only if they request skill
   selection help, tree browsing, or catalog maintenance.
2. Use the workflow template, `toolkit/templates/workflow.md` in the source repository. Write the file
   to the toolkit's workflows/<name>.md with concrete entry skill paths, required
   inputs, conditional steps, deliverables, and completion criteria. The workflow
   chooses entry points; each skill still navigates relevant dependencies itself.
3. Add a concise row to [the session menu](../../../workflows/INDEX.md). Keep the
   detailed skills catalog separate; avoid copying entire skill instructions.
4. Update the changelog and relevant docs; run the toolkit validator. Check that
   all entry paths exist and the sequence produces the requested deliverable.

Example: "Use toolkit-maintain to create design-review combining
mattpocock/codebase-design and review-change; finish with written recommendations."

Complete when the editable file/menu entry exist, paths validate, and invocation
is explained. Creating a workflow does not execute it or change the session's
selected workflow unless the user requests that switch.
