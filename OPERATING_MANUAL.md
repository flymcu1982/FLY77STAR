# FLYSTAR77 STUDIO OS v1.0

Claude Code（CTO）はこのファイルを参照して作業する。

## Priority Rules

このリポジトリでは、以下のファイルを最優先ルールとして扱う。

1. `OPERATING_MANUAL.md`
2. `SNS_OPERATIONS.md`
3. `PRODUCTION_BIBLE.md`
4. `AI_RULES.md`
5. `CODEX_RULES.md`
6. `PALMIER_RULES.md`
7. `ProductionBible/RULE.md`

以後の作業は、このルールに従って進める。

不足しているフォルダやファイルがあれば、自動で提案する。

作業開始時は、まずプロジェクト構成を確認し、改善点があれば報告する。

## Organization

- **YU — CEO**: 最終判断者。すべての意思決定はYUの承認をもって確定する。
- それ以外のAI/ツールは全員「AI社員」として、担当領域内では自律的に判断・提案する。詳細な役割分担、得意な仕事、禁止事項、作業開始前に読むべきファイルは `AI_RULES.md` を参照する。

## Vision

AIと人の創造力を組み合わせ、映画品質の映像作品を効率的かつ継続的に制作する。

## Mission

AIと人の創造力を組み合わせ、映画品質の映像作品を効率的かつ継続的に制作する。

## Core Values

- 感情を最優先する。
- 技術は作品のために使う。
- 妥協ではなく改善を積み重ねる。
- 一つの作品ごとに制作フローを進化させる。
- AIは代役ではなくチームメンバー。

## Web Operations Note

- 公式Webサイトの公開URL確認は、編集作業と分けて扱う
- サイト内の表示テキスト変更と、Netlify側の実URL変更は別作業
- `netlify.app` サブドメイン変更はNetlify管理画面側で行い、HTML修正だけでは変更されない
- 2026-07-17時点の公開確認:
  - 正: `https://fly77star-studio.netlify.app/`
  - 旧: `https://flystar77-studio.netlify.app/` は無効
- Web動画運用:
  - `Distance` ショート2本のみ公開継続
  - `Distance` フル / teaser、`TOMORROW`、ENERGY-D CM、FANG CM 動画は停止
  - 停止動画はポスター表示へ置換する

## Production Pipeline

```text
企画
↓
脚本
↓
絵コンテ
↓
キャラクター制作
↓
映像生成
↓
仮編集
↓
本編集
↓
カラー
↓
音響
↓
書き出し
↓
広報
```

## Studio OS Layers

FLYSTAR77 STUDIO OSは、以下の5レイヤーで運用する。

1. 制作: 企画、脚本、絵コンテ、キャラクター、CUT設計を管理する。
2. 編集: Palmierへ渡す編集指示、尺、同期、フェード、音響を管理する。
3. 広報: YouTube、TikTok、Instagram向けの書き出しと投稿素材を管理する。
4. 品質管理: 映像、音、余韻、ルール準拠をチェックする。
5. 自動化: フォルダ生成、構成検証、編集指示書生成、GitHub Actionsを整備する。

## AI Team

### YU（CEO）

役割:

- 最終判断
- 全体方針の承認

### ChatGPT / Claude（チャット）

役割:

- 企画
- 戦略
- 演出
- プロンプト設計
- 世界観設計
- 脚本
- Production Bible管理

### Claude Code（CTO）

役割:

- GitHub運用
- Web公開（Netlify連携）
- フォルダ・ファイル整理
- 編集指示生成
- 自動化スクリプト管理
- Palmierとの連携

### Higgsfield / GPT Image

役割:

- キャラクター・ビジュアル生成
- 2026-07-11の制作方針変更により標準エンジンをHiggsfield / Nano BananaからHiggsfield / GPT Imageへ変更。Nano BananaはProductionフローから除外。Soul 2(Higgsfield Soul 2.0)はCharacter Masterに使用せず、アーティスト写真・ファッションカット・SNSビジュアル・雰囲気重視の一枚絵・コンセプトアートに限定(詳細: `IMAGE_GENERATION_POLICY.md`)

### Seedance / Gemini Omni Flash

役割:

- MV・動画生成
- リップシンク
- キャラクター演技

### Palmier

役割:

- 仮編集
- タイムライン生成
- セリフ同期
- BGM同期
- 書き出し

### ElevenLabs

役割:

- ナレーション
- セリフ
- ボイス制作

### Obsidian

役割:

- 会社の記憶・社内Wiki

### GitHub

役割:

- 資産保管庫

### Netlify

役割:

- 公式サイト公開

## Supporting Operations Documents

The following documents provide detailed operational procedures for specific layers:

- **`SNS_OPERATIONS.md`** (Layer 3 - 広報): SNS account strategy, handle reservation, content management, and reporting for YouTube, TikTok, and Instagram
- **`GITHUB_OPERATIONS.md`** (Layer 5 - 自動化): GitHub branching, CI/CD, and large-file policies
- **`IMAGE_GENERATION_POLICY.md`**: Image generation engine standards and production policy
- **`PROMPT_GUIDE.md`**: Prompt structure and generation guidelines

These documents are authoritative for their respective domains and should be consulted during implementation.

## Standard Folder Structure

```text
FLYSTAR77/
├── README.md
├── OPERATING_MANUAL.md
├── PRODUCTION_BIBLE.md
├── AI_RULES.md
├── CODEX_RULES.md
├── PALMIER_RULES.md
├── PROMPT_GUIDE.md
├── FOLDER_STRUCTURE.md
├── Projects/
├── Assets/
├── Templates/
├── ProductionBible/
├── Exports/
└── Archive/
```

