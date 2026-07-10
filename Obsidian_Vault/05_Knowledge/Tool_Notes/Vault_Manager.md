# Vault Manager
（制作中に決まった内容を、このVaultへ自動で整理・保存するツール）

実体はGitHub上の `scripts/vault_manager.py`(stdlib Pythonのみで動作)です。使い方の正本はGitHub側にあります。ここでは概要とVault側の利用者向けの注意だけ書きます。

## できること

- 今日決まった内容を、Character・Costume・MV・Prompt・Discoveryのいずれかへ振り分けて保存する
- 対象ノートが無ければ [[99_Templates/Hub_Note|Hub Noteテンプレート]] から新規作成する
- 同じ内容の二重登録を防ぐ
- 登録済みの人物・キャラクター・作品名を自動で `[[Internal Link]]` にする
- その日の [[09_Daily_Studio_Report/_Index|Daily Studio Report]] に1行のポインタを残す
- すべての変更を [[変更履歴]] に記録する

## できないこと(今のところ)

- 「これはCharacterかCostumeかMVか」の判断は自動化されていません。人間かAI(Claude Code)が読んで分類してから実行します。自然言語の分類をルールベースのスクリプトだけで確実にやるのは無理があるためです。
- ChatGPTとの制作会話からの自動抽出(`ingest` サブコマンド)は、まだ実装されていません。今は会話を読んで、決まった項目ごとにこのツールを手動で呼び出す運用です。

## 実行例

```bash
python3 scripts/vault_manager.py file --category character --target MIU --text "..."
python3 scripts/vault_manager.py file --category costume --target WAKE_UP --text "..."
python3 scripts/vault_manager.py next-action --project WAKE_UP --done "配色案"
```

## 関連

- Knowledge:
- Projects:
- People:
- Characters:
- AI Employees: [[04_Team/AI_Employees/Claude_Code|Claude Code]]
- Prompt:
- GitHub(正本): `scripts/vault_manager.py`, `AUTOMATION.md`, `CLAUDE.md`
