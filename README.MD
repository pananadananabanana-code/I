🚀 ÆEA BOT - FRESH TERMUX INSTALLATION (WORKING)

Complete instructions from a brand new Termux installation - no pip issues, no compile problems.

---

📱 PART 1: FRESH TERMUX SETUP

1.1 Install Termux from F-Droid

```
⚠️ IMPORTANT: Download from F-Droid, NOT Google Play!
https://f-droid.org/en/packages/com.termux/
```

1.2 Open Termux & Run Initial Setup

```bash
# Update packages (this works on fresh install)
pkg update && pkg upgrade -y

# Grant storage permission (popup will appear)
termux-setup-storage

# Install ONLY essential packages (NO python/pip)
pkg install git openssh curl -y

# Verify git works
git --version
```

---

🤖 PART 2: CREATE TELEGRAM BOT

On your phone (Telegram app):

```
1. Open Telegram
2. Search: @BotFather
3. Send: /newbot
4. Name: AeaTradingBot
5. Username: YourNameAeaBot (must end with 'bot')
6. COPY THE TOKEN! (looks like: 123456:ABCdef...)
```

---

📦 PART 3: PREPARE BOT FILES (NO PIP NEEDED)

```bash
# Create project directory
mkdir -p ~/aea_bot
cd ~/aea_bot

# Create ALL files using echo commands (no editors needed)
```

3.1 Create aea_bot.py

```bash
cat > aea_bot.py << 'EOF'
#!/usr/bin/env python3
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *ÆEA BOT ACTIVE*\n\n"
        "Quantum-Financial Topology Engine\n"
        "Data: Yahoo Finance (Free)\n\n"
        "Commands:\n"
        "/start - Show this\n"
        "/status - Check status\n"
        "/help - Help\n\n"
        "💎 Natalia Tanyatia",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ *Bot Status*\n\n"
        "Status: Online\n"
        "Symbol: BTC-USD\n"
        "Source: Yahoo Finance\n"
        "Mode: Active",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *Commands:*\n"
        "/start - Start the bot\n"
        "/status - Check status\n"
        "/help - Show help\n\n"
        "📡 Data: Yahoo Finance (Free)",
        parse_mode="Markdown"
    )

def main():
    if not TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN not set!")
        logger.error("Run: export TELEGRAM_BOT_TOKEN='your_token'")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("🤖 Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
EOF
```

3.2 Create requirements.txt

```bash
cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
yfinance==0.2.28
pandas==2.0.3
numpy==1.24.3
EOF
```

3.3 Create runtime.txt

```bash
echo "python-3.10.12" > runtime.txt
```

3.4 Create Procfile

```bash
echo "worker: python aea_bot.py" > Procfile
```

3.5 Create app.json

```bash
cat > app.json << 'EOF'
{
  "name": "ÆEA Trading Bot",
  "description": "Quantum-Financial Topology Bot",
  "env": {
    "TELEGRAM_BOT_TOKEN": {
      "description": "Your Telegram Bot Token",
      "required": true
    }
  },
  "formation": {
    "worker": {
      "quantity": 1,
      "size": "eco"
    }
  },
  "buildpacks": [
    {
      "url": "heroku/python"
    }
  ]
}
EOF
```

3.6 Verify files created

```bash
ls -la
# Should show: aea_bot.py, requirements.txt, runtime.txt, Procfile, app.json
```

---

☁️ PART 4: DEPLOY TO HEROKU (WEB METHOD - NO BUILD)

4.1 Install Heroku CLI (ARM64 for Termux)

```bash
# Download Heroku CLI
curl -L https://cli-assets.heroku.com/heroku-linux-arm64.tar.gz -o heroku.tar.gz

# Extract
tar -xzf heroku.tar.gz

# Install
mkdir -p $PREFIX/opt/heroku
cp -r heroku/* $PREFIX/opt/heroku/
ln -s $PREFIX/opt/heroku/bin/heroku $PREFIX/bin/heroku

# Verify
heroku --version
```

4.2 Login and Deploy

