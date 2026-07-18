#!/usr/bin/env node

/**
 * daily_reminder.js
 * 毎朝 08:55 にメール送信スクリプト
 *
 * 宛先: fly77star.official@gmail.com (YU)
 * 件名: 「本日のチェックシート準備完了」
 * 内容: 朝のチェックシート開始準備の通知
 *
 * 実行方法: node scripts/daily_reminder.js
 * スケジュール: cron ジョブで毎日 08:55 実行
 */

const nodemailer = require('nodemailer');
require('dotenv').config();
const path = require('path');

// ANSI カラー出力
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
  cyan: '\x1b[36m',
  blue: '\x1b[34m'
};

/**
 * Gmail メール送信
 */
async function sendDailyReminder() {
  try {
    console.log(`${colors.cyan}=== Daily Reminder Email Sender ===${colors.reset}`);
    console.log(`${colors.cyan}実行時刻: ${new Date().toLocaleString('ja-JP')}${colors.reset}\n`);

    // Gmail SMTP トランスポーター設定
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_ADDRESS || 'fly77star.official@gmail.com',
        pass: process.env.GMAIL_APP_PASSWORD || process.env.GMAIL_PASSWORD,
      },
    });

    // メール内容設定
    const mailOptions = {
      from: 'Claude Code <fly77star.official@gmail.com>',
      to: process.env.YU_EMAIL || 'fly77star.official@gmail.com',
      subject: '【朝のチェックシート準備完了】本日の運用開始 08:55',
      html: generateEmailBody(),
      replyTo: 'fly77star.official@gmail.com',
    };

    // メール送信
    console.log(`${colors.yellow}📧 メール送信中...${colors.reset}`);
    console.log(`To: ${mailOptions.to}`);
    console.log(`Subject: ${mailOptions.subject}\n`);

    const info = await transporter.sendMail(mailOptions);

    console.log(`${colors.green}✅ メール送信成功！${colors.reset}`);
    console.log(`Message ID: ${info.messageId}`);
    console.log(`Response: ${info.response}\n`);

    // ログファイルに記録
    logSendResult(true, info);

    return true;
  } catch (error) {
    console.error(`${colors.red}❌ エラー発生: ${error.message}${colors.reset}\n`);
    logSendResult(false, error);
    return false;
  }
}

/**
 * メール本文生成（HTML形式）
 */
