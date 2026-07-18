# Daily Reminder メール送信 — セットアップガイド

**機能:** 毎朝 08:55 に自動メール送信スクリプト  
**宛先:** YU（fly77star.official@gmail.com）  
**件名:** 「本日のチェックシート準備完了」  
**目的:** 朝のチェックシート開始を支援するリマインダーメール

---

## ⚙️ セットアップ手順

### ステップ 1: Node.js 環境確認

```bash
# Node.js インストール確認
node --version
# 出力例: v16.14.0 以上

# npm インストール確認
npm --version
# 出力例: v8.0.0 以上
```

**必要なバージョン:** Node.js 14 以上

---

### ステップ 2: 依存パッケージインストール

```bash
# リポジトリルートから実行
cd /path/to/FLY77STAR

# nodemailer と dotenv をインストール
npm install nodemailer dotenv
```

**package.json への追記:**
```json
{
  "dependencies": {
    "nodemailer": "^6.9.0",
    "dotenv": "^16.0.0"
  }
}
```

---

### ステップ 3: Gmail App Password 取得

Gmail の SMTP 認証には **App Password** が必要です（2FA 有効な場合）

#### 取得手順:

1. **Google Account にログイン**
   - https://myaccount.google.com

2. **Security settings を開く**
   - 左メニュー → 「Security」を選択

3. **2-Step Verification を有効化**（未設定の場合）
   - 「2-Step Verification」 → 「Get Started」
   - 画面に従って設定

4. **App passwords を生成**
   - 「App passwords」をクリック
   - Select app: **Mail** を選択
   - Select device: **Windows PC / Mac / Linux** を選択
   - 「Generate」をクリック
   - 表示された 16 文字のパスワードをコピー

---

### ステップ 4: .env ファイル設定

リポジトリルートに `.env` ファイルを作成します：

```bash
# .env テンプレート
cat > .env << 'EOF'
# Gmail 設定
GMAIL_ADDRESS=fly77star.official@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
YU_EMAIL=fly77star.official@gmail.com

# ベース URL（チェックシートへのリンク）
BASE_URL=https://github.com/flymcu1982/FLY77STAR/tree/claude/fly77star-obsidian-structure-a010jj/Edit

# タイムゾーン
TZ=Asia/Tokyo
EOF
```

**重要:** `.env` は Git に含めない（.gitignore に既に追加済み）

```bash
# 確認
cat .gitignore | grep "^\.env$"
# 出力: .env
```

---

### ステップ 5: スクリプト実行権限設定

```bash
# 実行権限を付与
chmod +x scripts/daily_reminder.js
chmod +x scripts/setup_cron.sh
```

---

### ステップ 6: 手動テスト実行

```bash
# リポジトリルートから実行
cd /path/to/FLY77STAR

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
# Message ID: <...@gmail.com>
```

**テスト結果確認:**
- YU のメールボックス（fly77star.official@gmail.com）に メール到着確認
- HTML 形式のメールが正しく表示されているか確認

---

## 🕐 Cron ジョブ設定（自動実行）

### 方法 1: 自動セットアップスクリプト（推奨）

```bash
# セットアップスクリプト実行
bash scripts/setup_cron.sh

# 出力例:
# ✅ Node.js インストール確認済み
# ✅ nodemailer インストール確認済み
# ✅ .env ファイル確認済み
# ✅ Cron ジョブが登録されました
# 
# Cron コマンド:
#   55 08 * * * cd /path/to/FLY77STAR && /usr/bin/node scripts/daily_reminder.js >> logs/daily_reminder_cron.log 2>&1
```

### 方法 2: 手動設定

```bash
# Cron 編集モード開く
crontab -e

# 以下の行を追加（08:55 に毎日実行）
55 08 * * * cd /path/to/FLY77STAR && /usr/bin/node scripts/daily_reminder.js >> logs/daily_reminder_cron.log 2>&1

# Ctrl+X → Y → Enter で保存
```

### Cron 設定確認

```bash
# 登録済みの Cron ジョブ一覧
crontab -l

# 出力例:
# 55 08 * * * cd /path/to/FLY77STAR && /usr/bin/node scripts/daily_reminder.js >> logs/daily_reminder_cron.log 2>&1
```

---

## 📊 ログ管理

### ログファイル位置

```
/path/to/FLY77STAR/logs/
├── daily_reminder.log          (メール送信ログ)
└── daily_reminder_cron.log     (Cron 実行ログ)
```

### ログ内容確認

```bash
# 最新 10 行表示
tail -10 logs/daily_reminder.log

# 出力例:
# [2026-07-19T00:55:00.123Z] SUCCESS - <message_id@gmail.com>
# [2026-07-19T00:55:00.456Z] SUCCESS - <message_id@gmail.com>

# 全ログ表示
cat logs/daily_reminder.log

# エラーログのみ表示
grep "FAILED" logs/daily_reminder.log
```