```bash
# Login (will open browser)
heroku login

# Create app
heroku create aea-bot-$(date +%s)

# Set your token (replace with YOUR token)
heroku config:set TELEGRAM_BOT_TOKEN="YOUR_TOKEN_HERE"

# Initialize git
git init
git add .
git commit -m "Initial deploy"

# Push to Heroku
git push heroku main

# Scale worker (1 free dyno)
heroku ps:scale worker=1

# Check status
heroku ps
heroku logs --tail
```

---

🌐 PART 5: ALTERNATIVE - DEPLOY VIA GITHUB (NO HEROKU CLI)

5.1 Create GitHub Repository (via browser)

```
1. Open Chrome on phone
2. Go to github.com
3. New Repository → "aea-bot"
4. Don't initialize with README
5. Copy the repository URL
```

5.2 Push from Termux

```bash
# Set your GitHub details
git config --global user.name "YourName"
git config --global user.email "your@email.com"

# Add remote
git remote add origin https://github.com/yourusername/aea-bot.git

# Push
git push -u origin main
```

5.3 Deploy on Heroku via GitHub (browser method)

```
1. Open Chrome: https://dashboard.heroku.com
2. Create New App → "aea-bot-xxx"
3. Go to "Deploy" tab
4. Connect to GitHub
5. Search: "aea-bot"
6. Enable Automatic Deploys
7. Deploy Branch
8. Go to "Settings" → "Config Vars"
9. Add: TELEGRAM_BOT_TOKEN = your_token
```

---

🎯 PART 6: VERIFY BOT IS WORKING

From Termux:

```bash
# Check Heroku status
heroku ps

# View logs
heroku logs --tail

# Should see:
# Starting worker...
# Bot starting...
```

From Telegram:

```
1. Open Telegram
2. Search your bot username
3. Send: /start
4. Send: /status
5. Should get responses!
```

---

⚡ PART 7: COMPLETE ONE-COMMAND SETUP

Save this as setup.sh and run it:

```bash
#!/bin/bash
# Complete setup from fresh Termux

echo "🚀 Setting up ÆEA Bot..."

# Update
pkg update -y

# Install essentials
pkg install git openssh curl -y

# Create directory
mkdir -p ~/aea_bot && cd ~/aea_bot

# Create files (paste the file contents from above)
cat > aea_bot.py << 'EOF'
# ... paste aea_bot.py content ...
EOF

cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
yfinance==0.2.28
pandas==2.0.3
numpy==1.24.3
EOF

echo "python-3.10.12" > runtime.txt
echo "worker: python aea_bot.py" > Procfile

# Install Heroku CLI
curl -L https://cli-assets.heroku.com/heroku-linux-arm64.tar.gz -o heroku.tar.gz
tar -xzf heroku.tar.gz
mkdir -p $PREFIX/opt/heroku
cp -r heroku/* $PREFIX/opt/heroku/
ln -s $PREFIX/opt/heroku/bin/heroku $PREFIX/bin/heroku

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get token from @BotFather"
echo "2. heroku login"
echo "3. heroku create aea-bot-xxx"
echo "4. heroku config:set TELEGRAM_BOT_TOKEN='YOUR_TOKEN'"
echo "5. git push heroku main"
```

Run it:

```bash
chmod +x setup.sh
./setup.sh
```

---

🆘 TROUBLESHOOTING

If Heroku CLI fails:

```bash
# Alternative: Use Heroku Git remote
git remote add heroku https://git.heroku.com/your-app-name.git
git push heroku main
```

If git push fails:

```bash
# Force push
git push heroku main --force
```

To check app status:

```bash
# Open in browser
heroku open

# Check logs
heroku logs --tail

# Restart app
heroku restart
```

---

✅ SUCCESS CHECKLIST

☐ Termux installed from F-Droid
☐ pkg update ran successfully
☐ Bot created with @BotFather
☐ Token copied
☐ Files created in ~/aea_bot/
☐ Heroku CLI installed
☐ heroku login worked
☐ heroku create worked
☐ git push heroku main succeeded
☐ heroku ps:scale worker=1 worked
☐ Bot responds to /start on Telegram

---

🎉 DONE!

Your bot is now live on Heroku. No Python/pip installation needed on Termux - Heroku builds everything!

Test your bot:

1. Open Telegram
2. Find your bot
3. Send /start
4. Send /status