# FLYSTAR77 GitHub Operations

FLYSTAR77をGitHubリポジトリとして運用する場合の実装可能な構成。

## Recommended Repository Root

`FLYSTAR77/` をGitHubリポジトリのルートにする。

```text
FLYSTAR77/
├── .github/workflows/validate.yml
├── scripts/
├── README.md
├── OPERATING_MANUAL.md
├── PRODUCTION_BIBLE.md
├── AI_RULES.md
├── CODEX_RULES.md
├── PALMIER_RULES.md
├── PROMPT_GUIDE.md
├── FOLDER_STRUCTURE.md
├── AUTOMATION.md
├── QUALITY_CONTROL.md
├── GITHUB_OPERATIONS.md
├── Projects/
├── Assets/
├── Templates/
├── ProductionBible/
├── Exports/
└── Archive/
```

## Scripts

### Validate Structure

```bash
python scripts/validate_structure.py --project Distances
```

標準フォルダ、必須ファイル、`project.json`、`CUT_LIST.json` を検証する。

### Create Project

```bash
python scripts/create_project.py NewProjectName --cuts 18
```

新規プロジェクトの標準フォルダと初期ファイルを作成する。

### Generate Edit Plan

```bash
python scripts/generate_edit_plan.py --project Distances --force
```

`CUT_LIST.json` から `Edit/EDIT_PLAN.md` を生成する。

### Import Assets

```bash
python scripts/import_assets.py Projects/Distances --dry-run
python scripts/import_assets.py Projects/Distances --apply
```

`Projects/Distances/Import/` 内の画像、動画、音声を分類し、標準フォルダへ移動・リネームする。

`--apply` のときだけ実際に移動し、`CUT_LIST.json` を更新する。

CUT番号がファイル名から判断できない動画・画像・セリフ音声は `Unsorted/` へ移動する。

既存の `CUT01.mp4` などは上書きしない。同名ファイルがある場合は `CUT01_take02.mp4` のように連番を付ける。

確認後、手動でCUTへ割り当てる。

```bash
python scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17
```

### Watch Import Folder

```bash
python scripts/watch_import.py --project Distances --once --dry-run
python scripts/watch_import.py --project Distances
```

`config.json` の `watchFolders` を監視し、新しい画像・動画・音声を `Projects/Distances/Import/` へコピーしてから `import_assets.py` を実行する。

デフォルトの監視フォルダは `Projects/Distances/Watch/`。外部フォルダを使う場合は `config.json` の `watchFolders` を変更する。

macOSではターミナルで常駐実行できる。LaunchAgent化する場合も、このコマンドを実行対象にする。

## GitHub Actions

`.github/workflows/validate.yml` で、push / pull_request 時に構成チェックを実行する。

## Branch Strategy

- `main`: 安定版。完成済みルール、作品構成、納品可能な状態。
- `develop`: 制作中の更新。
- `project/作品名`: 作品ごとの制作ブランチ。
- `automation/機能名`: 自動化スクリプト追加。

## Pull Request Checklist

- [ ] `OPERATING_MANUAL.md` と `PRODUCTION_BIBLE.md` に反していない。
- [ ] `python scripts/validate_structure.py --project Distances` が成功する。
- [ ] CUT、Dialogue、Promptの命名規則を守っている。
- [ ] 編集指示を変更した場合、`Edit/EDIT_PLAN.md` も更新した。
- [ ] 完成動画や大容量素材を意図せずコミットしていない。

## Large File Rule

動画、音声、完成書き出しは大きくなりやすい。

- 軽い管理ファイル、プロンプト、編集指示、JSONはGitで管理する。
- 大容量の完成動画は必要なものだけ意図して管理する。
- `Exports/*.mp4` と `Projects/*/Export/*.mp4` は `.gitignore` で除外している。

## Future Automation

将来的なワンクリック編集開始:

```text
create_project.py
↓
CUT_LIST.json編集
↓
generate_edit_plan.py
↓
validate_structure.py
↓
PalmierへEDIT_PLAN.mdを渡す
↓
仮編集
↓
QC
↓
Export
```
