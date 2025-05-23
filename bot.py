import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Get TOKEN and CHAT_ID from environment variables
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if TOKEN is None or CHAT_ID is None:
    print("Error: Please set the TOKEN and CHAT_ID environment variables.")
    sys.exit(1)

try:
    CHAT_ID = int(CHAT_ID)
except ValueError:
    print("Error: CHAT_ID must be an integer.")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! The bot is active.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_received = update.message.text
    await update.message.reply_text(f"You said: {text_received}")

async def send_startup_notification(application):
    try:
        await application.bot.send_message(chat_id=CHAT_ID, text="✅ System started and bot is active.")
    except Exception as e:
        print(f"Failed to send startup notification: {e}")

async def on_startup(application):
    await send_startup_notification(application)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")

    # Send startup notification when the bot starts
    app.post_init = on_startup

    app.run_polling()
