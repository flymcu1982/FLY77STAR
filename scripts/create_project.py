#!/usr/bin/env python3
"""Create a FLYSTAR77 project scaffold."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


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


def write_text_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Project name")
    parser.add_argument("--root", default=".", help="FLYSTAR77 repository root")
    parser.add_argument("--cuts", type=int, default=18, help="Number of cuts")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    project_root = root / "Projects" / args.name
    project_root.mkdir(parents=True, exist_ok=True)

    for folder in PROJECT_DIRS:
        (project_root / folder).mkdir(parents=True, exist_ok=True)

    project_json = {
        "projectName": args.name,
        "studio": "FLYSTAR77 STUDIO",
        "version": "v1.0",
        "status": "production_start",
        "cutCount": args.cuts,
        "priorityRules": [
            "../../OPERATING_MANUAL.md",
            "../../PRODUCTION_BIBLE.md",
            "../../AI_RULES.md",
            "../../CODEX_RULES.md",
            "../../PALMIER_RULES.md",
        ],
        "folders": {folder.lower(): folder for folder in PROJECT_DIRS},
    }
    write_text_if_missing(
        project_root / "project.json",
        json.dumps(project_json, ensure_ascii=False, indent=2) + "\n",
    )

    write_text_if_missing(
        project_root / "README.md",
        f"# {args.name}\n\nFLYSTAR77 STUDIO project.\n",
    )
    write_text_if_missing(
        project_root / "PROJECT_BRIEF.md",
        f"# {args.name} Project Brief\n\n## Concept\n\n未設定。\n",
    )
    write_text_if_missing(
        project_root / "STATUS.md",
        "# Status\n\n- [ ] CUT素材配置\n- [ ] EDIT_PLAN作成\n- [ ] Palmier編集\n- [ ] QC\n- [ ] Export\n",
    )
    write_text_if_missing(
        project_root / "QC" / "QC_CHECKLIST.md",
        "# QC Checklist\n\n- [ ] 余韻を切っていない。\n- [ ] BGMがセリフを邪魔していない。\n",
    )
    write_text_if_missing(
        project_root / "Edit" / "PALMIER_HANDOFF.md",
        "# Palmier Handoff\n\n- CUTを読み込む。\n- EDIT_PLANに従って編集する。\n",
    )

    print(f"Created project scaffold: {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
