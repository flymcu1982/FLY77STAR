# WAKE UP — CANON Scene 1（オープニング）制作パッケージ

**構成基準**: FLY77STAR CANON（`/CANON_FLY77STAR_20260716_final.md` §6）ACT01 SHIBUYA_NIGHT — Panel 1（ドローン→青い時刻4:30AM）＋ Panel 2（クラブ出口、SE77NTH.三人）
**制作日**: 2026-07-21
**ワークフロー**: Studio OS 標準制作ワークフロー Version 1（`AI_WORKFLOW_V1.md`、CINE→SOUL→CUT→MASTER 4段階リレー）
**Legacy との関係**: 旧12カット構成の `CUT01.md`（渋谷スクランブル交差点、MIU単独）とは**別内容**。Legacy ファイルは変更していない（`00_LEGACY_STRUCTURE_NOTICE.md` 参照）。

---

## 生成前チェック（Step 0）

- **Character Bible**: AYA / MIU / NANA — `Reference/CHAR_AYA_MASTER.md` / `CHAR_MIU_MASTER.md` / `CHAR_NANA_MASTER.md`（採用済み素材、CANON でも有効）を確認
- **Costume Bible**: 3人ともクラブナイト衣装は**未登録**。生成一貫性維持のみを目的とした中立的な仮描写（ノーロゴ・ダークトーン）で進行。正式デザインは Director 判断待ち
- **Universe Rule**: 「キャラクターは時間を生きる」— 4:30AM＝オール明けの時間帯として、遊び疲れと高揚の残り香を演技に反映。矛盾なし
- **Production Bible**: 実在ブランド・ロゴ不使用。クラブは FLY77STAR オリジナルの架空店舗（看板は判読不能なネオン形状で処理し、店名の正式決定は Director へ委ねる）
- **矛盾（既知）2点**:
  1. クラブ外観の Location Master が未登録（既存は CROSSING / STREET / DINER_EXT / DINER_INT / SIDEWALK の5点のみ）。本ファイル内に `LOC_CLUB_EXT01`（仮）の基準記述を置く。正式な Location Master 昇格は Director 承認後
  2. 衣装未登録（上記）

## リレー実行ログ（Step 1〜4）

```
🎬 CINE — 演出・カメラ・照明・演技方針
夜明け前4:30AMの「青い時刻」の渋谷を、上空→街→クラブ入口→3人登場まで
ワンカット風に降下・前進する映画的オープニング。照明はブルーアワーの青と
クラブのネオン暖色の対比で設計。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
オール明けの解放感と心地よい疲労。「夜が終わるのに、まだ終わらせたくない」。
セリフなし（MIUの「始発まであそこで待とう！」は Scene 2 冒頭へ温存）。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
4パネル(各1×8カウント=5.02秒、計約20秒)のワンカット風構成。生成用に
4セグメントへ分割し、つなぎ目のフレームマッチ設計まで含めて Prompt 化。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
3人の Character Lock Prompt は Master と一致。衣装・クラブ外観は未登録のため
仮描写と明記。実在ブランド排除を Prompt レベルで担保(no logos 指定)。CANON
§6 Panel 1-2 と整合、Scene 2(Panel 3)への視線バトンも設計済み。
状態: 完了
```

---

## 1. ショット構成

**形式**: ワンカット風オープニング（実生成は4セグメント分割→編集で接続）
**総尺**: 約20秒（BPM 95.7 / 1×8カウント＝5.02秒 × 4）
**時間帯**: 4:30AM 青い時刻（ブルーアワー直前、空は深い藍、街灯とネオンはまだ点灯）

| Panel | タイム | 8ct | ショット | カメラ | 内容 |
|---|---|---|---|---|---|
| 1 | 0:00–0:05 | 1×8 | 超ロング（空撮） | ドローン俯瞰、緩やかな前進降下 | 渋谷の夜景全景。藍色の空、まばらな車のライト。街はまだ眠っている |
| 2 | 0:05–0:10 | 2×8 | ロング→ミディアムロング | ビル間を縫って降下・前進 | 高度が下がり路地へ。ネオンの残光、濡れた路面の反射。人気の少ない裏通り |
| 3 | 0:10–0:15 | 3×8 | ミディアム | 地上高さで前進ドリー | クラブ入口へ接近。判読不能なネオンサイン、ドアの隙間から漏れる暖色光と低音の気配 |
| 4 | 0:15–0:20 | 4×8 | ミディアム→3ショット | 前進停止→わずかに引き | ドアが開き、AYA・MIU・NANA が笑いながら出てくる。3人が横並びになったところでカットが「息をつく」 |

**Scene 2 への接続**: Panel 4 の最終拍で MIU だけが画面外（ダイナー方向）へ視線を送る。この視線が Scene 2 Panel 3「始発まであそこで待とう！」の第一声を受ける視線バトンとなる。

