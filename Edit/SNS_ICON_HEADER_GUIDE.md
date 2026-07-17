# SNS Icon & Header Guide（ビジュアル設定指示）

**Document Version:** 1.0  
**Last Updated:** 2026-07-17  
**Status:** 設定指示書 完成

---

## Overview

各SNSプラットフォームのアイコン・ヘッダー画像設定仕様。  
YU がアカウント登録時に参照して、画像をアップロードします。

**Available Asset:**
- `Assets/FLY77STAR_Logo.png` (1.9MB, existing)

---

## Gmail

### Profile Picture
- **Size:** N/A （Gmail では不使用）
- **Note:** Gmail の Google Account profile picture は Profile Settings で設定（SNS連携用ではない）

---

## TikTok

### Profile Picture

**File:** `Assets/FLY77STAR_Logo.png`

**Specs:**
- **Recommended Size:** 1024×1024px or larger
- **Display Size:** 200×200px (circular crop)
- **File Type:** PNG, JPG, GIF
- **File Size:** Max 10MB
- **Format:** Circular (auto-cropped to circle)
- **Quality:** High resolution (auto-downscaled, no compression artifacts)

**Upload Location:**
```
TikTok App > Profile > Edit profile > Profile photo > Upload or change photo
```

**Best Practices:**
- Center the logo in the frame
- Ensure good contrast and visibility at small sizes
- No text overlay (logo text should be part of the image)
- Transparent background recommended (PNG)

---

## Instagram

### Profile Picture

**File:** `Assets/FLY77STAR_Logo.png`

**Specs:**
- **Recommended Size:** 1080×1080px or larger
- **Display Size:** 110×110px (circular crop on desktop, 150×150 on mobile)
- **File Type:** PNG, JPG
- **File Size:** Max 4MB
- **Format:** Circular (auto-cropped by Instagram)
- **Quality:** High resolution

**Upload Location:**
```
Instagram > Profile > Edit profile > Change profile picture
```

**Best Practices:**
- High contrast logo
- Center positioned
- Clean, recognizable at small sizes
- Transparent background (PNG recommended)
- No text overlay

---

### Header Image (Bio Section)

**Optional - Not Standard Feature on Instagram**

Note: Instagram does not have a traditional "header" image like other platforms.  
Instead, use:
- **Story Highlights:** Cover images (optional, aesthetic)
- **Grid Layout:** First 9 posts form visual impression

---

## X (Twitter)

### Profile Picture - Both Accounts

**File:** `Assets/FLY77STAR_Logo.png`

**Specs:**
- **Recommended Size:** 1024×1024px or larger
- **Display Size:** 48×48px (web), 96×96px (app), 200×200px (profile page)
- **File Type:** PNG, JPG, GIF
- **File Size:** Max 5MB
- **Format:** Square (no auto-crop, use as-is)
- **Quality:** High resolution

**Upload Location (Desktop):**
```
Settings and privacy > Account > Your account > Profile picture > Upload
```

**Upload Location (Mobile App):**
```
Profile > Edit profile > Profile photo > Change photo
```

**Best Practices:**
- Clear, recognizable logo
- High contrast on light and dark backgrounds
- No transparency needed (use white or light background)
- Center the logo
- Ensure text is readable at 48×48px

---

### Header Image (Banner) - @FLY77STAR_JP (Official)

**Status:** ✅ Required

**Specs:**
- **Recommended Size:** 1500×500px
- **Display Size:** 1500×500px (desktop), 1200×315px (mobile)
- **File Type:** PNG, JPG
- **File Size:** Max 5MB
- **Aspect Ratio:** 3:1 (1500×500)
- **Format:** Rectangular (no auto-crop, use as-is)

**Upload Location:**
```
Profile > Edit profile > Header photo > Upload
```

**Design Specification - JP Official:**

```
【要素】
- 中央：正式 FLY77STAR. Fロゴ
- 左下：FLY77STAR.
- 右上：From One Light, Infinite Possibilities.
- 右下：ひとつの光から、無限の可能性へ。

【カラー】
- 背景：黒 / ミッドナイトネイビー（深い紺）
- アクセント：シルバー / 青い光（電気的な青）
- 帯：グラデーション（黒 → ミッドナイトネイビー → 青い光）

【スタイル】
- 静止画のみ（動画不可）
- プロフェッショナル・シネマティック
- 未来型スタジオのイメージ
- 高コントラスト・読みやすいテキスト
```

