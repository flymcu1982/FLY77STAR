# WAKE UP — Image Asset List / Asset ID / 撮影優先順位

Production Phase 1。Panel Storyboard(`Storyboard/CUT<番号>_絵コンテ.md`)・Director Notes・生成プロンプト本体(`Storyboard/CUT<番号>.md`)を元に、各CUT・各Panelの必要画像(キャラクター/背景/小物)を一覧化し、Asset IDを付与する。Studio OSの改修は行わず、既存のPanel Storyboard/Director Notesの内容は変更しない。

## Asset IDの命名規則

```
CUT<番号2桁>_P<パネル番号2桁>_<種別><連番2桁>
```

- `IMG`: そのPanelの最終合成カット(画像生成の主成果物。この画像を元に動画Promptを実行する)
- `BG`: 背景/環境プレート。同一ロケーション・同一アングルの場合は既存PanelのBGを流用し、新規IDは発行しない(備考欄に流用元を明記)
- `<キャラクター名>`(MIU/AYA/NANA/KAI/HINA): そのPanelでキャラクターの表情・ポーズを個別に指定する必要がある場合の人物アセット
- `PROP`: 画面上で識別性が必要な小物(スマホ、看板、ペンダント、皿など)

## 前提: Character Master Reference

全Panelの生成に先立ち、以下5キャラクターの固定リファレンスが必要。**仕様策定完了(2026-07-11、Production Phase 2)**。真正面/左右45°/横顔/全身/表情差分6種を各ファイルに整理済み。実際の画像生成(Higgsfield + GPT Image。2026-07-11制作方針変更によりNano Banana不使用、Character MasterにSoul 2不使用。詳細: `IMAGE_GENERATION_POLICY.md`)は次工程。

| キャラクター | Asset ID | 内容 | 仕様書 |
|---|---|---|---|
| MIU | `CHAR_MIU_MASTER01` | ロング緩巻きライトブラウン+白ヘアバンド | `Reference/CHAR_MIU_MASTER.md` |
| AYA | `CHAR_AYA_MASTER01` | センターパートストレートダークブラウン | `Reference/CHAR_AYA_MASTER.md` |
| NANA | `CHAR_NANA_MASTER01` | 顎ラインの内巻き黒ボブ+ピーチピンクインナー、左目下ほくろ固定 | `Reference/CHAR_NANA_MASTER.md` |
| KAI | `CHAR_KAI_MASTER01` | MA-1期意匠(銀の「7」ペンダント含む) | `Reference/CHAR_KAI_MASTER.md`("East Asian Japanese"明記必須) |
| HINA | `CHAR_HINA_MASTER01` | NANAより短い黒ボブ、インナーカラーなし | `Reference/CHAR_HINA_MASTER.md` |

私服/衣装は全キャラクターCostume Bible未登録のため、各仕様書内で中立的な仮描写を採用(創作上の決定ではない、生成一貫性のための技術的仮置き)。

## 前提: Location Master

**仕様策定完了(2026-07-11、Production Phase 2)**。

| ロケーション | Asset ID | 使用CUT | 仕様書 |
|---|---|---|---|
| 渋谷スクランブル交差点(夜) | `LOC_CROSSING01` | CUT01〜03 | `Reference/LOC_CROSSING_MASTER.md` |
| 渋谷大通り〜路地(夜) | `LOC_STREET01` | CUT04 | `Reference/LOC_STREET_MASTER.md` |
| POP DINER外観(架空店舗) | `LOC_DINER_EXT01` | CUT05 | `Reference/LOC_DINER_EXT_MASTER.md` |
| POP DINER内装(架空店舗) | `LOC_DINER_INT01` | CUT06〜08 | `Reference/LOC_DINER_INT_MASTER.md`(CUT08崩壊VFXバリエーション含む) |
| 渋谷帰り道の雑踏(夜) | `LOC_SIDEWALK01` | CUT09〜12 | `Reference/LOC_SIDEWALK_MASTER.md`(CUT09空き区画〜CUT12夜景まで) |