function generateEmailBody() {
  const today = new Date().toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    weekday: 'long'
  });

  const baseUrl = process.env.BASE_URL || 'https://github.com/flymcu1982/FLY77STAR/tree/claude/fly77star-obsidian-structure-a010jj/Edit';

  return `
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 20px;
      margin: 0;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background: white;
      border-radius: 10px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      overflow: hidden;
    }
    .header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 30px 20px;
      text-align: center;
    }
    .header h1 {
      margin: 0;
      font-size: 24px;
      font-weight: 600;
    }
    .header p {
      margin: 10px 0 0 0;
      font-size: 14px;
      opacity: 0.9;
    }
    .content {
      padding: 30px 20px;
    }
    .greeting {
      font-size: 18px;
      color: #333;
      margin-bottom: 20px;
      line-height: 1.6;
    }
    .checklist-section {
      margin: 25px 0;
    }
    .checklist-item {
      background: #f5f5f5;
      border-left: 4px solid #667eea;
      padding: 15px;
      margin: 12px 0;
      border-radius: 4px;
    }
    .checklist-item-title {
      font-weight: 600;
      color: #333;
      margin-bottom: 8px;
    }
    .checklist-item-time {
      font-size: 13px;
      color: #666;
      margin-bottom: 8px;
    }
    .checklist-link {
      display: inline-block;
      background: #667eea;
      color: white;
      padding: 8px 12px;
      border-radius: 4px;
      text-decoration: none;
      font-size: 13px;
      font-weight: 600;
      margin-top: 8px;
      transition: background 0.3s;
    }
    .checklist-link:hover {
      background: #764ba2;
    }
    .schedule-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin: 20px 0;
    }
    .schedule-item {
      background: #f0f4ff;
      padding: 12px;
      border-radius: 4px;
      text-align: center;
      border: 1px solid #dde3f0;
    }
    .schedule-time {
      font-weight: 600;
      color: #667eea;
      font-size: 16px;
    }
    .schedule-task {
      font-size: 12px;
      color: #666;
      margin-top: 4px;
    }
    .footer {
      background: #f9f9f9;
      padding: 20px;
      text-align: center;
      border-top: 1px solid #eee;
      font-size: 12px;
      color: #999;
    }
    .signature {
      color: #667eea;
      font-weight: 600;
      margin-top: 20px;
    }
    .emoji {
      font-size: 24px;
    }
    .status-badge {
      display: inline-block;
      background: #10b981;
      color: white;
      padding: 4px 8px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      margin-left: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="emoji">🌅</div>
      <h1>本日のチェックシート準備完了</h1>
      <p>${today}</p>
    </div>

    <div class="content">
      <div class="greeting">
        おはようございます！<br>
        Claude Code（AI社員）です。<br><br>
        本日のチェックシートの準備ができました。<br>
        <strong>08:55</strong> から、下記のファイルを開いて実行をお願いします。
      </div>

      <div class="schedule-grid">
        <div class="schedule-item">
          <div class="schedule-time">09:00-09:30</div>
          <div class="schedule-task">Gmail確認</div>
        </div>
        <div class="schedule-item">
          <div class="schedule-time">09:30-10:00</div>
          <div class="schedule-task">SNS DM確認</div>
        </div>
        <div class="schedule-item">
          <div class="schedule-time">15:00</div>
          <div class="schedule-task">返信下書き生成</div>
        </div>
        <div class="schedule-item">
          <div class="schedule-time">18:00</div>
          <div class="schedule-task">日報作成</div>
        </div>
      </div>

      <div class="checklist-section">
        <h3 style="margin-top: 0; color: #333;">📋 本日のチェックシート</h3>

        <div class="checklist-item">
          <div class="checklist-item-title">📧 Gmail メール確認</div>
          <div class="checklist-item-time">実行時刻: 09:00-09:30（想定30分）</div>
          <p style="margin: 8px 0; font-size: 13px; color: #666;">
            fly77star.official@gmail.com にログインして、<br>
            受信トレイのメール全件を確認・分類してください。
          </p>
          <a href="${baseUrl}/DAILY_MAIL_REVIEW_CHECKLIST.md" class="checklist-link">
            📋 チェックシートを開く
          </a>
        </div>

        <div class="checklist-item">
          <div class="checklist-item-title">📱 SNS DM 確認</div>
          <div class="checklist-item-time">実行時刻: 09:30-10:00（想定30分）</div>
          <p style="margin: 8px 0; font-size: 13px; color: #666;">
            TikTok / Instagram / X のメッセージを確認して、<br>
            新着 DM 全件を分類・集計してください。
          </p>
          <a href="${baseUrl}/SNS_DM_DAILY_CHECKLIST.md" class="checklist-link">
            📋 チェックシートを開く
          </a>
        </div>
      </div>

      <div style="background: #fffbea; border-left: 4px solid #fbbf24; padding: 15px; margin: 20px 0; border-radius: 4px;">
        <div style="font-weight: 600; color: #92400e; margin-bottom: 8px;">⚠️ 注意</div>
        <ul style="margin: 0; padding-left: 20px; color: #78350f; font-size: 13px;">
          <li>メール件数が多い場合は、URGENT → HIGH → MEDIUM の順から処理してください</li>
          <li>時間に制限がある場合は、URGENT + HIGH のみ記入し、後で MEDIUM 以下を追記しても OK です</li>
          <li>URGENT メールが到着した場合は、即座に Claude Code に通知してください</li>
        </ul>
      </div>

      <p style="color: #666; font-size: 13px; line-height: 1.6; margin: 20px 0;">
        ご不明な点や質問があれば、<br>
        いつでもお気軽にお声がけください。<br><br>
        本日も宜しくお願いします！🚀
      </p>

      <div class="signature">
        Claude Code（AI社員）<br>
        FLY77STAR Studio CTO
      </div>
    </div>

    <div class="footer">
      <p style="margin: 0;">このメールは毎朝 08:55 に自動送信されます</p>
      <p style="margin: 8px 0 0 0; color: #ccc;">
        送信元: Claude Code Automated System<br>
        © 2026 FLY77STAR Studio. All rights reserved.
      </p>
    </div>
  </div>
</body>
</html>
  `;
}

/**
 * 送信結果をログファイルに記録
 */
function logSendResult(success, info) {
  const fs = require('fs');
  const timestamp = new Date().toISOString();
  const logsDir = path.join(__dirname, '..', 'logs');

  // ログディレクトリ作成
  if (!fs.existsSync(logsDir)) {
    fs.mkdirSync(logsDir, { recursive: true });
  }

  const logFile = path.join(logsDir, 'daily_reminder.log');
  const logEntry = `[${timestamp}] ${success ? 'SUCCESS' : 'FAILED'} - ${success ? info.messageId : info.message}\n`;

  fs.appendFileSync(logFile, logEntry);
}

/**
 * メイン実行
 */
if (require.main === module) {
  sendDailyReminder().then(success => {
    process.exit(success ? 0 : 1);
  }).catch(error => {
    console.error(`${colors.red}Fatal error: ${error.message}${colors.reset}`);
    process.exit(1);
  });
}

module.exports = { sendDailyReminder };
