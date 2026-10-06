"""Local packaging checks; run with python -B -m unittest discover -s tests -v."""

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / ".agents"


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, SOURCE / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_module("toolkit_validate", "validate.py")
activator = load_module("toolkit_activate", "activate.py")


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="portable-toolkit-")
        self.project = Path(self.temp.name).resolve() / "sample project"
        self.project.mkdir()
        self.root = self.project / ".agents"
        shutil.copytree(SOURCE, self.root)

    def tearDown(self):
        # The recursive cleanup is confined to the TemporaryDirectory we created.
        self.assertTrue(self.project.is_relative_to(Path(self.temp.name).resolve()))
        self.temp.cleanup()

    def errors(self, project=False):
        return validator.validate(self.root, self.project if project else None)[0]

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in error for error in self.errors()), self.errors())

    def test_copy_activation_preserves_guidance_and_is_idempotent(self):
        guidance = self.project / "AGENTS.md"
        original = b"\xef\xbb\xbf# Project requirements\r\n\r\nKeep existing guidance.\r\n"
        guidance.write_bytes(original)
        activator.activate(self.project, self.root)
        activated = guidance.read_bytes()
        self.assertTrue(activated.startswith(original))
        self.assertEqual([], self.errors(project=True))
        activator.activate(self.project, self.root)
        self.assertEqual(activated, guidance.read_bytes())

    def test_copied_cli_works_from_unrelated_working_directory(self):
        for script, extra in (("activate.py", []), ("validate.py", [])):
            result = subprocess.run(
                [sys.executable, "-B", str(self.root / "scripts" / script),
                 "--project-root", str(self.project)] + extra,
                cwd=self.temp.name, capture_output=True, text=True,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual([], self.errors(project=True))

    def test_root_override_refuses_activation_without_writing(self):
        (self.project / "AGENTS.override.md").write_text("Project override", encoding="utf-8")
        with self.assertRaises(ValueError):
            activator.activate(self.project, self.root)
        self.assertFalse((self.project / "AGENTS.md").exists())

    def test_foreign_target_refuses_activation(self):
        with self.assertRaises(ValueError):
            activator.activate(Path(self.temp.name), self.root)

    def test_malformed_or_changed_section_refuses_overwrite(self):
        target = self.project / "AGENTS.md"
        target.write_text("<!-- personal-toolkit:begin -->", encoding="utf-8")
        before = target.read_bytes()
        with self.assertRaises(ValueError):
            activator.activate(self.project, self.root)
        self.assertEqual(before, target.read_bytes())
        target.write_text("", encoding="utf-8")
        activator.activate(self.project, self.root)
        target.write_text(target.read_text(encoding="utf-8").replace("Personal toolkit defaults", "Changed defaults"), encoding="utf-8")
        before = target.read_bytes()
        with self.assertRaises(ValueError):
            activator.activate(self.project, self.root)
        self.assertEqual(before, target.read_bytes())

    def test_disable_enable_and_catalog_state(self):
        manifest = self.root / "skills" / "review-change" / "SKILL.md"
        disabled = manifest.with_name("SKILL.md.disabled")
        manifest.rename(disabled)
        self.assert_error("Catalog/manifest mismatch")
        catalog = self.root / "CATALOG.md"
        original = catalog.read_text(encoding="utf-8")
        updated = original.replace("skills/review-change/SKILL.md)", "skills/review-change/SKILL.md.disabled)")
        updated = "\n".join(line.replace("| enabled |", "| disabled |") if "[review-change]" in line else line for line in updated.splitlines()) + "\n"
        catalog.write_text(updated, encoding="utf-8")
        self.assertFalse(manifest.exists())
        self.assertEqual(2, len(list((self.root / "skills").rglob("SKILL.md"))))
        self.assertEqual([], self.errors())
        disabled.rename(manifest)
        catalog.write_text(original, encoding="utf-8")
        self.assertEqual([], self.errors())

    def test_catalog_status_alone_does_not_disable(self):
        catalog = self.root / "CATALOG.md"
        catalog.write_text(catalog.read_text(encoding="utf-8").replace("| enabled |", "| disabled |"), encoding="utf-8")
        self.assert_error("Catalog/manifest mismatch")
        self.assertEqual(3, len(list((self.root / "skills").rglob("SKILL.md"))))

    def test_broken_and_escaping_links(self):
        readme = self.root / "README.md"
        with readme.open("a", encoding="utf-8") as stream:
            stream.write("\n[missing](missing.md)\n[escape](../outside.md)\n")
        self.assert_error("Broken link")
        self.assert_error("Link leaves toolkit")

    def test_missing_metadata(self):
        manifest = self.root / "skills" / "diagnose-bug" / "SKILL.md"
        manifest.write_text("---\nname: diagnose-bug\n---\nInstructions", encoding="utf-8")
        self.assert_error("Expected exactly one description")

    def test_duplicate_skill_names(self):
        copy = self.root / "skills" / "duplicate"
        shutil.copytree(self.root / "skills" / "diagnose-bug", copy)
        self.assert_error("Duplicate skill name")

    def test_missing_skill_manifest(self):
        (self.root / "skills" / "empty-skill").mkdir()
        self.assert_error("Missing skill manifest")

    def test_machine_path_and_private_key_detection(self):
        note = self.root / "bad-example.txt"
        note.write_text("C:" + chr(92) + "machine-specific" + "\n-----BEGIN PRIVATE KEY-----", encoding="utf-8")
        self.assert_error("Absolute machine path")
        self.assert_error("Credential-like text")

    def test_metadata_strings_and_rejects_unsupported_scalars(self):
        for value in ('"A focused description"', "'A focused description'", "A focused description"):
            parsed = validator.metadata("---\nname: a-skill\ndescription: " + value + "\n---\nBody")
            self.assertEqual("A focused description", parsed["description"])
        for value in ("", "true", "123", "'unclosed", ">", '"unclosed'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validator.metadata("---\nname: a-skill\ndescription: " + value + "\n---\nBody")


if __name__ == "__main__":
    unittest.main()