## Project Structure

```text
Projects/
└── Distances/
    ├── Import/
    ├── Unsorted/
    ├── CUT/
    ├── Audio/
    ├── Dialogue/
    ├── Reference/
    ├── Prompt/
    ├── Edit/
    ├── Storyboard/
    ├── Color/
    ├── QC/
    ├── Delivery/
    ├── Export/
    └── project.json
```

## Naming Rules

### CUT

```text
CUT01.mp4
CUT02.mp4
CUT03.mp4
```

### Dialogue

```text
CUT06_dialogue.wav
CUT12_dialogue.wav
CUT17_dialogue.wav
```

### Prompt

```text
CUT06_Dreamina.md
CUT17_Dreamina.md
```

## Dreamina Rules

全カット共通:

- Cinematic Style
- Character
- Location
- Camera
- Scene
- Acting
- Emotion
- Director's Notes
- Negative Prompt

## Director Rule

AIへ「演技」ではなく「感情」を伝える。

## Golden Rule

AIにセリフを読ませるのではない。

感情を演じさせる。

## Editing Rules

### CUT17

余韻を切らない。

### CUT18

- 肩を寄せるあと約1秒残す。
- セリフ後は急にカットしない。

## Color Rules

標準:

- Kodak Vision3
- Blue Hour
- Warm Skin
- Natural Contrast

## Camera Rules

基本:

- 85mm
- f1.8
- Static Camera
- Movie Composition

## Audio Rules

- BGMを邪魔しない。
- 環境音を残す。
- セリフは囁くように。

## Release Rules

SNS実装・運用の詳細ルールは `SNS_OPERATIONS.md` を参照する。

### YouTube

- 4K と 1K
- 公式Gmailは新規作成してよい。
- 公式YouTubeは新規開設しない。既存チャンネル `@yuyama6664` を FLY77STAR. 公式チャンネルへブランド移行する。
- 既存動画は削除禁止。公開継続、限定公開、非公開、再編集活用のいずれかに分類して扱う。
- ハンドル確定、本番変更、公開、削除、既存動画の公開設定変更は、必ずYU最終承認後に行う。

### TikTok

- 9:16

### Instagram

- Reels

## AI Production Policy

適用範囲: 広告・CM・クライアントワークでAI生成楽曲・AI生成映像を使用する場合。著作権・JASRAC対応・AI利用の説明責任を明確にするための方針。

- Suno等のAI音楽生成ツールは、原則として「デモ制作・アイデア出し・仮歌・方向性確認」の用途として扱う。
- クライアントワークでは、人間の創作的寄与を明確にする。
- 作詞、構成、メロディ方向性、演出意図、最終判断はYUが行う。
- AIが自律生成しただけの作品を、そのまま権利管理・商用納品しない。
- 広告・CM案件では、AI使用箇所を記録する。
- 必要に応じて、人間による再編曲、再録音、ミックス、マスタリングを行う。
- 実在するブランド・大会・企業名は、正式な許諾がない限り公式タイアップに見せない。
- 架空のブランドやCM風の作品として制作する場合は、その旨を明記する。

## Claude Code Rule（CTO）

Claude Codeは:

- `Projects/` フォルダを管理する。
- 不足ファイルを通知する。
- Palmierへ編集指示を生成する。
- Production Bibleを最優先ルールとして扱う。
- GitHub運用時は構成検証スクリプトを実行する。
- Web公開（Netlify連携）を管理する。
- 作業終了時は、変更内容を必ず日本語で要約し、必要に応じてGitへコミットする。

## Palmier Rule

Palmierは:

- CUTを読み込む。
- BGM同期。
- セリフ同期。
- フェード生成。
- 書き出し。

## Quality Control Rule

書き出し前に必ず確認する。

- 余韻を切っていないか。
- セリフ後に急なカットがないか。
- BGMがセリフを邪魔していないか。
- 9:16、4Kなど媒体別の仕様に合っているか。
- CUT名、Dialogue名、Prompt名が命名規則に沿っているか。

## Automation Rule

Claude Codeで自動化する:

- プロジェクト作成
- 標準フォルダ作成
- `project.json` 作成
- `Import/` 素材整理
- CUT番号なし素材の `Unsorted/` 退避と手動割り当て
- CUTリスト作成
- EDIT_PLAN生成
- 構成検証
- GitHub Actionsによる自動チェック
- Web公開（Netlify連携）
- 作業終了時の日本語要約とGitコミット

Palmierへ渡す:

- CUT読み込み
- タイムライン編集
- BGM同期
- セリフ同期
- フェード生成
- 動画書き出し

## Brand Rule

FLYSTAR77作品は「派手さ」ではなく「余韻」。

大きな感情ではなく、静かな感情。

## Version Rule

```text
v1.0
制作開始
↓
v1.1
改善
↓
v2.0
新機能
```

## Long Term Vision

```text
YU（CEO）
↓
ChatGPT / Claude
↓
Claude Code
↓
Higgsfield / GPT Image
↓
Seedance / Gemini Omni Flash
↓
Palmier
↓
Premiere（必要時）
↓
SNS / Netlify
↓
AI広報
```

## Short Instruction Template

Claude Codeへは短い指示だけ出す。

例:

```text
このリポジトリの OPERATING_MANUAL.md と PRODUCTION_BIBLE.md を最優先ルールとして扱ってください。

以後の作業は、このルールに従って進めてください。

不足しているフォルダやファイルがあれば提案してください。

まずはプロジェクト構成を確認し、改善点があれば教えてください。
```
