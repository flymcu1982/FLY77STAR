# WAKE UP — Pilot Production: CUT01 Panel01（Location Validation）

Production Phase 5(Pilot Production)。対象: Scene01 / CUT01 / Panel01のみ。

## Director Decision(2026-07-11、承認済み・Production Baseline変更)

社長承認。ただしProduction Baselineを以下の通り変更:

| Panel | 役割(変更後) |
|---|---|
| CUT01 Panel01 | **Location Validation**(本ファイルの対象) |
| CUT01 Panel02 | Camera Validation |
| CUT01 Panel03 | **Golden Production Image**(今後のProduction QC・Character QC・Costume QC・Director Approvalの基準画像) |

本Panel(Panel01)はもはやGolden Production Imageではなく、**Location Validation**(ロケーション・光・トーンの検証用)として位置づけを変更する。これにより、下記③Director Review Pointの項目1・4は本Director Decisionをもって解決済みとする(取り消し線付きで決定履歴として残す)。Character/Costume/Story Bible/Panel Storyboard整合の最終基準は、今後CUT01 Panel03(Golden Production Image)側で扱う。

---

Production Source of Truth: Character Master(`Reference/CHAR_*_MASTER.md`) / Costume Master(Costume Bible、現状未登録) / Location Master(`Reference/LOC_CROSSING_MASTER.md`) / Story Bible(Obsidian Vault `06_Projects/WAKE_UP/Overview.md`) / Panel Storyboard(`Storyboard/CUT01_絵コンテ.md`) / Director Notes(`Storyboard/CUT01_Panel03_DirectorNotes.md`、Panel01には無し)。

既存成果物(CUT01.md / CUT01_絵コンテ.md / LOC_CROSSING_MASTER.md 等)は本Pilot Productionにあたり変更していない。本ファイルは補助資料として新規追加する。

**AI社員は画像生成を実行していない。** 以下はProduction Promptの最終確認・QC準備・Director Approval Sheet更新準備・Production Reportである(Director Decisionを反映した更新版)。

---

## 対象Panelの前提(重要)

CUT01 Panel01は**人物が登場しないPanel**である(`CUT01_絵コンテ.md` Panel1: 「芝居: なし(群衆のみ、MIUはまだ画面内で識別されない)」)。MIUが画面内で初めて識別されるのはPanel3から。したがって本Panelにおいて Character Master / Costume Master は**適用対象外**であり、Location Master(渋谷スクランブル交差点、俯瞰)が主たるSource of Truthとなる。この前提は下記レビュー・QC・Director Review Pointの全体に影響するため最初に明記する。

---

## Production Prompt(最終確認版)

Location Master(`LOC_CROSSING_MASTER.md`)のOVERHEAD角度バリエーションと、Panel Storyboard Panel1仕様を統合した最終プロンプト。

```
Wide establishing aerial/drone-height view of Shibuya scramble crossing
at night, East Asian metropolitan intersection, dense pedestrian crowd
crossing in multiple diagonal directions, no single figure identified
or emphasized within the crowd, neon signage and digital billboards
reflecting on wet pavement, vibrant saturated night colors, warm neon
light mixed with cooler ambient tones, generic fictional store signage
only (no real brand names or logos), fixed low-altitude drone
perspective, extreme wide shot, 16-24mm lens look, cinematic
composition, 35mm film grain, atmospheric mood of a city at full
energy just before something begins
```

---

## ① Production Prompt Review

| 項目 | 判定 | 備考 |
|---|---|---|
| Character整合 | **対象外** | Panel01に人物は登場しない(`CUT01_絵コンテ.md`前提と一致)。MIUのCharacter Masterが最初に適用されるのはPanel3から |
| Costume整合 | **対象外** | 同上理由。MIU私服未登録(Costume Bible)の残課題もPanel01には影響しない |
| Location整合 | **一致** | `LOC_CROSSING_MASTER.md`のLocation Lock Prompt(暖色ネオン、彩度の高い夜景、架空店舗表記のみ)およびOVERHEAD角度バリエーションをすべて反映済み |
| Storyboard整合 | **一致(注記あり)** | `CUT01_絵コンテ.md` Panel1(ELS・俯瞰固定・被写体特定なし・「渋谷の熱量」提示)と一致。**注記**: `CUT01.md`本体の「画像生成Prompt」はMIUを含む構図で書かれており、これはPanel3以降寄りの代表フレームに近い。Panel1単体の生成では、CUT全体プロンプトではなくPanel Storyboardの Panel1仕様とLocation Masterを優先参照する必要がある(既存ファイル間に矛盾はなく、記述粒度の違い) |
| Director Notes整合 | **対象外** | CUT01のDirector NotesはPanel03のみに存在(Studio OS v1.2「重要Panelのみ」ルールに沿った状態)。Panel01への作成義務はない |

