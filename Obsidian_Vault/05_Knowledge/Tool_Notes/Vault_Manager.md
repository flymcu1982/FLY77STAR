# Vault Manager
（制作中に決まった内容を、このVaultへ自動で整理・保存し、会社の知識として育てるツール）

実体はGitHub上の `scripts/vault_manager.py`(stdlib Pythonのみで動作)です。使い方の正本はGitHub側にあります。ここでは概要とVault側の利用者向けの注意だけ書きます。

## Vaultの7つの区画とVault Managerの対応

| 区画 | 実体フォルダ | Vault Managerでの書き方 |
|---|---|---|
| Daily Log(今日やったこと/完成したこと/次回やること) | [[09_Daily_Studio_Report/_Index|Daily Studio Report]] | `daily-log --did/--done/--next` |
| Discovery(発見/失敗/改善点/アイデア/次回試したい) | [[02_Discovery_Log/_Index|Discovery Log]] | `file --category discovery --kind ...` |
| Decision Log(採用したもの/却下したもの/採用理由) | [[03_Company/Decisions/README|Decisions]] | `file --category decision --outcome 採用\|却下` |
| Character Bible | [[10_Characters/_Index|Characters]] | `file --category character` |
| Costume Bible(デザインと採用理由) | [[11_Costume_Bible/_Index|Costume Bible]] | `file --category costume --character/--project` |
| MV Bible(脚本・絵コンテ・CUT・プロンプト) | [[06_Projects/_Index|Projects]] | `file --category mv --section 脚本\|絵コンテ\|CUT\|プロンプト` |
| Prompt Library | [[05_Knowledge/Prompt_Library/README|Prompt Library]] | `file --category prompt` |

## できること

- 今日決まった内容を、上の7区画のいずれかへ振り分けて保存する
- 対象ノートが無ければ [[99_Templates/Hub_Note|Hub Noteテンプレート]] から新規作成する(Character/MV)。Costumeは既存のCharacterかProjectに必ず紐付ける(何もない衣装は作らない)
- 同じ内容の二重登録を防ぐ
- 登録済みの人物・キャラクター・作品名を自動で `[[Internal Link]]` にする
- Costume/Promptは `--character`/`--project` で該当ノートと相互参照する
- Daily Studio Reportに1行のポインタを残す(`file`は「今日やったこと」扱い)
- すべての変更を [[変更履歴]] に記録する

## できないこと(今のところ)

- 「これはCharacterかCostumeかMVか」「発見か失敗かアイデアか」「採用か却下か」の判断は自動化されていません。人間かAI(Claude Code)が読んで分類してから実行します。自然言語の分類をルールベースのスクリプトだけで確実にやるのは無理があるためです。
- ChatGPTとの制作会話からの自動抽出(`ingest` サブコマンド)は、まだ実装されていません。今は会話を読んで、決まった項目ごとにこのツールを手動で呼び出す運用です。

## 実行例

```bash
python3 scripts/vault_manager.py file --category character --target MIU --text "..."
python3 scripts/vault_manager.py file --category costume --character MIU --project WAKE_UP \
  --text "ウェイトレス衣装、ピンク系" --reason "3人の見分けやすさのため"
python3 scripts/vault_manager.py file --category mv --target WAKE_UP --section CUT --text "..."
python3 scripts/vault_manager.py file --category discovery --target "プロンプトのコツ" --kind 発見 --text "..."
python3 scripts/vault_manager.py file --category decision --target "衣装カラー案" --outcome 採用 --text "..." --reason "..."
python3 scripts/vault_manager.py daily-log --did "..." --done "..." --next "..."
```

## 関連

- Knowledge:
- Projects:
- People:
- Characters:
- AI Employees: [[04_Team/AI_Employees/Claude_Code|Claude Code]]
- Prompt:
- GitHub(正本): `scripts/vault_manager.py`, `AUTOMATION.md`, `CLAUDE.md`
