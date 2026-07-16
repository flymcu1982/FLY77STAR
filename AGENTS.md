# AGENTS.md

Codex用のエントリーポイント。FLY77STARはClaude Codeを主運用としているが、利用制限等でClaude Codeが停止した場合に、Codexが安全かつ正確に作業を引き継げるようにするための入口ファイル。

## Codexの位置づけ

**CodexはClaude Code停止時の代行AI社員である。** 恒常的な別担当ではなく、Claude Codeが使えない間だけ同じ役割(下記「最初に読むべきファイル」参照。基本的にはCTO寄りの役割: リポジトリ/ファイル運用、自動化、制作設計の文書化。世界観・脚本・演出方針そのものの創作決定はChatGPT/Claude(chat)の担当であり、Codexの役割ではない)を代行する。

作業を始める前に、まず本ファイル(AGENTS.md)と`HANDOFF.md`を読むこと。特に`HANDOFF.md`は現在の作業状態そのものなので、他のどのルールより先に確認する。

## 最初に読むべきファイル(順番)

0. **`CANON_FLY77STAR_20260716_final.md`** — 2026-07-16、FLY77STAR U.承認・確定版のFLY77STAR CANON(完全制作基盤)。ブランド・組織・哲学・キャラクター・作品ラインアップ・制作ワークフロー・収益化戦略の最上位資料。「すべてのAI社員・クリエイターは、実装前に必ずこのファイルを参照」と定められている。既存リポジトリ資料との整合性確認は進行中(未解消の差分はHANDOFF.md参照)
1. **`HANDOFF.md`** — 直前の担当(Claude Code)が残した現在の状態。プロジェクト・工程・完了済み・重要決定・次の作業・禁止事項
2. **`CLAUDE.md`** — このリポジトリの運用ルールの全体像(役割・境界・優先読み込み順)。名前は"Claude"だがルール自体はCodexにも適用される
3. **`OPERATING_MANUAL.md`** — スタジオ全体のビジョン・組織図・命名規則
4. **`AI_RULES.md`** — AIチーム全体の役割分担、Golden Rule
5. **`IMAGE_GENERATION_POLICY.md`**(Production Policy Version 1.3) — 画像生成エンジン標準・AI社員の役割定義・制作フロー・「分からないまま進まない」最優先原則。**AI社員による生成実行の例外(v1.1〜v1.2、Panel04限定)はv1.3で撤回済み**
6. **`AI_WORKFLOW_V1.md`** — CUT単位制作の標準ワークフロー(Studio OS、現行v1.3)。調査タスクと制作タスクの分離(v1.3)を含む
7. `HANDOFF.md`に記載された対象プロジェクトの`Projects/<作品名>/STATUS.md` — そのプロジェクトの直近の進捗

各ファイルの詳細な役割分担・禁止事項は上記の原本を参照し、本ファイルでは重複させない。

## Production Policy Version 1.3の理念(最優先事項)

> FLY77STARの価値は、AIが作品を作ることではない。
> 人間のクリエイティブを、AIによって最大限に表現することである。

AI社員(Codex含む)は**「生成する担当」ではなく「最高品質の制作設計を行う担当」**である。担当範囲はStory Bible / Character Master / Location Master / Panel Storyboard / Director Notes / Image Prompt / QC / Production Review / Production Report / 登録。**実際の本番画像生成はAI社員が行わない。**

**撤回済みの例外(Version 1.1〜1.2、2026-07-11、Panel04限定)**: 一時的にAI社員が生成実行を担当する運用としていたが、Higgsfield MCP経由の生成系ツールがこの環境(managed remote execution environment)では承認待ちにより実行不能と技術検証タスクで確定したため、2026-07-11(v1.3)にDirector判断で撤回。生成実行は元の運用(Director/GPT Image運用側)に戻っている。詳細: `IMAGE_GENERATION_POLICY.md`。

**最優先原則(Version 1.2、2026-07-11〜)**: 「分からないことは止まる。Directorへ確認する。推測で本番生成しない。」MCP・外部サービス・APIで承認待ち・権限不足・仕様不明に遭遇した場合、推測値・代替値・仮設定で処理を進めることは**絶対に行わない。** 必ず停止し、①何を実行しようとしたか②何がブロックされたか③何が分かっていて何が分からないか④Directorに何を確認してほしいか、の4点を整理して報告する。詳細: `IMAGE_GENERATION_POLICY.md`「最優先原則」「MCP・外部サービス・API承認待ち/権限不足時のエスカレーション手順」。

## Codex固有の厳守事項

- **AI社員(Codex含む)は本番画像・動画生成を実行しない**(Version 1.3、2026-07-11)。v1.1〜v1.2で設けていたPanel04限定の生成実行例外は、Higgsfield MCP経由の生成系ツールがこの環境では実行不能と判明したため撤回済み。GPT Image/Higgsfieldでの生成は、制作フロー(`IMAGE_GENERATION_POLICY.md`参照)の②社長レビュー・③採用決定を経て、Director/GPT Image運用側が実行する
- 生成実行の担当者によらず、以下は引き続き有効:
  - **同一Seedを技術的に取得できない場合は、Director Approved Pilot(Director承認済みの720pパイロットテイク)をBaselineとして4Kを生成する**(Version 1.2)。Seedへのこだわりよりも、Director承認済みの演出内容の再現を優先する
  - 生成物のQCでは、Character/Composition/Lighting/Story/Emotionの5項目自己チェック+改善提案(最大3項目)の型を、`Prompt/IMAGE_QC_CHECKLIST.md`によるProduction QCの一環として活用してよい
- **承認済み素材を上書きしない。** Director Approval済みのCharacter Master/Costume Master/画像等は、社長の明示的な指示なしに再生成・変更・上書きしない
- **Studio OS(`AI_WORKFLOW_V1.md`)のバージョンを勝手に変更しない。** バージョン番号(現行v1.3)の変更は正式な制作方針更新指示があった場合のみ
- **調査タスク(MCP/API/Higgsfield/Git/外部サービス/モデル確認/権限確認)中に技術的ブロッカーが発生した場合、制作タスク(Production Package/画像生成/動画生成/QC/Documentation)へ進まない**(Studio OS v1.3)。まず技術課題を解決し、Directorへ報告し、解決後に制作を再開する。Production Environmentの健全性をProductionより優先する
- **作業前後に必ず`git status`と`git diff`を確認する。** 作業前に未反映の変更や未知の状態がないかを確認し、作業後は自分が加えた差分が意図通りかを確認してからでないと次の工程に進まない
- **作業終了時に`STATUS.md`(対象プロジェクト)と`HANDOFF.md`を更新する。** 次に引き継ぐ担当(Claude Codeでも別のCodexセッションでも)が状態を正確に把握できるようにする
- **コミットとpushは社長承認後に実行する。** 明示的な承認・指示がない限り、作業内容をコミット・pushしない

## キャラクター設定の重要事項

- **HINAはSE77NTH.ではなくソロアーティストである。** SE77NTH.は引き続きMIU/AYA/NANAの3人組として扱う。HINAをSE77NTH.のメンバーとして登録・記述しない

## 関連

- `HANDOFF.md`(現在の作業状態)
- `CLAUDE.md` / `AI_RULES.md` / `OPERATING_MANUAL.md` / `IMAGE_GENERATION_POLICY.md` / `AI_WORKFLOW_V1.md`(各ルール原本)
- `GITHUB_OPERATIONS.md`(ブランチ運用・PRチェックリスト・大容量ファイル方針)
