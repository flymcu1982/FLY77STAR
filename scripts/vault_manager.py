#!/usr/bin/env python3
"""FLYSTAR77 Obsidian Vault Manager.

Routes a decided-today production item into the right note under
Obsidian_Vault/, avoiding duplicates, auto-linking known entity names,
leaving a one-line pointer in the Daily Studio Report, and keeping a
changelog. Operates only on Obsidian_Vault/; it does not touch the
GitHub production folders under Projects/.

Categorization (character / costume / mv / prompt / discovery / decision)
is a judgment call this script does not make for you -- decide it
yourself (or have an AI read the raw text and decide), then call this
script once per decided item.

Examples:
  python scripts/vault_manager.py registry

  # Character Bible
  python scripts/vault_manager.py file --category character --target MIU \\
      --text "衣装は白ヘアバンドに変更"

  # Costume Bible (needs an existing Character or Project to attach to)
  python scripts/vault_manager.py file --category costume --character MIU --project WAKE_UP \\
      --text "ウェイトレス衣装、ピンク系" --reason "3人の中で一番華やかな色を求められたため"

  # MV Bible (--section targets 脚本/絵コンテ/CUT/プロンプト/制作ログ)
  python scripts/vault_manager.py file --category mv --target WAKE_UP --section CUT \\
      --text "CUT12はローラースケートのワイドショットに変更"

  # Prompt Library
  python scripts/vault_manager.py file --category prompt --target "MIU笑顔プロンプト" \\
      --character MIU --text "smiling, warm lighting, East Asian Japanese, Soul ID固定"

  # Discovery (--kind is required: 発見/失敗/改善点/アイデア/次回試したい)
  python scripts/vault_manager.py file --category discovery --target "プロンプトのコツ" --kind 発見 \\
      --text "ネガティブプロンプトにdriftを入れると顔ブレが減る"

  # Decision Log (--outcome is required: 採用/却下)
  python scripts/vault_manager.py file --category decision --target "衣装カラー案" --outcome 採用 \\
      --text "MIU=ピンク/AYA=ブルー/NANA=イエロー" --reason "3人の見分けやすさを優先"

  # Daily Log (今日やったこと/完成したこと/次回やること)
  python scripts/vault_manager.py daily-log --did "CUT01-05を生成" --done "MIU衣装確定" --next "CUT06-10"

  python scripts/vault_manager.py next-action --project WAKE_UP --add "衣装の最終レンダリング"
  python scripts/vault_manager.py next-action --project WAKE_UP --done "配色案"
  python scripts/vault_manager.py changelog --limit 10
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
AI_COMMENT_MARKER = "## AI社員から一言"

DISCOVERY_KINDS = ["発見", "失敗", "改善点", "アイデア", "次回試したい"]
DECISION_OUTCOMES = ["採用", "却下"]
MV_SECTIONS = ["脚本", "絵コンテ", "CUT", "プロンプト", "制作ログ"]

# Daily Studio Report auto-record sections, keyed by the daily-log flag that targets them.
DAILY_SECTIONS = {
    "did": "今日やったこと(自動記録)",
    "done": "完成したこと(自動記録)",
    "next": "次回やること(自動記録)",
}


@dataclass
class Entity:
    name: str
    path: Path
    kind: str


def now_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def safe_name(value: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", value.strip())
    cleaned = cleaned.replace(" ", "_")
    return cleaned or "untitled"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    data: dict = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
            data[key] = items
        else:
            data[key] = value.strip('"').strip("'")
    return data, text[match.end():]


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            return stripped[2:].strip()
    return fallback


def build_hub_registry(vault_root: Path) -> dict[str, Entity]:
    registry: dict[str, Entity] = {}
    templates_root = vault_root / "99_Templates"
    for md_path in vault_root.rglob("*.md"):
        if md_path.name.startswith("_"):
            continue
        if templates_root in md_path.parents:
            continue
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            continue
        data, body = parse_frontmatter(text)
        if "type" not in data:
            continue
        title = extract_title(body, md_path.stem)
        for name in [title] + list(data.get("aliases", [])):
            key = name.strip().lower().replace("_", " ")
            if key and key not in registry:
                registry[key] = Entity(name=title, path=md_path, kind=data["type"])
    return registry


def parse_glossary(vault_root: Path) -> dict[str, Entity]:
    glossary_path = vault_root / "00_Start_Here" / "用語集.md"
    registry: dict[str, Entity] = {}
    if not glossary_path.exists():
        return registry
    lines = glossary_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines) - 1:
        term = lines[i].strip()
        desc = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if term and not term.startswith("#") and desc.startswith("（") and desc.endswith("）"):
            key = term.lower()
            registry.setdefault(key, Entity(name=term, path=glossary_path, kind="term"))
            i += 2
            continue
        i += 1
    return registry


def full_registry(vault_root: Path) -> dict[str, Entity]:
    registry = build_hub_registry(vault_root)
    for key, entity in parse_glossary(vault_root).items():
        registry.setdefault(key, entity)
    return registry


def find_unlinked_occurrence(text: str, name: str) -> int:
    start = 0
    while True:
        idx = text.find(name, start)
        if idx == -1:
            return -1
        before = text[:idx]
        if before.count("[[") <= before.count("]]"):
            return idx
        start = idx + 1


def auto_link(text: str, registry: dict[str, Entity], exclude_path: Path | None = None) -> str:
    seen: dict[str, Entity] = {}
    for entity in registry.values():
        if entity.path == exclude_path:
            continue
        seen.setdefault(entity.name, entity)
    for entity in sorted(seen.values(), key=lambda e: len(e.name), reverse=True):
        idx = find_unlinked_occurrence(text, entity.name)
        if idx == -1:
            continue
        text = text[:idx] + f"[[{entity.name}]]" + text[idx + len(entity.name):]
    return text


def append_bullet(content: str, marker: str, bullet: str, create_after: str | None = None) -> str:
    """Append `bullet` (e.g. '- text') to the section under `marker` (e.g. '## Heading').

    Rebuilds the section's bullet list from scratch each time so repeated appends can't
    accumulate stray blank lines into a "loose" list. If `marker` is absent, creates the
    section -- before `create_after` if that marker is present, otherwise at the end.
    """
    if marker in content:
        start = content.index(marker)
        after_heading = content.index("\n", start) + 1
        next_match = re.search(r"^#{1,2} ", content[after_heading:], re.MULTILINE)
        section_end = after_heading + next_match.start() if next_match else len(content)
        bullets = re.findall(r"^-.*$", content[after_heading:section_end], re.MULTILINE)
        bullets.append(bullet)
        body = "\n" + "\n".join(bullets) + "\n"
        if section_end < len(content):
            body += "\n"
        return content[:start] + marker + "\n" + body + content[section_end:]

    new_section = f"{marker}\n\n{bullet}\n\n"
    if create_after and create_after in content:
        idx = content.index(create_after)
        return content[:idx] + new_section + content[idx:]
    return content.rstrip("\n") + "\n\n" + marker + "\n\n" + bullet + "\n"


def ensure_related_link(content: str, field: str, name: str | None) -> str:
    """Ensure `[[name]]` is listed on the '- field: ...' line under '## 関連'. No-op if
    `name` is falsy, the field line isn't found, or the link is already there."""
    if not name:
        return content
    pattern = re.compile(rf"^- {re.escape(field)}:(.*)$", re.MULTILINE)
    match = pattern.search(content)
    if not match:
        return content
    existing = match.group(1).strip()
    link = f"[[{name}]]"
    if name in existing:
        return content
    new_value = f"{existing}, {link}" if existing else link
    new_line = f"- {field}: {new_value}"
    return content[:match.start()] + new_line + content[match.end():]


