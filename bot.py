import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, filters, ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Xabar yozing, men ✅ qo'yaman.")

async def galichka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅")

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, galichka))
app.run_polling()
