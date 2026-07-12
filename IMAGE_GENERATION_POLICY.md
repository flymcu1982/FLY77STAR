# FLYSTAR77 Image Generation Policy（Production Policy Version 1.3）

制作方針変更(2026-07-11、Production Phase 2修正指示・Production Policy更新指示・Panel04方針変更指示)に基づく画像生成エンジンおよび制作フローの標準ルール。Studio OS(`AI_WORKFLOW_V1.md`)のバージョン番号(v1.2)は変更せず、本ポリシーのみを更新する。

## バージョン履歴

| Version | 日付 | 内容 |
|---|---|---|
| v1.0 | 2026-07-11 | AI社員は「生成する担当」ではなく「制作設計を行う担当」と定義。実際の本番画像生成はAI社員が行わない方針を確立 |
| v1.1 | 2026-07-11 | Panel04以降、AI社員(Claude Code)がHiggsfield/GPT Imageでの本番生成を実行する運用へ変更(WAKE UP)。ただし下記「AI社員による生成実行」の厳格運用サイクルを必須とする |
| v1.1(追記) | 2026-07-11 | Director Additional Instruction: 厳格運用サイクルの自己チェック報告に「改善提案(Improvement Suggestions、1〜3項目)」の提出を追加。Directorは提案を採用/却下/保留のいずれかで判断する |
| v1.2 | 2026-07-11 | WAKE UP Panel04の4K本番生成試行時、Higgsfield MCPツール(`models_explore`/`show_generations`)が承認待ちで実行不能という技術的ブロッカーに遭遇。推測のモデルID・Seedでの本番生成を行わず停止した対応をDirectorが承認・評価し、この経験をルール化: ①同一Seedを取得できない場合のBaseline運用ルール、②MCP・外部サービス・API承認待ち/権限不足時のエスカレーション手順(4点報告)を新設。「分からないまま進まない」を最優先事項として明文化 |
| v1.3 | 2026-07-11 | 技術検証タスクとして`generate_video`(get_cost:trueの無課金見積りプリフライトを含む)を試行した結果、Higgsfield MCP経由の生成系ツールがこの環境(managed remote execution environment)では実行不可能と確定。**v1.1で導入した「AI社員による生成実行」の例外を撤回し、生成実行は元の運用(Director/GPT Image側が担当)へ戻す。** AI社員はProduction Package作成・QC・記録・Git管理を担当する原則に復帰。「分からないまま進まない」最優先原則、Seed未取得時のBaseline運用ルール、MCP承認待ち時のエスカレーション手順(v1.2で新設)は生成実行の担当者によらず引き続き有効 |

## 制作理念(最優先事項)

> FLY77STARの価値は、AIが作品を作ることではない。
> 人間のクリエイティブを、AIによって最大限に表現することである。

この理念を、以下すべての制作フロー・役割定義の最優先事項として扱う。

## 最優先原則: 分からないまま進まない(Version 1.2、2026-07-11)

WAKE UP Panel04の4K本番生成試行時、Higgsfield MCPツール(`models_explore`/`show_generations`)が承認待ちで実行不能という技術的ブロッカーが発生した。AI社員はモデルID・Seedを推測で補って生成を強行せず、停止してDirectorへ報告した。Directorはこの対応を承認・評価し、以下を**Production Policyの最優先事項**として明文化する。

> **分からないことは止まる。Directorへ確認する。推測で本番生成しない。**

- MCP・外部サービス・API等で承認待ち・権限不足・仕様不明に遭遇した場合、推測値・代替値・仮設定で処理を進めることは**絶対に行わない**
- 詳細な手順は下記「MCP・外部サービス・API承認待ち/権限不足時のエスカレーション手順」を参照

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

**実際の本番画像生成は、AI社員(Claude Code)は行わない。** 2026-07-11、v1.1でPanel04以降のWAKE UP本番生成に限りAI社員が生成実行を担当する例外を設けたが、Higgsfield MCP経由の生成系ツールがこの環境では技術的に実行不可能であることが判明したため、**v1.3で当該例外を撤回した。** 生成実行は元の運用(Director/GPT Image側が担当)に戻る。

## AI社員による生成実行(Version 1.1〜1.2、Panel04限定 — **Version 1.3で撤回、履歴として保持**)

