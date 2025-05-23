import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن و چت آیدی رو از متغیرهای محیطی (env) می‌گیریم
TOKEN = os.getenv("TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فعال است.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_received = update.message.text
    await update.message.reply_text(f"پیام شما: {text_received}")

async def send_startup_notification(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="✅ سیستم روشن شد و ربات فعال است.")

async def on_startup(application):
    await send_startup_notification(application)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("ربات داره اجرا میشه...")

    # پیام استارتاپ رو وقتی ربات بالا اومد می‌فرستیم
    app.post_init = on_startup

    app.run_polling()
