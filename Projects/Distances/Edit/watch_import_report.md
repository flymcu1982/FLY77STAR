# Watch Import Report

- Generated: 2026-07-01 01:38:33
- Mode: APPLY
- Project: Distances
- Import mode: apply
- Poll seconds: 5
- Settle seconds: 3

## Watch Folders

- `/Users/yamamotohiroshi/Documents/Codex/2026-06-21/p/FLYSTAR77/Projects/Distances/Watch`

## Copied Assets

| Source | Destination | Status |
|---|---|---|
| `/Users/yamamotohiroshi/Documents/Codex/2026-06-21/p/FLYSTAR77/Projects/Distances/Watch/dreamina-2026-06-30-1606-Slow handheld camera. Very subtle forwar....mp4` | `Import/dreamina-2026-06-30-1606-Slow handheld camera. Very subtle forwar....mp4` | copied |

## import_assets.py

- Return code: 0

```text
Mode: APPLY
video    -     Import/dreamina-2026-06-30-1606-Slow handheld camera. Very subtle forwar....mp4 -> Unsorted/video_001.mp4

Unsortedへ送ったファイル一覧
- Import/dreamina-2026-06-30-1606-Slow handheld camera. Very subtle forwar....mp4 -> Unsorted/video_001.mp4

CUTへ割り当てたファイル一覧
- なし

CUT_LIST.jsonの更新内容
- globalAssets.unsorted += Unsorted/video_001.mp4

実行コマンド例
- python3 scripts/import_assets.py Projects/Distances --dry-run
- python3 scripts/import_assets.py Projects/Distances --apply
- python3 scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17
- python3 scripts/watch_import.py --project Distances --once --dry-run
- python3 scripts/watch_import.py --project Distances --once
Report written: Edit/import_report.md
```