## 2. 演出意図

- **円環構造の起点**: CANON の WAKE UP は「現実の渋谷→ダイナー→現実へ帰還」の円環。オープニングの空撮は、エピローグ（SHIBUYA_RETURN）で再び引きの画に戻るための「原点の画」として設計する
- **青い時刻の意味**: 4:30AM は「夜と朝のどちらでもない時間」。現実とパラレルワールドの境界が緩む本作のテーマを、色彩（藍×ネオン暖色）で最初に予告する
- **降下＝観客の招待**: 神の視点（空撮）から3人の目線の高さまで一息に降りることで、観客を「彼女たちの夜の続き」へ引き込む。映画のオープニングロールに相当する没入導線
- **3人の登場を「事件にしない」**: ドアが開いて出てくるだけ。ポーズも決めない。オール明けの自然な笑いと疲れの中に SE77NTH. の関係性（姉御肌の MIU、クールな AYA、無邪気な NANA）が滲むことを最優先する
- **音との同期**: 各パネル頭を 8 カウント頭に一致させる。Panel 4 のドア開放はイントロの最初のアクセント（またはビート強拍）に合わせる想定

## 3. Storyboard

Panel Storyboard（映画レベル絵コンテ、簡易フレーム図付き）は別ファイル:
**`WAKE_UP_CANON_SCENE01_OPENING_絵コンテ.md`**

重要 Panel（主人公初登場: Panel 4）の Director Notes:
**`WAKE_UP_CANON_SCENE01_PANEL04_クラブ出口3人_DirectorNotes.md`**

## 4. Higgsfield 向け画像生成プロンプト

各セグメントの起点フレーム（image-to-video 用スタート画像）。エンジンは Higgsfield + GPT Image（`IMAGE_GENERATION_POLICY.md` 準拠、Soul 2 不使用、生成実行は Director/GPT Image 運用側）。

### Panel 1 起点 — 空撮

```
Aerial drone view high above a vast Japanese metropolis inspired by
Shibuya at 4:30AM blue hour, deep indigo pre-dawn sky, dense cityscape
with scattered neon signs still glowing, sparse car headlights tracing
empty streets, no readable text or real brand logos on any signage,
cinematic anamorphic look, cool blue color grade with warm neon
accents, 35mm film grain, moody and quiet atmosphere
```

### Panel 2 起点 — ビル間降下

```
Low aerial shot descending between buildings into a narrow back street
of a fictional Shibuya-like district at 4:30AM, wet asphalt reflecting
pink and cyan neon remnants, shuttered shops, steam from a vent, empty
street with one distant taxi, all signage abstract and unreadable, no
real brand logos, deep blue pre-dawn light mixing with artificial neon,
cinematic wide angle, film grain
```

### Panel 3 起点 — クラブ入口（LOC_CLUB_EXT01 仮基準）

```
Street-level dolly view approaching the entrance of a fictional
underground club "LOC_CLUB_EXT01", heavy black double door slightly
ajar, warm amber light and faint haze spilling out, abstract glowing
neon sign shapes above the door (unreadable, no letters, no logos),
stickers and posters rendered as indistinct color patches, blue
pre-dawn street contrasting with warm doorway glow, cinematic, shallow
depth cue toward the door, film grain
```

### Panel 4 起点 — 3人がドアから出てくる（3ショット）

```
Three East Asian Japanese young women stepping out of a club doorway
together at 4:30AM, warm doorway light behind them, blue pre-dawn
street light in front:
(AYA) center-parted straight dark brown hair, nude-toned lips, silver
accessories, cool composed expression softened by a small tired smile;
(MIU) long light brown loose wavy hair with a white hairband,
warm-toned glossy lips, gold accessories including a red heart necklace,
hoop earrings, warm caring smile mid-laugh;
(NANA) chin-length inward-curled black bob with heavy blunt bangs,
peach-pink inner hair color, a small mole fixed under her left eye,
rosy cheeks, bright open laugh;
club-night casual outfits in dark tones, no visible logos or brand
marks, natural relaxed after-party posture, not posing, three-shot
medium framing, exact facial consistency per fixed reference
descriptions, cinematic, film grain
```

## 5. Higgsfield 向け動画生成プロンプト

各セグメント 5〜6 秒、シンプルな単一カメラ動作に限定（AI 生成の破綻回避）。つなぎはフレームマッチ＋編集（Palmier）で処理。

### Segment 1（Panel 1、5秒）

```
Slow forward-descending drone move over a night metropolis at blue
hour, constant gentle speed, no camera shake, city lights flickering
subtly, clouds drifting very slowly, 5 seconds, cinematic
```

### Segment 2（Panel 2、5秒）

