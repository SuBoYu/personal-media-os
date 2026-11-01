#!/usr/bin/env python3
"""Offline workspace initializer and allowlisted Skill packager (Python 3.9+)."""
import argparse
import json
from pathlib import Path
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = (
    "SKILL.md", "references/notion.md", "references/publishing.md",
)


def initialize(destination):
    destination = Path(destination).expanduser().resolve()
    # Never overlay a folder that might already contain a user's work.
    if destination.exists():
        raise ValueError("Workspace already exists; reuse it without initializing again.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    profile = {
        "schema_version": 1, "brand": {"name": None, "audience": [], "goals": [],
        "voice": None, "boundaries": [], "weekly_capacity": None},
        "timezone": None, "strategy_status": "needs_interview",
        "publishing_paused": True, "channels": [], "notion_bindings": None,
    }
    # Prepare all content before exposing a complete workspace.
    with tempfile.TemporaryDirectory(dir=destination.parent) as temporary:
        stage = Path(temporary) / "workspace"
        stage.mkdir()
        (stage / "profile.json").write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n")
        for name in ("sources.jsonl", "publications.jsonl"):
            (stage / name).write_text("")
        (stage / "NEXT.md").write_text(
            "# Start here\n\nAnswer the brand interview before drafting a calendar.\n"
            "Publishing is paused. No accounts are connected.\n"
        )
        # mkdir is exclusive even if another process initialized concurrently.
        destination.mkdir()
        for path in stage.iterdir():
            path.rename(destination / path.name)
    return destination


def package(output):
    output = Path(output).expanduser().resolve()
    folder = ROOT / "skills" / "personal-media-os"
    # Explicit allowlist: adding a credential or private file to the repo can't leak it into the ZIP.
    for relative in SKILL_FILES:
        source = folder / relative
        if source.is_symlink() or not source.is_file():
            raise ValueError("Missing or unsafe Skill resource: " + relative)
    output.mkdir(parents=True, exist_ok=True)
    target = output / "personal-media-os-skill.zip"
    if target.exists():
        raise ValueError("Package exists; choose a fresh output directory.")
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as archive:
        for relative in SKILL_FILES:
            archive.write(folder / relative, "personal-media-os/" + relative)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init").add_argument("--workspace", required=True)
    commands.add_parser("package").add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        result = initialize(args.workspace) if args.command == "init" else package(args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")
    print(result)


if __name__ == "__main__":
    main()