**Best Practices:**
- Must be static image (X does not support video headers)
- No text that will be cut off on mobile
- High contrast, readable text
- Brand colors consistent with logo
- File must not exceed 5MB

---

### Header Image (Banner) - @FLY77STAR_LAB (Lab Account)

**Status:** ✅ Required

**Specs:**
- **Recommended Size:** 1500×500px
- **Display Size:** 1500×500px (desktop), 1200×315px (mobile)
- **File Type:** PNG, JPG
- **File Size:** Max 5MB
- **Aspect Ratio:** 3:1 (1500×500)
- **Format:** Rectangular (no auto-crop, use as-is)

**Upload Location:**
```
Profile > Edit profile > Header photo > Upload
```

**Design Specification - LAB:**

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

**Best Practices:**
- Must be static image
- Emphasize laboratory / behind-the-scenes aesthetics
- Tech-forward design language
- High visibility for small text elements

---

## Content Format Guidelines

### All Platforms - Profile Picture Requirements

| Platform | Shape | Size (Display) | Format | Upload Size Limit |
|----------|-------|----------------|--------|-------------------|
| **TikTok** | Circle | 200×200px | PNG/JPG/GIF | 10MB |
| **Instagram** | Circle | 110×110px (desktop) | PNG/JPG | 4MB |
| **X (JP)** | Square | 200×200px | PNG/JPG/GIF | 5MB |
| **X (LAB)** | Square | 200×200px | PNG/JPG/GIF | 5MB |

### Header Image Requirements

| Platform | Shape | Size (Display) | Format | Notes |
|----------|-------|----------------|--------|-------|
| **TikTok** | N/A | N/A | N/A | No header image |
| **Instagram** | N/A | N/A | N/A | No header (Story covers optional) |
| **X** | Rectangle | 1500×500px | PNG/JPG (Static only) | Optional |

---

## Potential Future Assets

Once created, the following may be added to `/Assets/`:

- [ ] `FLY77STAR_Header_X.png` - X header image (1500×500px)
- [ ] `FLY77STAR_Icon_Small.png` - Small icon variant (512×512px)
- [ ] `FLY77STAR_Icon_Dark.png` - Dark theme variant (if needed)
- [ ] `FLY77STAR_Icon_Light.png` - Light theme variant (if needed)
- [ ] `SE77NTH_Group_Banner.png` - Character group visual (for Reels)
- [ ] `FLY77STAR_Signature_Overlay.png` - Watermark for video (optional)

---

## Current Asset Status

### Assets/FLY77STAR_Logo.png
- **Status:** ✅ Available
- **Size:** 1.9MB (original uploaded file)
- **Format:** PNG with transparency
- **Use Case:** All platform profile pictures
- **Verified:** Logo is clear, readable, professional
- **Ready for Upload:** ✅ Yes

---

## Upload Checklist

Before uploading to each platform:

### TikTok
- [ ] FLY77STAR_Logo.png downloaded/accessible
- [ ] Image quality verified at 200×200px display size
- [ ] Logo is centered in frame
- [ ] Platform supports PNG with transparency
- [ ] File size <10MB confirmed
- [ ] Upload successful confirmation

### Instagram
- [ ] FLY77STAR_Logo.png downloaded/accessible
- [ ] Image quality verified at 110×110px display size (mobile aware)
- [ ] Logo centered and visible
- [ ] Platform supports PNG
- [ ] File size <4MB confirmed
- [ ] Upload successful confirmation
- [ ] Creator Account enabled before upload (if applicable)

### X - @FLY77STAR_JP
- [ ] FLY77STAR_Logo.png downloaded/accessible
- [ ] Image quality verified at 200×200px display size
- [ ] Logo centered (square format, no circular crop)
- [ ] File size <5MB confirmed
- [ ] Platform supports PNG/JPG
- [ ] Upload successful confirmation
- [ ] (Optional) Header image if desired - verified at 1500×500px

