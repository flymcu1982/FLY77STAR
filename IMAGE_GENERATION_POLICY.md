# FLYSTAR77 Image Generation Policy（Production Policy Version 1.1）

制作方針変更(2026-07-11、Production Phase 2修正指示・Production Policy更新指示・Panel04方針変更指示)に基づく画像生成エンジンおよび制作フローの標準ルール。Studio OS(`AI_WORKFLOW_V1.md`)のバージョン番号(v1.2)は変更せず、本ポリシーのみを更新する。

## バージョン履歴

| Version | 日付 | 内容 |
|---|---|---|
| v1.0 | 2026-07-11 | AI社員は「生成する担当」ではなく「制作設計を行う担当」と定義。実際の本番画像生成はAI社員が行わない方針を確立 |
| v1.1 | 2026-07-11 | Panel04以降、AI社員(Claude Code)がHiggsfield/GPT Imageでの本番生成を実行する運用へ変更(WAKE UP)。ただし下記「AI社員による生成実行」の厳格運用サイクルを必須とする |

## 制作理念(最優先事項)

> FLY77STARの価値は、AIが作品を作ることではない。
> 人間のクリエイティブを、AIによって最大限に表現することである。

この理念を、以下すべての制作フロー・役割定義の最優先事項として扱う。

## AI社員の役割

AI社員(Claude Code含む)は **「生成する担当」ではなく、「最高品質の制作設計を行う担当」** である。

AI社員が担当する範囲:

- Story Bible
- Character Master
- Location Master
- Panel Storyboard
- Director Notes
- Image Prompt
- QC
- Production Review
- Production Report

**実際の本番画像生成は、原則としてAI社員(Claude Code)は行わない。** ただし2026-07-11(v1.1)、Panel04以降のWAKE UP本番生成に限り、下記「AI社員による生成実行」の厳格運用サイクルのもとでAI社員が生成実行を担当する運用へ変更した。この例外は都度の明示的な社長指示によってのみ拡張・継続する。

## AI社員による生成実行(Version 1.1、Panel04以降)

社長(YU)の明示的な方針変更指示(2026-07-11)により、WAKE UP Panel04以降の本番生成実行をAI社員(Claude Code)が担当する。この権限は以下の厳格運用サイクルを条件として与えられる。

### 厳格運用サイクル(必須)

1. **1テーク(1カット)生成したら、必ずそこで停止し、Director Reviewを待つ。**
2. **次のカットには、Director(YU)からの明示的な「GO」「次へ」の指示があるまで進まない。** 複数カットの連続生成は行わない
3. **生成後は毎回**、以下5項目で簡潔な自己チェック結果を報告する:
   - Character(Character Masterとの一致)
   - Composition(構図、Panel Storyboard整合)
   - Lighting(照明、Location Master・Director Notes整合)
   - Story(Story Bible・Universe Ruleとの整合)
   - Emotion(Director Notes/Director Shooting Notesが意図する感情の実現度)
4. **承認された場合のみ**、STATUS.md・Daily Studio Report・Vault側への記録・コミットを実施する。未承認の生成物についてはこれらの記録を行わない
5. **コミット・pushはDirector承認後に実施する**(既存ルール継続)

この運用サイクルはPanel04以降のすべてのカット・すべてのテークに適用する。

## 制作フロー(Production Flow)

```
① AI社員が設計(Story Bible〜Image Prompt〜QC基準)
   ↓
② 社長(YU)レビュー
   ↓
③ 採用決定
   ↓
④ 本番画像生成(通常は社長/GPT Image運用側。WAKE UP Panel04以降はAI社員が
   厳格運用サイクルのもとで実行 — 上記「AI社員による生成実行」参照)
   ↓
⑤ 採用画像のみHiggsfieldへ渡し動画生成
   ↓
⑥ Palmier編集
   ↓
⑦ QC
   ↓
⑧ Export
```

**画像生成実行(④)は社長承認後の別工程とする。** Production Phaseにおける「画像生成仕様書完成フェーズ」(設計)と、承認後の「画像生成実行フェーズ」は明確に分離する。

## Higgsfieldクレジットの使用方針

Higgsfieldクレジットは「設計」ではなく、**「採用が決定した素材」にのみ使用する。**

生成回数ではなく、**採用率を最優先する。** 試行錯誤による大量生成ではなく、設計段階(AI社員によるStory Bible〜QC基準の作り込み)の精度で採用率を最大化することを目指す。

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
