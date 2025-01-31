from config import Config

def validate_audio(audio: str):
    if audio not in Config.AUDIO_OPTIONS:
        raise ValueError(f"Invalid audio option. Valid options: {Config.AUDIO_OPTIONS}")

def validate_category(category: str):
    if category not in Config.CATEGORIES:
        raise ValueError(f"Invalid category. Valid options: {Config.CATEGORIES}")

def validate_priority(priority: str):
    if priority not in Config.PRIORITIES:
        raise ValueError(f"Invalid priority. Valid options: {Config.PRIORITIES}")

def validate_request_limit(user_data):
    if user_data['daily_requests'] >= Config.REQUEST_LIMITS['daily']:
        raise Exception("Daily request limit reached")
    if user_data['pending_requests'] >= Config.REQUEST_LIMITS['pending']:
        raise Exception("Too many pending requests")