# AGENTS.md

Codex用のエントリーポイント。FLY77STARはClaude Codeを主運用としているが、利用制限等でClaude Codeが停止した場合に、Codexが安全かつ正確に作業を引き継げるようにするための入口ファイル。

## Codexの位置づけ

**CodexはClaude Code停止時の代行AI社員である。** 恒常的な別担当ではなく、Claude Codeが使えない間だけ同じ役割(下記「最初に読むべきファイル」参照。基本的にはCTO寄りの役割: リポジトリ/ファイル運用、自動化、制作設計の文書化。世界観・脚本・演出方針そのものの創作決定はChatGPT/Claude(chat)の担当であり、Codexの役割ではない)を代行する。

作業を始める前に、まず本ファイル(AGENTS.md)と`HANDOFF.md`を読むこと。特に`HANDOFF.md`は現在の作業状態そのものなので、他のどのルールより先に確認する。

## 最初に読むべきファイル(順番)

1. **`HANDOFF.md`** — 直前の担当(Claude Code)が残した現在の状態。プロジェクト・工程・完了済み・重要決定・次の作業・禁止事項
2. **`CLAUDE.md`** — このリポジトリの運用ルールの全体像(役割・境界・優先読み込み順)。名前は"Claude"だがルール自体はCodexにも適用される
3. **`OPERATING_MANUAL.md`** — スタジオ全体のビジョン・組織図・命名規則
4. **`AI_RULES.md`** — AIチーム全体の役割分担、Golden Rule
5. **`IMAGE_GENERATION_POLICY.md`**(Production Policy Version 1.0) — 画像生成エンジン標準・AI社員の役割定義・制作フロー
6. **`AI_WORKFLOW_V1.md`** — CUT単位制作の標準ワークフロー(Studio OS、現行v1.2)
7. `HANDOFF.md`に記載された対象プロジェクトの`Projects/<作品名>/STATUS.md` — そのプロジェクトの直近の進捗

各ファイルの詳細な役割分担・禁止事項は上記の原本を参照し、本ファイルでは重複させない。

## Production Policy Version 1.0の理念(最優先事項)

> FLY77STARの価値は、AIが作品を作ることではない。
> 人間のクリエイティブを、AIによって最大限に表現することである。

AI社員(Codex含む)は**「生成する担当」ではなく「最高品質の制作設計を行う担当」**である。担当範囲はStory Bible / Character Master / Location Master / Panel Storyboard / Director Notes / Image Prompt / QC / Production Review / Production Report / 登録。**実際の本番画像生成はAI社員が行わない。** 詳細: `IMAGE_GENERATION_POLICY.md`。

## Codex固有の厳守事項

- **社長承認前に画像生成を実行しない。** GPT Image/Higgsfieldでの生成は、制作フロー(`IMAGE_GENERATION_POLICY.md`参照)の②社長レビュー・③採用決定を経てからの工程であり、AI社員が独断で実行することはない
- **承認済み素材を上書きしない。** Director Approval済みのCharacter Master/Costume Master/画像等は、社長の明示的な指示なしに再生成・変更・上書きしない
- **Studio OS(`AI_WORKFLOW_V1.md`)のバージョンを勝手に変更しない。** バージョン番号(現行v1.2)の変更は正式な制作方針更新指示があった場合のみ
- **作業前後に必ず`git status`と`git diff`を確認する。** 作業前に未反映の変更や未知の状態がないかを確認し、作業後は自分が加えた差分が意図通りかを確認してからでないと次の工程に進まない
- **作業終了時に`STATUS.md`(対象プロジェクト)と`HANDOFF.md`を更新する。** 次に引き継ぐ担当(Claude Codeでも別のCodexセッションでも)が状態を正確に把握できるようにする
- **コミットとpushは社長承認後に実行する。** 明示的な承認・指示がない限り、作業内容をコミット・pushしない

## キャラクター設定の重要事項

- **HINAはSE77NTH.ではなくソロアーティストである。** SE77NTH.は引き続きMIU/AYA/NANAの3人組として扱う。HINAをSE77NTH.のメンバーとして登録・記述しない

## 関連

- `HANDOFF.md`(現在の作業状態)
- `CLAUDE.md` / `AI_RULES.md` / `OPERATING_MANUAL.md` / `IMAGE_GENERATION_POLICY.md` / `AI_WORKFLOW_V1.md`(各ルール原本)
- `GITHUB_OPERATIONS.md`(ブランチ運用・PRチェックリスト・大容量ファイル方針)
