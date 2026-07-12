# Studio OS 標準制作ワークフロー Version 1（Studio OS v1.3）

CUT単位の制作(演出設計〜プロンプト生成)を、CINE→SOUL→CUT→MASTERの4段階リレーで行う標準フロー。2026-07-10、WAKE UP CUT01の試験運用が成功と判断されたことを受けて正式運用に昇格。

**適用範囲**: 今後のすべてのMV・ドラマ・映画のCUT単位制作に共通で使用する。

## バージョン履歴

Studio OSの機能追加はマイナーバージョンとして記録する(v2への更新は運用結果を確認した上で判断)。

| Version | 日付 | 内容 |
|---|---|---|
| v1.0 | 2026-07-10 | CINE→SOUL→CUT→MASTER 4段階リレーが正式運用開始(WAKE UP CUT01試験運用の成功を受けて) |
| v1.1 | 2026-07-10 | Panel Storyboard(Step 3.5、映画レベル絵コンテ)を正式採用 |
| v1.2 | 2026-07-10 | Director Notes(Step 3.6、監督ノート)を正式採用 |
| v1.3 | 2026-07-11 | WAKE UP Panel04の4K本番生成試行時、Higgsfield MCPの承認待ちブロッカーに遭遇。技術調査を止めないまま制作作業へ進むことのリスクをDirectorが指摘し、「調査タスクと制作タスクの分離」を運用原則として正式採用 |

## 前提: CINE/SOUL/CUT/MASTERの実体は未確定

4つの役割名はGitHub `AI_RULES.md` にまだ正式定義されていない(Obsidian Vault `03_Company/Decisions/2026-07-09_未決事項リスト.md` の1番、未決)。既存ロール(Higgsfield/Palmier等)の改名か新設部署かでAI_RULES.mdの変更範囲が変わるため、これはYUの判断待ち。

**それまでの間**: このワークフローは「4段階リレーの型」を定義するものとして運用する。各段階の実行は、依頼を受けたAI(Claude Code、ChatGPT等、その時点で作業しているAI)が4役を代行し、型を再現する。

## 運用原則: 調査タスクと制作タスクの分離(v1.3、必須)

2026-07-11、WAKE UP Panel04の4K本番生成試行中にHiggsfield MCPの承認待ちブロッカーが発生した際のDirector Additional Instructionにより正式採用。全プロジェクト・全AI社員に共通する運用原則として、以下を**Studio OS標準運用**とする。

**タスクの分類**:

- **調査タスク**: MCP / API / Higgsfield / Git / 外部サービス / モデル確認 / 権限確認
- **制作タスク**: Production Package / 画像生成 / 動画生成 / QC / Documentation

**ルール**:

- 調査タスク中に技術的ブロッカー(承認待ち・権限不足・仕様不明等)が発生した場合、**制作タスクへ進まない**
- まず技術課題を解決し、Directorへ報告し、解決後に制作を再開する
- **Production(制作)よりも、Production Environment(制作環境)の健全性を優先する**
- 推測のモデルID・Seed・代替値・仮設定で制作タスクを進めることは行わない(`IMAGE_GENERATION_POLICY.md`「MCP・外部サービス・API承認待ち/権限不足時のエスカレーション手順」と連動)

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

## Step 3.5: Panel Storyboard(映画レベル絵コンテ、標準採用)

2026-07-10、WAKE UP CUT01で試作し成功と判断されたため、Studio OS標準フォーマットとして正式採用。📷 CUTのアウトプットには、Step 3の生成Prompt(CUT<番号>.mdへ格納)に加えて、そのCUTをショットサイズ・カメラワーク・構図・BPM同期まで分解した**Panel Storyboard**を必ず作成する。

- 目的: 単一の演出メモ("俯瞰→降下→ミディアム"のような一行)ではなく、実写映画の絵コンテに相当する精度でカット割りを設計し、生成・編集(Palmier)双方の判断材料にする
- パネル数: そのCUTの尺・演技の転換点に応じて可変(目安: 8秒前後で4〜5パネル。尺が長い、または芝居の転換が多いCUTはパネル数を増やす)
- 各パネルに含める項目: タイムコード、拍(BPM同期の目安)、ショットサイズ、カメラワーク、簡易フレーム図(テキストのAAで構図を示す)、芝居、補足
- テンプレート: `Obsidian_Vault/99_Templates/Panel_Storyboard_V1.md`
- 参考実装: `Projects/WAKE_UP/Storyboard/CUT01_絵コンテ.md`
- 保存先: `Projects/<作品名>/Storyboard/CUT<番号>_絵コンテ.md`(CUT<番号>.mdと同フォルダ、別ファイル)

