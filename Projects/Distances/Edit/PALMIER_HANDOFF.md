# Distances Palmier Handoff

Palmierへ渡すファイル:

- `CUT/`
- `Audio/`
- `Dialogue/`
- `Edit/EDIT_PLAN.md`
- `Edit/edit_project.json`
- `CUT_LIST.json`
- `project.json`

## Palmier Task

1. `Edit/edit_project.json` を読み込む。
2. CUT01〜CUT18を順番に読み込む。
3. `EDIT_PLAN.md` の推奨尺に合わせてタイムラインを組む。
4. CUT06、CUT12、CUT17のセリフ同期を優先する。
5. BGMはセリフを邪魔しない音量にする。
6. CUT17の余韻とCUT18の最後1秒を残す。
7. 書き出し前に `QC/QC_CHECKLIST.md` を確認する。

## Output

- 仮書き出し: `Projects/Distances/Export/`
- 完成動画: `Exports/`
