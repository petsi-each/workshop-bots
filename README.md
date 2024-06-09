# Workshop Syllabus: Creating a Basic Telegram Bot with python-telegram-bot 21.3

## Workshop Overview
This workshop is designed to guide participants through the process of creating a basic Telegram bot using the `python-telegram-bot` library, version 21.3. By the end of the workshop, participants will have a working Telegram bot that can respond to commands and messages.

## Target Audience
- Beginner to intermediate Python developers
- Individuals interested in building Telegram bots
- No prior experience with Telegram bot development required

## Duration
- Total: 4 hours
- Divided into four 1-hour sessions

## Session 1: Introduction and Setup

**Duration: 1 hour**

**Objectives:**
- Understand the basics of Telegram bots
- Set up the development environment

**Agenda:**
1. **Introduction to Telegram Bots (15 mins)**
   - What are Telegram bots?
   - Use cases and examples
   - Overview of the `python-telegram-bot` library

2. **Creating a Bot on Telegram (15 mins)**
   - Interacting with the BotFather
   - Creating a new bot
   - Obtaining the bot token

3. **Setting Up the Development Environment (30 mins)**
   - Installing Python and pip
   - Setting up a virtual environment
   - Installing `python-telegram-bot` version 21.3
     ```bash
     pip install python-telegram-bot==21.3
     ```

## Session 2: Basic Bot Development

**Duration: 1 hour**

**Objectives:**
- Create a basic Telegram bot
- Implement simple command handlers

**Agenda:**
1. **Writing the Bot Script (20 mins)**
   - Setting up the project structure
   - Writing the basic bot script
   - Explanation of the main function and handlers

   ```python
   from telegram import Update
   from telegram.ext import Application, CommandHandler

   BOT_TOKEN = 'YOUR_BOT_TOKEN'

   async def start(update: Update, context):
       await update.message.reply_text('Hi!')

   async def help_command(update: Update, context):
       await update.message.reply_text('Help!')

   def main():
       application = Application.builder().token(BOT_TOKEN).build()
       application.add_handler(CommandHandler("start", start))
       application.add_handler(CommandHandler("help", help_command))
       application.run_polling()

   if __name__ == '__main__':
       main()
    ```

2. **Running the Bot (20 mins)**
    - Running the script
    - Testing the bot with /start and /help commands

3. **Q&A and Troubleshooting (20 mins)**
    - Common issues and solutions
    - Interactive troubleshooting

## Session 3: Enhancing Bot Functionality

**Duration: 1 hour**

**Objectives:**
- Add message handlers to the bot
- Implement more interactive features

**Agenda:**
1. **Adding Message Handlers (20 mins)**
   - Introduction to message handlers
   - Writing an echo handler to respond to text messages

   ```python
   from telegram.ext import MessageHandler, filters

   async def echo(update: Update, context):
       await update.message.reply_text(update.message.text)

   # In main()
   application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    ```

2. Implementing Additional Commands (20 mins)
    - Adding more commands like /about, /contact, etc.
    - Best practices for command naming and handling

3. Interactive Features (20 mins)
    - Adding buttons and menus
    - Using inline keyboards