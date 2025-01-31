from pymongo import MongoClient, DESCENDING
from pymongo.errors import PyMongoError
from config import Config
from datetime import datetime

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client.anime_requests
    
    async def create_request(self, user_data):
        request = {
            "request_id": f"REQ-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "user_id": user_data['user_id'],
            "anime_name": user_data['anime_name'],
            "quality": user_data['quality'],
            "audio": user_data['audio'],
            "category": user_data['category'],
            "priority": user_data['priority'],
            "status": "pending",
            "timestamp": datetime.now(),
            "tags": []
        }
        return self.db.requests.insert_one(request)
    
    async def get_stats(self):
        return {
            "total_requests": self.db.requests.count_documents({}),
            "completed_requests": self.db.requests.count_documents({"status": "completed"}),
            "rejected_requests": self.db.requests.count_documents({"status": "rejected"}),
            "avg_response_time": self._calculate_avg_response(),
            "category_distribution": self._get_distribution("category"),
            "audio_distribution": self._get_distribution("audio")
        }
    
    def _calculate_avg_response(self):
        pipeline = [
            {"$match": {"status_date": {"$exists": True}}},
            {"$project": {"response_time": {
                "$divide": [{"$subtract": ["$status_date", "$timestamp"]}, 3600000]
            }}},
            {"$group": {"_id": None, "avg": {"$avg": "$response_time"}}}
        ]
        result = list(self.db.requests.aggregate(pipeline))
        return result[0]['avg'] if result else 0
    
    def _get_distribution(self, field):
        return dict(self.db.requests.aggregate([
            {"$group": {"_id": f"${field}", "count": {"$sum": 1}}},
            {"$project": {"_id": 0, "name": "$_id", "count": 1}}
        ]))