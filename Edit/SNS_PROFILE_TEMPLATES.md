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
Music × Film × Story × AI Creative Studio. SE77NTH. | KAI / RUI / RUKA / HINA / LIEN. MV制作過程と作品情報を発信。
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Additional Notes (Internal)
- **Profile picture:** Assets/FLY77STAR_Logo.png
- **Account type:** Standard (Creator upgrade option: later)
- **Primary use:** Shorts中心、制作過程と作品導線
- **Content focus:** MV制作過程、キャラクター紹介、作品情報、作品へのリード
- **Character focus:** SE77NTH. (KAI / RUI / RUKA / HINA / LIEN)

---

## Instagram

### Display Name
```
FLY77STAR.
```

### Bio
```
Music × Film × Story × AI Creative Studio. SE77NTH. | KAI / RUI / RUKA / HINA / LIEN. MV制作過程と作品情報を発信。
```

### Website Link
```
https://flystar77-studio.netlify.app
```

### Additional Settings
- **Profile picture:** Assets/FLY77STAR_Logo.png
- **Account type:** Creator Account (mandatory for analytics)
- **Category:** Entertainment or Artist
- **Primary use:** Reels中心、制作過程と作品導線
- **Content focus:** MV Reels、キャラクター紹介、制作ビハインド・スティル、制作雰囲気、アート制作過程
- **Character focus:** SE77NTH. (KAI / RUI / RUKA / HINA / LIEN)

---

## X - @FLY77STAR_JP (Official)

### Display Name
```
FLY77STAR.
```

### Bio
```
FLY77STAR. 公式｜音楽・映像・物語・AIクリエイティブをつなぐ未来型スタジオ。SE77NTH. / KAI / RUI / RUKA / HINA / LIEN。MV・Shorts・note公開情報を発信。
```

### Alternative Bio (English)
```
FLY77STAR Official | AI × Film × Music × Story Studio. Connecting art, music, and technology. Latest work announcements on YouTube, TikTok, note.
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
- **Profile picture:** Assets/FLY77STAR_Logo.png （正式Fロゴ）
- **Account status:** Active / Official
- **Primary use:** 公式告知、作品公開、YouTube / TikTok / note導線
- **Content focus:** 新作公開情報、プロジェクト告知、クロスプラットフォーム導線、SE77NTH.関連ニュース
- **Email recovery:** fly77star.official@gmail.com （YU手動追加）
- **Character focus:** SE77NTH. (KAI / RUI / RUKA / HINA / LIEN)

---

## X - @FLY77STAR_LAB (Lab / Behind-the-Scenes)

### Display Name
```
FLY77STAR. Lab
```

### Bio
```
FLY77STAR. LAB｜AI MV制作の実験室。プロンプト、失敗生成、修正、CANON管理、AI社員運用、制作ノートを記録。
```

### Alternative Bio (English)
```
FLY77STAR Lab | AI Production Laboratory. Prompt logs, failed attempts, fixes, CANON management, AI team operations, production notes.
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
- **Profile picture:** Assets/FLY77STAR_Logo.png （正式Fロゴ）
- **Account status:** Active / Production Process Documentation
- **Primary use:** AI制作ログ、失敗生成、プロンプト検証、CANON管理、AI社員運用、制作裏側
- **Content focus:** AI生成ログ、失敗生成例と修正、プロンプト検証、CANON管理記録、制作過程ノート、AI社員運用状況
- **Email recovery:** fly77star.official@gmail.com （YU手動追加）
- **Launch policy:** 実験室・制作現場感を出す、完成品だけでなく完成までの過程を公開
- **Tone:** データドリブン、透明性重視、失敗からの学習を重視

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

---

## YU Final Approval Checklist

プロフィール文をすべてのプラットフォームに反映する前に、以下を確認してください：

- [ ] X @FLY77STAR_JP プロフィール文確認
- [ ] X @FLY77STAR_LAB プロフィール文確認
- [ ] TikTok プロフィール文確認
- [ ] Instagram プロフィール文確認
- [ ] SE77NTH.キャラクター表記統一確認
- [ ] 各プラットフォームのWebサイトリンク確認
- [ ] 全プラットフォーム完了確認

**YU 署名:** ________________  
**日時:** ________________

---

**Document maintained by:** Claude Code (CTO)  
**Copy-paste ready:** ✅ All text ready for direct pasting into SNS fields  
**Version:** 2.0 - Platform-specific profiles with role division  
**Last updated:** 2026-07-17
