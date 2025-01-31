from datetime import datetime, timedelta
from database import Database

class StatsManager:
    def __init__(self):
        self.db = Database()
    
    async def generate_dashboard(self):
        return {
            "total_requests": await self.db.get_total_requests(),
            "completed_requests": await self.db.get_completed_requests(),
            "rejected_requests": await self.db.get_rejected_requests(),
            "avg_response_time": await self.db.get_avg_response_time(),
            "category_distribution": await self.db.get_category_distribution(),
            "audio_distribution": await self.db.get_audio_distribution()
        }
    
    async def export_csv(self, period):
        filename = f"stats_{datetime.now().strftime('%Y%m%d')}.csv"
        # Generate CSV logic
        return filename