---

## CUT01 — 渋谷

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT01_P01_BG01` | 背景 | 渋谷スクランブル交差点、俯瞰、夜 | `LOC_CROSSING01`バリエーション |
| P01 | `CUT01_P01_IMG01` | 画像 | 俯瞰交差点、被写体なし | |
| P02 | `CUT01_P02_BG01` | 背景 | 同上、降下アングル | P01のBGを高度違いで再生成 |
| P02 | `CUT01_P02_IMG01` | 画像 | 降下クレーン、被写体なし | |
| P03 | `CUT01_P03_BG01` | 背景 | 交差点、群衆、路上レベル | 以降P04・P05で流用 |
| P03 | `CUT01_P03_MIU01` | キャラクター | MIU、静止ポーズ | `CHAR_MIU_MASTER01`使用、重要Panel(主人公初登場) |
| P03 | `CUT01_P03_IMG01` | 画像 | 交差点の中でMIUのみ静止 | |
| P04 | `CUT01_P04_MIU01` | キャラクター | MIU、スマホを見る仕草 | |
| P04 | `CUT01_P04_PROP01` | 小物 | スマートフォン | |
| P04 | `CUT01_P04_IMG01` | 画像 | MIU、スマホ確認 | BG: `CUT01_P03_BG01`流用 |
| P05 | `CUT01_P05_MIU01` | キャラクター | MIU、顔を上げる仕草 | |
| P05 | `CUT01_P05_IMG01` | 画像 | MIU、視線が画面外へ | BG: `CUT01_P03_BG01`流用 |

## CUT02 — AYA到着

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT02_P01_BG01` | 背景 | 交差点付近、群衆 | |
| P01 | `CUT02_P01_AYA01` | キャラクター | AYA、駆け寄る仕草 | `CHAR_AYA_MASTER01`使用、重要Panel(主人公初登場) |
| P01 | `CUT02_P01_IMG01` | 画像 | AYA、人混みから接近 | |
| P02 | `CUT02_P02_MIU01` | キャラクター | MIU、振り返る仕草 | |
| P02 | `CUT02_P02_IMG01` | 画像 | MIU反応ショット | BG: `CUT01_P03_BG01`流用 |
| P03 | `CUT02_P03_MIU01` `CUT02_P03_AYA01` | キャラクター | MIU(待つ)、AYA(手を上げる) | |
| P03 | `CUT02_P03_IMG01` | 画像 | 二人の距離が詰まる | BG: `CUT01_P03_BG01`流用 |
| P04 | `CUT02_P04_MIU01` `CUT02_P04_AYA01` | キャラクター | 向き合って笑う二人 | |
| P04 | `CUT02_P04_IMG01` | 画像 | 合流、セリフ「待った？」 | BG: `CUT01_P03_BG01`流用 |

