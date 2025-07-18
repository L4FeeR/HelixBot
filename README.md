# 🧬 HelixBot: Multipurpose, Modern, Evolving

HelixBot is a versatile Telegram bot designed for developers and power users.  
Explore GitHub profiles, run safe shell commands, get server info, and more—all from one evolving bot.

---

## ✨ Features

- **General Commands**
  - `/start` – Personalized greeting from HelixBot
  - `/help` – List all commands and features
  - `/aboutme` – Your Telegram info

- **Linux Tools**
  - `/cmd` – Run shell commands *(trusted users only)*

- **GitHub Explorer**
  - `/gituser <username>` – Fetch a GitHub user’s profile
  - `/getrepo <username>` – List all public repos for a user
  - `/repo <repo>` – Get details of a specific repo (after `/gituser`)

- **Utilities**
  - `/date` – Get the current server date and time

---

## 🔑 How to Get Your Telegram Bot Token

1. **Open Telegram and search for [@BotFather](https://t.me/botfather).**
2. Start a chat and send the command `/newbot`.
3. Follow the prompts to choose a name and username for your bot.
4. When your bot is created, BotFather will give you a token that looks like:  
   ```
   123456789:ABCdefGhIJKlmNoPQRstUvwxYZ1234567890
   ```
5. **Copy this token and keep it safe!**  
   Do **not** share it publicly.

---

## 🚀 Setup & Installation

1. **Clone the repo**
   ```sh
   git clone https://github.com/yourusername/helixbot.git
   cd helixbot
   ```

2. **(Recommended) Set up a virtual environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure your bot token**  
   - **Never share your token publicly!**
   - Create a `token.py` file (excluded from git):
     ```python
     TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
     ```
   - For extra security, consider using environment variables.

5. **Run HelixBot**
   ```sh
   python main.py
   ```

---

## 🗂️ Project Structure

```
.
├── main.py           # Bot launcher & command registration
├── handler.py        # All Telegram command handler functions
├── priv_methods.py   # GitHub API utilities
├── token.py          # Your bot token (excluded from repo)
├── requirements.txt  # Python dependencies
└── README.md         # This file!
```

---

## 🔒 Security Tips

- **Never commit `token.py` or your bot token!**
- If your token leaks, regenerate it immediately via [@BotFather](https://t.me/botfather).
- The `/cmd` command is restricted for a reason. Double-check trusted user IDs in your code.

---

## 💡 Credits

Handcrafted with ❤️ by **Lafeer**  
Feel free to fork, improve, and send your pull requests!

---

## 📝 License

MIT – Use, share, and remix as you like!

---