---

## ② Production QC Checklist(生成後に実施)

Panel01はLocation Validation(Director Decision、2026-07-11)としてQCを行う。生成画像が提供され次第、`Prompt/IMAGE_QC_CHECKLIST.md`の一般基準に加え、本Panel固有の判定基準は以下の通り。

| 項目 | 判定基準 |
|---|---|
| Character | 対象外(人物が写り込んでいないことの確認のみ行う。誤って人物が生成された場合は不採用) |
| Costume | 対象外(同上) |
| Location | `LOC_CROSSING01`のOVERHEAD Lock Promptとの一致。実在の渋谷スクランブル交差点の地理的特徴(交差点の広さ、群衆密度)を保ちつつ、個別店舗名・ロゴが一切表示されていないか |
| Lighting | 彩度の高いネオン夜景、暖色ネオン+寒色アンビエントのバランス、路面への光の反射 |
| Composition | ELS構図で群衆の流れのみを見せ、画面内に特定の被写体・視線誘導点を作っていないか(Panel3で初めてMIUが際立つ対比を成立させるため、Panel1で誰かが目立ってはいけない) |
| Emotion | 「渋谷の熱量」「これから何かが始まる予感の前段階」。まだ感情のピークではなく、無人称の高揚感に留まっているか |

---

## ③ Director Review Point(社長確認事項)

1. ~~**Golden Image選定の妥当性**~~ — **解決済み(Director Decision、2026-07-11)**: Panel01はLocation Validationへ再分類、Panel03をGolden Production Imageとする
2. **実在地名の描写深度**: 渋谷スクランブル交差点という実在地名を使用しつつ架空店舗表記のみとする方針(Production Bible AI Production Policy)について、俯瞰カットでどこまで「渋谷そのもの」と識別可能な描写にするか(交差点の形状・規模感の再現度)の線引き
3. **CUT01.md本体プロンプトとPanel Storyboardの粒度差の扱い**: 上記「Storyboard整合」注記の通り、CUT01.md本体プロンプト(MIU込み)とPanel1個別仕様(MIUなし)に差がある。今後の全Panel制作で「Panel単位の仕様を優先する」という運用を正式な前提としてよいか
4. ~~**Panel02の位置づけ**~~ — **解決済み(Director Decision、2026-07-11)**: Panel02はCamera Validationとして位置づけ、Panel01→02→03と順に進める(Panel03がGolden Production Image)
5. **Costume Bible着手タイミング**: Panel01自体は衣装に無関係だが、Pilot Production全体(Panel02・03以降)にはMIUの私服が必要になる。Golden Image確定と並行してCostume Bible着手のタイミングをご判断いただきたい

---

## ④ Panel02へ進むためのGo / Hold判定

**Panel01: Go**(社長承認済み、2026-07-11。Location Validationとして④GPT Imageでの生成に進めて差し支えない状態)

**Panel02への進行: Go**(Director Decision、2026-07-11。Camera Validationとして順に進める)

**Panel03(Golden Production Image)**: Panel01・02のValidationを経て、Character/Costume/Story Bible/Panel Storyboard整合を含む本番のProduction QC・Character QC・Costume QC・Director Approvalの基準として扱う。Panel03固有のPilot Production資料は別途必要になった時点で作成する。

---

## 関連

- Production Prompt元資料: `Storyboard/CUT01.md`(生成プロンプト本体) / `Storyboard/CUT01_絵コンテ.md`(Panel Storyboard、Panel1仕様)
- Location Master: `Reference/LOC_CROSSING_MASTER.md`
- Director Notes(参考、Panel03のみ存在): `Storyboard/CUT01_Panel03_DirectorNotes.md`
- Image QC Checklist(一般基準): `Prompt/IMAGE_QC_CHECKLIST.md`
- Director Approval Sheet: `Prompt/DIRECTOR_APPROVAL_SHEET.md`
- Story Bible: Obsidian Vault `06_Projects/WAKE_UP/Overview.md`
