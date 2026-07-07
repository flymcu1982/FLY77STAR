#!/usr/bin/env python3
"""Generate Palmier edit_project.json from CUT_LIST.json and EDIT_PLAN.md."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MEDIA_SUFFIXES = {
    "video": {".mp4", ".mov"},
    "image": {".png", ".jpg", ".jpeg", ".webp"},
    "audio": {".wav", ".mp3"},
}

HANDOFF_MEDIA_DIRS = {"CUT", "Audio", "Dialogue", "Reference"}
STAGING_MEDIA_DIRS = {"Import", "Unsorted", "Watch"}

DIALOGUE_HOLDS = {
    "CUT06": {
        "preRollSeconds": 0.5,
        "postHoldSeconds": 1.0,
        "priority": "emotion_change",
        "notes": "声の出だしは口元だけでなく、表情が変わる瞬間へ合わせる。",
    },
    "CUT12": {
        "preRollSeconds": 0.5,
        "postHoldSeconds": 1.5,
        "priority": "natural_voice_front",
        "notes": "BGMを少し下げ、声を前に出しすぎず自然に聞かせる。",
    },
    "CUT17": {
        "preRollSeconds": 1.0,
        "postHoldSeconds": 2.0,
        "priority": "afterglow",
        "notes": "セリフ後2秒以上ホールドし、余韻を急いで切らない。",
    },
}


def parse_timecode(value: str) -> float:
    value = value.strip()
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    return float(value)


def format_timecode(seconds: float) -> str:
    minutes = int(seconds // 60)
    rest = seconds - minutes * 60
    return f"{minutes:02d}:{rest:04.1f}"


def parse_edit_plan_table(edit_plan_path: Path) -> dict[str, dict[str, Any]]:
    if not edit_plan_path.exists():
        return {}

    rows: dict[str, dict[str, Any]] = {}
    for line in edit_plan_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| CUT"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"CUT\d{2}", cells[0]):
            continue

        start_seconds = None
        end_seconds = None
        timeline = cells[1]
        if "-" in timeline:
            start_raw, end_raw = timeline.split("-", 1)
            start_seconds = parse_timecode(start_raw)
            end_seconds = parse_timecode(end_raw)

        rows[cells[0]] = {
            "timeline": timeline,
            "startSeconds": start_seconds,
            "endSeconds": end_seconds,
            "durationLabel": cells[2],
            "role": cells[3],
            "editTiming": cells[4],
            "dialogueSyncPoint": cells[5],
        }

    return rows


def detect_media(project_root: Path) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    staging_files: list[dict[str, Any]] = []
    bgm_candidates: list[str] = []
    ambient_candidates: list[str] = []

    for path in sorted(project_root.rglob("*")):
        if not path.is_file() or path.name == ".DS_Store":
            continue

        relative = path.relative_to(project_root).as_posix()
        suffix = path.suffix.lower()
        media_type = None
        for candidate_type, suffixes in MEDIA_SUFFIXES.items():
            if suffix in suffixes:
                media_type = candidate_type
                break

        if media_type is None:
            continue

        top_level = relative.split("/", 1)[0]
        entry = {
            "path": relative,
            "type": media_type,
            "exists": True,
        }

        if top_level in STAGING_MEDIA_DIRS:
            staging_files.append(entry)
            continue

        if top_level not in HANDOFF_MEDIA_DIRS:
            continue

        files.append(entry)

        lower_name = path.name.lower()
        if media_type == "audio" and "dialogue" not in lower_name and "voice" not in lower_name:
            bgm_candidates.append(relative)
            if "ambient" in lower_name or "room" in lower_name or "env" in lower_name:
                ambient_candidates.append(relative)

    return {
        "files": files,
        "stagingFiles": staging_files,
        "bgmCandidates": bgm_candidates,
        "ambientCandidates": ambient_candidates,
    }


def transition_for(cut_name: str) -> dict[str, Any]:
    transition_in = {"type": "cut", "durationSeconds": 0.0}
    transition_out = {"type": "cut", "durationSeconds": 0.0}

    if cut_name == "CUT01":
        transition_in = {"type": "none", "durationSeconds": 0.0}
        transition_out = {
            "type": "short_fade",
            "durationSeconds": 0.3,
            "note": "導入の空気を残すため、終端のみ短いフェード可。",
        }
    elif cut_name == "CUT05":
        transition_out = {
            "type": "breath_cut",
            "durationSeconds": 0.0,
            "note": "CUT06へ息継ぎでつなぐ。",
        }
    elif cut_name == "CUT11":
        transition_out = {
            "type": "pause_cut",
            "durationSeconds": 0.0,
            "note": "CUT12の前に0.3秒ほど間を残す。",
        }
    elif cut_name == "CUT17":
        transition_out = {
            "type": "held_cut",
            "durationSeconds": 0.0,
            "note": "余韻を切らず、表情と沈黙を最後まで残す。",
        }
    elif cut_name == "CUT18":
        transition_out = {
            "type": "fade_to_black",
            "durationSeconds": 1.2,
            "note": "映像、BGM、環境音を同時に自然に落とす。",
        }

    return {"in": transition_in, "out": transition_out}


def fade_for(cut_name: str) -> dict[str, float]:
    fade = {
        "videoInSeconds": 0.0,
        "videoOutSeconds": 0.0,
        "clipAudioInSeconds": 0.0,
        "clipAudioOutSeconds": 0.0,
        "bgmOutSeconds": 0.0,
        "ambientOutSeconds": 0.0,
    }

    if cut_name == "CUT01":
        fade["videoOutSeconds"] = 0.3
        fade["clipAudioOutSeconds"] = 0.2
    elif cut_name == "CUT18":
        fade["videoOutSeconds"] = 1.2
        fade["clipAudioOutSeconds"] = 1.2
        fade["bgmOutSeconds"] = 1.2
        fade["ambientOutSeconds"] = 1.2

    return fade


def bgm_sync_for(cut_name: str) -> dict[str, Any]:
    if cut_name == "CUT02":
        return {
            "mode": "entry",
            "targetGainDb": -24.0,
            "notes": "BGMの入りを視線の動きに合わせ、作品の距離感を作る。",
        }
    if cut_name in {"CUT06", "CUT12"}:
        return {
            "mode": "duck_under_dialogue",
            "targetGainDb": -30.0,
            "notes": "セリフを邪魔しない音量まで自然に下げる。",
        }
    if cut_name == "CUT15":
        return {
            "mode": "expand",
            "targetGainDb": -22.0,
            "notes": "Blue Hourの空気感に合わせて少しだけ広げる。",
        }
    if cut_name == "CUT17":
        return {
            "mode": "duck_then_sink",
            "targetGainDb": -31.0,
            "notes": "セリフ中は静かに、後半からCUT18へ向けて自然に沈める。",
        }
    if cut_name == "CUT18":
        return {
            "mode": "final_fade",
            "targetGainDb": -36.0,
            "notes": "終端でBGM、環境音、映像を同時にフェードアウト。",
        }
    return {
        "mode": "thin_bed",
        "targetGainDb": -26.0,
        "notes": "全体に薄く敷き、感情と環境音を優先する。",
    }


def environment_for(cut_name: str, dialogue_enabled: bool) -> dict[str, Any]:
    level = -28.0 if not dialogue_enabled else -32.0
    notes = "環境音を完全に消さず、部屋鳴りや空気を薄く残す。"

    if cut_name == "CUT09":
        level = -25.0
        notes = "手元や小物の近さを出すため、環境音を少し近くする。"
    elif cut_name == "CUT18":
        level = -30.0
        notes = "肩を寄せる動作後の1秒を残し、終端で自然に落とす。"

    return {
        "keep": True,
        "source": "embedded_clip_audio_or_ambient_track",
        "targetGainDb": level,
        "notes": notes,
    }


def build_sequence(
    project_root: Path,
    cut_list: dict[str, Any],
    edit_rows: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    sequence: list[dict[str, Any]] = []
    missing_assets: list[str] = []
    running_seconds = 0.0

    for index, cut in enumerate(cut_list.get("cuts", []), start=1):
        cut_name = cut["cut"]
        edit_row = edit_rows.get(cut_name, {})
        duration = float(cut.get("recommendedSeconds", 0))
        start_seconds = edit_row.get("startSeconds")
        end_seconds = edit_row.get("endSeconds")

        if start_seconds is None:
            start_seconds = running_seconds
        if end_seconds is None:
            end_seconds = start_seconds + duration
        running_seconds = end_seconds

        asset = cut.get("asset")
        asset_exists = bool(asset and (project_root / asset).exists())
        if asset and not asset_exists:
            missing_assets.append(asset)

        dialogue_asset = cut.get("dialogueAsset")
        dialogue_asset_exists = bool(dialogue_asset and (project_root / dialogue_asset).exists())
        if dialogue_asset and not dialogue_asset_exists:
            missing_assets.append(dialogue_asset)

        dialogue_config = DIALOGUE_HOLDS.get(cut_name, {})
        dialogue_enabled = bool(cut.get("dialogue"))
        pre_roll = dialogue_config.get("preRollSeconds", 0.0)
        dialogue_sync = {
            "enabled": dialogue_enabled,
            "asset": dialogue_asset,
            "assetExists": dialogue_asset_exists,
            "track": "A1_dialogue",
            "timelineStartSeconds": round(start_seconds + pre_roll, 3) if dialogue_enabled else None,
            "preRollSeconds": pre_roll if dialogue_enabled else 0.0,
            "postHoldSeconds": dialogue_config.get("postHoldSeconds", 0.0) if dialogue_enabled else 0.0,
            "priority": dialogue_config.get("priority") if dialogue_enabled else None,
            "syncPoint": edit_row.get("dialogueSyncPoint", "セリフなし。"),
            "notes": dialogue_config.get("notes") if dialogue_enabled else edit_row.get("dialogueSyncPoint", ""),
        }

        sequence.append(
            {
                "order": index,
                "cut": cut_name,
                "asset": asset,
                "assetExists": asset_exists,
                "track": "V1_main",
                "startSeconds": round(start_seconds, 3),
                "endSeconds": round(end_seconds, 3),
                "startTimecode": format_timecode(start_seconds),
                "endTimecode": format_timecode(end_seconds),
                "recommendedSeconds": duration,
                "role": edit_row.get("role", cut.get("role", "")),
                "editTiming": edit_row.get("editTiming", ""),
                "transition": transition_for(cut_name),
                "fade": fade_for(cut_name),
                "bgmSync": bgm_sync_for(cut_name),
                "dialogueSync": dialogue_sync,
                "environment": environment_for(cut_name, dialogue_enabled),
            }
        )

    return sequence, missing_assets


def build_edit_project(project_root: Path) -> dict[str, Any]:
    cut_list_path = project_root / "CUT_LIST.json"
    edit_plan_path = project_root / "Edit" / "EDIT_PLAN.md"
    project_json_path = project_root / "project.json"

    cut_list = json.loads(cut_list_path.read_text(encoding="utf-8"))
    project_json = json.loads(project_json_path.read_text(encoding="utf-8"))
    edit_rows = parse_edit_plan_table(edit_plan_path)
    media = detect_media(project_root)
    sequence, missing_assets = build_sequence(project_root, cut_list, edit_rows)
    project_name = cut_list.get("projectName", project_json.get("projectName", project_root.name))

    return {
        "schema": "flystar77.palmier.edit_project.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "studio": project_json.get("studio", "FLYSTAR77 STUDIO"),
        "project": {
            "name": project_name,
            "version": project_json.get("version", "v1.0"),
            "status": project_json.get("status"),
            "primaryFormat": project_json.get("format", {}).get("primary", "9:16"),
            "releaseTargets": project_json.get("format", {}).get("releaseTargets", []),
        },
        "sourceDocuments": {
            "editPlan": "Edit/EDIT_PLAN.md",
            "cutList": "CUT_LIST.json",
            "project": "project.json",
            "palmierHandoff": "Edit/PALMIER_HANDOFF.md",
        },
        "timeline": {
            "name": f"{project_name}_main_{cut_list.get('totalRecommendedSeconds', 90):g}s",
            "fps": 30,
            "resolution": {
                "width": 1080,
                "height": 1920,
                "aspectRatio": "9:16",
            },
            "totalRecommendedSeconds": cut_list.get("totalRecommendedSeconds", 90),
            "tracks": [
                {"id": "V1_main", "type": "video", "purpose": "CUT01-CUT18 main picture"},
                {"id": "A1_dialogue", "type": "audio", "purpose": "CUT06/CUT12/CUT17 dialogue"},
                {"id": "A2_bgm", "type": "audio", "purpose": "thin BGM bed and fades"},
                {"id": "A3_environment", "type": "audio", "purpose": "embedded ambience and room tone"},
            ],
            "sequence": sequence,
        },
        "audioPlan": {
            "bgm": {
                "track": "A2_bgm",
                "assetCandidates": media["bgmCandidates"],
                "assetRequired": False,
                "globalRule": "BGMは全体に薄く敷き、CUT06、CUT12、CUT17では下げる。",
                "finalFadeStartsAtCut": "CUT18",
            },
            "dialogue": [
                item["dialogueSync"]
                | {
                    "cut": item["cut"],
                    "startTimecode": item["startTimecode"],
                }
                for item in sequence
                if item["dialogueSync"]["enabled"]
            ],
            "environment": {
                "track": "A3_environment",
                "assetCandidates": media["ambientCandidates"],
                "useEmbeddedClipAudio": True,
                "globalRule": "環境音は完全に消さない。セリフ箇所では薄く下げる。",
            },
        },
        "transitionPlan": {
            "default": "cut",
            "exceptions": [
                {"cut": "CUT01", "type": "short_fade", "durationSeconds": 0.3},
                {"cut": "CUT18", "type": "fade_to_black", "durationSeconds": 1.2},
            ],
        },
        "colorPlan": {
            "look": "Kodak Vision3",
            "timeOfDay": "Blue Hour",
            "skinTone": "Warm Skin",
            "contrast": "Natural Contrast",
        },
        "export": {
            "draft": {
                "path": f"Projects/{project_name}/Export/{project_name}_draft_9x16.mp4",
                "format": "mp4",
                "codec": "h264",
                "resolution": "1080x1920",
                "fps": 30,
                "audioSampleRateHz": 48000,
            },
            "final": {
                "path": f"Exports/{project_name}_final_9x16.mp4",
                "format": "mp4",
                "codec": "h264",
                "resolution": "1080x1920",
                "fps": 30,
                "audioLoudnessTargetLufs": -14,
            },
            "platforms": [
                {"name": "TikTok", "aspectRatio": "9:16", "resolution": "1080x1920"},
                {"name": "Instagram Reels", "aspectRatio": "9:16", "resolution": "1080x1920"},
                {"name": "YouTube", "aspectRatio": "9:16", "resolution": "1080x1920"},
            ],
        },
        "palmierInstructions": [
            "CUT01からCUT18まで順番通りにV1_mainへ配置する。",
            "recommendedSecondsを基準に尺を調整し、セリフ後は急に切らない。",
            "CUT06、CUT12、CUT17はdialogueSyncを優先してA1_dialogueへ配置する。",
            "BGMはA2_bgmへ薄く敷き、セリフ箇所ではduck_under_dialogueに従って下げる。",
            "環境音はA3_environmentへ残し、完全な無音を避ける。",
            "CUT17の余韻とCUT18の肩寄せ後1秒を必ず残す。",
            "書き出し前にQC/QC_CHECKLIST.mdを確認する。",
        ],
        "mediaManifest": media,
        "missingAssets": sorted(set(missing_assets)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Project folder, for example Projects/Distances")
    parser.add_argument(
        "--output",
        default=None,
        help="Output JSON path. Defaults to PROJECT/Edit/edit_project.json",
    )
    args = parser.parse_args()

    project_root = Path(args.project_path).resolve()
    if not project_root.exists():
        print(f"Project path not found: {project_root}", file=sys.stderr)
        return 1

    output_path = Path(args.output).resolve() if args.output else project_root / "Edit" / "edit_project.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    edit_project = build_edit_project(project_root)
    output_path.write_text(
        json.dumps(edit_project, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Generated {output_path}")
    print(f"Missing assets: {len(edit_project['missingAssets'])}")
    for item in edit_project["missingAssets"]:
        print(f"- {item}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
