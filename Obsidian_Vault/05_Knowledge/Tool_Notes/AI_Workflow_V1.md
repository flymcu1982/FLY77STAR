# Studio OS標準制作ワークフロー Version 1(Studio OS v1.2)
（CINE→SOUL→CUT→MASTERの4段階リレーでCUT単位の制作を行う、全MV/ドラマ/映画共通の標準フロー）

実体はGitHub `AI_WORKFLOW_V1.md`。使い方の正本はGitHub側にあります。2026-07-10、WAKE UP CUT01の試験運用を経て正式運用に昇格しました。

## バージョン履歴

- v1.0: CINE→SOUL→CUT→MASTER 4段階リレー正式運用開始
- v1.1: Panel Storyboard(映画レベル絵コンテ)を正式採用
- v1.2: Director Notes(監督ノート、重要Panelのみ)を正式採用

## 流れ

生成前チェック(Character Bible/Costume Bible/Universe Rule/Production Bible確認) → 🎬CINE → 🎭SOUL → 📷CUT(+Panel Storyboard、重要Panelのみ+Director Notes) → 🛡MASTER → 4者レビュー → `Projects/<作品名>/Storyboard/`に保存 → Daily Studio Reportへ記録

## 出力テンプレート

- [[99_Templates/CUT_Workflow_V1|CUT_Workflow_V1]](生成プロンプト本体)
- [[99_Templates/Panel_Storyboard_V1|Panel_Storyboard_V1]](Panel Storyboard)
- [[99_Templates/Director_Notes_V1|Director_Notes_V1]](Director Notes、重要Panelのみ)

## 注意

CINE/SOUL/CUT/MASTERは、まだ個別のAIサービスに紐づいていません([[03_Company/Decisions/2026-07-09_未決事項リスト|未決事項リスト]] 1番、未決)。決まるまでは、依頼を受けたAIが4役を代行します。

## 関連

- Knowledge:
- Projects: [[06_Projects/WAKE_UP/Overview|WAKE UP]]
- People:
- Characters:
- AI Employees: [[04_Team/AI_Employees/CINE|CINE]], [[04_Team/AI_Employees/SOUL|SOUL]], [[04_Team/AI_Employees/CUT (AI Employee)|CUT]], [[04_Team/AI_Employees/MASTER|MASTER]]
- Prompt:
- GitHub(正本): `AI_WORKFLOW_V1.md`
