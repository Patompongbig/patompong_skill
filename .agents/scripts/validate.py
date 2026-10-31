"""Read-only, standard-library static validation of a portable .agents toolkit."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "README.md", "PREFERENCES.md", "WORKFLOW-GUIDE.md", "CATALOG.md",
    "STARTUP.md", "CHANGELOG.md", "templates/activation.md",
    "scripts/activate.py", "scripts/validate.py", "workflows/INDEX.md",
    "templates/workflow.md", "COMPATIBILITY.md", "IMPORTS.json",
)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
MACHINE_PATH = re.compile(r"(?<![\w])(?:(?i:[a-z]:[\\/]|\\\\[a-z0-9_.-]+[\\/])|/(?:home|Users|mnt|tmp|var|opt|etc)/)")
SECRET = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bsk-[A-Za-z0-9_-]{20,}")
LINK = re.compile(r"!?\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\)")
REF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?([^\s>]+)>?", re.M)


def metadata(content):
    if not content.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    end = content.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Unclosed YAML frontmatter")
    result = {}
    for key in ("name", "description"):
        values = re.findall(rf"^{key}:\s*(.*?)\s*$", content[4:end], re.M)
        if len(values) != 1:
            raise ValueError(f"Expected exactly one {key}")
        value = values[0]
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'"):
            if not re.fullmatch(r"'(?:[^']|'')*'", value):
                raise ValueError(f"Malformed quoted {key}")
            value = value[1:-1].replace("''", "'")
        else:
            value = re.split(r"\s+#", value, maxsplit=1)[0]
            if value.lower() in ("", "|", ">", "|-", ">-", "|+", ">+", "null", "true", "false", "yes", "no", "on", "off", "~") or value.startswith(("[", "{", "&", "*", "!", "#", "@", "`")) or ": " in value or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value):
                raise ValueError(f"{key} must be a single-line YAML string")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Empty or non-string {key}")
        result[key] = value
    if not NAME.fullmatch(result["name"]) or len(result["name"]) > 64:
        raise ValueError("Invalid skill name")
    if len(result["description"]) > 1024:
        raise ValueError("Description exceeds 1024 characters")
    return result


def validate(root, project=None):
    root = root.resolve()
    errors = []
    approved_platform_literals = {}
    inventory_file = root / "IMPORTS.json"
    if inventory_file.is_file():
        import hashlib
        records = json.loads(inventory_file.read_text(encoding="utf-8"))
        for record in records.get("imports", []):
            for resource in record.get("files", []):
                literals = resource.get("platform_path_literals", [])
                candidate = (root / resource["path"]).resolve()
                if (literals and candidate.is_relative_to(root) and candidate.is_file()
                        and resource["upstream_sha256"] == resource["installed_sha256"]
                        and hashlib.sha256(candidate.read_bytes()).hexdigest() == resource["installed_sha256"]
                        and all(value in ("/" + "tmp/", "C:" + "/" + "Users/", "/c" + "/" + "Users/") for value in literals)):
                    approved_platform_literals[resource["path"]] = literals
    manifests = {}
    names = {}
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"Symlink is not portable: {relative}")
            continue
        if not path.is_file():
            continue
        if path.name == ".env" or path.suffix in (".pem", ".key") or path.name in ("credentials.json", "auth.json", "id_rsa", "id_ed25519"):
            errors.append(f"Credential-like file: {relative}")
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeError:
            if path.suffix in (".md", ".disabled", ".py", ".yaml", ".yml", ".json", ".toml", ".txt"):
                errors.append(f"Expected UTF-8 text: {relative}")
            continue
        path_check = content
        for literal in approved_platform_literals.get(relative, []):
            path_check = path_check.replace(literal, "<platform-path>/")
        if MACHINE_PATH.search(path_check):
            errors.append(f"Absolute machine path: {relative}")
        if SECRET.search(content):
            errors.append(f"Credential-like text: {relative}")
        if path.name in ("SKILL.md", "SKILL.md.disabled"):
            try:
                info = metadata(content)
                name = info["name"]
                if name in names:
                    errors.append(f"Duplicate skill name {name}: {names[name]} and {relative}")
                names[name] = relative
                try:
                    parts = path.relative_to(root / "skills").parts
                except ValueError:
                    parts = ()
                flat = len(parts) == 2 and parts[0] == name
                grouped = len(parts) == 3 and NAME.fullmatch(parts[0]) and parts[1] == name
                if not (flat or grouped):
                    errors.append(f"Skill folder must be skills/{name} or skills/<author>/{name}: {relative}")
                policy_path = path.parent / "agents/openai.yaml"
                if not policy_path.is_file():
                    errors.append(f"Missing explicit invocation policy: {relative}")
                else:
                    policy_text = policy_path.read_text(encoding="utf-8-sig")
                    blocks = re.findall(r"(?m)^policy:[ \t]*\n((?:[ \t]+[^\n]*\n?)*)", policy_text)
                    if len(blocks) != 1 or not re.search(r"(?m)^  allow_implicit_invocation: false[ \t]*$", blocks[0]):
                        errors.append(f"Expected explicit-only policy: {relative}")
                manifests[relative] = (name, "disabled" if path.name.endswith(".disabled") else "enabled")
            except (ValueError, TypeError) as error:
                errors.append(f"{relative}: {error}")
        if path.suffix == ".md" or path.name == "SKILL.md.disabled":
            # Ignore fenced examples; validate ordinary inline and reference links.
            prose = re.sub(r"(?ms)^\s*(```|~~~).*?^\s*\1[^\n]*$", "", content)
            # Inline-code links are generated-project examples, not bundled files.
            prose = re.sub(r"`[^`\n]*`", "", prose)
            targets = [a or b for a, b in LINK.findall(prose)] + REF.findall(prose)
            for target in targets:
                if target.startswith("#"):
                    continue
                parsed = urlsplit(target)
                if parsed.scheme in ("https", "http", "mailto"):
                    continue
                if parsed.scheme or parsed.netloc or target.startswith(("/", "\\")):
                    errors.append(f"Nonportable link in {relative}: {target}")
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                # Activation template intentionally resolves from project root.
                if relative == "templates/activation.md":
                    resolved = (root.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(root):
                    errors.append(f"Link leaves toolkit in {relative}: {target}")
                elif not resolved.exists():
                    errors.append(f"Broken link in {relative}: {target}")
    skills = root / "skills"
    if not manifests:
        errors.append("No skill manifests found")
    if skills.exists():
        for folder in skills.iterdir():
            if not folder.is_dir():
                continue
            if any((folder / filename).is_file() for filename in ("SKILL.md", "SKILL.md.disabled")):
                continue
            children = [child for child in folder.iterdir() if child.is_dir()]
            if not children:
                errors.append(f"Empty author group: skills/{folder.name}")
            for child in children:
                if not any((child / filename).is_file() for filename in ("SKILL.md", "SKILL.md.disabled")):
                    errors.append(f"Missing grouped skill manifest: skills/{folder.name}/{child.name}")
    catalog = root / "CATALOG.md"
    rows = {}
    if catalog.is_file():
        for line in catalog.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("| ["):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            match = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", cells[0])
            if len(cells) != 6 or not match:
                errors.append("Malformed catalog row")
                continue
            name, target = match.groups()
            if target in rows:
                errors.append(f"Duplicate catalog row: {target}")
            rows[target] = (name, cells[-1])
            if any(not cell for cell in cells):
                errors.append(f"Missing catalog field: {name}")
        for target in sorted(set(rows) | set(manifests)):
            if rows.get(target) != manifests.get(target):
                errors.append(f"Catalog/manifest mismatch: {target}")
    # Verify pinned resources without executing upstream code.
    inventory_path = root / "IMPORTS.json"
    if inventory_path.is_file():
        import hashlib
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        imported = set()
        for record in inventory.get("imports", []):
            target = record["manifest"]
            imported.add(target)
            if target not in manifests:
                errors.append(f"Imported manifest missing: {target}")
            if not (root / record["license"]).is_file():
                errors.append(f"Missing import license: {record['name']}")
            if not re.fullmatch(r"[0-9a-f]{40}", record.get("revision", "")) or record["revision"] not in record["source_url"]:
                errors.append(f"Unpinned import: {record['name']}")
            for resource in record.get("files", []):
                local = (root / resource["path"]).resolve()
                if not local.is_relative_to(root):
                    errors.append(f"Import resource escapes toolkit: {resource['path']}")
                    continue
                if not local.is_file():
                    errors.append(f"Missing imported resource: {resource['path']}")
                elif hashlib.sha256(local.read_bytes()).hexdigest() != resource["installed_sha256"]:
                    errors.append(f"Unrecorded imported resource change: {resource['path']}")
                if local.suffix in (".sh", ".cjs") and resource["upstream_sha256"] != resource["installed_sha256"]:
                    errors.append(f"Imported executable changed without script review: {resource['path']}")
        grouped_manifests = {target for target in manifests if len(Path(target).parts) == 4}
        if grouped_manifests - imported:
            errors.append("Author-grouped imports missing provenance inventory")
    # Workflow entry paths and adapted named skill calls must exist. Generic
    # placeholders in the reusable template are intentionally ignored.
    for path in list((root / "workflows").glob("*.md")) + list((root / "skills").rglob("*.md")):
        content = path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"`(\.agents/skills/[^`\n]+/SKILL\.md)`", content):
            if "<" in target:
                continue
            local = (root.parent / target).resolve()
            if not local.is_relative_to(root) or not local.is_file():
                errors.append(f"Broken skill entry path in {path.relative_to(root)}: {target}")
    # The editable menu, not historical example names, defines selectable workflows.
    menu_path = root / "workflows/INDEX.md"
    menu_entries = {}
    if menu_path.is_file():
        for line in menu_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("| ") or line.startswith(("| Workflow |", "| ---")):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 3 or not NAME.fullmatch(cells[0]):
                errors.append("Malformed workflow menu row")
                continue
            name = cells[0]
            expected = f"{name}.md"
            if name in menu_entries:
                errors.append(f"Duplicate workflow menu entry: {name}")
            menu_entries[name] = expected
            link = re.fullmatch(r"\[[^\]]+\]\(([^)]+)\)", cells[2])
            if not cells[1] or not link or link.group(1) != expected:
                errors.append(f"Workflow menu target mismatch: {name}")
            if not (root / "workflows" / expected).is_file():
                errors.append(f"Missing menu workflow: {expected}")
        if not menu_entries:
            errors.append("Workflow menu has no selections")
        for path in (root / "workflows").glob("*.md"):
            if path.name != "INDEX.md" and path.stem not in menu_entries:
                errors.append(f"Workflow missing menu entry: {path.name}")
    if project is not None:
        project = project.resolve()
        if root != (project / ".agents").resolve():
            errors.append("Toolkit is not the target project's .agents folder")
        if (project / "AGENTS.override.md").exists():
            errors.append("Root AGENTS.override.md can hide activation; inspect manually")
        guidance = project / "AGENTS.md"
        template = root / "templates" / "activation.md"
        if not guidance.is_file():
            errors.append("Missing root AGENTS.md activation")
        elif template.is_file():
            text = guidance.read_text(encoding="utf-8-sig")
            section = template.read_text(encoding="utf-8-sig").strip()
            if text.count("<!-- personal-toolkit:begin -->") != 1 or text.count("<!-- personal-toolkit:end -->") != 1 or section not in text:
                errors.append("Root activation section is missing, duplicated, or differs")
    return errors, len(manifests)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path)
    args = parser.parse_args()
    try:
        errors, count = validate(Path(__file__).resolve().parents[1], args.project_root)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        parser.exit(1)
    print(f"PASS: {count} skills; static toolkit checks passed.")


if __name__ == "__main__":
    main()
