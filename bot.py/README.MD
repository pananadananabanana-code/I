🚀 ÆEA BOT - FRESH TERMUX INSTALLATION (WORKING)

Complete instructions from a brand new Termux installation - using your existing files.

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

🎉 DONE!

Your bot is now live!

Test it:

1. Open Telegram
2. Search your bot
3. Send /start
4. Send /status

No Python/pip installation needed on Termux! 🚀