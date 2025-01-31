from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def stats_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📅 Daily", callback_data="stats_daily"),
            InlineKeyboardButton("📆 Weekly", callback_data="stats_weekly"),
            InlineKeyboardButton("📅 Monthly", callback_data="stats_monthly")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="admin_main"),
            InlineKeyboardButton("📤 Export CSV", callback_data="stats_export")
        ]
    ])

def request_actions(request_id):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Accept", callback_data=f"accept_{request_id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject_{request_id}"),
        ],
        [
            InlineKeyboardButton("🔄 Ongoing", callback_data=f"ongoing_{request_id}"),
            InlineKeyboardButton("ℹ️ Need Info", callback_data=f"info_{request_id}"),
        ],
        [InlineKeyboardButton("📝 Add Note", callback_data=f"note_{request_id}")]
    ])