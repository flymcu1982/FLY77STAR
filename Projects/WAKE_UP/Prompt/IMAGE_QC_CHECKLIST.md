# WAKE UP — Image QC Checklist

Production Policy Version 1.0(`IMAGE_GENERATION_POLICY.md`)に基づく品質チェック基準。AI社員(Claude Code)が担当するQC工程は、**本番生成された画像そのものの生成ではなく、本チェックリストの整備と、生成後の画像に対する照合**である。実際の画像は④(GPT Imageでの本番生成)以降、社長承認を経て作成される。

## 適用タイミング

制作フロー`① 設計 → ② 社長レビュー → ③ 採用決定 → ④ GPT Image本番生成`の**④の直後**に、本チェックリストを使って生成画像を照合する。QCを通過した画像のみ⑤(Higgsfieldでの動画生成)へ進める。

## チェック項目

各Asset ID(`Prompt/IMAGE_ASSET_LIST.md`参照)の生成画像について、以下6項目を確認する。

### 1. Character Masterとの一致

- [ ] 該当キャラクターの`Reference/CHAR_<名前>_MASTER.md`のCharacter Lock Promptと矛盾しないか
- [ ] 一貫性アンカー(例: NANAのほくろ位置、HINAのインナーカラーなし、KAIの"East Asian Japanese"+MA-1期意匠)が守られているか
- [ ] 複数キャラクターが同一Panelに映る場合、取り違え(顔の特徴が別キャラのものと混ざる)が起きていないか

### 2. 表情

- [ ] 該当Panelの生成プロンプト(`Storyboard/CUT<番号>.md`)・Director Notes(該当する場合)が指定する感情・表情と一致するか
- [ ] Character Masterの表情差分6種のうち、意図した種別(例: KAI「穏やかな微笑み(コックとして)」)が使われているか
- [ ] 重要Panel(Director Notes該当、全12件)は特に、演技指示(観客に何を感じてほしいか)が表情に反映されているか

### 3. 衣装

- [ ] Character Masterの「衣装に関する注意」に記載した仮描写(私服/コック衣装/白い服)から逸脱していないか
- [ ] Costume Bible未登録のため正式デザインではない旨を前提に、少なくとも**キャラクター間で衣装の色・トーンが混同されていない**か(例: MIU=ダーク系、AYA=ムーテッドトーン、NANA=明るいトーン)
- [ ] 架空表記ポリシー(POP DINER看板、KAIのエプロン等)に反する実在ブランドを想起させる要素が紛れ込んでいないか

### 4. 背景

- [ ] 該当Location Master(`Reference/LOC_*_MASTER.md`)のLocation Lock Promptと一致するか
- [ ] 同一CUT内でBG流用指定のあるPanel同士(Image Asset List参照)で背景の一貫性が保たれているか
- [ ] Scene2(現実→パラレル)・Scene3(パラレル→現実)のReality Scale(`Storyboard/Scene2_Review.md`・`Scene3_Review.md`参照)に対応した光・色温度になっているか

### 5. Story Bibleとの整合

- [ ] Obsidian Vault `06_Projects/WAKE_UP/Overview.md`のStory Bible(あらすじ・テーマ・12カット構成)と矛盾しないか
- [ ] 架空ブランドポリシー・実在地名の扱い(渋谷は実在地名可、店舗名は架空)に沿っているか
- [ ] HINA=RIN混同なし等、既存のDecision Log確定事項に反していないか

### 6. Panel Storyboardとの一致

- [ ] `Storyboard/CUT<番号>_絵コンテ.md`該当Panelのショットサイズ・カメラワーク・構図と一致するか
- [ ] パネル間の繋ぎ(編集意図)を踏まえた画角・構図になっているか(前後Panelとの連続性)
- [ ] 生成上のメモ(既知の注意点、例: KAIの銀ペンダントが消えやすい、POP DINER看板の文字崩れ)が反映されているか

## 判定

各Asset IDについて、6項目すべてを満たす場合のみ「採用」とする。1項目でも不一致がある場合は「要リテイク」とし、原因(プロンプト側の問題か生成側の問題か)を記録した上で③(採用決定)へ差し戻す。

| 判定 | 意味 |
|---|---|
| 採用 | 6項目すべて満たす。⑤(Higgsfieldでの動画生成)へ進める |
| 要リテイク | いずれかの項目で不一致。原因を記録し再生成 |
| 保留 | Costume Bible等、上流の未確定事項に起因する判断不能。上流確定を待つ |

## 関連

- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
- Character Master: `Reference/CHAR_*_MASTER.md`
- Location Master: `Reference/LOC_*_MASTER.md`
- Production Policy: GitHub `IMAGE_GENERATION_POLICY.md`
