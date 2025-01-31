import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import Config
from database import Database
from utilities.scheduler import Scheduler
from handlers import user_handlers, admin_handlers, common_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def post_init(app):
    await Scheduler().setup(app)
    await app.bot.set_my_commands([
        ("start", "Start the bot"),
        ("request", "Submit new anime request"),
        ("stats", "View statistics"),
        ("help", "Show help guide")
    ])

def main():
    application = Application.builder().token(Config.BOT_TOKEN).post_init(post_init).build()
    
    # User handlers
    application.add_handler(CommandHandler("start", user_handlers.start))
    application.add_handler(CommandHandler("request", user_handlers.new_request))
    application.add_handler(CommandHandler("stats", user_handlers.show_stats))
    
    # Admin handlers
    application.add_handler(CommandHandler("admin", admin_handlers.admin_panel))
    application.add_handler(CallbackQueryHandler(admin_handlers.handle_admin_actions, pattern="^admin_"))
    
    # Common handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, common_handlers.handle_message))
    application.add_handler(CallbackQueryHandler(common_handlers.handle_callback))
    
    application.run_polling()

if __name__ == "__main__":
    main()