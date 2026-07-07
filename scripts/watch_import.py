#!/usr/bin/env python3
"""Watch user folders and import new assets into a FLYSTAR77 project.

The watcher copies new files into Import/ and then runs import_assets.py.
Files without a CUT number are handled by import_assets.py; videos, images,
and dialogue audio go to Unsorted/ until the user assigns a CUT.

Examples:
  python scripts/watch_import.py --project Distances --once
  python scripts/watch_import.py --project Distances
  python scripts/watch_import.py --config config.json --project Distances --dry-run --once
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov", ".wav", ".mp3"}
STATE_FILE = "Edit/watch_state.json"
REPORT_FILE = "Edit/watch_import_report.md"


@dataclass
class WatchConfig:
    root: Path
    project_name: str
    project_root: Path
    watch_folders: list[Path]
    poll_seconds: int
    settle_seconds: int
    import_mode: str
    recursive: bool
    run_import_assets: bool


@dataclass
class Candidate:
    source: Path
    size: int
    mtime_ns: int


def expand_path(value: str, root: Path) -> Path:
    expanded = Path(value).expanduser()
    if not expanded.is_absolute():
        expanded = root / expanded
    return expanded.resolve()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_config(config_path: Path, project_name: str | None) -> WatchConfig:
    root = config_path.resolve().parent
    data = load_json(config_path)
    watcher = data.get("watcher", {})
    projects = data.get("projects", [])

    selected: dict[str, Any] | None = None
    for project in projects:
        if project_name is None or project.get("name") == project_name:
            selected = project
            break

    if selected is None:
        names = ", ".join(project.get("name", "-") for project in projects)
        raise SystemExit(f"Project not found in config: {project_name}. Available: {names}")

    selected_name = str(selected.get("name", project_name or ""))
    project_root = expand_path(str(selected["projectPath"]), root)
    watch_folders = [expand_path(str(path), root) for path in selected.get("watchFolders", [])]

    return WatchConfig(
        root=root,
        project_name=selected_name,
        project_root=project_root,
        watch_folders=watch_folders,
        poll_seconds=int(selected.get("pollSeconds", watcher.get("pollSeconds", 5))),
        settle_seconds=int(selected.get("settleSeconds", watcher.get("settleSeconds", 3))),
        import_mode=str(selected.get("importMode", watcher.get("importMode", "apply"))),
        recursive=bool(selected.get("recursive", watcher.get("recursive", True))),
        run_import_assets=bool(selected.get("runImportAssets", watcher.get("runImportAssets", True))),
    )


def file_signature(path: Path) -> tuple[int, int]:
    stat = path.stat()
    return stat.st_size, stat.st_mtime_ns


def is_supported(path: Path) -> bool:
    return path.is_file() and not path.name.startswith(".") and path.suffix.lower() in SUPPORTED_EXTENSIONS


def iter_files(folder: Path, recursive: bool) -> list[Path]:
    if not folder.exists():
        return []
    iterator = folder.rglob("*") if recursive else folder.iterdir()
    return sorted(path for path in iterator if is_supported(path))


def is_settled(path: Path, settle_seconds: int) -> bool:
    try:
        mtime = path.stat().st_mtime
    except FileNotFoundError:
        return False
    return (time.time() - mtime) >= settle_seconds


def load_state(project_root: Path) -> dict[str, Any]:
    state = load_json(project_root / STATE_FILE)
    state.setdefault("processed", {})
    state.setdefault("copied", [])
    return state


def source_key(path: Path) -> str:
    return str(path.resolve())


def is_processed(path: Path, state: dict[str, Any]) -> bool:
    try:
        size, mtime_ns = file_signature(path)
    except FileNotFoundError:
        return False
    processed = state.get("processed", {}).get(source_key(path))
    return bool(processed and processed.get("size") == size and processed.get("mtimeNs") == mtime_ns)


def mark_processed(source: Path, copied_to: Path, project_root: Path, state: dict[str, Any]) -> None:
    size, mtime_ns = file_signature(source)
    state.setdefault("processed", {})[source_key(source)] = {
        "size": size,
        "mtimeNs": mtime_ns,
        "copiedTo": copied_to.relative_to(project_root).as_posix(),
        "processedAt": datetime.now().isoformat(timespec="seconds"),
    }
    state.setdefault("copied", []).append(
        {
            "source": str(source),
            "copiedTo": copied_to.relative_to(project_root).as_posix(),
            "processedAt": datetime.now().isoformat(timespec="seconds"),
        }
    )


def unique_destination(path: Path) -> Path:
    candidate = path
    index = 2
    while candidate.exists():
        candidate = path.with_name(f"{path.stem}_take{index:02d}{path.suffix}")
        index += 1
    return candidate


def discover_candidates(config: WatchConfig, state: dict[str, Any]) -> tuple[list[Candidate], list[str]]:
    candidates: list[Candidate] = []
    notes: list[str] = []

    for folder in config.watch_folders:
        if not folder.exists():
            notes.append(f"Watch folder not found: {folder}")
            continue
        for path in iter_files(folder, config.recursive):
            if is_processed(path, state):
                continue
            if not is_settled(path, config.settle_seconds):
                notes.append(f"Waiting for file to settle: {path}")
                continue
            size, mtime_ns = file_signature(path)
            candidates.append(Candidate(source=path, size=size, mtime_ns=mtime_ns))

    return candidates, notes


def copy_candidates(config: WatchConfig, candidates: list[Candidate], state: dict[str, Any], dry_run: bool) -> list[dict[str, str]]:
    import_root = config.project_root / "Import"
    import_root.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, str]] = []

    for candidate in candidates:
        destination = unique_destination(import_root / candidate.source.name)
        if not dry_run:
            shutil.copy2(candidate.source, destination)
            mark_processed(candidate.source, destination, config.project_root, state)
        copied.append(
            {
                "source": str(candidate.source),
                "destination": destination.relative_to(config.project_root).as_posix(),
                "status": "planned" if dry_run else "copied",
            }
        )

    return copied


def run_import_assets(config: WatchConfig, dry_run: bool) -> tuple[int, str]:
    mode = "--dry-run" if dry_run or config.import_mode != "apply" else "--apply"
    command = [
        sys.executable,
        "scripts/import_assets.py",
        config.project_root.relative_to(config.root).as_posix(),
        mode,
    ]
    result = subprocess.run(
        command,
        cwd=config.root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def write_report(
    config: WatchConfig,
    copied: list[dict[str, str]],
    notes: list[str],
    dry_run: bool,
    import_output: str,
    import_return_code: int | None,
) -> None:
    report_path = config.project_root / REPORT_FILE
    report_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "DRY-RUN" if dry_run else "APPLY"

    lines = [
        "# Watch Import Report",
        "",
        f"- Generated: {timestamp}",
        f"- Mode: {mode}",
        f"- Project: {config.project_name}",
        f"- Import mode: {config.import_mode}",
        f"- Poll seconds: {config.poll_seconds}",
        f"- Settle seconds: {config.settle_seconds}",
        "",
        "## Watch Folders",
        "",
    ]
    lines.extend(f"- `{folder}`" for folder in config.watch_folders)

    lines.extend(
        [
            "",
            "## Copied Assets",
            "",
            "| Source | Destination | Status |",
            "|---|---|---|",
        ]
    )
    if copied:
        for item in copied:
            lines.append(f"| `{item['source']}` | `{item['destination']}` | {item['status']} |")
    else:
        lines.append("| - | - | no new supported assets |")

    if notes:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {note}" for note in notes)

    if import_return_code is not None:
        lines.extend(
            [
                "",
                "## import_assets.py",
                "",
                f"- Return code: {import_return_code}",
                "",
                "```text",
                import_output.rstrip(),
                "```",
            ]
        )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_once(config: WatchConfig, dry_run: bool) -> int:
    state = load_state(config.project_root)
    candidates, notes = discover_candidates(config, state)
    copied = copy_candidates(config, candidates, state, dry_run=dry_run)

    import_return_code: int | None = None
    import_output = ""
    if config.run_import_assets and (copied or dry_run):
        import_return_code, import_output = run_import_assets(config, dry_run=dry_run)

    if not dry_run:
        write_json(config.project_root / STATE_FILE, state)

    write_report(config, copied, notes, dry_run, import_output, import_return_code)

    for item in copied:
        print(f"{item['status']}: {item['source']} -> {item['destination']}")
    if not copied:
        print("No new supported assets found.")
    for note in notes:
        print(note)
    if import_return_code is not None:
        print(import_output.rstrip())
    print("Report written: Edit/watch_import_report.md")

    return import_return_code or 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.json", help="Watcher config JSON")
    parser.add_argument("--project", default=None, help="Project name in config.json")
    parser.add_argument("--once", action="store_true", help="Run one scan and exit")
    parser.add_argument("--dry-run", action="store_true", help="Do not copy files or update state")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(Path(args.config), args.project)

    if args.once:
        return run_once(config, dry_run=args.dry_run)

    print(f"Watching project {config.project_name}. Press Ctrl+C to stop.")
    while True:
        run_once(config, dry_run=args.dry_run)
        time.sleep(config.poll_seconds)


if __name__ == "__main__":
    raise SystemExit(main())
