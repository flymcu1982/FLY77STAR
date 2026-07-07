#!/usr/bin/env python3
"""Organize assets from a project's Import folder.

Examples:
  python scripts/import_assets.py Projects/Distances --dry-run
  python scripts/import_assets.py Projects/Distances --apply
  python scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".mov"}
AUDIO_EXTENSIONS = {".wav", ".mp3"}
DIALOGUE_HINTS = {"dialogue", "voice", "cut06", "cut6", "cut12", "cut17"}
CUT_RE = re.compile(r"cut[\s_-]*(?<!\d)(1[0-8]|0?[1-9])(?!\d)", re.IGNORECASE)


@dataclass
class AssetRecord:
    source: Path
    extension: str
    media_type: str
    explicit_cut: str | None
    source_relative: str = ""
    assigned_cut: str | None = None
    assignment_reason: str = ""
    destination: Path | None = None
    destination_relative: str = ""
    status: str = "planned"


def normalize_name(value: str) -> str:
    return re.sub(r"[\s_-]+", "", value.lower())


def detect_cut(path: Path) -> str | None:
    match = CUT_RE.search(path.stem)
    if not match:
        return None
    number = int(match.group(1))
    if 1 <= number <= 18:
        return f"CUT{number:02d}"
    return None


def classify(path: Path) -> str | None:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTENSIONS:
        return "image"
    if ext in VIDEO_EXTENSIONS:
        return "video"
    if ext in AUDIO_EXTENSIONS:
        compact = normalize_name(path.stem)
        if any(hint in compact for hint in DIALOGUE_HINTS):
            return "dialogue"
        return "music"
    return None


def created_time(path: Path) -> float:
    stat = path.stat()
    return getattr(stat, "st_birthtime", stat.st_ctime)


def clean_extension(path: Path) -> str:
    return path.suffix.lower()


def as_posix_relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def unique_destination(path: Path, reserved: set[Path]) -> Path:
    candidate = path
    index = 2
    while candidate.exists() or candidate in reserved:
        candidate = path.with_name(f"{path.stem}_take{index:02d}{path.suffix}")
        index += 1
    reserved.add(candidate)
    return candidate


def next_unsorted_destination(project_root: Path, media_type: str, extension: str, reserved: set[Path]) -> Path:
    prefix = {
        "video": "video",
        "image": "image",
        "dialogue": "dialogue",
    }.get(media_type, "asset")
    folder = project_root / "Unsorted"
    index = 1
    while True:
        stem = f"{prefix}_{index:03d}"
        if not any(folder.glob(f"{stem}.*")):
            candidate = folder / f"{stem}{extension}"
            if candidate not in reserved:
                reserved.add(candidate)
                return candidate
        index += 1


def destination_for(record: AssetRecord, project_root: Path, bgm_index: int, reserved: set[Path]) -> Path:
    ext = record.extension
    cut = record.assigned_cut

    if record.media_type == "video":
        if not cut:
            return next_unsorted_destination(project_root, record.media_type, ext, reserved)
        folder = project_root / "CUT"
        name = f"{cut}{ext}"
    elif record.media_type == "image":
        if not cut:
            return next_unsorted_destination(project_root, record.media_type, ext, reserved)
        folder = project_root / "Reference"
        name = f"{cut}_reference{ext}"
    elif record.media_type == "dialogue":
        if not cut:
            return next_unsorted_destination(project_root, record.media_type, ext, reserved)
        folder = project_root / "Dialogue"
        name = f"{cut}_dialogue{ext}"
    elif record.media_type == "music":
        folder = project_root / "Audio"
        name = f"{cut}_audio{ext}" if cut else f"BGM{bgm_index:02d}{ext}"
    else:
        folder = project_root / "Reference"
        name = f"UNSUPPORTED_{record.source.name}"

    return unique_destination(folder / name, reserved)


def collect_assets(import_root: Path) -> tuple[list[AssetRecord], list[Path]]:
    records: list[AssetRecord] = []
    unsupported: list[Path] = []

    if not import_root.exists():
        return records, unsupported

    for path in sorted(import_root.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        media_type = classify(path)
        if media_type is None:
            unsupported.append(path)
            continue
        records.append(
            AssetRecord(
                source=path,
                extension=clean_extension(path),
                media_type=media_type,
                explicit_cut=detect_cut(path),
                source_relative=as_posix_relative(path, import_root.parent),
            )
        )

    return records, unsupported


def assign_cuts(records: list[AssetRecord]) -> None:
    for record in records:
        if record.explicit_cut:
            record.assigned_cut = record.explicit_cut
            record.assignment_reason = "filename contains CUT number"

    needs_manual_assignment = [
        record
        for record in records
        if record.assigned_cut is None and record.media_type in {"image", "video", "dialogue"}
    ]
    needs_manual_assignment.sort(key=lambda item: (created_time(item.source), item.source.name.lower()))
    for record in needs_manual_assignment:
        record.assignment_reason = "no CUT number; moved to Unsorted for manual assignment"

    music_without_cut = [
        record for record in records if record.assigned_cut is None and record.media_type == "music"
    ]
    music_without_cut.sort(key=lambda item: (created_time(item.source), item.source.name.lower()))
    for record in music_without_cut:
        record.assignment_reason = "music without CUT number assigned as BGM sequence"


def plan_destinations(records: list[AssetRecord], project_root: Path) -> None:
    reserved: set[Path] = set()
    bgm_index = 1
    for record in sorted(records, key=lambda item: (item.media_type, created_time(item.source), item.source.name.lower())):
        if record.media_type == "music" and record.assigned_cut is None:
            destination = destination_for(record, project_root, bgm_index, reserved)
            bgm_index += 1
        else:
            destination = destination_for(record, project_root, bgm_index, reserved)
        record.destination = destination
        record.destination_relative = as_posix_relative(destination, project_root)


def find_cut_entry(cut_list: dict, cut: str) -> dict | None:
    for entry in cut_list.get("cuts", []):
        if entry.get("cut") == cut:
            return entry
    return None


def append_unique(entry: dict, key: str, value: str) -> bool:
    values = entry.setdefault(key, [])
    if value not in values:
        values.append(value)
        return True
    return False


def remove_global_asset(data: dict, value: str) -> list[str]:
    updates: list[str] = []
    global_assets = data.get("globalAssets", {})
    for key, values in list(global_assets.items()):
        if isinstance(values, list) and value in values:
            values[:] = [item for item in values if item != value]
            updates.append(f"globalAssets.{key}: removed {value}")
    return updates


def update_cut_list(project_root: Path, moved_records: list[AssetRecord]) -> list[str]:
    cut_list_path = project_root / "CUT_LIST.json"
    if not cut_list_path.exists():
        return ["CUT_LIST.json not found; no updates applied"]

    data = json.loads(cut_list_path.read_text(encoding="utf-8"))
    global_assets = data.setdefault("globalAssets", {})
    updates: list[str] = []

    for record in moved_records:
        rel = record.destination_relative
        cut = record.assigned_cut
        entry = find_cut_entry(data, cut) if cut else None
        if record.source_relative:
            updates.extend(remove_global_asset(data, record.source_relative))

        if record.media_type == "video" and entry:
            previous = entry.get("asset")
            entry["asset"] = rel
            if previous == rel:
                updates.append(f"{cut}.asset unchanged: {rel}")
            elif previous:
                updates.append(f"{cut}.asset: {previous} -> {rel}")
            else:
                updates.append(f"{cut}.asset: {rel}")
        elif record.media_type == "dialogue" and entry:
            previous = entry.get("dialogueAsset")
            entry["dialogue"] = True
            entry["dialogueAsset"] = rel
            if previous == rel:
                updates.append(f"{cut}.dialogueAsset unchanged: {rel}")
            elif previous:
                updates.append(f"{cut}.dialogueAsset: {previous} -> {rel}")
            else:
                updates.append(f"{cut}.dialogueAsset: {rel}")
        elif record.media_type == "image" and entry:
            if append_unique(entry, "referenceAssets", rel):
                updates.append(f"{cut}.referenceAssets += {rel}")
            else:
                updates.append(f"{cut}.referenceAssets already contains {rel}")
        elif record.media_type == "music" and entry:
            if append_unique(entry, "audioAssets", rel):
                updates.append(f"{cut}.audioAssets += {rel}")
            else:
                updates.append(f"{cut}.audioAssets already contains {rel}")
        elif record.media_type == "music":
            if append_unique(global_assets, "audio", rel):
                updates.append(f"globalAssets.audio += {rel}")
            else:
                updates.append(f"globalAssets.audio already contains {rel}")
        elif record.assigned_cut is None:
            if append_unique(global_assets, "unsorted", rel):
                updates.append(f"globalAssets.unsorted += {rel}")
            else:
                updates.append(f"globalAssets.unsorted already contains {rel}")
        else:
            if append_unique(global_assets, "unassigned", rel):
                updates.append(f"globalAssets.unassigned += {rel}")
            else:
                updates.append(f"globalAssets.unassigned already contains {rel}")

    cut_list_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return updates


def summarize_unsorted(records: list[AssetRecord]) -> list[str]:
    return [
        f"{record.source_relative or record.source.name} -> {record.destination_relative}"
        for record in records
        if record.destination_relative.startswith("Unsorted/")
    ]


def summarize_assigned(records: list[AssetRecord]) -> list[str]:
    assigned: list[str] = []
    for record in records:
        if not record.assigned_cut:
            continue
        assigned.append(
            f"{record.assigned_cut}: {record.source_relative or record.source.name} -> {record.destination_relative}"
        )
    return assigned


def command_examples() -> list[str]:
    return [
        "python3 scripts/import_assets.py Projects/Distances --dry-run",
        "python3 scripts/import_assets.py Projects/Distances --apply",
        "python3 scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17",
        "python3 scripts/watch_import.py --project Distances --once --dry-run",
        "python3 scripts/watch_import.py --project Distances --once",
    ]


def print_post_summary(records: list[AssetRecord], cut_updates: list[str]) -> None:
    sections = [
        ("Unsortedへ送ったファイル一覧", summarize_unsorted(records)),
        ("CUTへ割り当てたファイル一覧", summarize_assigned(records)),
        ("CUT_LIST.jsonの更新内容", cut_updates or ["No CUT_LIST.json updates"]),
        ("実行コマンド例", command_examples()),
    ]
    for title, items in sections:
        print(f"\n{title}")
        if items:
            for item in items:
                print(f"- {item}")
        else:
            print("- なし")


def write_report(
    project_root: Path,
    records: list[AssetRecord],
    unsupported: list[Path],
    mode: str,
    import_root: Path,
    cut_updates: list[str] | None = None,
) -> None:
    report_path = project_root / "Edit" / "import_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Import Report",
        "",
        f"- Generated: {timestamp}",
        f"- Mode: {mode}",
        f"- Import folder: `{as_posix_relative(import_root, project_root) if import_root.exists() else 'Import'}`",
        f"- Planned assets: {len(records)}",
        f"- Unsupported files: {len(unsupported)}",
        "",
        "## Planned Moves",
        "",
        "| Source | Type | CUT | Destination | Status | Reason |",
        "|---|---|---|---|---|---|",
    ]

    for record in records:
        source = as_posix_relative(record.source, project_root)
        cut = record.assigned_cut or "-"
        destination = record.destination_relative or "-"
        lines.append(
            f"| `{source}` | {record.media_type} | {cut} | `{destination}` | {record.status} | {record.assignment_reason} |"
        )

    if unsupported:
        lines.extend(["", "## Unsupported Files", ""])
        for path in unsupported:
            lines.append(f"- `{as_posix_relative(path, project_root)}`")

    summary_sections = [
        ("Unsortedへ送ったファイル一覧", summarize_unsorted(records)),
        ("CUTへ割り当てたファイル一覧", summarize_assigned(records)),
        ("CUT_LIST.jsonの更新内容", cut_updates or ["No CUT_LIST.json updates"]),
        ("実行コマンド例", command_examples()),
    ]
    for title, items in summary_sections:
        lines.extend(["", f"## {title}", ""])
        if items:
            lines.extend(f"- `{item}`" if item.startswith("python3 ") else f"- {item}" for item in items)
        else:
            lines.append("- なし")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_plan(records: list[AssetRecord], unsupported: list[Path], mode: str, project_root: Path) -> None:
    print(f"Mode: {mode}")
    if not records:
        print("No supported assets found in Import/.")
    for record in records:
        source = as_posix_relative(record.source, project_root)
        cut = record.assigned_cut or "-"
        print(f"{record.media_type:8} {cut:5} {source} -> {record.destination_relative}")

    if unsupported:
        print("Unsupported files:")
        for path in unsupported:
            print(f"- {as_posix_relative(path, project_root)}")


def move_records(records: list[AssetRecord]) -> list[AssetRecord]:
    moved: list[AssetRecord] = []
    for record in records:
        if record.destination is None:
            record.status = "skipped: no destination"
            continue
        record.destination.parent.mkdir(parents=True, exist_ok=True)
        if not record.source.exists():
            record.status = "skipped: source missing"
            continue
        shutil.move(str(record.source), str(record.destination))
        record.status = "moved"
        moved.append(record)
    return moved


def normalize_cut(value: str) -> str:
    match = CUT_RE.fullmatch(value.strip())
    if match:
        return f"CUT{int(match.group(1)):02d}"
    match = re.fullmatch(r"(0?[1-9]|1[0-8])", value.strip())
    if match:
        return f"CUT{int(match.group(1)):02d}"
    raise ValueError(f"Invalid CUT number: {value}. Use CUT01-CUT18.")


def assign_existing_asset(project_root: Path, source_arg: str, cut_arg: str) -> int:
    cut = normalize_cut(cut_arg)
    source = (project_root / source_arg).resolve()
    if not source.exists() or not source.is_file():
        print(f"Source file not found: {source_arg}", file=sys.stderr)
        return 1
    try:
        source_relative = as_posix_relative(source, project_root)
    except ValueError:
        print(f"Source must be inside project folder: {source_arg}", file=sys.stderr)
        return 1

    media_type = classify(source)
    if media_type is None:
        print(f"Unsupported file type for assignment: {source_arg}", file=sys.stderr)
        return 1

    record = AssetRecord(
        source=source,
        extension=clean_extension(source),
        media_type=media_type,
        explicit_cut=cut,
        source_relative=source_relative,
        assigned_cut=cut,
        assignment_reason=f"manual assignment to {cut}",
    )
    plan_destinations([record], project_root)
    print_plan([record], [], "ASSIGN", project_root)
    moved = move_records([record])
    cut_updates = update_cut_list(project_root, moved)
    print_post_summary([record], cut_updates)
    write_report(project_root, [record], [], "ASSIGN", project_root / "Unsorted", cut_updates)
    print("Report written: Edit/import_report.md")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Project folder, for example Projects/Distances")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Show planned moves without moving files")
    mode.add_argument("--apply", action="store_true", help="Move files and update CUT_LIST.json")
    mode.add_argument("--assign", nargs=2, metavar=("SOURCE", "CUT"), help="Assign an Unsorted asset to a CUT, for example: --assign Unsorted/video_001.mp4 CUT17")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.project).resolve()
    import_root = project_root / "Import"

    if not project_root.exists():
        print(f"Project folder not found: {project_root}", file=sys.stderr)
        return 1

    if args.assign:
        source_arg, cut_arg = args.assign
        return assign_existing_asset(project_root, source_arg, cut_arg)

    mode = "APPLY" if args.apply else "DRY-RUN"

    records, unsupported = collect_assets(import_root)
    assign_cuts(records)
    plan_destinations(records, project_root)

    print_plan(records, unsupported, mode, project_root)

    cut_updates = ["dry-run: CUT_LIST.jsonは更新しません"]
    if args.apply:
        moved = move_records(records)
        cut_updates = update_cut_list(project_root, moved)

    print_post_summary(records, cut_updates)
    write_report(project_root, records, unsupported, mode, import_root, cut_updates)
    print("Report written: Edit/import_report.md")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