```
Continuous forward descent from rooftop height down between buildings
into an empty neon-lit back street, single smooth path, no obstacles
crossing frame, wet road reflections shimmering, 5 seconds, cinematic
```

### Segment 3（Panel 3、5秒）

```
Steady ground-level forward dolly toward a club entrance door, warm
light and thin haze drifting from the slightly open door, neon shapes
glowing softly, extremely stable motion, 5 seconds, cinematic
```

### Segment 4（Panel 4、5〜6秒）

```
Static-to-slight-pullback shot: club double door opens outward, three
young women step out together laughing naturally, subtle handheld
feel, warm backlight from doorway, blue street light on faces, they
stop in a loose line, one of them (MIU) glances off-screen right at
the end, 5-6 seconds, cinematic
```

### つなぎ目設計（編集指示、Palmier 向け）

- Seg1→2: 降下速度をマッチさせ、ビル影が画面を横切る瞬間にディゾルブ 4〜6 フレーム（速度ランプで隠す）
- Seg2→3: 路面が画面下 1/3 を占める構図同士で接続。前進ベクトル一致が最優先
- Seg3→4: ドアが画面中央に来たフレームで接続し、Seg4 頭の「ドアが開く」動作をビート強拍に同期
- 全体に薄いフィルムグレインとブルーグレードを統一適用し、セグメント間の質感差を均す

## 6. 制作時の注意点（AI 生成で破綻しやすいポイントと改善案）

1. **ワンカット全体を1回で生成しない**。長尺・複雑カメラパスは形状崩壊の最大要因。上記の通り4分割し、各セグメントは「単一方向の等速移動」に限定する
2. **空撮の都市ディテール**: 実在の渋谷ランドマーク（スクランブル交差点の実在ビル群等）が出やすい。"inspired by / fictional district" を必ず残し、生成結果に実在ロゴ・判読可能な看板が出たら QC で弾く（`Prompt/IMAGE_QC_CHECKLIST.md`）
3. **3人同時登場は最難関**: 複数人物は顔の入れ替わり・混同が頻発する。対策:
   - Panel 4 は「3ショット静止画（起点フレーム）を GPT Image で確定 → Higgsfield で動かす」の順を厳守
   - 起点フレーム QC で NANA の泣きぼくろ（左目下）・MIU のヘアバンド・AYA のセンターパートを個別確認してから動画へ進む
   - 3人の顔が小さくなりすぎるフレーミング（ロング）を避け、ミディアムを維持
4. **ドアが開く動作**: 「開く方向の反転」「ドアの増殖」が起きやすい。プロンプトで "opens outward" と方向を固定し、破綻時はドア開放を Seg3 末尾に移してSeg4 を「既に開いたドアから出てくる」に単純化する（改善案 B）
5. **手の描写**: 笑いながら出てくる動作で手が絡む（肩を組む等）と破綻リスク増。手つなぎ・肩組みは指示しない。自然に歩くだけにする
6. **青い時刻の色再現**: "blue hour" だけだと昼夜が揺れる。"4:30AM / pre-dawn / deep indigo sky" を全プロンプトで併記し、グレードは編集で最終統一する
7. **衣装の一貫性**: Costume Bible 未登録のため、セグメント間で服装が変わるリスクがある。Panel 4 起点フレーム確定後、その衣装描写を文章化して動画プロンプトへ逆輸入すること（Take 管理は `テイク修正上限ルール.md`＝同一テイク修正上限2回に従う）
8. **音との同期は生成ではなく編集で取る**: 生成尺は 5〜6 秒で余裕を持たせ、8カウント（5.02秒）への正確な合わせ込みは Palmier のタイムライン側で行う

## 4者レビュー（Step 5）

```
🎬 CINE「空撮からドアまでの降下は"観客を夜に招き入れる"導線として機能する。Seg3→4の強拍同期だけは編集で妥協しないでほしい。」
🎭 SOUL「3人の笑いは"演技"ではなく"続き"。ドアの内側で起きていた楽しさが漏れ出す感じを起点フレームの表情で担保したい。」
📷 CUT「4分割それぞれは生成難度低〜中。唯一の山は Panel 4 の3人同時。起点フレームQC→動画の順序を崩さなければ通せる。」
🛡 MASTER「CANON §6 Panel 1-2 と整合。クラブ Location Master 未登録と衣装未登録の2点は Director 判断待ちとして明示済み。Legacy ファイルへの影響なし。」
```

## 未決事項（Director への確認依頼）

1. クラブの店名・外観デザイン（`LOC_CLUB_EXT01` の正式 Location Master 昇格）
2. 3人のクラブナイト衣装の正式デザイン（Costume Bible 登録）
3. 総尺 20 秒（4×8）で確定してよいか（曲のイントロ実尺との照合）
