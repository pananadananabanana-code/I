🚀 ÆEA BOT - FRESH TERMUX INSTALLATION (WORKING)

Complete instructions from a brand new Termux installation - using your existing files.

📱 PART 1: FRESH TERMUX SETUP

1.1 Install Termux

```
⚠️ DOWNLOAD FROM F-DROID ONLY!
https://f-droid.org/en/packages/com.termux/

DO NOT use Google Play version!
```

1.2 Open Termux & Initial Setup

```bash
# Update packages
pkg update && pkg upgrade -y

# Grant storage permission (popup will appear)
termux-setup-storage

# Install ONLY git (no python/pip needed)
pkg install git openssh curl -y

# Verify git
git --version
```

🤖 PART 2: CREATE TELEGRAM BOT

On your phone (Telegram app):

```
1. Open Telegram
2. Search: @BotFather
3. Send: /newbot
4. Name: AeaTradingBot
5. Username: YourNameAeaBot (must end with 'bot')
6. COPY THE TOKEN! 
   Example: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

📂 PART 3: GET YOUR FILES

If files are in internal storage:

```bash
# Copy from internal storage to Termux
cp /storage/emulated/0/Download/aea_bot.py ~/
cp /storage/emulated/0/Download/requirements.txt ~/
cp /storage/emulated/0/Download/runtime.txt ~/
cp /storage/emulated/0/Download/Procfile ~/

