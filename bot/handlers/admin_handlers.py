from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from utilities import formatters
from database import Database
from config import Config

db = Database()

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id not in Config.ADMIN_IDS:
        await update.message.reply_text("⛔ Access Denied!")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Live Dashboard", callback_data="admin_dashboard")],
        [
            InlineKeyboardButton("📥 Pending Requests", callback_data="admin_pending"),
            InlineKeyboardButton("📈 Statistics", callback_data="admin_stats")
        ],
        [InlineKeyboardButton("⚙️ Manage Users", callback_data="admin_users")]
    ])
    
    await update.message.reply_text(
        "🛠️ *Admin Control Panel*\nChoose an action:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def handle_admin_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    action = query.data.split("_")[1]
    
    if action == "dashboard":
        stats = await db.get_real_time_stats()
        await query.edit_message_text(
            formatters.format_stats(stats),
            parse_mode="Markdown"
        )
    
    elif action == "pending":
        requests = await db.get_pending_requests()
        formatted = "\n\n".join([formatters.format_request(r) for r in requests[:5]])
        await query.edit_message_text(
            f"📭 *Pending Requests*\n\n{formatted}",
            parse_mode="Markdown"
        )
    
    # Add other actions...