## CUT03 — 3人集合

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT03_P01_BG01` | 背景 | 交差点付近、群衆 | |
| P01 | `CUT03_P01_NANA01` | キャラクター | NANA、駆け込む仕草 | `CHAR_NANA_MASTER01`使用、重要Panel(主人公初登場) |
| P01 | `CUT03_P01_IMG01` | 画像 | NANA登場、セリフ「お待たせー！」 | |
| P02 | `CUT03_P02_MIU01` `CUT03_P02_AYA01` `CUT03_P02_NANA01` | キャラクター | 3人の手元(ハイタッチ) | |
| P02 | `CUT03_P02_IMG01` | 画像 | ハイタッチ | BG: `CUT03_P01_BG01`流用 |
| P03 | `CUT03_P03_MIU01` `CUT03_P03_AYA01` `CUT03_P03_NANA01` | キャラクター | 3人それぞれの笑顔(切り返し用) | ほくろ位置(NANA)等キャラクター一貫性に注意 |
| P03 | `CUT03_P03_IMG01`〜`IMG03` | 画像 | 3人分の顔クローズアップ(3カット) | |
| P04 | `CUT03_P04_MIU01` `CUT03_P04_AYA01` `CUT03_P04_NANA01` | キャラクター | 横並び静止 | 重要Panel(象徴カット) |
| P04 | `CUT03_P04_IMG01` | 画像 | 3ショットへ引く | BG: `CUT03_P01_BG01`流用 |

## CUT04 — 歩き出す

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT04_P01_BG01` | 背景 | 渋谷大通り〜路地への通り | `LOC_STREET01`、重要Panel(感情変化) |
| P01 | `CUT04_P01_MIU01` `CUT04_P01_AYA01` `CUT04_P01_NANA01` | キャラクター | 3人並んで歩く(背中) | |
| P01 | `CUT04_P01_IMG01` | 画像 | 背後トラッキング | |
| P02 | `CUT04_P02_MIU01` `CUT04_P02_AYA01` `CUT04_P02_NANA01` | キャラクター | じゃれ合いながら歩く | |
| P02 | `CUT04_P02_IMG01` | 画像 | 横からの並走 | BG: `CUT04_P01_BG01`流用 |
| P03 | `CUT04_P03_NANA01` | キャラクター | NANA、路地を指差す | |
| P03 | `CUT04_P03_IMG01` | 画像 | NANAのセリフ「こっち行ってみない？」 | BG: `CUT04_P01_BG01`流用 |
| P04 | `CUT04_P04_BG01` | 背景 | 路地入口、光量変化 | |
| P04 | `CUT04_P04_MIU01` `CUT04_P04_AYA01` `CUT04_P04_NANA01` | キャラクター | 路地へ折れる3人 | |
| P04 | `CUT04_P04_IMG01` | 画像 | 路地へ折れる | |

## CUT05 — ダイナー発見

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT05_P01_BG01` | 背景 | 暗い路地、奥に暖色の光 | 重要Panel(伏線)、被写体なし |
| P01 | `CUT05_P01_IMG01` | 画像 | 路地奥の光(発見) | |
| P02 | `CUT05_P02_MIU01` `CUT05_P02_AYA01` `CUT05_P02_NANA01` | キャラクター | 足を止め見つめる3人 | |
| P02 | `CUT05_P02_IMG01` | 画像 | 3人の反応 | BG: `CUT05_P01_BG01`流用 |
| P03 | `CUT05_P03_MIU01` `CUT05_P03_AYA01` `CUT05_P03_NANA01` | キャラクター | 歩み寄る3人 | AYAのセリフ「こんな店、あったっけ？」 |
| P03 | `CUT05_P03_IMG01` | 画像 | 歩み寄り | BG: `CUT05_P01_BG01`流用 |
| P04 | `CUT05_P04_BG01` | 背景 | POP DINER外観、看板 | `LOC_DINER_EXT01` |
| P04 | `CUT05_P04_PROP01` | 小物 | POP DINER看板(架空店名) | 文字崩れ注意 |
| P04 | `CUT05_P04_IMG01` | 画像 | ダイナー外観ドリーイン | |

## CUT06 — 店内

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT06_P01_BG01` | 背景 | ドア枠、店内の光 | `LOC_DINER_INT01`、重要Panel(世界観説明) |
| P01 | `CUT06_P01_PROP01` | 小物 | ダイナーの扉 | |
| P01 | `CUT06_P01_IMG01` | 画像 | 扉を開ける(POV寄り) | |
| P02 | `CUT06_P02_BG01` | 背景 | ダイナー店内、カウンター・ブース | 以降P03〜P05で流用 |
| P02 | `CUT06_P02_IMG01` | 画像 | 店内パン、空間提示 | |
| P03 | `CUT06_P03_MIU01` `CUT06_P03_AYA01` `CUT06_P03_NANA01` | キャラクター | 驚いて見渡す3人 | |
| P03 | `CUT06_P03_IMG01` | 画像 | 見渡す3人 | BG: `CUT06_P02_BG01`流用 |
| P04 | `CUT06_P04_MIU01` `CUT06_P04_AYA01` `CUT06_P04_NANA01` | キャラクター | ブースへ移動 | |
| P04 | `CUT06_P04_IMG01` | 画像 | ブースへ | BG: `CUT06_P02_BG01`流用 |
| P05 | `CUT06_P05_MIU01` `CUT06_P05_AYA01` `CUT06_P05_NANA01` | キャラクター | 着席、NANA「なんか、落ち着く」 | |
| P05 | `CUT06_P05_IMG01` | 画像 | 着席 | BG: `CUT06_P02_BG01`流用 |

