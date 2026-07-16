# CHAR_NANA_MASTER — Character Master Reference（WAKE UP）

Character Bible参照: NANA（Obsidian Vault `10_Characters/NANA.md`）
Asset ID: `CHAR_NANA_MASTER01`
目的: 今後すべての画像・動画生成で同一人物(NANA)を維持するための固定リファレンス。実際の生成はHiggsfield + GPT Image側の作業(2026-07-11制作方針変更、`IMAGE_GENERATION_POLICY.md`準拠。Nano Banana不使用、Character MasterにSoul 2は使用しない)。本ファイルはその仕様書。

## 基本情報

SE77NTH.ボーカル。MIUの実妹、末っ子。感情表現豊かで人懐っこい。顎ラインの内巻き黒ボブ+重めのぱっつん前髪、ピーチピンクのインナーカラー、左目の下の泣きぼくろ(キャラクター同一性維持アンカー)、血色チーク。

## Character Lock Prompt(共通ベース記述、GPT Image用、全アングル・表情で必ず含める)

```
East Asian Japanese young woman (NANA), chin-length inward-curled black
bob with heavy blunt bangs, peach-pink inner hair color, a small mole
fixed under her left eye, rosy cheeks, expressive lively expression
base, consistent facial structure across all angles and expressions,
exact facial consistency maintained via this fixed reference
description (GPT Image, Soul 2 not used)
```

## アングル

### 真正面(Front)
```
CHAR_NANA_MASTER01_FRONT — NANA, front-facing portrait, direct eye
contact with camera, mole clearly visible under left eye, lively warm
expression, studio-neutral background, even lighting, 35mm portrait
lens look
```

### 左45°
```
CHAR_NANA_MASTER01_L45 — NANA, head turned 45 degrees to her left,
three-quarter view, mole under left eye remains visible, same lighting
and background as front reference
```

### 右45°
```
CHAR_NANA_MASTER01_R45 — NANA, head turned 45 degrees to her right,
three-quarter view, mole under left eye position consistent with front
reference, same lighting and background
```

### 横顔(Profile)
```
CHAR_NANA_MASTER01_PROFILE — NANA, full left profile, blunt bangs and
bob silhouette clearly visible, mole position consistent, same lighting
and background as front reference
```

### 全身(Full Body)
```
CHAR_NANA_MASTER01_FULLBODY — NANA, full body standing pose, energetic
casual stance, casual placeholder outfit(下記衣装に関する注意を参照),
studio-neutral background, consistent proportions with portrait
references
```

## 表情差分(6種)

1. **通常(ニュートラル)** — `soft neutral expression, rosy cheeks, relaxed mouth`
2. **明るい笑顔** — `wide bright smile, eyes crinkled with joy, most characteristic expression`
3. **控えめな微笑み** — `small warm smile, shy undertone`
4. **驚き** — `wide eyes, open mouth, exaggerated expressive surprise` (性格上、驚きの表現が大きめ)
5. **真剣な表情** — `focused curious expression, head slightly tilted`
6. **代表表情(人懐っこさ)** — `beaming high-energy smile, eyes crinkled, mole under left eye prominent, embodies her playful younger-sister energy`

## 一貫性アンカー(キャラクター崩れ防止の重要ポイント)

- **左目の下の泣きぼくろは全生成で位置固定**(NANAの同一性を保証する最重要アンカー、Character Bible既定)
- ピーチピンクのインナーカラーを必ず描写(姉妹・ユニットのアクセントカラーとして統一)
- 重めのぱっつん前髪を崩さない(MIU・AYAの前髪スタイルと明確に区別する)
- 血色チークを毎回描写(表情の生き生きした印象の核)

## 衣装に関する注意

Costume Bible未登録(既知の残課題)。正式デザイン決定までの**技術的な仮置き**として、以下の中立的な私服描写を全生成で共通使用する: `casual bright-toned top, simple skirt or shorts, no visible logos or brand marks`。これは創作上の衣装デザイン決定ではなく、生成の一貫性を保つための暫定処理。正式デザインが決定次第、Costume Bible登録の上で本ファイルを更新すること。

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §5「キャラクター & アーティスト」のNANA記述。物語構成(Legacy/CANON)の判断によらず有効
- Character Bible: Obsidian Vault `10_Characters/NANA.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
