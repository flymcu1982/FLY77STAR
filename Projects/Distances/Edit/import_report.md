# Import Report

- Generated: 2026-07-01 01:41:43
- Mode: ASSIGN
- Import folder: `Unsorted`
- Planned assets: 1
- Unsupported files: 0

## Planned Moves

| Source | Type | CUT | Destination | Status | Reason |
|---|---|---|---|---|---|
| `Unsorted/video_001.mp4` | video | CUT17 | `CUT/CUT17.mp4` | moved | manual assignment to CUT17 |

## Unsortedへ送ったファイル一覧

- なし

## CUTへ割り当てたファイル一覧

- CUT17: Unsorted/video_001.mp4 -> CUT/CUT17.mp4

## CUT_LIST.jsonの更新内容

- globalAssets.unsorted: removed Unsorted/video_001.mp4
- CUT17.asset unchanged: CUT/CUT17.mp4

## 実行コマンド例

- `python3 scripts/import_assets.py Projects/Distances --dry-run`
- `python3 scripts/import_assets.py Projects/Distances --apply`
- `python3 scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17`
- `python3 scripts/watch_import.py --project Distances --once --dry-run`
- `python3 scripts/watch_import.py --project Distances --once`
