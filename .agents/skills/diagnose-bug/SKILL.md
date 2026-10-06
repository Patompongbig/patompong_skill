---
name: diagnose-bug
description: "Reproduce and diagnose a reported software failure, regression, or incorrect behavior, then fix it when implementation is requested. Use for concrete defects; not feature planning, generic code review, or toolkit maintenance."
---

# Diagnose a reported defect

Establish expected and observed behavior from the report and applicable project
context. Find the smallest useful reproduction using existing tools and fixtures.
If reproduction is unavailable, state the gap and distinguish hypotheses from
observed causes.

Trace the failing path and test the most plausible explanation with evidence.
Avoid changing several unrelated mechanisms at once. When a fix is authorized,
address the cause with a focused change and a regression check that reproduces
the original defect when practical. An investigation-only request stops at
findings and a proposed fix.

Verify the reproduction after the fix and run relevant nearby checks. Report
cause, change, observed verification, and any untested environment dependency.

Example: `$diagnose-bug Diagnose and fix the crash when this parser receives an empty file.`

Complete when the cause is supported by evidence and the authorized fix is
verified, or a concrete blocker and the next discriminating check are documented.