## CUT07 — KAI登場

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT07_P01_BG01` | 背景 | 厨房、逆光 | |
| P01 | `CUT07_P01_KAI01` | キャラクター | KAI、シルエットのみ | |
| P01 | `CUT07_P01_IMG01` | 画像 | 厨房奥のシルエット登場 | |
| P02 | `CUT07_P02_KAI01` | キャラクター | KAI、正面(MA-1期+エプロン)、コックとしてのみ登場 | `CHAR_KAI_MASTER01`使用、重要Panel(主人公初登場)。演技は抑制方針(Director Notes参照) |
| P02 | `CUT07_P02_PROP01` | 小物 | 銀の「7」ペンダント | 小物のため生成時に消えやすい、強調指定が必要(既知の課題) |
| P02 | `CUT07_P02_IMG01` | 画像 | 正面が見える | BG: `CUT06_P02_BG01`流用 |
| P03 | `CUT07_P03_MIU01` `CUT07_P03_AYA01` `CUT07_P03_NANA01` | キャラクター | 見惚れる3人 | |
| P03 | `CUT07_P03_IMG01` | 画像 | 3人の反応 | BG: `CUT06_P02_BG01`流用 |
| P04 | `CUT07_P04_KAI01` | キャラクター | KAI、皿を置く手元動作 | |
| P04 | `CUT07_P04_PROP02` | 小物 | 皿・料理 | |
| P04 | `CUT07_P04_IMG01` | 画像 | 皿を置く | BG: `CUT06_P02_BG01`流用 |
| P05 | `CUT07_P05_KAI01` | キャラクター | KAI、穏やかな微笑み、セリフ「お待たせ」 | |
| P05 | `CUT07_P05_IMG01` | 画像 | KAIのセリフ | BG: `CUT06_P02_BG01`流用 |

## CUT08 — パラレル終了

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT08_P01_BG01` | 背景 | 店内、不規則な明滅 | `CUT06_P02_BG01`のVFXバリエーション |
| P01 | `CUT08_P01_IMG01` | 画像 | 明滅の始まり | |
| P02 | `CUT08_P02_KAI01` | キャラクター | KAI、輪郭が光に溶けるVFX | 生成モデルによって品質差が出やすい(既知の課題) |
| P02 | `CUT08_P02_IMG01` | 画像 | KAIの輪郭が滲む | |
| P03 | `CUT08_P03_MIU01` | キャラクター | MIU、手を伸ばす仕草、セリフ「え……？」 | |
| P03 | `CUT08_P03_IMG01` | 画像 | MIUの反応 | |
| P04 | `CUT08_P04_IMG01` | 画像 | ホワイトアウト、被写体なし | 重要Panel(象徴カット) |

