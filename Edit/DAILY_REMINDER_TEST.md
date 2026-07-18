# Daily Reminder メール送信 — テスト実行ガイド

**テスト日時:** 2026-07-19 朝 08:55  
**テスト対象:** メール自動送信スクリプト  
**テスト方法:** 手動実行 → 送信確認

---

## 🧪 テスト実行手順

### テスト 1: スクリプト初期確認

```bash
# リポジトリルートから実行
cd /path/to/FLY77STAR

# スクリプトが存在するか確認
ls -la scripts/daily_reminder.js

# 出力例:
# -rwxr-xr-x  1 user  staff  8192 Jul 18 22:00 scripts/daily_reminder.js
```

**確認項目:**
- ✅ ファイルが存在する
- ✅ 実行権限がある（x フラグ）

---

### テスト 2: .env ファイル確認

```bash
# .env ファイルが存在するか確認
ls -la .env

# 出力例:
# -rw-r--r--  1 user  staff  256 Jul 18 22:00 .env

# 内容確認
cat .env

# 出力例:
# GMAIL_ADDRESS=fly77star.official@gmail.com
# GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
# YU_EMAIL=fly77star.official@gmail.com
# BASE_URL=https://github.com/...
```

**確認項目:**
- ✅ ファイルが存在する
- ✅ GMAIL_ADDRESS が設定されている
- ✅ GMAIL_APP_PASSWORD が 16 文字（スペース含む）
- ✅ YU_EMAIL が設定されている

---

### テスト 3: パッケージインストール確認

```bash
# nodemailer がインストールされているか確認
npm list nodemailer

# 出力例:
# FLY77STAR@1.0.0 /path/to/FLY77STAR
# └── nodemailer@6.9.0
```

**確認項目:**
- ✅ nodemailer がインストール済み

パッケージが見つからない場合：
```bash
npm install nodemailer dotenv
```

---

### テスト 4: 手動スクリプト実行

```bash
# スクリプト実行
node scripts/daily_reminder.js

# 期待される出力:
# === Daily Reminder Email Sender ===
# 実行時刻: 2026-07-19 09:00:00
# 
# 📧 メール送信中...
# To: fly77star.official@gmail.com
# Subject: 【朝のチェックシート準備完了】本日の運用開始 08:55
# 
# ✅ メール送信成功！
# Message ID: <message_id_here@gmail.com>
# Response: 250 2.0.0 OK
```

**トラブルシューティング:**

エラーが出た場合は以下を確認：

```bash
# エラー: "Cannot find module 'nodemailer'"
npm install nodemailer

# エラー: "Gmail SMTP 認証失敗"
# → .env の GMAIL_APP_PASSWORD が正しいか確認
# → Google Account で App Password を再生成

# エラー: "Cannot read property 'xxxxx' of undefined"
# → .env ファイルが正しく読み込まれているか確認
# → 環境変数を手動で設定: export GMAIL_ADDRESS=...
```

---

### テスト 5: メール到着確認（YU のメールボックス）

**手順:**

1. `fly77star.official@gmail.com` にログイン
2. 受信トレイを確認
3. 件名「【朝のチェックシート準備完了】本日の運用開始 08:55」のメールを探す
4. メールを開いて内容確認

**確認項目:**

- ✅ メールが到着している
- ✅ 送信者: Claude Code
- ✅ 件名: 「【朝のチェックシート準備完了】本日の運用開始 08:55」
- ✅ HTML 形式で正しく表示されている
- ✅ チェックシートへのリンクが表示されている
- ✅ スケジュール表（09:00/09:30/15:00/18:00）が表示されている

**表示されるべき内容:**

```
🌅 本日のチェックシート準備完了
2026年7月19日 金曜日

おはようございます！
Claude Code（AI社員）です。

本日のチェックシートの準備ができました。
08:55 から、下記のファイルを開いて実行をお願いします。

[スケジュール表]
09:00-09:30  Gmail確認
09:30-10:00  SNS DM確認
15:00        返信下書き生成
18:00        日報作成

📋 本日のチェックシート

📧 Gmail メール確認
実行時刻: 09:00-09:30（想定30分）
fly77star.official@gmail.com にログインして、
受信トレイのメール全件を確認・分類してください。
[📋 チェックシートを開く] ← クリック可能

📱 SNS DM 確認
実行時刻: 09:30-10:00（想定30分）
TikTok / Instagram / X のメッセージを確認して、
新着 DM 全件を分類・集計してください。
[📋 チェックシートを開く] ← クリック可能

⚠️ 注意
- メール件数が多い場合は、URGENT → HIGH → MEDIUM の順から処理
- 時間に制限がある場合は、URGENT + HIGH のみ記入し、後で追記でも OK
- URGENT メールが到着した場合は、即座に Claude Code に通知

ご不明な点や質問があれば、
いつでもお気軽にお声がけください。

本日も宜しくお願いします！🚀

Claude Code（AI社員）
FLY77STAR Studio CTO
```

---

## 📊 テスト結果記録

### テスト実行日: 2026-07-19 朝 08:55

**テスト 1: スクリプト初期確認**
- [ ] ✅ パス
- [ ] ❌ 失敗（理由: ______________________）

**テスト 2: .env ファイル確認**
- [ ] ✅ パス
- [ ] ❌ 失敗（理由: ______________________）

**テスト 3: パッケージ確認**
- [ ] ✅ パス
- [ ] ❌ 失敗（理由: ______________________）

**テスト 4: 手動実行テスト**
- [ ] ✅ パス（Message ID: ______________________）
- [ ] ❌ 失敗（エラー内容: ______________________）

**テスト 5: メール到着確認**
- [ ] ✅ 到着確認
- [ ] ❌ 未到着（原因調査中）

---

## 🔍 ログ確認方法

### 手動実行時のログ

```bash
# 実行ログ表示
cat logs/daily_reminder.log

# 出力例:
# [2026-07-19T00:55:00.123Z] SUCCESS - <message_id@gmail.com>
```

### Cron 実行時のログ

```bash
# Cron ログ表示
cat logs/daily_reminder_cron.log

# 出力例:
# === Daily Reminder Email Sender ===
# 実行時刻: 2026-07-19 08:55:00
# 📧 メール送信中...
# To: fly77star.official@gmail.com
# ✅ メール送信成功！
```

---

## ✅ テスト完了チェックリスト

- [ ] スクリプト初期確認 ✅
- [ ] .env ファイル確認 ✅
- [ ] パッケージインストール確認 ✅
- [ ] 手動スクリプト実行成功 ✅
- [ ] メール到着確認 ✅
- [ ] HTML 形式表示確認 ✅
- [ ] チェックシートリンク確認 ✅
- [ ] ログファイル作成確認 ✅

**全項目完了 = テスト合格 🎉**

---

## 🚀 本番運用開始

テストが完了したら、Cron ジョブを設定して本番運用を開始します：

```bash
# Cron セットアップ実行
bash scripts/setup_cron.sh

# または手動設定
crontab -e
# 以下の行を追加:
# 55 08 * * * cd /path/to/FLY77STAR && node scripts/daily_reminder.js >> logs/daily_reminder_cron.log 2>&1
```

以降は毎日 08:55 に自動的にメールが送信されます。

---

**テスト実行日時:** 2026-07-19 朝 08:55  
**テスト実施者:** Claude Code（AI 社員）  
**テスト環境:** 本番環境（fly77star.official@gmail.com）

ご質問やトラブルがあればお気軽にお声がけください！
