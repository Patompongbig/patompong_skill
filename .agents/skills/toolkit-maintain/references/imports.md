# Find and import a skill

## Evaluate candidates

Establish the recurring job and target agent before searching. Consult the local
catalog for overlap. Prefer an upstream repository or maintainer's published
package; read the actual instructions and relevant resource files, not just a
marketplace summary. If sources cannot be accessed, disclose that limitation
instead of claiming inspection.

Search for a small useful selection and read each candidate's actual `SKILL.md`
and relevant supporting resources. Compare purpose, trigger, overlap with local
skills, dependencies, source trust, licensing, and portability. Link the source
and recommend reuse, adaptation, or skipping. Separate instruction-only content
from integrations that require tools, accounts, credentials, or network access.

Present a compact comparison with these columns: candidate and source link,
purpose/trigger, local overlap, dependencies, portability/license concerns, and
recommendation (reuse, adapt, or skip). Usually two or three strong candidates are
enough; include fewer when the available evidence supports fewer. Explain the
recommended choice and material adaptations in plain language. Avoid adding a
skill that merely repeats normal Codex behavior or an already available capability.

Evaluate whether the description will trigger for a representative intended
request and stay out of an unrelated request. Identify any absolute paths,
unbundled resources, unsupported tools, credential assumptions, or broad scripted
side effects that prevent direct use. Treat static inspection as static evidence;
do not call a candidate runtime-tested without running the relevant behavior.

Complete an evaluation when the user has a small evidence-backed selection and
clear recommendations, including dependencies and unresolved gaps. A request to
evaluate alone ends here without installing packages or changing accounts.

## Import after authorization

Discovery is not installation authorization. When installation is authorized,
place the skill inside this toolkit's `skills` directory and resolve name/purpose
collisions. Never silently install globally. Pin an upstream release or commit;
record its source URL, revision, license, attribution, acquisition date, and local
adaptations in a bundled provenance file linked from the catalog. Preserve
applicable license and notice files. If reuse rights are unclear, report that
before copying the material.

Inspect bundled scripts before execution, including downloads, subprocesses,
filesystem writes, environment access, and external calls. Keep private values
outside the toolkit. Do not run an installer merely to read its instructions.

Check relative resources, metadata, same-name collisions, and actual dependencies.
Adapt unsupported discovery paths without misrepresenting the upstream version.
Update the catalog, README if necessary, and changelog; run available checks.
Distinguish recommended, downloaded, installed, statically validated, and
runtime-tested states. Claim only states supported by observed actions.
