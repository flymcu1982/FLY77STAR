# FLYSTAR77 Codex Rules

Codexは制作管理AIとして、プロジェクト構成、ファイル、編集指示、自動化を管理する。

## Priority

作業前に以下を参照する。

1. `OPERATING_MANUAL.md`
2. `PRODUCTION_BIBLE.md`
3. `AI_RULES.md`
4. `CODEX_RULES.md`
5. `PALMIER_RULES.md`

## Codex Responsibilities

- `Projects/` を管理する。
- 不足フォルダと不足ファイルを通知する。
- 標準構成を作成する。
- `Import/` 内の素材を分類・リネームする。
- CUT番号が判断できない素材は `Unsorted/` に退避し、勝手にCUTへ割り当てない。
- 既存のCUT素材は上書きしない。同名ファイルは `_take02` 形式で保存する。
- `project.json` を管理する。
- CUTリスト、プロンプト、編集指示書を作る。
- Palmierへ渡す内容とCodexで自動化する内容を分ける。
- GitHub運用時は検証スクリプトを整備する。

## Codex Can Automate

- プロジェクト作成
- 標準フォルダ生成
- Import素材の分類、移動、リネーム
- Unsorted素材の手動CUT割り当て
- CUT01〜CUT18の管理ファイル生成
- EDIT_PLAN.md生成
- 命名規則チェック
- 必須ファイルチェック
- GitHub Actionsでの構成チェック

## Codex Should Hand Off To Palmier

- CUTの実読み込み
- タイムライン上の編集
- BGM同期
- セリフ同期
- フェード生成
- 動画書き出し

## Output Rule

完成動画は `Exports/`、作品別の書き出し作業中ファイルは `Projects/作品名/Export/` に保存する。
