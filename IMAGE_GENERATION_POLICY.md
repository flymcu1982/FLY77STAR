# FLYSTAR77 Image Generation Policy

制作方針変更(2026-07-11、Production Phase 2修正指示)に基づく画像生成エンジンの標準ルール。Studio OS(`AI_WORKFLOW_V1.md`)のバージョン番号(v1.2)は変更せず、本ポリシーのみを更新する。

## エンジン変更

画像生成エンジンを **「Higgsfield / Nano Banana」** から **「Higgsfield / GPT Image」** へ変更する。

**Nano BananaはProductionフローから除外する。**

## 通常制作(Standard Production)

以下すべてで **GPT Image** を標準とする:

- Character Master
- Location Master
- Storyboard
- Panel Image
- Production Image

## Soul 2(Higgsfield Soul 2.0)の扱い

Soul 2はProduction標準では使用しない。**Character Masterには使用しない。**

使用用途は以下に限定する:

- アーティスト写真
- ファッションカット
- SNSビジュアル
- 雰囲気重視の一枚絵
- コンセプトアート

上記はいずれも「制作(Production)」の管理下にある画像ではなく、広報・雰囲気醸成用のクリエイティブ素材として個別に扱う。

## 適用範囲

- 本ポリシーは全プロジェクト共通のStudio OS運用ルールとして扱う(WAKE UP限定ではない)
- 既存プロジェクトの完成済みStoryboard/Panel Storyboard/生成プロンプト内に残る"Soul ID locked for consistency"等の表記は、本ポリシー制定時点では遡及的に修正しない(既知の残課題、Discovery Log参照)。新規に作成する成果物から本ポリシーを適用する

## 経緯

- Character Masterの技術的な同一人物担保は、従来Higgsfield Soul 2.0(Soul ID)を前提として設計されていた
- 2026-07-11の制作方針変更により、Higgsfield + GPT Imageを標準エンジンとする方針へ切り替え
- 詳細な決定理由・承認記録は Obsidian Vault `03_Company/Decisions/` の該当エントリを参照

## 関連

- `AI_WORKFLOW_V1.md`(Studio OS標準制作ワークフロー、バージョン番号は本ポリシーの影響を受けない)
- `CLAUDE.md` / `AI_RULES.md` / `OPERATING_MANUAL.md`(役割・組織図側の該当箇所も本ポリシーに合わせて更新済み)
- `PROMPT_GUIDE.md`(プロンプト構造ルール)
