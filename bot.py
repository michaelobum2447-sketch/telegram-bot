from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8766888112:AAF_9F2ZFyM2dH2MXyLml92-2wFDY-GTbkI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to SAFE BETTING ODDS 🔥\n\n"
        "I will be giving you free odds every day ⚽💰\n\n"
        "Join my group for daily games:\n"
        "https://t.me/+UEq55Zwr4gZjNDk0\n\n"
        "VIP Subscription: ₦5,000\n"
        "Type VIP to subscribe."
    )

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "vip" in text:
        await update.message.reply_text(
            "🔥 VIP SUBSCRIPTION – ₦5,000 🔥\n\n"
            "To activate VIP access, make payment to:\n\n"
            "Bank: Opay\n"
            "Account Name: Michael Uchendu\n"
            "Account Number: 7030009791\n\n"
            "After payment, send your proof of payment here.\n"
            "You will be activated immediately after confirmation. ✅"
        )
    else:
        await update.message.reply_text(
            "Send VIP to access premium betting tips."
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

app.run_polling()
