# Studio OS 標準制作ワークフロー Version 1

CUT単位の制作(演出設計〜プロンプト生成)を、CINE→SOUL→CUT→MASTERの4段階リレーで行う標準フロー。2026-07-10、WAKE UP CUT01の試験運用が成功と判断されたことを受けて正式運用に昇格。

**適用範囲**: 今後のすべてのMV・ドラマ・映画のCUT単位制作に共通で使用する。

## 前提: CINE/SOUL/CUT/MASTERの実体は未確定

4つの役割名はGitHub `AI_RULES.md` にまだ正式定義されていない(Obsidian Vault `03_Company/Decisions/2026-07-09_未決事項リスト.md` の1番、未決)。既存ロール(Higgsfield/Palmier等)の改名か新設部署かでAI_RULES.mdの変更範囲が変わるため、これはYUの判断待ち。

**それまでの間**: このワークフローは「4段階リレーの型」を定義するものとして運用する。各段階の実行は、依頼を受けたAI(Claude Code、ChatGPT等、その時点で作業しているAI)が4役を代行し、型を再現する。

## フロー全体

```
Step 0: 生成前チェック(必須、矛盾があれば停止して報告)
   ↓
Step 1: 🎬 CINE  — 演出・カメラ・照明・演技方針
   ↓
Step 2: 🎭 SOUL  — 感情・セリフ・心理描写
   ↓
Step 3: 📷 CUT   — 絵コンテ・構図・画像生成Prompt・動画Prompt
   ↓
Step 4: 🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
   ↓
Step 5: 4者レビュー(一言ずつ)
   ↓
Step 6: 保存(Projects/<作品名>/Storyboard/CUT<番号>.md)
   ↓
Step 7: Daily Studio Report記録(制作日・作品・CUT番号)
```

## Step 0: 生成前チェック(必須)

CINEに着手する前に、以下4つを確認する。矛盾があれば**生成前に**報告し、生成を止める。

1. **Character Bible** — Obsidian Vault `10_Characters/` の該当キャラクターのハブノート
2. **Costume Bible** — Obsidian Vault `11_Costume_Bible/` の該当衣装(未登録なら、その旨を明記して仮置きするか判断)
3. **Universe Rule** — Obsidian Vault `10_Characters/FLY77STAR_Universe.md` の共通ルール(「キャラクターは時間を生きる」等)
4. **Production Bible** — GitHub `PRODUCTION_BIBLE.md` / `ProductionBible/RULE.md`

## Step 1〜4: リレーの実行ログ

出力時は必ずこの順・このフォーマットで、各段階が「何を担当したか」「完了したか」が分かるように表示する。

```
🎬 CINE — 演出・カメラ・照明・演技方針
[担当内容を1〜3行で]
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
[担当内容を1〜3行で]
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
[担当内容を1〜3行で]
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
[担当内容と照合結果を1〜3行で。矛盾があれば明記]
状態: 完了
```

## Step 5: 4者レビュー

MASTER完了後、4人全員が一言レビューを行う。

```
🎬 CINE「(演出面の一言)」
🎭 SOUL「(感情・セリフ面の一言)」
📷 CUT「(絵コンテ・構図面の一言)」
🛡 MASTER「(整合性の一言)」
```

## Step 6: 保存先

`Projects/<作品名>/Storyboard/CUT<番号>.md`

既存の標準プロジェクト構成(`FOLDER_STRUCTURE.md`、`scripts/create_project.py`)にある `Storyboard/` フォルダを使う。番号なし。

## Step 7: Daily Studio Report記録

生成完了後、Obsidian Vaultの当日のDaily Studio Reportへ、制作日・作品・CUT番号を追記する。

```bash
python3 scripts/vault_manager.py daily-log --done "制作日:YYYY-MM-DD / 作品:<作品名> / CUT:CUT<番号> 完成"
```

## 出力ファイルのテンプレート

`Obsidian_Vault/99_Templates/CUT_Workflow_V1.md` を参照。

## 実績

- WAKE UP CUT01 — 試験運用(2026-07-10)、成功と判断され本フローがVersion 1として正式運用開始