def append_to_section(path: Path, heading: str, entry: str, new_file_title: str | None = None) -> bool:
    """Append `entry` as a bullet under `## heading`, creating the note/section if missing.

    Returns False (no-op) if an identical entry already exists anywhere in the note.
    """
    marker = f"## {heading}"
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        content = f"# {new_file_title or path.stem}\n"

    if entry.strip() in content:
        return False

    content = append_bullet(content, marker, f"- {entry}")
    path.write_text(content, encoding="utf-8")
    return True


def related_block() -> str:
    return (
        "## 関連\n\n"
        "- Knowledge:\n"
        "- Projects:\n"
        "- People:\n"
        "- Characters:\n"
        "- AI Employees:\n"
        "- Prompt:\n"
        "- GitHub(正本):\n"
    )


def create_hub_note(path: Path, name: str, type_: str, aliases: list[str]) -> bool:
    if path.exists():
        return False
    alias_str = ", ".join(aliases)
    frontmatter = f"---\naliases: [{alias_str}]\ntype: {type_}\n---\n\n"
    if type_ == "project":
        body = (
            f"# {name}\n\n"
            "(自動生成。概要は追って整備する)\n\n"
            "## 脚本\n\n"
            "## 絵コンテ\n\n"
            "## CUT\n\n"
            "## プロンプト\n\n"
            f"{related_block()}"
        )
    else:
        body = f"# {name}\n\n(自動生成。世界観・詳細は追って整備する)\n\n{related_block()}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter + body, encoding="utf-8")
    return True


