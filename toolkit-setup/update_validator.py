"""Update the existing checker for author groups and explicit session workflows."""
from pathlib import Path

path = Path(__file__).resolve().parents[1] / '.agents/scripts/validate.py'
text = path.read_text(encoding='utf-8')
text = text.replace('"scripts/activate.py", "scripts/validate.py",', '"scripts/activate.py", "scripts/validate.py", "workflows/INDEX.md",\n    "templates/workflow.md", "COMPATIBILITY.md", "IMPORTS.json",')
text = text.replace('''                if path.parent.parent != root / "skills" or path.parent.name != name:
                    errors.append(f"Skill folder must be skills/{name}: {relative}")''', '''                try:
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
                    blocks = re.findall(r"(?m)^policy:[ \\t]*\\n((?:[ \\t]+[^\\n]*\\n?)*)", policy_text)
                    if len(blocks) != 1 or not re.search(r"(?m)^  allow_implicit_invocation: false[ \\t]*$", blocks[0]):
                        errors.append(f"Expected explicit-only policy: {relative}")''')
text = text.replace('''    if skills.exists():
        for folder in skills.iterdir():
            if folder.is_dir() and not any((folder / name).is_file() for name in ("SKILL.md", "SKILL.md.disabled")):
                errors.append(f"Missing skill manifest: skills/{folder.name}")''', '''    if skills.exists():
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
                    errors.append(f"Missing grouped skill manifest: skills/{folder.name}/{child.name}")''')
insert = '''    # Verify pinned resources without executing upstream code.
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
        for target in re.findall(r"`(\\.agents/skills/[^`\\n]+/SKILL\\.md)`", content):
            if "<" in target:
                continue
            local = (root.parent / target).resolve()
            if not local.is_relative_to(root) or not local.is_file():
                errors.append(f"Broken skill entry path in {path.relative_to(root)}: {target}")
    for filename in ("interview.md", "planning.md", "build-review.md", "review.md", "lone-skill.md"):
        if not (root / "workflows" / filename).is_file():
            errors.append(f"Missing example workflow: {filename}")
'''
text = text.replace('    if project is not None:\n', insert + '    if project is not None:\n')
path.write_text(text, encoding='utf-8', newline='\n')
print('Updated existing validator for author groups, policies, imports, and workflow entry paths.')
