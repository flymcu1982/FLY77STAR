# CHAR_AYA_MASTER — Character Master Reference（WAKE UP）

Character Bible参照: AYA（Obsidian Vault `10_Characters/AYA.md`）
Asset ID: `CHAR_AYA_MASTER01`
目的: 今後すべての画像・動画生成で同一人物(AYA)を維持するための固定リファレンス。実際の生成はHiggsfield + GPT Image側の作業(2026-07-11制作方針変更、`IMAGE_GENERATION_POLICY.md`準拠。Nano Banana不使用、Character MasterにSoul 2は使用しない)。本ファイルはその仕様書。

## 基本情報

SE77NTH.ボーカル/ラップ。グループ随一の歌唱力・ダンススキル、クールなお姉さん。センターパートのストレートダークブラウンヘア、ヌードリップ、シルバー系アクセサリー。

## Character Lock Prompt(共通ベース記述、GPT Image用、全アングル・表情で必ず含める)

```
East Asian Japanese young woman (AYA), center-parted straight dark
brown hair, nude-toned lips, silver accessories, cool composed
expression base, consistent facial structure across all angles and
expressions, exact facial consistency maintained via this fixed
reference description (GPT Image, Soul 2 not used)
```

## アングル

### 真正面(Front)
```
CHAR_AYA_MASTER01_FRONT — AYA, front-facing portrait, direct eye
contact with camera, calm cool expression, studio-neutral background,
even lighting, 35mm portrait lens look
```

### 左45°
```
CHAR_AYA_MASTER01_L45 — AYA, head turned 45 degrees to her left,
three-quarter view, same lighting and background as front reference
```

### 右45°
```
CHAR_AYA_MASTER01_R45 — AYA, head turned 45 degrees to her right,
three-quarter view, same lighting and background as front reference
```

### 横顔(Profile)
```
CHAR_AYA_MASTER01_PROFILE — AYA, full left profile, center-parted hair
line clearly visible, same lighting and background as front reference
```

### 全身(Full Body)
```
CHAR_AYA_MASTER01_FULLBODY — AYA, full body standing pose, confident
relaxed stance, casual placeholder outfit(下記衣装に関する注意を参照),
studio-neutral background, consistent proportions with portrait
references
```

## 表情差分(6種)

1. **通常(ニュートラル)** — `calm composed expression, steady eyes, closed mouth`
2. **明るい笑顔** — `rare bright smile, eyes softened, breaks her usual cool composure`
3. **控えめな微笑み** — `small controlled smile, cool undertone` (CUT02合流での標準表情)
4. **驚き** — `subtle raised eyebrows, slightly parted lips, restrained surprise` (CUT05・CUT09で使用)
5. **真剣な表情** — `focused intense gaze, slight furrow, sharp concentration`
6. **代表表情(クールな余裕)** — `confident half-smile, one eyebrow slightly raised, effortless cool` (グループ内の実力No.1を象徴する表情)

## 一貫性アンカー(キャラクター崩れ防止の重要ポイント)

- センターパートを崩さない(サイドパートや前髪ありへの変化を避ける)
- 髪は直毛のストレートで統一(ウェーブ化を避け、MIUと明確に区別する)
- リップはヌードトーンで統一(MIUのグロス感・NANAの血色感と混同しない)
- シルバー系アクセサリーのみ使用

## 衣装に関する注意

Costume Bible未登録(既知の残課題)。正式デザイン決定までの**技術的な仮置き**として、以下の中立的な私服描写を全生成で共通使用する: `casual muted-tone top, simple trousers or skirt, no visible logos or brand marks`。これは創作上の衣装デザイン決定ではなく、生成の一貫性を保つための暫定処理。正式デザインが決定次第、Costume Bible登録の上で本ファイルを更新すること。

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §5「キャラクター & アーティスト」のSE77NTH. (AYA記述)。Character Referenceとして確定
- Character Bible: Obsidian Vault `10_Characters/AYA.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
