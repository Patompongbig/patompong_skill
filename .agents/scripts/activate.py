"""Append the bundled root instruction section without replacing project guidance."""

import argparse
from pathlib import Path

BEGIN = b"<!-- personal-toolkit:begin -->"
END = b"<!-- personal-toolkit:end -->"


def activate(project, toolkit):
    project = project.resolve()
    if toolkit.resolve() != (project / ".agents").resolve():
        raise ValueError("Copy this toolkit into the target project's .agents first.")
    target = project / "AGENTS.md"
    if (project / "AGENTS.override.md").exists():
        raise ValueError("Root AGENTS.override.md exists; inspect and integrate manually.")
    if target.is_symlink():
        raise ValueError("Refusing to append through a symlink.")
    existing = target.read_bytes() if target.exists() else b""
    if existing.startswith((b"\xff\xfe", b"\xfe\xff")):
        raise ValueError("UTF-16 instruction file; integrate manually preserving its encoding.")
    existing.decode("utf-8-sig")
    section = (toolkit / "templates" / "activation.md").read_bytes().strip()
    if existing.count(BEGIN) or existing.count(END):
        if existing.count(BEGIN) != 1 or existing.count(END) != 1:
            raise ValueError("Malformed or duplicate integration markers; inspect manually.")
        start = existing.index(BEGIN)
        stop = existing.index(END) + len(END)
        if stop <= start or existing[start:stop].replace(b"\r\n", b"\n") != section.replace(b"\r\n", b"\n"):
            raise ValueError("Existing integration differs; reconcile manually.")
        return "Already activated; no files changed."
    newline = b"\r\n" if b"\r\n" in existing else b"\n"
    section = section.replace(b"\r\n", b"\n").replace(b"\n", newline)
    separator = (b"" if existing.endswith(newline * 2) else newline if existing.endswith(newline) else newline * 2) if existing else b""
    with target.open("ab") as stream:
        stream.write(separator + section + newline)
    return "Activated: appended toolkit section to root AGENTS.md."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        print(activate(args.project_root, Path(__file__).resolve().parents[1]))
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(1, f"Activation failed: {error}\n")


if __name__ == "__main__":
    main()
