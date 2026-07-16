# CHAR_MIU_MASTER — Character Master Reference（WAKE UP）

Character Bible参照: MIU（Obsidian Vault `10_Characters/MIU.md`）
Asset ID: `CHAR_MIU_MASTER01`
目的: 今後すべての画像・動画生成で同一人物(MIU)を維持するための固定リファレンス。実際の生成はHiggsfield + GPT Image側の作業(2026-07-11制作方針変更、`IMAGE_GENERATION_POLICY.md`準拠。Nano Banana不使用、Character MasterにSoul 2は使用しない)。本ファイルはその仕様書。

## 基本情報

SE77NTH.リードボーカル/センター。面倒見のいい姉御肌。NANAの実姉。長い緩巻きライトブラウンヘア+白ヘアバンド、血色感のあるグロスリップ、ゴールド系アクセサリー。

## Golden Reference v1.0(2026-07-11、Panel04開発より)

本セッション外(社長⇄ChatGPT/GPT Image/Higgsfieldでのやり取り)でPanel04制作時に確定した、より詳細なアクセサリー仕様。従来の「ゴールド系アクセサリー」という汎用記述を以下で具体化する:

- **赤いハートネックレス**
- **ブレスレット**
- **フープピアス**

これらはPanel04の720pテイクで使用され、Director承認済み。Golden Production Image(Panel03)制作時点ではこの詳細仕様は未確定だったため、Panel03のCharacter Lock Promptは汎用的な「gold accessories」表記のまま。Panel04以降、本仕様(Golden Reference v1.0)を優先する。Panel03側を遡及更新するかは別途Director判断待ち。

## Character Lock Prompt(共通ベース記述、GPT Image用、全アングル・表情で必ず含める)

```
East Asian Japanese young woman (MIU), long light brown loose wavy hair
with a white hairband, warm-toned glossy lips, gold accessories, warm
and caring expression base, consistent facial structure across all
angles and expressions, exact facial consistency maintained via this
fixed reference description (GPT Image, Soul 2 not used)
```

## アングル

### 真正面(Front)
```
CHAR_MIU_MASTER01_FRONT — MIU, front-facing portrait, direct eye
contact with camera, neutral warm expression, studio-neutral
background for reference sheet use, even lighting, 35mm portrait lens
look
```

### 左45°
```
CHAR_MIU_MASTER01_L45 — MIU, head turned 45 degrees to her left,
three-quarter view, same lighting and background as front reference
```

### 右45°
```
CHAR_MIU_MASTER01_R45 — MIU, head turned 45 degrees to her right,
three-quarter view, same lighting and background as front reference
```

### 横顔(Profile)
```
CHAR_MIU_MASTER01_PROFILE — MIU, full left profile, hairband and hair
wave silhouette clearly visible, same lighting and background as front
reference
```

### 全身(Full Body)
```
CHAR_MIU_MASTER01_FULLBODY — MIU, full body standing pose, relaxed
natural stance, hands loosely at sides, casual placeholder outfit(下記
衣装に関する注意を参照), studio-neutral background, consistent
proportions with portrait references
```

## 表情差分(6種)

1. **通常(ニュートラル)** — `calm neutral expression, soft warm eyes, relaxed mouth`
2. **明るい笑顔** — `bright open smile, warm caring energy, eyes slightly crinkled`
3. **控えめな微笑み** — `small gentle smile, mouth closed, soft eyes` (CUT02合流シーン等で使用)
4. **驚き** — `slightly widened eyes, lips parted, subtle surprise` (CUT08「え……？」で使用)
5. **真剣な表情** — `focused searching expression, eyes slightly narrowed, contemplative` (CUT10・CUT11の既視感シーンで使用)
6. **代表表情(面倒見の良さ)** — `warm reassuring smile, slightly tilted head, older-sister warmth` (グループ内での立ち位置を象徴する表情)

## 一貫性アンカー(キャラクター崩れ防止の重要ポイント)

- 白ヘアバンドは全カットで欠かさず描写する(識別性の核)
- 髪の緩巻きウェーブの質感・長さを毎回統一(直毛化・極端な巻き髪化を避ける)
- リップは血色感のあるグロス系で統一、色調を変えない
- ゴールド系アクセサリーのみ使用(シルバー等他キャラクターの色と混同しない)

## 衣装に関する注意

Costume Bible未登録(既知の残課題)。正式デザイン決定までの**技術的な仮置き**として、以下の中立的な私服描写を全生成で共通使用する: `casual dark top, simple jeans or skirt, no visible logos or brand marks`。これは創作上の衣装デザイン決定ではなく、生成の一貫性を保つための暫定処理。正式デザインが決定次第、Costume Bible登録の上で本ファイルを更新すること。

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §5「キャラクター & アーティスト」のMIU記述。物語構成(Legacy/CANON)の判断によらず有効
- Character Bible: Obsidian Vault `10_Characters/MIU.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
