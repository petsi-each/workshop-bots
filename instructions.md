# Instructions for the Tutor

## Overview
This document provides detailed instructions for the tutor conducting the workshop on creating a basic Telegram bot using the `python-telegram-bot` library, version 21.3. Follow the outlined agenda, encourage participation, and provide hands-on guidance to ensure participants achieve the workshop objectives.

## Session 1: Introduction and Setup

### Duration: 1 hour

### Objectives
- Understand the basics of Telegram bots
- Set up the development environment

### Preparation
- Prepare a slide deck covering the introduction to Telegram bots, use cases, and examples.
- Create a new Telegram bot using BotFather and secure the bot token.
- Ensure your development environment is ready with Python installed.

### Agenda

#### 1. Introduction to Telegram Bots (15 mins)
**Goal:** Provide participants with an understanding of what Telegram bots are and their use cases.

**Instructions:**
1. **Introduction**
   - Explain what Telegram bots are.
   - Show examples of popular Telegram bots and their use cases.

2. **Overview of `python-telegram-bot` Library**
   - Introduce the `python-telegram-bot` library.
   - Discuss its features and benefits for developing Telegram bots.

3. **Q&A Session**
   - Allow participants to ask questions about Telegram bots and the library.

#### 2. Creating a Bot on Telegram (15 mins)
**Goal:** Participants should create their own bot on Telegram using BotFather and obtain a bot token.

**Instructions:**
1. **Interacting with BotFather**
   - Demonstrate how to create a new bot using BotFather.
   - Guide participants through the steps of creating a bot and obtaining the bot token.

2. **Securing the Bot Token**
   - Emphasize the importance of keeping the bot token secure.
   - Show how to store the bot token securely in their development environment.

3. **Q&A Session**
   - Address any questions or issues participants encounter during the bot creation process.

#### 3. Setting Up the Development Environment (30 mins)
**Goal:** Ensure participants have their development environment set up with Python, pip, and `python-telegram-bot` installed.

**Instructions:**
1. **Installing Python and pip**
   - Provide instructions for installing Python and pip on different operating systems.

