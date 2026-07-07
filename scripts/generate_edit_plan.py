#!/usr/bin/env python3
"""Generate a simple EDIT_PLAN.md from CUT_LIST.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def fmt_time(seconds: float) -> str:
    minutes = int(seconds // 60)
    remaining = seconds - minutes * 60
    return f"{minutes:02d}:{remaining:04.1f}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="FLYSTAR77 repository root")
    parser.add_argument("--project", default="Distances", help="Project name")
    parser.add_argument("--force", action="store_true", help="Overwrite existing EDIT_PLAN.md")
    args = parser.parse_args()

    project_root = Path(args.root).resolve() / "Projects" / args.project
    cut_list_path = project_root / "CUT_LIST.json"
    edit_plan_path = project_root / "Edit" / "EDIT_PLAN.md"

    data = json.loads(cut_list_path.read_text(encoding="utf-8"))
    cuts = data["cuts"]

    if edit_plan_path.exists() and not args.force:
        print(f"Skipped existing file: {edit_plan_path}")
        return 0

    lines = [
        f"# {args.project} EDIT PLAN",
        "",
        "Generated from `CUT_LIST.json`.",
        "",
        "| CUT | Timeline | 推奨尺 | 役割 | セリフ同期 |",
        "|---|---:|---:|---|---|",
    ]

    cursor = 0.0
    for cut in cuts:
        duration = float(cut["recommendedSeconds"])
        start = cursor
        end = cursor + duration
        sync = cut.get("dialogueAsset", "セリフなし")
        lines.append(
            f"| {cut['cut']} | {fmt_time(start)}-{fmt_time(end)} | {duration:.1f}s | {cut['role']} | {sync} |"
        )
        cursor = end

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- セリフ後は急にカットしない。",
            "- CUT17は余韻を切らない。",
            "- CUT18は肩を寄せるあと約1秒残す。",
        ]
    )

    edit_plan_path.parent.mkdir(parents=True, exist_ok=True)
    edit_plan_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {edit_plan_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
