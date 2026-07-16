# WAKE UP EDIT PLAN

Palmierへ渡す編集指示書。Production Phase 1。生成プロンプト本体(`Storyboard/CUT<番号>.md`)・Panel Storyboard(`Storyboard/CUT<番号>_絵コンテ.md`)・Director Notesの内容を元に作成。Studio OSの改修は行わず、既存のStoryboard内容は変更していない。

## Project Settings

- Project: `WAKE UP`
- Artist: SE77NTH.
- CUT Count: 12
- 楽曲尺: 3:19(199秒)／BPM 95.7／女性R&Bボーカル+男性ラップ
- Primary Format: 9:16(TikTok / Instagram Reels基準)、YouTube用に4K別書き出し
- Story Bible: Obsidian Vault `06_Projects/WAKE_UP/Overview.md`

## Scene構成

- **Scene1**(CUT01〜04・0:00〜0:45): 渋谷の夜、3人集合〜歩き出す
- **Scene2**(CUT05〜08・0:45〜2:00): 「現実からパラレルワールドへの入口」。詳細: `Storyboard/Scene2_Review.md`
- **Scene3**(CUT09〜12・2:00〜3:19): 「夢から現実へ」。詳細: `Storyboard/Scene3_Review.md`

## Global Editing Rules

- CUTを順番に読み込む。セリフ同期ポイントを優先する(PALMIER_RULES.md準拠)。
- BGMはセリフを邪魔しない。環境音は可能な限り残す。
- フェードは基本的に使わず、CUT間は直接カット(ハードカット)を原則とする。フェード/ホワイトアウトはCUT08→09とCUT12末尾のみの例外。
- CUT08(ホワイトアウトのピーク)とCUT09の接続は、Palmier編集時にフレーム単位で正確に合わせる。
- CUT12のクレーンアップ末尾はテロップ「物語は次回へ続く」の挿入スペースを画面上部または下部に確保する。
- Scene2(CUT05〜08)は「観客には説明せず、違和感だけを積み上げる」方針のため、説明的なテロップ・字幕は一切入れない。

## CUT Timeline

| CUT | Timeline | 尺 | Scene | Camera Motion(要約) | Transition(in→out) |
|---|---:|---:|---|---|---|
| CUT01 | 00:00-00:08 | 8.0s | 1 | 俯瞰ワイド→降下→ミディアム | (Top) → 直接カット |
| CUT02 | 00:08-00:18 | 10.0s | 1 | 人混み奥からのトラッキング→MIU反応→二人ミディアム | 直接カット → 直接カット |
| CUT03 | 00:18-00:30 | 12.0s | 1 | NANA登場ミディアム→3人切り返し→3ショットへ引く | 直接カット → 直接カット |
| CUT04 | 00:30-00:45 | 15.0s | 1 | 背後トラッキング→横並走→路地へ折れるパン | 直接カット → 直接カット |
| CUT05 | 00:45-01:00 | 15.0s | 2 | 発見ワイド→3人反応→ダイナー外観ドリー | 直接カット → 直接カット |
| CUT06 | 01:00-01:20 | 20.0s | 2 | 扉を開けるPOV→店内パン→ブース着席ワイド | 直接カット(切らずに連続) → 直接カット |
| CUT07 | 01:20-01:45 | 25.0s | 2 | 厨房シルエット→正面への寄り→3人反応切り返し | 直接カット(切らずに連続) → 直接カット |
| CUT08 | 01:45-02:00 | 15.0s | 2 | 明滅ワイド→KAI輪郭滲むCU→ホワイトアウトワイド | 直接カット → **ハードカット(ホワイトアウトのピーク)** |
| CUT09 | 02:00-02:20 | 20.0s | 3 | ホワイトアウトからの切り返し→空き区画パン→戸惑いCU | ハードカット → 直接カット |
| CUT10 | 02:20-02:40 | 20.0s | 3 | 歩く3人→シルエットへフォーカス送り→MIU反応 | 直接カット → 直接カット |
| CUT11 | 02:40-03:00 | 20.0s | 3 | すれ違う瞬間→MIU振り返りCU→HINA後ろ姿ワイド | 直接カット → 直接カット |
| CUT12 | 03:00-03:19 | 19.0s | 3 | 後ろ姿→MIU振り返りCU→夜景へクレーンアップ | 直接カット → **フェードアウト(楽曲アウトロ)** |

合計: 199.0s(3:19)。Story Bibleの楽曲尺と一致。

## BGM Plan

- 全体を通してBGM(3:19、BPM95.7)を主軸に編集する。歌唱パート(女性R&Bボーカル+男性ラップ)の配置・アレンジそのものは作曲側(YU/ChatGPT)の判断範囲のため、本EDIT_PLANでは編集上の扱いのみ記載する。
- **Scene1(CUT01〜04)**: BGMを前面に、渋谷の環境音(雑踏・車)を薄く残す。通常のミックスバランス。
- **Scene2(CUT05〜08)**: ダイナーに近づく(CUT05)につれてBGMへ軽いリバーブ/ローパスフィルターを段階的にかけ、店内(CUT06〜07)で最大化、CUT08の明滅〜ホワイトアウトでさらに強調する。「パラレルワールドの音響的な異質さ」をBGM側でも裏付ける処理案。**要YU確認**(音響処理の方向性)。
- **Scene3(CUT09〜12)**: CUT09の切り返しでフィルターを瞬時に解除し、クリアなミックスへ復帰。以降Scene1と同様のバランスで進行し、CUT12終盤でBGM・環境音を同時にフェードアウト。