社長(YU)の明示的な方針変更指示(2026-07-11)により、一時的にWAKE UP Panel04以降の本番生成実行をAI社員(Claude Code)が担当する運用としていたが、Higgsfield MCP経由の生成系ツール(`generate_video`のget_cost:trueプリフライトを含む)がこの環境(managed remote execution environment)では承認待ちにより実行不能であることが技術検証タスクで確定したため、**2026-07-11、Director判断によりこの例外は撤回された。** 以下は撤回前に定めていた運用ルールの記録として保持する。

### 厳格運用サイクル(必須)

1. **1テーク(1カット)生成したら、必ずそこで停止し、Director Reviewを待つ。**
2. **次のカットには、Director(YU)からの明示的な「GO」「次へ」の指示があるまで進まない。** 複数カットの連続生成は行わない
3. **生成後は毎回**、以下5項目で簡潔な自己チェック結果を報告する:
   - Character(Character Masterとの一致)
   - Composition(構図、Panel Storyboard整合)
   - Lighting(照明、Location Master・Director Notes整合)
   - Story(Story Bible・Universe Ruleとの整合)
   - Emotion(Director Notes/Director Shooting Notesが意図する感情の実現度)
4. **改善提案(Improvement Suggestions、最大3項目)を必ず提出する**(2026-07-11追記、Director Additional Instruction)。自己チェック5項目の直後に、Character/Composition/Lighting/Story/Emotionのいずれかに関する改善余地を最大3項目、簡潔に提案する。Directorは各提案を採用/却下/保留のいずれかで判断する
5. **Directorの判断(GO/採用/却下/保留)なしに、AI社員が自ら修正・再生成・次Panelへの進行を行うことはない**
6. **承認された場合のみ**、STATUS.md・Daily Studio Report・Vault側への記録・コミットを実施する。未承認の生成物についてはこれらの記録を行わない
7. **コミット・pushはDirector承認後に実施する**(既存ルール継続)

この運用サイクルはPanel04以降のすべてのカット・すべてのテークに適用する。サイクルの流れ: **1テーク生成 → 自己チェック → 改善提案 → Director Review → Director GO**。

### Seedを取得できない場合のBaseline運用(Version 1.2)

4K本番生成を「720pパイロットと同一Seed」で行う運用が原則だが、MCPツールの承認待ち等により同一Seed値を技術的に取得できない場合がある。この場合の代替ルールを以下の通り正式に定める:

**同一Seedを取得できない場合は、Director Approved Pilot(Directorが承認した720pパイロットテイク)をBaselineとして4Kを生成する。** 同一Seedへのこだわりよりも、Director承認済みの演出内容(Character/Composition/Lighting/Story/Emotion)を再現することを優先する。

### MCP・外部サービス・API承認待ち/権限不足時のエスカレーション手順(Version 1.2、必須)

MCPツール・外部サービス・APIの呼び出しが「承認待ち」「権限不足」等で実行できない場合、AI社員は**推測・代替値・仮設定で処理を進めてはならない。** 必ず処理を停止し、以下4点を整理してDirectorへ報告する:

1. **何を実行しようとしたか**
2. **何がブロックされたか**
3. **何が分かっていて、何が分からないか**
4. **Directorに何を確認してほしいか**

## 制作フロー(Production Flow)

```
① AI社員が設計(Story Bible〜Image Prompt〜QC基準)
   ↓
② 社長(YU)レビュー
   ↓
③ 採用決定
   ↓
④ 本番画像生成(社長/GPT Image運用側が実行。2026-07-11のv1.3により、
   AI社員による生成実行の例外(v1.1〜v1.2、Panel04限定)は撤回済み)
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
- 2026-07-11、WAKE UP Panel04の4K本番生成を機にAI社員による生成実行を一時許可(v1.1)したが、Higgsfield MCP経由の生成系ツールがこの環境では実行不可能と判明したため撤回(v1.3)。生成実行はDirector/GPT Image運用側が継続する原則の元の形へ戻った
- 詳細な決定理由・承認記録は Obsidian Vault `03_Company/Decisions/` の該当エントリを参照

## 関連

- `AI_WORKFLOW_V1.md`(Studio OS標準制作ワークフロー、バージョン番号は本ポリシーの影響を受けない)
- `CLAUDE.md` / `AI_RULES.md` / `OPERATING_MANUAL.md`(役割・組織図側の該当箇所も本ポリシーに合わせて更新済み)
- `PROMPT_GUIDE.md`(プロンプト構造ルール)
