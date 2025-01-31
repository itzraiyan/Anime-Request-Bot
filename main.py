from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers.user_requests import handle_request
from handlers.admin_panel import handle_admin_commands
from handlers.callbacks import handle_callback

app = Application.builder().token(BOT_TOKEN).build()

# Register Handlers
app.add_handler(CommandHandler("start", handle_request))
app.add_handler(CommandHandler("admin", handle_admin_commands))
app.add_handler(CallbackQueryHandler(handle_callback))

# Run Bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()