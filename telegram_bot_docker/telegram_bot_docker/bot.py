import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вы написали: " + update.message.text)

def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN (переменная окружения)")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