def resolve_or_create_entity_note(
    vault_root: Path, registry: dict[str, Entity], category: str, target: str, aliases: list[str]
) -> Path:
    key = target.strip().lower().replace("_", " ")
    if key in registry and registry[key].kind in ("character", "project"):
        return registry[key].path
    if category == "character":
        path = vault_root / "10_Characters" / f"{safe_name(target)}.md"
        create_hub_note(path, target, "character", aliases)
        return path
    if category == "mv":
        path = vault_root / "06_Projects" / safe_name(target) / "Overview.md"
        create_hub_note(path, target, "project", aliases)
        return path
    raise SystemExit(f"unknown category: {category}")


def resolve_existing_entity(registry: dict[str, Entity], name: str, kinds: tuple[str, ...]) -> Entity | None:
    key = name.strip().lower().replace("_", " ")
    entity = registry.get(key)
    if entity and entity.kind in kinds:
        return entity
    return None


# ---------------------------------------------------------------------------
# Character Bible / MV Bible: file() dispatches into resolve_or_create_entity_note()
# and appends to a section within that note (see cmd_file).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Costume Bible: one dedicated note per costume design under 11_Costume_Bible/,
# cross-linked to (not duplicated into) the Character/Project it belongs to.
# ---------------------------------------------------------------------------


def costume_bible_path(vault_root: Path, title: str) -> Path:
    return vault_root / "11_Costume_Bible" / f"{safe_name(title)[:60]}.md"


def write_costume_entry(
    path: Path, title: str, character: str | None, project: str | None, text: str, reason: str | None
) -> bool:
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = (
            "---\naliases: []\ntype: costume\n---\n\n"
            f"# {title}\n\n"
            "## 概要\n\n"
            "## 採用理由\n\n"
            f"{related_block()}"
        )
    changed = False
    if text.strip() not in content:
        content = append_bullet(content, "## 概要", f"- {text}")
        changed = True
    if reason and reason.strip() not in content:
        content = append_bullet(content, "## 採用理由", f"- {reason}")
        changed = True
    content = ensure_related_link(content, "Characters", character)
    content = ensure_related_link(content, "Projects", project)
    if not changed:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Discovery: one note per topic under 02_Discovery_Log/YYYY-MM/, sections for
# each of the 5 kinds so the same topic can accumulate 発見/失敗/改善点/... over time.
# ---------------------------------------------------------------------------


def discovery_path(vault_root: Path, date_str: str, title: str) -> Path:
    month = date_str[:7]
    slug = safe_name(title)[:40]
    return vault_root / "02_Discovery_Log" / month / f"{date_str}_{slug}.md"


