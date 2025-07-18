import telegram, os, time, sys
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder
from mytoken import TOKEN
from handler import *
from telegram.error import NetworkError

def main():
    try:
        print("\nHelix_Bot starting...\n\n")
        print("press ctrl+c to stop this bot from running...")
        app = ApplicationBuilder().token(TOKEN).build()
        appFunction(app, "start", start)
        appFunction(app, "help", help)
        appFunction(app, "aboutme", aboutme)
        appFunction(app, "cmd", linuxcmd)
        appFunction(app, "gituser", gituser_info)
        appFunction(app, "getrepo", getrepo)
        appFunction(app, "repo", gitrepo_info)
        appFunction(app, "date", date)
        app.run_polling()

    except KeyboardInterrupt:
        print("\n[-]Bot getting terminated...")
    except NetworkError:
        print("\n[-]Connect internet and run this script again...")
        
def appFunction(app, x, y):
    app.add_handler(CommandHandler(x, y))


if __name__ == "__main__":
    main()
