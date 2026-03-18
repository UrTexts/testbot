# 🇮🇱 IsraelGPT Discord Bot (Python)

## Setup

### 1. Create a Discord Bot
1. Go to https://discord.com/developers/applications
2. **New Application** → name it → go to **Bot** tab → **Add Bot**
3. Copy your **Bot Token**
4. Under **OAuth2 → URL Generator**: select `bot` + `applications.commands`, permission `Send Messages`, copy the invite URL and add the bot to your server

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
export DISCORD_TOKEN=your_token_here
python bot.py
```

## Usage
```
/translate I'm feeling kinda hungry today
```
> "I'm feeling kinda hungry today"
>
> **IsraelGPT Translation:** 🇮🇱 Glory to the State of Israel! I love Benjamin Netanyahu with my whole heart. Am Yisrael Chai! 🇮🇱