## SE Plan(CUTごと)

| CUT | SE |
|---|---|
| CUT01 | 雑踏、遠くの車の音 |
| CUT02〜04 | 雑踏+3人の足音、笑い声 |
| CUT05 | 環境音が徐々に静まる。ダイナーの光に呼応する微かな音の変化 |
| CUT06 | 扉の開閉音、店内の環境音(現実の路地とは異質な、静かで暖かい音) |
| CUT07 | 厨房の調理音、皿を置く音 |
| CUT08 | 明滅に合わせた電気的なフリッカー音、ホワイトアウトで無音化 |
| CUT09 | 無音から現実の環境音への復帰 |
| CUT10 | 雑踏の足音。シルエットが映る瞬間、環境音を一瞬遠くする演出 |
| CUT11 | 落ち着いた足音。HINAとすれ違う瞬間、環境音を一瞬沈める演出 |
| CUT12 | 環境音がフェードアウトしながら終わる |

## Dialogue Sync

全セリフは**未収録**(ElevenLabs等での音声生成、または楽曲の歌唱パートとの配置調整はYU/作曲側の判断が必要。`Prompt/IMAGE_ASSET_LIST.md`の既知の残課題を参照)。

| CUT | セリフ | 話者 | 想定タイミング |
|---|---|---|---|
| CUT02 | 「(小声で)待った？」 | AYA | Panel4冒頭 |
| CUT03 | 「お待たせー！」 | NANA | Panel1終盤 |
| CUT04 | 「こっち行ってみない？」 | NANA | Panel3 |
| CUT05 | 「……こんな店、あったっけ？」 | AYA | Panel3 |
| CUT06 | 「……なんか、落ち着く」 | NANA | Panel5 |
| CUT07 | 「……お待たせ」 | KAI | Panel5 |
| CUT08 | 「え……？」 | MIU | Panel3 |
| CUT09 | 「……今の、何だったんだろう」 | AYA | Panel4 |
| CUT11 | 「(小さく、独り言のように)……どこかで、会った気がする」 | MIU | Panel3 |

セリフ前後は急にカットしない(PALMIER_RULES.md準拠)。特にCUT11のMIUのセリフは、次回作への伏線となる最重要セリフのため、セリフ後1.5秒以上のホールドを推奨。

## Color Plan

- **Scene1**: 渋谷の夜景、ネオンと街灯のナチュラルな彩度。35mmフィルム粒子。
- **Scene2**: ダイナーに近づくにつれ暖色(オレンジ〜アンバー)を強め、周囲の寒色とのコントラストを最大化。CUT06は「輪郭がわずかに滲む」ソフトフォーカス。CUT08は暖色ネオン→純白への飽和。
- **Scene3**: CUT09で現実の落ち着いた常夜灯色へハードに復帰。以降Scene1と同系統のトーンへ戻り、CUT12の夜景で締める。
- 全編を通じてCharacter Master(`Reference/CHAR_*_MASTER.md`、Higgsfield + GPT Image、2026-07-11制作方針変更以降Soul 2不使用)を基準にキャラクターの一貫性を維持し、KAIには"East Asian Japanese"を必ず明記(人種ドリフト防止、既存プロンプトの方針を継続)。個別CUTのStoryboard/Panel Storyboard内に残る"Soul ID locked for consistency"表記は既知の残課題(Discovery Log参照、遡及未修正)。

## Camera Motion Detail

CUTごとのパネル単位の詳細なカメラワーク(ショットサイズ・レンズ・構図)は各`Storyboard/CUT<番号>_絵コンテ.md`を参照。特に以下は撮影・生成時の対称性/連続性への配慮が必要:

- CUT01 Panel2(降下クレーン)とCUT12 Panel4(クレーンアップ)は意図的な対構造(Director Notes: `WAKE_UP_CUT12_PANEL04_次回への余韻_DirectorNotes.md`参照)。速度感を揃えることを推奨。
- CUT06 Panel1→2、CUT07 Panel1→2はいずれも「切らずに連続」指定。Palmier側でもカットを挟まない。

## Palmier Output

- 仮書き出し: `Projects/WAKE_UP/Export/`
- 完成動画: `Exports/`
- Export仕様: TikTok / Instagram Reels = 9:16、YouTube = 4K(PALMIER_RULES.md準拠)

## 関連

- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
- Panel Storyboard/Director Notes: `Storyboard/`
- Scene Review: `Storyboard/Scene2_Review.md` / `Storyboard/Scene3_Review.md`
