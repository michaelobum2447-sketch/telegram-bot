from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8766888112:AAHYe11sKXslg5T_qRCqptoXy1txOu9e6eQ"

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
            "🔥 VIP Subscription 🔥\n\n"
            "Price: ₦5,000\n"
            "You will receive premium daily sure odds.\n\n"
            "Reply PAY to continue."
        )
    elif "pay" in text:
        await update.message.reply_text(
            "Send your payment and screenshot to admin to activate VIP access."
        )
    else:
        await update.message.reply_text(
            "Send VIP to access premium betting tips."
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
app.run_polling()
