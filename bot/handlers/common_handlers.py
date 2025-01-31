from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from database import Database
from utilities import formatters

db = Database()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Unrecognized command. Use /help for assistance")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("⚠️ This button action isn't implemented yet")