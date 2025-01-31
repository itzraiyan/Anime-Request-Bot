from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def request_priority_buttons(anime_name):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔵 Low", callback_data=f"priority_{anime_name}_Low")],
        [InlineKeyboardButton("🟢 Normal", callback_data=f"priority_{anime_name}_Normal")],
        [InlineKeyboardButton("🟠 High", callback_data=f"priority_{anime_name}_High")],
        [InlineKeyboardButton("🔴 Urgent", callback_data=f"priority_{anime_name}_Urgent")]
    ])

def admin_buttons(request_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Accept", callback_data=f"accept_{request_id}"),
         InlineKeyboardButton("❌ Reject", callback_data=f"reject_{request_id}")],
        [InlineKeyboardButton("🕒 Ongoing", callback_data=f"ongoing_{request_id}")]
    ])