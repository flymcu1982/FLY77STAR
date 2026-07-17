# SNS Profile Templates（プロフィール文テンプレート）

**Document Version:** 1.0  
**Last Updated:** 2026-07-17  
**Status:** テンプレート完成

---

## Overview

各SNSプラットフォームのプロフィール設定用テキストテンプレート。  
YU が実アカウント登録時に使用します。

---

## Gmail

### Account Email
```
fly77star.official@gmail.com
```

### Recovery Information
- **Recovery email:** （登録ユーザーの予備メールアドレス）
- **Recovery phone:** （登録ユーザーの電話番号）
- **2FA:** Authenticator app（Google Authenticator / Authy / Microsoft Authenticator）

---

## TikTok

### Display Name
```
FLY77STAR.
```

### Bio
```
🎬✨ Music × Storytelling × AI. Imagining the future. Creating it now.
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Additional Notes (Internal)
- **Profile picture:** Assets/FLY77STAR_Logo.png
- **Account type:** Standard (Creator upgrade option: later)
- **Primary use:** Promotion, short-form content, engagement
- **Content focus:** Work releases, behind-the-scenes hooks, character spotlights

---

## Instagram

### Display Name
```
FLY77STAR.
```

### Bio
```
🎬✨ Music × Storytelling × AI. Imagining the future. Creating it now.
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Additional Settings
- **Profile picture:** Assets/FLY77STAR_Logo.png
- **Account type:** Creator Account (mandatory for analytics)
- **Category:** Entertainment or Artist
- **Primary use:** Visual storytelling, reels, stills, aesthetic branding
- **Content focus:** Still frames, character portraits, production mood, behind-the-scenes stills

---

## X - @FLY77STAR_JP (Official)

### Display Name
```
FLY77STAR.
```

### Bio
```
公式告知、作品公開、YouTube / TikTok / note 導線
Official announcements & work releases. Music × Film × Storytelling × AI.
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Location
```
Japan Tokyo
```

### Additional Notes (Internal)
- **Profile picture:** Assets/FLY77STAR_Logo.png （確認済みまたは更新）
- **Account status:** Active / Verified
- **Primary use:** Official announcements, work launches, cross-platform promotion
- **Content focus:** Latest releases, YouTube/TikTok guides, official updates
- **Email recovery:** fly77star.official@gmail.com （YU手動追加）

---

## X - @FLY77STAR_LAB (Lab / Behind-the-Scenes)

### Display Name
```
FLY77STAR. Lab
```

### Bio
```
AI制作ログ、失敗生成、プロンプト検証、AI社員運用、制作裏側
AI Production Lab - Process Notes, Experiments, Prompt Validation, Behind-the-Scenes
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Location
```
Japan Tokyo (Lab)
```

### Additional Notes (Internal)
- **Profile picture:** Assets/FLY77STAR_Logo.png または Lab テーマのアイコン（オプション）
- **Account status:** Active / Semi-public Documentation
- **Primary use:** AI production process sharing, experiment logs, internal team operations visibility
- **Content focus:** AI generation logs, failed attempts, prompt testing, CANON management, workflow documentation
- **Email recovery:** fly77star.official@gmail.com （YU手動追加）
- **Launch policy:** Handle reservation only or later activation acceptable

---

## Common Elements Across All Platforms

### Hashtag Strategy (Optional)

**TikTok / Instagram / X:**

Pinned / Highlighted content:
```
#FLY77STAR #AICreation #Storytelling #MusicVideo #CharacterArt
```

Launch content:
```
#新作公開 #MV #AI生成 #映像制作 #FLY77STAR
```

Promotional:
```
#YouTube #TikTok #note #SE77NTH
```

### Contact / Support (Internal Use Only)

- **Official email:** fly77star.official@gmail.com
- **Support channel:** (To be determined by YU)
- **DM policy:** Open to public / Limited to verified accounts (per YU discretion)

---

## Platform-Specific Customization Notes

### TikTok
- Bio character limit: ~80 characters (recommendation: keep concise)
- Emojis supported: ✅ Yes
- External links: Limited (Website link + YouTube link available)
- Creator Fund eligibility: Requires 10k followers + 100k video views

### Instagram
- Bio character limit: ~150 characters
- Emojis supported: ✅ Yes
- Clickable links: Website link + (optional) Stories links
- Creator Account: Enables Reels, analytics, shopping, collabs
- Account switching: Up to 5 accounts on one app

### X (Twitter)
- Bio character limit: ~160 characters
- Emojis supported: ✅ Yes
- External links: Website link + media links
- Verification: Requires official status review
- Account linking: Multiple account management via settings

### Gmail
- Account security: 2FA mandatory for all SNS recovery
- Backup codes: Generate and store securely (not in Git)
- Recovery options: Phone + alternate email recommended
- Account alias: fly77star.official@gmail.com is the canonical address

---

## Version Control & Updates

When updating profile text:
1. Update this template file
2. Add update note in "Last Updated"
3. Commit to Git with message: `docs: update SNS profile templates for [platform]`
4. If live profile update needed, YU applies change + confirms in SNS_IMPLEMENTATION_STATUS.md

---

## Related Documents

- `SNS_OPERATIONS.md` - Master SNS policy
- `SNS_MANUAL_SETUP_GUIDE.md` - Step-by-step account creation guide
- `SNS_IMPLEMENTATION_STATUS.md` - Account creation progress tracker
- `SNS_INITIAL_POSTS.md` - First post templates
- `SNS_ICON_HEADER_GUIDE.md` - Visual asset specifications

---

**Document maintained by:** Claude Code (CTO)  
**Copy-paste ready:** ✅ All text ready for direct pasting into SNS fields  
**Last verified:** 2026-07-17