## CUT09 — 現実

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT09_P01_BG01` | 背景 | 白飽和→路地の輪郭(切り返しVFX) | 重要Panel(象徴カット=タイトルの体現) |
| P01 | `CUT09_P01_IMG01` | 画像 | 切り返し | |
| P02 | `CUT09_P02_BG01` | 背景 | 路地裏、シャッター、空き区画 | `LOC_SIDEWALK01`バリエーション |
| P02 | `CUT09_P02_PROP01` | 小物 | 古びたシャッター | 架空表記を保ちつつ実在感が必要(既知の課題) |
| P02 | `CUT09_P02_IMG01` | 画像 | 空き区画 | |
| P03 | `CUT09_P03_MIU01` `CUT09_P03_AYA01` `CUT09_P03_NANA01` | キャラクター | 顔を見合わせる3人 | |
| P03 | `CUT09_P03_IMG01` | 画像 | 戸惑いの反応 | BG: `CUT09_P02_BG01`流用 |
| P04 | `CUT09_P04_AYA01` | キャラクター | AYA、戸惑いの表情、セリフ「今の、何だったんだろう」 | |
| P04 | `CUT09_P04_IMG01` | 画像 | AYAのセリフ | BG: `CUT09_P02_BG01`流用 |

## CUT10 — KAIとすれ違う

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT10_P01_BG01` | 背景 | 帰り道の雑踏 | `LOC_SIDEWALK01` |
| P01 | `CUT10_P01_MIU01` `CUT10_P01_AYA01` `CUT10_P01_NANA01` | キャラクター | 会話しながら歩く3人 | |
| P01 | `CUT10_P01_IMG01` | 画像 | 歩く3人 | |
| P02 | `CUT10_P02_KAI01` | キャラクター | KAIに似た逆光シルエット、遠景 | 顔は見せない、重要Panel(伏線) |
| P02 | `CUT10_P02_IMG01` | 画像 | 遠くのシルエット | BG: `CUT10_P01_BG01`流用 |
| P03 | `CUT10_P03_MIU01` | キャラクター | MIU、振り返る仕草 | |
| P03 | `CUT10_P03_IMG01` | 画像 | MIUの反応 | BG: `CUT10_P01_BG01`流用 |
| P04 | `CUT10_P04_IMG01` | 画像 | 消えたシルエット、探すMIUの視線 | BG: `CUT10_P01_BG01`流用 |

