# FLYSTAR77 STUDIO OS v1.0

Codexはこのファイルを参照して作業する。

## Priority Rules

このリポジトリでは、以下のファイルを最優先ルールとして扱う。

1. `OPERATING_MANUAL.md`
2. `PRODUCTION_BIBLE.md`
3. `AI_RULES.md`
4. `CODEX_RULES.md`
5. `PALMIER_RULES.md`
6. `ProductionBible/RULE.md`

以後の作業は、このルールに従って進める。

不足しているフォルダやファイルがあれば、自動で提案する。

作業開始時は、まずプロジェクト構成を確認し、改善点があれば報告する。

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

### ChatGPT

役割:

- 企画
- 演出
- プロンプト設計
- 世界観設計
- Production Bible管理

### Dreamina

役割:

- 映像生成
- リップシンク
- キャラクター演技

### Codex

役割:

- 制作進行
- フォルダ管理
- 編集指示生成
- ファイル整理
- Palmierとの連携

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

### YouTube

- 4K

### TikTok

- 9:16

### Instagram

- Reels

## Codex Rule

Codexは:

- `Projects/` フォルダを管理する。
- 不足ファイルを通知する。
- Palmierへ編集指示を生成する。
- Production Bibleを最優先ルールとして扱う。
- GitHub運用時は構成検証スクリプトを実行する。

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

Codexで自動化する:

- プロジェクト作成
- 標準フォルダ作成
- `project.json` 作成
- `Import/` 素材整理
- CUT番号なし素材の `Unsorted/` 退避と手動割り当て
- CUTリスト作成
- EDIT_PLAN生成
- 構成検証
- GitHub Actionsによる自動チェック

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
ChatGPT
↓
Codex
↓
Dreamina
↓
Palmier
↓
Premiere（必要時）
↓
SNS
↓
AI広報
```

## Short Instruction Template

Codexへは短い指示だけ出す。

例:

```text
このリポジトリの OPERATING_MANUAL.md と PRODUCTION_BIBLE.md を最優先ルールとして扱ってください。

以後の作業は、このルールに従って進めてください。

不足しているフォルダやファイルがあれば提案してください。

まずはプロジェクト構成を確認し、改善点があれば教えてください。
```