## Step 3.6: Director Notes(監督ノート、v1.2で正式採用・重要Panelのみ)

2026-07-10、WAKE UP CUT01 Panel03での試験運用が成功と判断されたため、Studio OS標準工程として正式採用(Studio OS v1.2)。Panel Storyboard(Step 3.5)では表現しきれない、監督の演出意図を記録する補完資料。

- **適用範囲(重要)**: 全Panelには適用しない。以下の「重要Panel」に該当する場合のみ作成する
- **重要Panelの定義**:
  1. 主人公初登場
  2. 感情変化
  3. 世界観説明
  4. 伏線
  5. 象徴カット
  6. ラストカット
- **位置づけ**: Director NotesはPanel Storyboardを**補完する資料**であり、Panel Storyboard本体(`CUT<番号>_絵コンテ.md`)の内容は変更しない
- **記載項目**: このパネルで観客に何を感じてほしいか／役者への演技指示／表情／視線／呼吸／間／カメラマンへの補足／照明・色の演出意図／編集時の注意／次パネルへの感情のバトン
- テンプレート: `Obsidian_Vault/99_Templates/Director_Notes_V1.md`
- 参考実装: `Projects/WAKE_UP/Storyboard/CUT01_Panel03_DirectorNotes.md`
- 保存先: `Projects/<作品名>/Storyboard/CUT<番号>_Panel<番号>_DirectorNotes.md`(該当パネルが重要Panelに当たる場合のみ)
- 判断者: どのPanelが「重要Panel」に当たるかは、Step 1(🎬CINE)・Step 2(🎭SOUL)の演出意図を踏まえてリレー実行時に判断し、生成前チェック同様に理由を1行明記する

## Step 6: 保存先

`Projects/<作品名>/Storyboard/CUT<番号>.md`（生成プロンプト本体）
`Projects/<作品名>/Storyboard/CUT<番号>_絵コンテ.md`（Panel Storyboard、Step 3.5参照）
`Projects/<作品名>/Storyboard/CUT<番号>_Panel<番号>_DirectorNotes.md`（Director Notes、Step 3.6参照。重要Panelのみ）

既存の標準プロジェクト構成(`FOLDER_STRUCTURE.md`、`scripts/create_project.py`)にある `Storyboard/` フォルダを使う。番号なし。

## Step 7: Daily Studio Report記録

生成完了後、Obsidian Vaultの当日のDaily Studio Reportへ、制作日・作品・CUT番号を追記する。

```bash
python3 scripts/vault_manager.py daily-log --done "制作日:YYYY-MM-DD / 作品:<作品名> / CUT:CUT<番号> 完成"
```

## 出力ファイルのテンプレート

- 生成プロンプト本体: `Obsidian_Vault/99_Templates/CUT_Workflow_V1.md`
- Panel Storyboard(Step 3.5): `Obsidian_Vault/99_Templates/Panel_Storyboard_V1.md`
- Director Notes(Step 3.6、重要Panelのみ): `Obsidian_Vault/99_Templates/Director_Notes_V1.md`

## 実績

- WAKE UP CUT01 — 試験運用(2026-07-10)、成功と判断され本フローがVersion 1として正式運用開始(Studio OS v1.0)
- WAKE UP CUT01 — Panel Storyboard試作(2026-07-10)、成功と判断されStep 3.5として正式採用(Studio OS v1.1)
- WAKE UP CUT01〜12 — Story Bible改訂(2026-07-10)に基づき全カット制作完了
- WAKE UP CUT01 Panel03 — Director Notes試験運用(2026-07-10)、成功と判断されStep 3.6として正式採用(Studio OS v1.2)
- WAKE UP CUT01 Panel04 — 4K本番生成試行時にHiggsfield MCP承認待ちブロッカーへ遭遇(2026-07-11)。推測せず停止・報告した対応をDirectorが評価し、「調査タスクと制作タスクの分離」を運用原則として正式採用(Studio OS v1.3)