## CUT11 — HINA登場

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT11_P01_BG01` | 背景 | 帰り道の歩道 | `LOC_SIDEWALK01`バリエーション |
| P01 | `CUT11_P01_HINA01` | キャラクター | HINA、白い服、全身 | `CHAR_HINA_MASTER01`使用、重要Panel(主人公初登場) |
| P01 | `CUT11_P01_MIU01` `CUT11_P01_AYA01` `CUT11_P01_NANA01` | キャラクター | すれ違う3人 | |
| P01 | `CUT11_P01_IMG01` | 画像 | すれ違う瞬間 | |
| P02 | `CUT11_P02_MIU01` | キャラクター | MIU、足を止め振り返る | |
| P02 | `CUT11_P02_IMG01` | 画像 | MIUだけ振り返る | BG: `CUT11_P01_BG01`流用 |
| P03 | `CUT11_P03_MIU01` | キャラクター | MIU、探すような表情、セリフ「どこかで、会った気がする」 | |
| P03 | `CUT11_P03_IMG01` | 画像 | MIUのセリフ | BG: `CUT11_P01_BG01`流用 |
| P04 | `CUT11_P04_HINA01` | キャラクター | HINA、後ろ姿 | |
| P04 | `CUT11_P04_IMG01` | 画像 | HINAの後ろ姿、雑踏に消える | BG: `CUT11_P01_BG01`流用 |

## CUT12 — エンディング

| Panel | Asset ID | 種別 | 内容 | 備考 |
|---|---|---|---|---|
| P01 | `CUT12_P01_BG01` | 背景 | 帰り道 | `LOC_SIDEWALK01`バリエーション |
| P01 | `CUT12_P01_MIU01` `CUT12_P01_AYA01` `CUT12_P01_NANA01` | キャラクター | 後ろ姿で歩き続ける3人 | |
| P01 | `CUT12_P01_IMG01` | 画像 | 後ろ姿 | |
| P02 | `CUT12_P02_MIU01` | キャラクター | MIU、一度だけ振り返る | |
| P02 | `CUT12_P02_IMG01` | 画像 | MIUの振り返り | BG: `CUT12_P01_BG01`流用 |
| P03 | `CUT12_P03_MIU01` `CUT12_P03_AYA01` `CUT12_P03_NANA01` | キャラクター | 前を向き歩調を合わせる | |
| P03 | `CUT12_P03_IMG01` | 画像 | 前を向く | BG: `CUT12_P01_BG01`流用 |
| P04 | `CUT12_P04_BG01` | 背景 | 渋谷夜景全体、俯瞰 | 重要Panel(ラストカット) |
| P04 | `CUT12_P04_IMG01` | 画像 | クレーンアップ、夜景へ | テロップ挿入スペース確保(既知の課題) |

---

## 撮影優先順位

### 画像生成順

1. **(最優先/ブロッカー) Character Master Reference確立** — MIU・AYA・NANA・KAI(MA-1期)・HINAの固定リファレンス5点(Higgsfield + GPT Image、`IMAGE_GENERATION_POLICY.md`準拠)。ここが未着手のため、パネル単位の生成は本質的にまだ開始できない
2. **Location Master確立** — 渋谷スクランブル交差点・POP DINER外観/内装・帰り道の雑踏。複数CUTで再利用するため先行生成が効率的
3. **重要Panel(Director Notes該当、全12件)を優先生成** — CUT01 P03 / CUT02 P01 / CUT03 P01・P04 / CUT04 P01 / CUT05 P01 / CUT06 P01 / CUT07 P02 / CUT08 P04 / CUT09 P01 / CUT10 P02 / CUT11 P01 / CUT12 P04。Scene全体の感情アーク・Reality Scale・MIUの違和感インデックスの見え方を最小セットで早期検証できる
4. **残りのPanelをCUT01→12の順で生成**
5. **技術難度の高いVFX系(CUT08のKAI輪郭溶解・ホワイトアウト、CUT09の切り返し)は並行して早期着手し、リテイクの時間を確保**

### 動画生成順

1. 各CUTの画像が全Panel揃ってから、そのCUT単位で動画化に着手する(Panel間の一貫性を保つため)
2. CUT01→12の順を基本としつつ、技術リスクの高いCUT(CUT07のシルエット→正面の連続ショット、CUT08の輪郭溶解〜ホワイトアウト、CUT12のクレーンアップ)は早期に試験生成する
3. セリフを含むCUT(CUT02・CUT03・CUT06・CUT07・CUT09・CUT11)は音声同期の検証が必要。Dialogue素材(未収録、下記参照)の確定と合わせて優先度を調整する

---

## 既知の残課題(Phase 1着手前に要確認)

- Costume Bible: MIU/AYA/NANAの私服、KAIのコック衣装、HINAの白い服、いずれも未登録
- Dialogue: 全セリフ(CUT02 AYA「待った？」、CUT03 NANA「お待たせー！」、CUT04 NANA「こっち行ってみない？」、CUT05 AYA「こんな店、あったっけ？」、CUT06 NANA「なんか、落ち着く」、CUT07 KAI「お待たせ」、CUT08 MIU「え……？」、CUT09 AYA「今の、何だったんだろう」、CUT11 MIU「どこかで、会った気がする」)は未収録。ElevenLabs等での音声生成、または楽曲の歌唱パートとの配置調整はYU/作曲側の判断が必要

## 関連

- Panel Storyboard/Director Notes: `Storyboard/CUT<番号>_絵コンテ.md` / `Storyboard/CUT<番号>_Panel<番号>_DirectorNotes.md`
- EDIT_PLAN: `Edit/EDIT_PLAN.md`
- Story Bible: Obsidian Vault `06_Projects/WAKE_UP/Overview.md`