def write_discovery_entry(path: Path, date_str: str, title: str, kind: str, text: str) -> bool:
    marker = f"## {kind}"
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = f"---\ndate: {date_str}\ntags: [{kind}]\n---\n\n# {title}\n"
    if text.strip() in content:
        return False
    content = append_bullet(content, marker, f"- {text}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Decision Log: one note per decision topic under 03_Company/Decisions/,
# 採用したもの/却下したもの/採用理由 accumulate as the topic gets revisited.
# ---------------------------------------------------------------------------


def decision_path(vault_root: Path, date_str: str, title: str) -> Path:
    slug = safe_name(title)[:50]
    return vault_root / "03_Company" / "Decisions" / f"{date_str}_{slug}.md"


def write_decision_entry(path: Path, date_str: str, title: str, outcome: str, text: str, reason: str | None) -> bool:
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = (
            f"---\ndate: {date_str}\n決定者: \n---\n\n"
            f"# {title}\n\n## 採用したもの\n\n## 却下したもの\n\n## 採用理由\n\n"
        )
    changed = False
    heading = "## 採用したもの" if outcome == "採用" else "## 却下したもの"
    if text.strip() not in content:
        content = append_bullet(content, heading, f"- {text}")
        changed = True
    if reason and reason.strip() not in content:
        content = append_bullet(content, "## 採用理由", f"- {reason}")
        changed = True
    if not changed:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Prompt Library: one note per reusable prompt, optionally cross-linked to a
# Character/Project via the same 関連 mechanism as Costume Bible.
# ---------------------------------------------------------------------------


def prompt_path(vault_root: Path, target: str) -> Path:
    slug = safe_name(target)[:60] if target else "prompt"
    return vault_root / "05_Knowledge" / "Prompt_Library" / f"{slug}.md"


def write_prompt_entry(
    path: Path, date_str: str, target: str, text: str, character: str | None, project: str | None
) -> bool:
    if path.exists():
        content = path.read_text(encoding="utf-8")
        if text.strip() in content:
            return False
        content = content.rstrip("\n") + f"\n\n## 追記({date_str})\n\n{text}\n"
    else:
        content = (
            "---\n"
            f"date: {date_str}\n"
            "tags: [prompt]\n"
            "---\n\n"
            f"# {target or path.stem}\n\n"
            f"{text}\n\n"
            f"{related_block()}"
        )
    content = ensure_related_link(content, "Characters", character)
    content = ensure_related_link(content, "Projects", project)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Daily Log + changelog
# ---------------------------------------------------------------------------


def new_daily_report(date_str: str) -> str:
    return (
        "---\n"
        f"date: {date_str}\n"
        "---\n\n"
        f"# {date_str}\n\n"
        "## 朝(AM)\n\n- (未記入)\n\n"
        "## 夜(PM)\n\n- (未記入)\n\n"
        f"{AI_COMMENT_MARKER}(報告があるAIのみ)\n\n"
    )


def daily_report_path(vault_root: Path, date_str: str) -> Path:
    return vault_root / "09_Daily_Studio_Report" / date_str[:7] / f"{date_str}.md"


def append_daily_pointer(vault_root: Path, date_str: str, timestamp: str, summary: str, target_rel: Path) -> None:
    """Auto-pointer left by `file`: filing something counts as 今日やったこと."""
    path = daily_report_path(vault_root, date_str)
    link_target = target_rel.as_posix()
    if link_target.endswith(".md"):
        link_target = link_target[:-3]
    entry = f"{timestamp} {summary} -> [[{link_target}]]"

    content = path.read_text(encoding="utf-8") if path.exists() else new_daily_report(date_str)
    if entry in content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    marker = f"## {DAILY_SECTIONS['did']}"
    content = append_bullet(content, marker, f"- {entry}", create_after=AI_COMMENT_MARKER)
    path.write_text(content, encoding="utf-8")


def append_changelog(vault_root: Path, timestamp: str, action: str, target_rel: Path, summary: str) -> None:
    path = vault_root / "00_Start_Here" / "変更履歴.md"
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        header = (
            "# 変更履歴\n"
            "（Vault Managerが自動で行った変更の記録。追記のみ）\n\n"
            "`scripts/vault_manager.py` 経由の機械的な変更を、日時・操作・対象・要約の形で記録します。"
            "人が手で編集した変更はここには残りません(それはコミット履歴を見てください)。\n\n"
        )
        path.write_text(header, encoding="utf-8")
    summary_clean = summary.replace("\n", " ")[:80]
    line = f"- {timestamp} | {action} | {target_rel.as_posix()} | {summary_clean}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line)


def cmd_registry(args: argparse.Namespace) -> int:
    vault_root = Path(args.root).resolve() / "Obsidian_Vault"
    registry = full_registry(vault_root)
    grouped: dict[Path, tuple[str, str, list[str]]] = {}
    for key, entity in registry.items():
        name, kind, aliases = grouped.setdefault(entity.path, (entity.name, entity.kind, []))
        if key != name.lower().replace("_", " ") and key not in aliases:
            aliases.append(key)
    for path in sorted(grouped, key=lambda p: p.relative_to(vault_root).as_posix()):
        name, kind, aliases = grouped[path]
        alias_note = f" (aliases: {', '.join(aliases)})" if aliases else ""
        print(f"{name}\t{kind}\t{path.relative_to(vault_root)}{alias_note}")
    return 0


def cmd_file(args: argparse.Namespace) -> int:
    vault_root = Path(args.root).resolve() / "Obsidian_Vault"
    registry = full_registry(vault_root)
    date_str = args.date or today()
    # Content timestamps follow --date (the studio's production calendar can run ahead of
    # or behind the real system clock); only the time-of-day comes from now(). The
    # changelog is a real audit trail of when the script ran, so it always uses now().
    timestamp = f"{date_str} {datetime.now().strftime('%H:%M')}"
    run_timestamp = now_timestamp()

    if args.category == "discovery":
        if not args.kind:
            raise SystemExit(f"--kind is required for --category discovery (choices: {DISCOVERY_KINDS})")
        title = args.target or args.text[:20]
        target_path = discovery_path(vault_root, date_str, title)
        text = auto_link(args.text, registry, exclude_path=target_path)
        changed = write_discovery_entry(target_path, date_str, title, args.kind, text)

    elif args.category == "decision":
        if not args.target:
            raise SystemExit("--target is required for --category decision")
        if not args.outcome:
            raise SystemExit(f"--outcome is required for --category decision (choices: {DECISION_OUTCOMES})")
        target_path = decision_path(vault_root, date_str, args.target)
        text = auto_link(args.text, registry, exclude_path=target_path)
        reason = auto_link(args.reason, registry, exclude_path=target_path) if args.reason else None
        changed = write_decision_entry(target_path, date_str, args.target, args.outcome, text, reason)

    elif args.category == "costume":
        if not args.character and not args.project:
            raise SystemExit("--character or --project is required for --category costume")
        character = resolve_existing_entity(registry, args.character, ("character",)) if args.character else None
        if args.character and not character:
            raise SystemExit(f"--character '{args.character}' not found. Create it first with --category character.")
        project = resolve_existing_entity(registry, args.project, ("project",)) if args.project else None
        if args.project and not project:
            raise SystemExit(f"--project '{args.project}' not found. Create it first with --category mv.")
        # Default title is suffixed ("MIU衣装") rather than the bare name, so a Costume
        # Bible entry never collides with the Character/Project note of the same name.
        default_title = f"{(character or project).name}衣装"
        title = args.target or default_title
        target_path = costume_bible_path(vault_root, title)
        text = auto_link(args.text, registry, exclude_path=target_path)
        reason = auto_link(args.reason, registry, exclude_path=target_path) if args.reason else None
        changed = write_costume_entry(
            target_path, title, character.name if character else None, project.name if project else None, text, reason
        )

    elif args.category == "prompt":
        if not args.target:
            raise SystemExit("--target is required for --category prompt")
        target_path = prompt_path(vault_root, args.target)
        text = auto_link(args.text, registry, exclude_path=target_path)
        changed = write_prompt_entry(target_path, date_str, args.target, text, args.character, args.project)

    elif args.category in ("character", "mv"):
        if not args.target:
            raise SystemExit(f"--target is required for --category {args.category}")
        target_path = resolve_or_create_entity_note(vault_root, registry, args.category, args.target, args.aliases)
        text = auto_link(args.text, registry, exclude_path=target_path)
        if args.category == "mv":
            section = args.section or "制作ログ"
            if section not in MV_SECTIONS:
                raise SystemExit(f"--section must be one of {MV_SECTIONS}")
            heading = "制作ログ(自動記録)" if section == "制作ログ" else section
        else:
            heading = "制作ログ(自動記録)"
        entry = f"{timestamp} {text}" if heading.endswith("(自動記録)") else text
        changed = append_to_section(target_path, heading, entry, new_file_title=args.target)

    else:
        raise SystemExit(f"unknown category: {args.category}")

    target_rel = target_path.relative_to(vault_root)
    if not changed:
        print(f"Duplicate, skipped: {target_rel}")
        return 0

    append_changelog(vault_root, run_timestamp, f"file:{args.category}", target_rel, args.text)
    if not args.no_daily_log:
        append_daily_pointer(vault_root, date_str, timestamp, args.text[:40], target_rel)
    print(f"Filed to {target_rel}")
    return 0


def cmd_daily_log(args: argparse.Namespace) -> int:
    vault_root = Path(args.root).resolve() / "Obsidian_Vault"
    registry = full_registry(vault_root)
    date_str = args.date or today()
    path = daily_report_path(vault_root, date_str)
    content = path.read_text(encoding="utf-8") if path.exists() else new_daily_report(date_str)

    changed = False
    summary_parts = []
    for key in ("did", "done", "next"):
        value = getattr(args, key)
        if not value:
            continue
        text = auto_link(value, registry, exclude_path=path)
        entry = f"- {text}"
        if entry.strip() in content:
            continue
        marker = f"## {DAILY_SECTIONS[key]}"
        content = append_bullet(content, marker, entry, create_after=AI_COMMENT_MARKER)
        changed = True
        summary_parts.append(f"{key}: {value}")

    if not changed:
        print("No change (nothing given, or all duplicates)")
        return 0

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    append_changelog(vault_root, now_timestamp(), "daily-log", path.relative_to(vault_root), "; ".join(summary_parts))
    print(f"Updated {path.relative_to(vault_root)}")
    return 0


def cmd_next_action(args: argparse.Namespace) -> int:
    vault_root = Path(args.root).resolve() / "Obsidian_Vault"
    path = vault_root / "06_Projects" / args.project / "Overview.md"
    if not path.exists():
        raise SystemExit(f"project overview not found: {path}")
    content = path.read_text(encoding="utf-8")
    changed = False
    summary = ""

    if args.add:
        registry = full_registry(vault_root)
        entry_text = auto_link(args.add, registry, exclude_path=path)
        line = f"- [ ] {entry_text}"
        if entry_text not in content:
            content = append_bullet(content, "## 次にやること", line)
            changed = True
            summary = f"add: {args.add}"

    if args.done:
        pattern = re.compile(r"^- \[ \] (.*" + re.escape(args.done) + r".*)$", re.MULTILINE)
        content, count = pattern.subn(lambda m: f"- [x] {m.group(1)}", content, count=1)
        if count:
            changed = True
            summary = (summary + "; " if summary else "") + f"done: {args.done}"

    if not changed:
        print("No change (duplicate, or no matching item found)")
        return 0

    path.write_text(content, encoding="utf-8")
    append_changelog(vault_root, now_timestamp(), "next-action", path.relative_to(vault_root), summary)
    print(f"Updated {path.relative_to(vault_root)}")
    return 0


def cmd_changelog(args: argparse.Namespace) -> int:
    vault_root = Path(args.root).resolve() / "Obsidian_Vault"
    path = vault_root / "00_Start_Here" / "変更履歴.md"
    if not path.exists():
        print("No changelog yet.")
        return 0
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("- ")]
    for line in lines[-args.limit:]:
        print(line)
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    print(
        "ingest is not implemented yet.\n"
        "Extracting decisions from a ChatGPT conversation export needs natural-language\n"
        "understanding this stdlib script does not have. For now: have a human or an AI\n"
        "(Claude Code / ChatGPT) read the conversation, pick out each decided item, and call\n"
        "`vault_manager.py file --category ... --text ...` (or `daily-log`) once per item.\n"
        "This command is the documented extension point for a future adapter that automates\n"
        "that reading step -- see AUTOMATION.md."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="FLYSTAR77 Obsidian Vault Manager")
    parser.add_argument("--root", default=".", help="FLYSTAR77 repository root")
    sub = parser.add_subparsers(dest="command", required=True)

    p_registry = sub.add_parser("registry", help="List known entities (hub notes + glossary terms)")
    p_registry.set_defaults(func=cmd_registry)

    p_file = sub.add_parser("file", help="Route a decided-today item into the right note")
    p_file.add_argument(
        "--category", required=True, choices=["character", "costume", "mv", "prompt", "discovery", "decision"]
    )
    p_file.add_argument("--target", help="Entity/topic name (character/project/prompt/discovery/decision title)")
    p_file.add_argument("--text", required=True, help="The decided content")
    p_file.add_argument("--kind", choices=DISCOVERY_KINDS, help="Required for --category discovery")
    p_file.add_argument("--outcome", choices=DECISION_OUTCOMES, help="Required for --category decision")
    p_file.add_argument("--reason", help="採用理由 (decision, costume)")
    p_file.add_argument("--character", help="Character name to attach to (costume, prompt)")
    p_file.add_argument("--project", help="Project name to attach to (costume, prompt)")
    p_file.add_argument("--section", choices=MV_SECTIONS, help="Target section for --category mv")
    p_file.add_argument("--aliases", nargs="*", default=[], help="Aliases to set if a new note is created")
    p_file.add_argument("--date", help="Override date (YYYY-MM-DD); defaults to system today")
    p_file.add_argument("--no-daily-log", action="store_true", help="Skip the Daily Studio Report pointer line")
    p_file.set_defaults(func=cmd_file)

    p_daily = sub.add_parser("daily-log", help="Record 今日やったこと/完成したこと/次回やること in the Daily Studio Report")
    p_daily.add_argument("--did", help="今日やったこと")
    p_daily.add_argument("--done", help="完成したこと")
    p_daily.add_argument("--next", help="次回やること")
    p_daily.add_argument("--date", help="Override date (YYYY-MM-DD); defaults to system today")
    p_daily.set_defaults(func=cmd_daily_log)

    p_next = sub.add_parser("next-action", help="Add or check off a project's 次にやること item")
    p_next.add_argument("--project", required=True, help="Folder name under 06_Projects/")
    p_next.add_argument("--add", help="New task text to add")
    p_next.add_argument("--done", help="Substring matching an existing unchecked item to check off")
    p_next.set_defaults(func=cmd_next_action)

    p_changelog = sub.add_parser("changelog", help="Show recent Vault Manager changes")
    p_changelog.add_argument("--limit", type=int, default=20)
    p_changelog.set_defaults(func=cmd_changelog)

    p_ingest = sub.add_parser("ingest", help="(not yet implemented) extract decisions from a conversation export")
    p_ingest.add_argument("--file", help="Path to an exported conversation")
    p_ingest.set_defaults(func=cmd_ingest)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
