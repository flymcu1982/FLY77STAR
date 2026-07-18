#!/bin/bash

# setup_cron.sh
# 毎朝 08:55 にメール送信スクリプトを実行する Cron ジョブをセットアップ

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SCRIPT_PATH="$SCRIPT_DIR/daily_reminder.js"

echo "=========================================="
echo "Daily Reminder Cron Setup"
echo "=========================================="
echo ""
echo "RepositoryRoot: $REPO_ROOT"
echo "ScriptPath: $SCRIPT_PATH"
echo ""

# Node.js インストール確認
if ! command -v node &> /dev/null; then
    echo "❌ エラー: Node.js がインストールされていません"
    echo "Node.js 14+ をインストールしてください"
    exit 1
fi

echo "✅ Node.js インストール確認済み"
echo "   Version: $(node --version)"
echo ""

# nodemailer インストール確認
if ! npm list nodemailer &> /dev/null; then
    echo "⚠️  nodemailer がインストールされていません"
    echo "📦 npm install nodemailer を実行してください"
    exit 1
fi

echo "✅ nodemailer インストール確認済み"
echo ""

# .env ファイル確認
if [ ! -f "$REPO_ROOT/.env" ]; then
    echo "⚠️  警告: .env ファイルが見つかりません"
    echo "以下の設定を .env に追加してください:"
    echo ""
    echo "GMAIL_ADDRESS=fly77star.official@gmail.com"
    echo "GMAIL_APP_PASSWORD=your_app_password_here"
    echo "YU_EMAIL=fly77star.official@gmail.com"
    echo "BASE_URL=https://github.com/flymcu1982/FLY77STAR/tree/main/Edit"
    echo ""
    echo "Google App Password 取得方法:"
    echo "1. Google Account にログイン"
    echo "2. Security settings を開く"
    echo "3. 2-Step Verification を有効化"
    echo "4. App passwords を生成"
    echo ""
    exit 1
else
    echo "✅ .env ファイル確認済み"
fi

echo ""
echo "=========================================="
echo "Cron Job セットアップ"
echo "=========================================="
echo ""

# Cron ジョブコマンド
CRON_COMMAND="55 08 * * * cd $REPO_ROOT && /usr/bin/node $SCRIPT_PATH >> $REPO_ROOT/logs/daily_reminder_cron.log 2>&1"

# 既存の Cron ジョブを確認
echo "現在の Cron ジョブを確認中..."
EXISTING_CRON=$(crontab -l 2>/dev/null | grep "daily_reminder.js" || true)

if [ -n "$EXISTING_CRON" ]; then
    echo "既存の Cron ジョブが見つかりました:"
    echo "  $EXISTING_CRON"
    echo ""
    read -p "上書きしますか？ (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cron ジョブのセットアップをキャンセルしました"
        exit 0
    fi

    # 既存ジョブを削除
    crontab -l | grep -v "daily_reminder.js" | crontab -
fi

# 新しい Cron ジョブを追加
(crontab -l 2>/dev/null; echo "$CRON_COMMAND") | crontab -

echo "✅ Cron ジョブが登録されました"
echo ""
echo "Cron コマンド:"
echo "  $CRON_COMMAND"
echo ""
echo "実行タイミング: 毎日 08:55"
echo "ログファイル: $REPO_ROOT/logs/daily_reminder_cron.log"
echo ""

# ログディレクトリ作成
mkdir -p "$REPO_ROOT/logs"

echo "=========================================="
echo "セットアップ完了！"
echo "=========================================="
echo ""
echo "📝 手動テスト方法:"
echo "  cd $REPO_ROOT"
echo "  node scripts/daily_reminder.js"
echo ""
echo "📋 Cron ジョブ確認方法:"
echo "  crontab -l"
echo ""
echo "❌ Cron ジョブ削除方法:"
echo "  crontab -e"
echo "  (daily_reminder.js の行を削除)"
echo ""