2. **Setting Up a Virtual Environment**
   - Explain the benefits of using a virtual environment.
   - Show how to set up and activate a virtual environment.
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
     ```

3. **Installing `python-telegram-bot`**
   - Demonstrate how to install the `python-telegram-bot` library.
     ```bash
     pip install python-telegram-bot==21.3
     ```

4. **Q&A Session**
   - Address any installation issues and ensure everyone has their environment set up.

**Homework:**
- Ensure Python and required packages are installed.
- Create a new bot on Telegram and secure the bot token.

## Session 2: Basic Bot Development

### Duration: 1 hour

### Objectives
- Create a basic Telegram bot
- Implement simple command handlers

### Preparation
- Prepare a basic bot script similar to the one provided below.
- Ensure your development environment is ready with the necessary packages installed.

### Agenda

#### 1. Writing the Bot Script (20 mins)
**Goal:** Participants should learn how to write a basic bot script with command handlers.

**Instructions:**
1. **Setting Up the Project Structure**
   - Explain how to organize the project files and directories.
   - Create a new Python script for the bot.

2. **Writing the Basic Bot Script**
   - Show the following code snippet:
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
   - Walk through the code:
     - Explain the `start` and `help_command` functions.
     - Describe the `Application` object and how to add command handlers.

3. **Live Coding Session**
   - Open your code editor and write the bot script live.
   - Encourage participants to follow along and write the script in their environment.

#### 2. Running the Bot (20 mins)
**Goal:** Participants should learn how to run their bot script and test the basic commands.

**Instructions:**
1. **Running the Script**
   - Demonstrate how to run the bot script from the command line.
     ```bash
     python bot_script.py
     ```

2. **Testing the Bot**
   - Show how to test the bot by sending `/start` and `/help` commands in Telegram.
   - Encourage participants to test their bots and ensure they respond correctly.

3. **Q&A and Troubleshooting**
   - Address common issues and provide solutions.
   - Assist participants with any problems they encounter while running their bot.

**Homework:**
- Experiment with modifying the bot's response messages.

## Session 3: Enhancing Bot Functionality

### Duration: 1 hour

### Objectives
- Add message handlers to the bot
- Implement more interactive features

### Preparation
- Ensure you have the latest version of `python-telegram-bot` (21.3) installed.
- Prepare a basic bot script similar to the one from Session 2.
- Have examples ready for additional commands and interactive features.
- Familiarize yourself with the `telegram.ext` library, particularly `MessageHandler` and `filters`.

### Agenda

#### 1. Adding Message Handlers (20 mins)
**Goal:** Participants should understand how to add message handlers and create an echo function.

**Instructions:**
1. **Introduction to Message Handlers**
   - Explain the concept of message handlers in Telegram bots.
   - Describe how handlers listen for specific types of messages and respond accordingly.

2. **Writing an Echo Handler**
   - Show the following code snippet:
     ```python
     from telegram.ext import MessageHandler, filters

     async def echo(update: Update, context):
         await update.message.reply_text(update.message.text)

     # In main()
     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
     ```
   - Walk through the code:
     - `MessageHandler`: listens for text messages.
     - `filters.TEXT & ~filters.COMMAND`: filters out commands, allowing only plain text messages.
     - `echo` function: sends back the same text received.

3. **Live Coding Session**
   - Open your code editor and add the echo handler to the existing bot script.
   - Run the bot and demonstrate how it echoes any text message sent to it.
   - Encourage participants to follow along and test the bot themselves.

#### 2. Implementing Additional Commands (20 mins)
**Goal:** Participants should learn how to add more commands and understand best practices.

**Instructions:**
1. **Adding More Commands**
   - Explain the purpose of additional commands like `/about`, `/contact`, etc.
   - Show the following example:
     ```python
     async def about(update: Update, context):
         await update.message.reply_text('This is a simple Telegram bot.')

     async def contact(update: Update, context):
         await update.message.reply_text('Contact us at example@example.com.')

     # In main()
     application.add_handler(CommandHandler("about", about))
     application.add_handler(CommandHandler("contact", contact))
     ```
   - Walk through the code for each command handler.

2. **Best Practices**
   - Discuss best practices for naming and organizing command handlers.
   - Encourage the use of clear, descriptive command names.

3. **Live Coding Session**
   - Add the `about` and `contact` command handlers to your script.
   - Run the bot and demonstrate the new commands.
   - Ask participants to implement and test these commands on their bots.

#### 3. Interactive Features (20 mins)
**Goal:** Participants should learn how to add buttons and inline keyboards to their bot.

**Instructions:**
1. **Introduction to Interactive Features**
   - Explain the concept of buttons and inline keyboards in Telegram bots.
   - Discuss their use cases and benefits for user interaction.

2. **Adding Buttons and Menus**
   - Show the following example:
     ```python
     from telegram import InlineKeyboardButton, InlineKeyboardMarkup

     async def start(update: Update, context):
         keyboard = [
             [InlineKeyboardButton("Option 1", callback_data='1')],
             [InlineKeyboardButton("Option 2", callback_data='2')],
         ]
         reply_markup = InlineKeyboardMarkup(keyboard)
         await update.message.reply_text('Please choose:', reply_markup=reply_markup)

     async def button(update: Update, context):
         query = update.callback_query
         await query.answer()
         await query.edit_message_text(text=f"Selected option: {query.data}")

     # In main()
     application.add_handler(CommandHandler("start", start))
     application.add_handler(CallbackQueryHandler(button))
     ```
   - Walk through the code:
     - `InlineKeyboardButton`: creates buttons.
     - `InlineKeyboardMarkup`: organizes buttons into a keyboard layout.
     - `start` function: sends a message with inline keyboard.
     - `button` function: handles button presses.

3. **Live Coding Session**
   - Add the inline keyboard to the `start` command in your script