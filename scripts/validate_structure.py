#!/usr/bin/env python3
"""Validate the FLYSTAR77 STUDIO OS folder structure."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT_FILES = [
    "README.md",
    "config.json",
    "OPERATING_MANUAL.md",
    "PRODUCTION_BIBLE.md",
    "AI_RULES.md",
    "CODEX_RULES.md",
    "PALMIER_RULES.md",
    "PROMPT_GUIDE.md",
    "FOLDER_STRUCTURE.md",
    "AUTOMATION.md",
    "QUALITY_CONTROL.md",
    "GITHUB_OPERATIONS.md",
]

ROOT_DIRS = [
    "Projects",
    "Assets",
    "Templates",
    "ProductionBible",
    "Exports",
    "Archive",
]

PROJECT_DIRS = [
    "Import",
    "Unsorted",
    "CUT",
    "Audio",
    "Dialogue",
    "Reference",
    "Prompt",
    "Edit",
    "Storyboard",
    "Color",
    "QC",
    "Delivery",
    "Export",
]

PROJECT_FILES = [
    "project.json",
    "README.md",
    "PROJECT_BRIEF.md",
    "STATUS.md",
    "CUT_LIST.json",
    "Edit/EDIT_PLAN.md",
    "Edit/PALMIER_HANDOFF.md",
    "Edit/edit_project.json",
    "QC/QC_CHECKLIST.md",
]


def check_path(root: Path, relative: str, missing: list[str]) -> None:
    if not (root / relative).exists():
        missing.append(relative)


def validate_project(root: Path, project_name: str, missing: list[str], errors: list[str]) -> None:
    project_root = root / "Projects" / project_name
    if not project_root.exists():
        missing.append(f"Projects/{project_name}")
        return

    for folder in PROJECT_DIRS:
        check_path(project_root, folder, missing)

    for file_path in PROJECT_FILES:
        check_path(project_root, file_path, missing)

    project_json = project_root / "project.json"
    if project_json.exists():
        try:
            data = json.loads(project_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Projects/{project_name}/project.json is invalid JSON: {exc}")
        else:
            if data.get("projectName") != project_name:
                errors.append(
                    f"Projects/{project_name}/project.json projectName should be {project_name!r}"
                )

    cut_list = project_root / "CUT_LIST.json"
    if cut_list.exists():
        try:
            data = json.loads(cut_list.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Projects/{project_name}/CUT_LIST.json is invalid JSON: {exc}")
        else:
            cut_count = data.get("cutCount")
            cuts = data.get("cuts", [])
            if cut_count != len(cuts):
                errors.append(
                    f"Projects/{project_name}/CUT_LIST.json cutCount={cut_count} but cuts={len(cuts)}"
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="FLYSTAR77 repository root")
    parser.add_argument("--project", default="Distances", help="Project name to validate")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    missing: list[str] = []
    errors: list[str] = []

    for file_path in ROOT_FILES:
        check_path(root, file_path, missing)

    for folder in ROOT_DIRS:
        check_path(root, folder, missing)

    validate_project(root, args.project, missing, errors)

    if missing:
        print("Missing paths:")
        for item in missing:
            print(f"- {item}")

    if errors:
        print("Errors:")
        for item in errors:
            print(f"- {item}")

    if missing or errors:
        return 1

    print(f"OK: FLYSTAR77 structure is valid for project {args.project}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
