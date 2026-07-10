# FLYSTAR77 Automation

制作フローをできるだけ自動化するための設計。

## Codexで自動化する部分

- プロジェクト作成
- 標準フォルダ生成
- `Import/` 素材の分類、移動、リネーム
- CUT番号なし素材の `Unsorted/` 退避
- `--assign` による確認後のCUT割り当て
- 同名ファイルは上書きせず `_take02` 形式で保存
- ユーザー指定フォルダの監視と自動取り込み
- `project.json` 生成
- CUTリスト生成
- EDIT_PLAN.md生成
- Promptテンプレート生成
- QCチェックリスト生成
- 命名規則チェック
- GitHub Actionsでの構成チェック

## Palmierへ渡す部分

- CUT読み込み
- タイムライン生成
- セリフ同期
- BGM同期
- フェード生成
- 書き出し

## One Click Editing Target

将来的に以下の流れをワンクリック化する。

```text
project.json
↓
watch_import.py
↓
import_assets.py
↓
validate_structure.py
↓
generate_edit_plan.py
↓
PalmierへEDIT_PLAN.mdを渡す
↓
Palmierでタイムライン生成
↓
QC
↓
Export
```

## Scripts

- `scripts/validate_structure.py`: 標準構成を検証する。
- `scripts/create_project.py`: 新規作品フォルダを作成する。
- `scripts/generate_edit_plan.py`: CUT情報からEDIT_PLAN.mdを生成する。
- `scripts/import_assets.py`: `Import/` 内の素材を標準構成へ整理する。
- `scripts/import_assets.py --assign`: `Unsorted/` 内の素材を指定CUTへ割り当てる。
- `scripts/watch_import.py`: `config.json` の監視フォルダを見張り、新規素材を `Import/` へコピーして `import_assets.py` を実行する。
- `scripts/vault_manager.py`: 制作中に決まった内容を `Obsidian_Vault/` の適切なノートへ整理・保存する(他のスクリプトと違い `Projects/` ではなく `Obsidian_Vault/` を操作する)。分類(Character/Costume/MV/Prompt/Discovery)は人間かAIが判断してから渡す。重複チェック・Internal Link自動付与・Daily Note追記・変更履歴記録まで行う。`ingest` サブコマンドは、将来ChatGPTとの会話ログから知識抽出する拡張ポイントとして用意(未実装)。

## Watch Import

監視フォルダは `config.json` で変更する。

```bash
python scripts/watch_import.py --project Distances --once --dry-run
python scripts/watch_import.py --project Distances --once
python scripts/watch_import.py --project Distances
```

macOS対応の標準ライブラリのみで動作する。常駐実行時はCtrl+Cで停止する。
