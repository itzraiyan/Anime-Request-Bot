import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    MONGO_URI = os.getenv("MONGO_URI")
    ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS").split(",")]
    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    REQUEST_LIMITS = {
        'daily': 5,
        'pending': 3
    }
    CLEANUP_DAYS = int(os.getenv("CLEANUP_DAYS", 30))
    TIMEZONE = os.getenv("TIMEZONE", "UTC")
    AUDIO_OPTIONS = ["Sub", "Dub", "Dual"]
    CATEGORIES = ["TV Series", "Movies", "OVAs", "Specials"]
    PRIORITIES = ["Low", "Normal", "High", "Urgent"]