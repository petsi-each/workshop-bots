import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()

# Your bot token obtained from BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi!')

async def help_command(update: Update, context):
    """Send a message when the command /help is issued."""
    await update.message.reply_text('Help!')

async def echo(update: Update, context):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    application.run_polling()

if __name__ == '__main__':
    main()