### ログローテーション（オプション）

```bash
# 7 日以上前のログを削除
find logs/ -name "*.log" -mtime +7 -delete
```

---

## 🔍 トラブルシューティング

### メールが送信されない

**1. .env ファイル確認**
```bash
cat .env

# 確認項目:
# - GMAIL_ADDRESS は正しい Gmail アドレスか？
# - GMAIL_APP_PASSWORD は 16 文字のパスワードか？
# - スペースが含まれているか？
```

**2. App Password 確認**
```bash
# Gmail Account Security で App Password が有効か確認
# https://myaccount.google.com/apppasswords
```

**3. Gmail IMAP / POP 有効化確認**
```bash
# Gmail の IMAP 設定が有効か確認
# Settings → Forwarding and POP/IMAP
```

### Cron ジョブが実行されない

**1. Cron 登録確認**
```bash
crontab -l | grep "daily_reminder"

# 出力がなければ Cron が登録されていない
```

**2. Cron ログ確認（Linux/Mac）**
```bash
# システム Cron ログ確認
log show --predicate 'process == "cron"' --level debug

# または
sudo journalctl -u cron.service -f
```

**3. Node.js パス確認**
```bash
# node コマンドのフルパス確認
which node
# 出力例: /usr/bin/node

# Cron コマンドで正しいパスを使用しているか確認
crontab -l
```

### メール形式が崩れている

**1. HTML メール対応確認**
```bash
# Gmail の設定を確認
# Settings → Display density を「Comfortable」に設定
```

**2. ブラウザ確認**
```bash
# 別のメールクライアント（Outlook など）で確認
# ブラウザキャッシュをクリア
```

---

## 📝 メール内容カスタマイズ

### メール本文変更

ファイル: `scripts/daily_reminder.js`

```javascript
// generateEmailBody() 関数内の HTML を編集

// 例: タイトル変更
<h1>本日のチェックシート準備完了</h1>
// ↓
<h1>【朝 09:00 開始】本日の業務チェックシート</h1>

// 例: リンク URL 変更
href="${baseUrl}/DAILY_MAIL_REVIEW_CHECKLIST.md"
// ↓
href="https://your-custom-url/checklist"
```

変更後は Cron を再度実行して確認してください：

```bash
node scripts/daily_reminder.js
```

---

## 🛑 Cron ジョブ削除方法

```bash
# Cron 編集モード
crontab -e

# daily_reminder.js の行を削除
# Ctrl+X → Y → Enter で保存

# 確認
crontab -l
```

---

## 📅 実行スケジュール

| 時刻 | 内容 | 実行者 |
|------|------|--------|
| 08:55 | チェックシート準備メール送信 | Claude Code（自動） |
| 09:00-09:30 | Gmail メール確認・分類 | YU |
| 09:30-10:00 | SNS DM 確認・分類 | YU |
| 15:00 | 返信下書き自動生成 | Claude Code |
| 18:00 | 日報作成・報告 | Claude Code |

---

## 🚀 本番環境への展開

### Linux / Mac サーバー

```bash
# リポジトリをクローン
git clone <repository-url>
cd FLY77STAR

# セットアップ実行
bash scripts/setup_cron.sh

# ログ確認
tail -f logs/daily_reminder_cron.log
```

### Windows Server

Windows では crontab ではなく **Task Scheduler** を使用：

```powershell
# PowerShell（管理者権限）で実行

# タスク作成
$taskName = "FLY77STAR Daily Reminder"
$scriptPath = "C:\path\to\FLY77STAR\scripts\daily_reminder.js"
$trigger = New-ScheduledTaskTrigger -Daily -At 08:55
$action = New-ScheduledTaskAction -Execute "C:\Program Files\nodejs\node.exe" -Argument $scriptPath
Register-ScheduledTask -TaskName $taskName -Trigger $trigger -Action $action -RunLevel Highest

# 確認
Get-ScheduledTask -TaskName $taskName
```

---

## ✅ セットアップチェックリスト

- [ ] Node.js 14+ インストール確認
- [ ] nodemailer パッケージインストール確認
- [ ] Gmail App Password 取得完了
- [ ] .env ファイル作成・設定完了
- [ ] スクリプト実行権限設定完了
- [ ] 手動テスト実行成功
- [ ] メール到着確認（YU のメールボックス）
- [ ] Cron ジョブ登録完了
- [ ] ログファイル作成確認

---

**セットアップ完了後は、毎朝 08:55 に自動的にメールが送信されます。** ✅

ご不明な点があれば、お気軽にお声がけください。
