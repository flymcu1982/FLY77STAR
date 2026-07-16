# CHAR_KAI_MASTER — Character Master Reference（WAKE UP）

Character Bible参照: KAI（Obsidian Vault `10_Characters/KAI.md`）
Asset ID: `CHAR_KAI_MASTER01`
目的: 今後すべての画像・動画生成で同一人物(KAI)を維持するための固定リファレンス。実際の生成はHiggsfield + GPT Image側の作業(2026-07-11制作方針変更、`IMAGE_GENERATION_POLICY.md`準拠。Nano Banana不使用、Character MasterにSoul 2は使用しない)。本ファイルはその仕様書。

## 基本情報

ゲストラッパー。WAKE UPでは「謎のコック」として登場(MA-1期の意匠を使用、US期は本作では不使用)。ネイビーブルーのショートヘア+ハイフェード、左耳シルバーフープ、オリーブMA-1+白T(店内ではエプロン着用)、シルバーの「7」ペンダント(SE77NTH.ブランドと接続する正史アイテム)。

## 生成時の必須注意(最重要)

**プロンプトに"East Asian Japanese"を必ず明示すること。** 明示しないと人種ドリフトが起きることがCharacter Bibleで既に警告済み。全アングル・全表情プロンプトに含める。

## Character Lock Prompt(共通ベース記述、GPT Image用、全アングル・表情で必ず含める)

```
East Asian Japanese young man (KAI), MA-1 era design, navy short hair
with a fade, silver hoop earring in left ear, olive MA-1 jacket over a
white T-shirt, silver "7" pendant necklace clearly visible, calm
enigmatic expression base, consistent facial structure across all
angles and expressions, exact facial consistency maintained via this
fixed reference description (GPT Image, Soul 2 not used)
```

## アングル

### 真正面(Front)
```
CHAR_KAI_MASTER01_FRONT — KAI, front-facing portrait, direct eye
contact with camera, silver "7" pendant clearly visible at chest level,
calm expression, studio-neutral background, even lighting, 35mm
portrait lens look
```

### 左45°
```
CHAR_KAI_MASTER01_L45 — KAI, head turned 45 degrees to his left,
three-quarter view, fade haircut and earring visible, same lighting and
background as front reference
```

### 右45°
```
CHAR_KAI_MASTER01_R45 — KAI, head turned 45 degrees to his right,
three-quarter view, same lighting and background as front reference
```

### 横顔(Profile)
```
CHAR_KAI_MASTER01_PROFILE — KAI, full left profile, fade haircut
silhouette and earring clearly visible, same lighting and background as
front reference
```

### 全身(Full Body)
```
CHAR_KAI_MASTER01_FULLBODY — KAI, full body standing pose, relaxed
confident stance, olive MA-1 jacket over white T-shirt, silver "7"
pendant visible, studio-neutral background, consistent proportions with
portrait references
```

### コック衣装バリエーション(WAKE UP専用、CUT06〜08で使用)
```
CHAR_KAI_MASTER01_COOK — KAI, MA-1 jacket layered with a plain white
apron over it, same face/hair/pendant as above, casual diner-cook
styling, no branded text on apron
```

## 表情差分(6種)

1. **通常(ニュートラル)** — `calm neutral expression, composed and still`
2. **明るい笑顔** — `rare warm smile, brief and genuine` (本作では基本使用しない、将来作品用に確保)
3. **穏やかな微笑み(コックとして)** — `calm gentle service-industry smile, ordinary and unremarkable` (CUT07で使用、意図的に「特別感を強調しない」表情。Director Notes `CUT07_Panel02_DirectorNotes.md`の抑制方針と一致)
4. **謎めいた表情** — `enigmatic composed expression, faint knowing smile, backlit ambiguity` (CUT01のシルエット等で輪郭のみ使用する場合の基準)
5. **溶解表情(VFX用)** — `calm smile maintained as silhouette edges dissolve into light particles` (CUT08専用、輪郭崩壊VFXのベース表情)
6. **代表表情(MA-1期の基準)** — `understated cool confidence, subtle half-smile, silver "7" pendant catching light`

## 一貫性アンカー(キャラクター崩れ防止の重要ポイント)

- **"East Asian Japanese"を全プロンプトで省略しない**(最重要、人種ドリフト防止)
- 銀の「7」ペンダントは小物のため生成時に消えやすい。全アングルで「clearly visible」等の強調指定を入れる(Image Asset List既知の課題と一致)
- MA-1期の意匠(ネイビーフェード、シルバーフープ、オリーブMA-1)をUS期(黒コーンロウ等)と混同しない。WAKE UPでは終始MA-1期のみを使用
- CUT07では「謎めいた」演出を表情・演技側で強調しすぎない(Director Notes参照)。ミステリアスさは光(逆光・シルエット)側の演出に委ね、表情自体は自然体に留める

## 衣装に関する注意

コック衣装(MA-1+エプロン)はWAKE UP用の仮設定、Costume Bible未登録(既知の残課題)。エプロンにはブランド/ロゴ表記を入れない(架空表記ポリシー、実在店舗との誤認防止)。正式デザインが決定次第、Costume Bible登録の上で本ファイルを更新すること。

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §5「キャラクター & アーティスト」のKAI記述。Character Referenceとして確定。ただしCANONではKAIはラッパー/ソロアーティストとして描写されており、「コックとしてのみ登場」という本ファイルの演出方針はLegacy構造(旧12カット)固有の設定である点に留意
- Character Bible: Obsidian Vault `10_Characters/KAI.md`
- Director Notes(コックとしてのみ登場の演出方針、Legacy構造): `Storyboard/CUT07_Panel02_DirectorNotes.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
