import os, sys, time, asyncio
import subprocess
from trusted import trusted_users
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder
from priv_methods import *
from datetime import datetime

global gituser
gituser = "l4feer"

# Functions

def log_userinput(x):
    print(f"[+]user_input  :  {x}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first = user.first_name or ""
    last = user.last_name or ""
    username = f"@{user.username}" if user.username else ""

    welcome_message = (
        f"👋 Hello {first} {last} {username}!\n\n"
        "🤖 *Welcome to HelixBot!*\n"
        "_Spawned from caffeine and code by L4FeeR._\n\n"
        "Type /help to see what I can do for you."
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
 🤖/*Helix Bot Help Menu*
Made by *L4FeeR*

📌 *Basic Commands*:
/start – Start the bot and greet user
/help – Show this help menu
/aboutme – Show info about the current Telegram user

🛠️ *Linux Tools*:
/cmd – Run shell commands (trusted users only)

🌐 *GitHub Explorer*:
/gituser `<username>` – Get GitHub user profile info  
/getrepo `<username>` – List all public repositories of a user  
/repo `<repo>` – Get details of a specific repo (after setting user via `/gituser`)

📅 *Utility*:
/date – Show current server date
/connectssh – Connect to SSH (feature in progress)
"""
    await update.message.reply_text(msg, parse_mode="Markdown")

async def aboutme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    name = (user.first_name or "") + " " + (user.last_name or "")
    user_id = user.id
    username = user.username
    chat_id = chat.id
    chat_title = chat.title
    chat_type = chat.type
    is_bot = user.is_bot
    msg = f"""
User Specific:
    
 [🔗]Username : @{username}
 [👤]Name     : {name}
 [🆔]User ID  : {user_id}
 [🤖]Is Bot    ? {is_bot}

Chat Specific:

 [🆔]Chat id    : {chat_id}
 [🏷️]Chat title : {chat_title}
 [📛]Chat type  : {chat_type}
 
 """
    await update.message.reply_text(msg)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You hit the hidden command!")
    msg = """
    Message animated
"""
    animated_text = ""
    sent = await update.message.reply_text(" . ")
    for word in msg.split():
        animated_text += word + " "
        await sent.edit_text(animated_text.strip())
        await asyncio.sleep(0.1)

async def linuxcmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("using linux command module...")
    print("checking user is trusted or not ...")
    if context.args and len(context.args) > 0:
        log_userinput(context.args[0])
    if update.effective_user.id in trusted_users.values():
        print("Trusted user!")
        await update.message.reply_text("currently unavailable*")
    else:
        print("Untrusty user!")
        await update.message.reply_text("Sorry! You are not a trusted user...")
        await update.message.reply_text("!Access Denied*")

async def gituser_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and len(context.args) > 0 and context.args[0]:
        log_userinput(context.args[0])
        user_arg = context.args[0]
        await update.message.reply_text(GitInfo(user_arg).get_gituserinfo())
    else:
        await update.message.reply_text("""No username mentioned!

        trythis /gituser torvalds

        """)

async def getrepo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and len(context.args) > 0 and context.args[0]:
        log_userinput(context.args[0])
        user_arg = context.args[0]
        j = 1
        await update.message.reply_text(f" Public Repositories of {user_arg}")
        for i in GitInfo(user_arg).get_repoinfo():
            await update.message.reply_text(f"{j}. {i}")
            j += 1
    else:
        await update.message.reply_text("""No reponame mentioned!

        trythis /getrepo moonlight

        """)

async def gitrepo_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and len(context.args) > 0 and context.args[0]:
        log_userinput(context.args[0])
        repo_arg = context.args[0]
        # Note: gituser can be set by /gituser command, but for stateless safety, we could require user as argument
        await update.message.reply_text(GitInfo(gituser).get_repdet(repo_arg))
    else:
        await update.message.reply_text("""No repository mentioned!

        trythis /getrepo cve

        """)

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    formatted = now.strftime(
        """
📅 *Date Information*

🕰️ Time         : %I:%M:%S %p
📆 Date         : %A, %d %B %Y
🗓️ Week Number  : %U
📍 Timezone     : %Z (UTC%z)
"""
    )
    await update.message.reply_text(formatted, parse_mode="Markdown")
