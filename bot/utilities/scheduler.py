from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from database import Database
from config import Config
from telegram import Bot
import logging

logger = logging.getLogger(__name__)

class Scheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.db = Database()
    
    async def setup(self, app):
        self.bot = app.bot
        self.scheduler.add_job(
            self.send_daily_reminders,
            CronTrigger(hour=12, timezone=Config.TIMEZONE)
        )
        self.scheduler.add_job(
            self.cleanup_old_requests,
            CronTrigger(hour=3, timezone=Config.TIMEZONE)
        )
        self.scheduler.start()
        logger.info("Scheduler started")
    
    async def send_daily_reminders(self):
        admins = Config.ADMIN_IDS
        pending = await self.db.get_pending_count()
        
        for admin_id in admins:
            await self.bot.send_message(
                chat_id=admin_id,
                text=f"📋 Daily Reminder\nPending requests: {pending}"
            )
    
    async def cleanup_old_requests(self):
        await self.db.cleanup_requests(Config.CLEANUP_DAYS)
        logger.info(f"Cleaned up requests older than {Config.CLEANUP_DAYS} days")