# Or if in a folder:
cp -r /storage/emulated/0/aea_bot/* ~/aea_bot/
```

If files are in Termux already:

```bash
cd ~/aea_bot
ls -la
# Should show: aea_bot.py, requirements.txt, runtime.txt, Procfile
```

If files are on GitHub:

```bash
git clone https://github.com/yourusername/aea-bot.git
cd aea-bot
```

☁️ PART 4: CREATE HEROKU APP (VIA BROWSER)

On your phone's browser:

```
1. Open Chrome/Firefox
2. Go to: https://dashboard.heroku.com
3. Login/Create account
4. Click "New" → "Create New App"
5. App name: aea-bot-xxxx (use unique name)
6. Region: United States
7. Click "Create App"
8. COPY YOUR APP NAME! (e.g., aea-bot-1234)
```

🚀 PART 5: DEPLOY FROM TERMUX

5.1 Initialize Git (if not done)

```bash
cd ~/aea_bot

# Initialize git
git init
git add .
git commit -m "Initial commit"
```

5.2 Add Heroku Remote

```bash
# Replace YOUR-APP-NAME with what you created
git remote add heroku https://git.heroku.com/YOUR-APP-NAME.git

# Example:
# git remote add heroku https://git.heroku.com/aea-bot-1234.git
```

5.3 Deploy to Heroku

```bash
# Push to Heroku
git push heroku main

# If prompted for password, use Heroku API key:
# Get it from: https://dashboard.heroku.com/account
# Click "Reveal" under API Key
```

5.4 Set Environment Variable

```bash
# Using Heroku CLI (if installed) OR do via browser

# Option A: Via Heroku Dashboard (EASIEST)
# Go to: https://dashboard.heroku.com/apps/YOUR-APP-NAME
# Click "Settings" → "Config Vars" → "Reveal Config Vars"
# Add: TELEGRAM_BOT_TOKEN = YOUR_TOKEN

# Option B: Via Heroku CLI (if you have it)
heroku config:set TELEGRAM_BOT_TOKEN="YOUR_TOKEN" -a YOUR-APP-NAME
```

5.5 Scale Worker (via Heroku Dashboard)

```
1. Go to: https://dashboard.heroku.com/apps/YOUR-APP-NAME
2. Click "Resources" tab
3. Find "worker" dyno
4. Click the pencil/edit icon
5. Turn it ON
6. Confirm
```

🎯 QUICK DEPLOYMENT COMMANDS

```bash
# Complete deployment in 3 commands:

# 1. Deploy
git push heroku main

# 2. Set token (via browser OR):
heroku config:set TELEGRAM_BOT_TOKEN="YOUR_TOKEN" -a YOUR-APP-NAME

# 3. Scale worker (via browser OR):
heroku ps:scale worker=1 -a YOUR-APP-NAME

# 4. Check status
heroku ps -a YOUR-APP-NAME
```

✅ PART 6: VERIFY DEPLOYMENT

Check Heroku Status (via browser):

```
1. Go to: https://dashboard.heroku.com/apps/YOUR-APP-NAME
2. Check "Resources" tab - worker should show "ON"
3. Check "More" → "View logs" for any errors
```

Test on Telegram:

```
1. Open Telegram
2. Search your bot
3. Send: /start
4. Send: /status
5. Should get responses!
```

🆘 TROUBLESHOOTING

If git push asks for password:

```
1. Go to: https://dashboard.heroku.com/account
2. Scroll to "API Key"
3. Click "Reveal"
4. Copy the key
5. Use as password when pushing
```

If "worker" not showing in Resources:

```
1. Check Procfile exists: cat Procfile
2. Should show: worker: python aea_bot.py
3. If missing, create it: echo "worker: python aea_bot.py" > Procfile
```

If app crashes:

```
1. Go to Heroku Dashboard
2. Click "More" → "View logs"
3. Look for error messages
4. Common fix: check TELEGRAM_BOT_TOKEN is set correctly
```

📋 COMPLETE SUCCESS CHECKLIST

☐ Termux installed from F-Droid
☐ pkg update ran successfully
☐ pkg install git worked
☐ Bot created with @BotFather
☐ Token copied
☐ Files exist in ~/aea_bot/
☐ Heroku app created in browser
☐ git remote add heroku worked
☐ git push heroku main succeeded
☐ TELEGRAM_BOT_TOKEN set in Config Vars
☐ Worker dyno turned ON
☐ Bot responds on Telegram

🎉 DONE!

Your bot is now live!

Test it:

1. Open Telegram
2. Search your bot
3. Send /start
4. Send /status

No Python/pip installation needed on Termux! 🚀

---

☁️ Google Cloud Shell Method (Manual Session)

Part 1: Access Google Cloud Shell

1. Open Chrome/Firefox on your phone
2. Go to: https://shell.cloud.google.com
3. Sign in with your Google account
4. A terminal will open in your browser - this is like Termux but in the cloud!

Part 2: Initial Setup in Cloud Shell

# Update packages (Cloud Shell comes with Python pre-installed!)
sudo apt update && sudo apt upgrade -y

# Install git if not present
sudo apt install git -y

# Check Python version (should be 3.7+)
python3 --version

# Install pip if needed
sudo apt install python3-pip -y
Part 3: Get Your Bot Files

Option A: Upload from your phone

# Cloud Shell has a "Upload" button (top-right)
# Click it and upload:
# - aea_bot.py
# - requirements.txt
# - (runtime.txt not needed)

# Or use the file browser in Cloud Shell
Option B: Clone from GitHub

git clone https://github.com/yourusername/aea-bot.git
cd aea-bot
Option C: Download from URL

# If files are hosted somewhere
wget https://your-file-host.com/aea_bot.py
wget https://your-file-host.com/requirements.txt
Part 4: Install Dependencies

# Install Python packages
pip3 install -r requirements.txt

# Or install manually if no requirements.txt:
pip3 install python-telegram-bot requests
Part 5: Run Your Bot

# Set your bot token (replace with your actual token)
export TELEGRAM_BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"

# Run the bot
python3 aea_bot.py
The bot will now run! Keep the Cloud Shell tab open to keep it running.

Part 6: Test Your Bot

1. Open Telegram on your phone
2. Search for your bot
3. Send /start - should get a response!

🔄 Keeping It Running

Important Limitations:

· Cloud Shell sessions timeout after 20-30 minutes of inactivity
· If you close the browser tab, the bot stops
· You'll need to restart every time you connect

To keep it running longer:

# Use nohup to run in background
nohup python3 aea_bot.py > bot.log 2>&1 &

# Check it's running
ps aux | grep python

# View logs
tail -f bot.log
To restart after disconnection:

1. Reopen Cloud Shell: https://shell.cloud.google.com
2. Navigate to your folder: cd ~/aea-bot (or wherever files are)
3. Set token: export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
4. Run: python3 aea_bot.py

📋 Comparison: Cloud Shell vs Termux

Feature Termux (Phone) Cloud Shell (Browser)
Access Phone only Any device with browser
Storage Limited phone storage 5GB free
Power Phone battery/CPU Google's servers
Internet Uses phone data Uses Google's bandwidth
Session Stays until you close Times out after inactivity
Python Must install Pre-installed

🚀 Pro Tips for Cloud Shell

1. Bookmark https://shell.cloud.google.com on your phone's home screen
2. Use tmux to keep session alive longer:

# Install tmux
sudo apt install tmux -y

# Start a new session
tmux new -s bot

# Run your bot inside tmux
export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
python3 aea_bot.py

# Detach with Ctrl+B, then D
# Reattach later: tmux attach -t bot
3. Create a startup script (run_bot.sh):

#!/bin/bash
echo "Starting AEA Bot..."
export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
cd ~/aea-bot
python3 aea_bot.py
Make it executable:

chmod +x run_bot.sh
./run_bot.sh
4. Save your token in a file (but be careful!):

echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env
source .env
python3 aea_bot.py
⚠️ Important Notes

· Free tier: Cloud Shell gives you 5GB of free storage and 50 hours per week
· File persistence: Your files stay saved even after session ends
· Python packages: Need to reinstall each session or use a requirements.txt
· Token security: Don't share your token or commit it to GitHub

🎯 Quick Start Command Summary

# One-time setup
cd ~
git clone https://github.com/yourusername/aea-bot.git
cd aea-bot
pip3 install -r requirements.txt

# Every session
export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
python3 aea_bot.py

# That's it! Bot runs until you close the tab

---

This is exactly like using Termux, but with the advantage of Google's servers instead of your phone's battery! 🚀