### X - @FLY77STAR_LAB
- [ ] FLY77STAR_Logo.png downloaded/accessible (same as JP, or custom variant)
- [ ] Image quality verified at 200×200px display size
- [ ] Logo centered (square format)
- [ ] File size <5MB confirmed
- [ ] Upload successful confirmation
- [ ] (Optional) Custom header or different icon if desired

---

## Image Quality Tips

When uploading across platforms:

1. **Do NOT use lossy compression** (JPEG quality below 85% will lose detail at small sizes)
2. **PNG is preferred** (preserves transparency and quality)
3. **Test at actual display size** (view at 48×48, 110×110, 200×200 before uploading)
4. **Ensure contrast** (readable on both light and dark platform backgrounds)
5. **No text overlay on small sizes** (logo text should be part of main image)
6. **High resolution master** (1024×1024 or larger prevents pixelation)

---

## Troubleshooting

### Image Appears Blurry
- **Cause:** Low resolution source / over-compression
- **Solution:** Use Assets/FLY77STAR_Logo.png (1.9MB is high quality)
- **Verify:** Check file at native resolution before upload

### Logo Appears Cropped Unexpectedly
- **Cause:** Platform auto-crops to circle (TikTok/Instagram) or different aspect ratio
- **Solution:** Center logo, ensure important elements are in center 70% of frame
- **Verify:** Test on platform's preview before finalizing

### Upload Size Exceeds Limit
- **Cause:** File is too large (PNG with high resolution can be large)
- **Solution:** Export at platform recommended size with compression (still use PNG)
- **Verify:** Keep quality high but reduce dimensions

### Background Transparency Causing Issues
- **Cause:** Some platforms may not display transparency correctly
- **Solution:** Add white or light background layer if needed
- **Verify:** Test on target platform

---

## Related Documents

- `SNS_OPERATIONS.md` - Master SNS policy
- `SNS_PROFILE_TEMPLATES.md` - Profile text templates
- `SNS_IMPLEMENTATION_STATUS.md` - Account creation tracker
- `SNS_MANUAL_SETUP_GUIDE.md` - Account setup instructions
- `SNS_INITIAL_POSTS.md` - First post templates

---

## Asset File Location

```
/home/user/FLY77STAR/Assets/
├── FLY77STAR_Logo.png (1.9MB) ✅ Ready
└── [Future assets to be added]
```

**Download instruction for offline use:**
```
git clone or pull latest from branch: claude/fly77star-obsidian-structure-a010jj
File available at: Assets/FLY77STAR_Logo.png
```

---

## YU Final Approval Checklist

アイコン・ヘッダー画像をすべてのプラットフォームに反映する前に、以下を確認してください：

### Icons - All Platforms
- [ ] Assets/FLY77STAR_Logo.png が正式Fロゴであることを確認
- [ ] アイコンを TikTok に設定
- [ ] アイコンを Instagram に設定
- [ ] アイコンを X @FLY77STAR_JP に設定
- [ ] アイコンを X @FLY77STAR_LAB に設定

### Headers - X Accounts
- [ ] X @FLY77STAR_JP ヘッダー画像（黒/ミッドナイトネイビー/シルバー/青い光）デザイン確認
- [ ] X @FLY77STAR_JP ヘッダー画像（1500×500px）がアップロード可能なサイズ確認
- [ ] X @FLY77STAR_LAB ヘッダー画像（実験室・制作現場感）デザイン確認
- [ ] X @FLY77STAR_LAB ヘッダー画像（1500×500px）がアップロード可能なサイズ確認

### General
- [ ] すべての画像が静止画（動画なし）であることを確認
- [ ] すべてのファイルサイズが制限以内（5MB以下）であることを確認
- [ ] モバイル表示でのテキスト切れがないことを確認
- [ ] 高コントラスト・読みやすいテキストであることを確認

**YU 署名:** ________________  
**日時:** ________________  
**デザイン確認メモ:** ________________

---

**Document Status:** Ready for YU implementation  
**Maintained by:** Claude Code (CTO)  
**Version:** 2.0 - JP Official & LAB header specifications  
**Last Updated:** 2026-07-17  
**Asset Status:** ✅ All icons/logos ready for upload
