# X @FLY77STAR_LAB Setup Guide（最終ステップ）

**Document Version:** 1.0  
**Created:** 2026-07-17  
**Status:** 実装準備完了・YU手動設定待ち

---

## Overview

X @FLY77STAR_LAB アカウントの最終セットアップ手順。  
既存アカウント（電話登録済み）に対して、以下の3ステップで設定を完了します。

---

## Step 1: Email Recovery 追加

### Action
1. X @FLY77STAR_LAB に ログイン
2. **Settings and privacy > Account > Email**
3. `fly77star.official@gmail.com` を Email Recovery として追加登録

**Verification:** Gmail inbox で確認メールを受け取り、認証完了

**Status:** ⏳ 待機中

---

## Step 2: Profile Update

### Profile Settings

| Field | Content |
|-------|---------|
| **Display Name** | `FLY77STAR. Lab` |
| **Bio** | `FLY77STAR. LAB｜AI MV制作の実験室。プロンプト、失敗生成、修正、CANON管理、AI社員運用、制作ノートを記録。デジタルクリエイター` |
| **Location** | `Japan Tokyo` （オプション） |
| **Website** | `https://flystar77-studio.netlify.app` （オプション） |
| **Profile Picture** | Assets/FLY77STAR_Logo.png（正式Fロゴ） |

### Action
1. X @FLY77STAR_LAB に ログイン
2. **Settings and privacy > Account > Your account > Profile**
3. 上記の情報を入力
4. **Save** をクリック

**Status:** ⏳ 待機中

---

## Step 3: Header Image 設定

### Header Specifications

| Property | Value |
|----------|-------|
| **Size** | 1500×500px（推奨） |
| **Format** | PNG / JPG（静止画のみ） |
| **File Size** | 5MB以下 |
| **Design** | 実験室・制作現場感・テック感 |

### Design Requirements

```
【要素】
- 中央：正式 FLY77STAR. Fロゴ
- 左：FLY77STAR. LAB
- 中央下：Behind the Making
- 右：AI Production / CANON / Prompt / QC / Studio OS

【カラー】
- 背景：黒 / ダークグレー（実験室感）
- アクセント：ネオングリーン / 電気的な青 / シルバー
- 帯：テッキーな感じ（グリッド・デジタル感）

【スタイル】
- 実験室・制作現場感を強調
- JP公式より少しカジュアル・テック感
- 制作プロセスの透明性を表現
- グリッドやモニター的なデザイン要素
```

### Action
1. ヘッダー画像を制作（上記デザイン要件に従う）
2. ファイルを `Edit/X_LAB_Header.png` として保存
3. X @FLY77STAR_LAB に ログイン
4. **Settings and privacy > Account > Your account > Header photo**
5. `Edit/X_LAB_Header.png` をアップロード

**Reference:** `SNS_ICON_HEADER_GUIDE.md` LAB Account section

**Status:** ⏳ 待機中（ヘッダー画像は別途制作）

---

## 2FA (Optional but Recommended)

X での 2FA 設定（オプション推奨）

1. **Settings and privacy > Account > Security and account access > Two-factor authentication**
2. Authenticator app または SMS による 2FA を有効化

**Status:** ⏳ オプション

---

## Verification Checklist

Before completing, verify:

- [ ] Email recovery: `fly77star.official@gmail.com` 登録完了
- [ ] Display Name: `FLY77STAR. Lab` に更新
- [ ] Bio: 「FLY77STAR. LAB｜AI MV制作の実験室…デジタルクリエイター」に更新
- [ ] Profile Picture: 正式Fロゴ設定（確認済み）
- [ ] Header Image: 設定完了（ネオングリーン/電気的な青のテック感）
- [ ] Profile URL: https://twitter.com/FLY77STAR_LAB にアクセスしてプロフィール確認

---

## Completion Confirmation

すべてのステップが完了したら、以下を確認してください：

```
✅ メールリカバリー追加完了
✅ プロフィール設定完了
✅ ヘッダー画像設定完了
✅ プロフィール・アイコン表示確認完了

X @FLY77STAR_LAB: https://twitter.com/FLY77STAR_LAB
```

---

## Next Steps (After X LAB Setup)

X @FLY77STAR_LAB のプロフィール設定完了後：

1. **初期投稿準備:** SNS_INITIAL_POSTS.md の TikTok / Instagram / X 初期投稿を実装
2. **ビジュアル資産:** X @FLY77STAR_JP のヘッダー画像も別途制作（黒/ミッドナイトネイビー/シルバー/青い光）
3. **最終承認:** SNS_YU_APPROVAL_CHECKLIST.md Phase 5 Final Approval を実行

---

## Timeline

**Phase 進捗:**
- ✅ Phase 1: Account Creation（Gmail / TikTok / Instagram / X JP・LAB 完了）
- ✅ Phase 2: Profile Content（TikTok / Instagram / X JP 完了）
- ⏳ Phase 3: Initial Posts（投稿準備中）
- ⏳ Phase 4: Visual Assets（X ヘッダー画像制作中）
- ⏳ Phase 5: Final Approval（最後のゲート）

---

**Document Status:** X LAB Setup 実装準備完了  
**Maintained by:** Claude Code (CTO)  
**Version:** 1.0  
**Last Updated:** 2026-07-17
