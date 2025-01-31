from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class AnimeRequest(BaseModel):
    request_id: str
    user_id: int
    anime_name: str
    quality: str
    audio: str
    category: str
    priority: str
    status: str = "pending"
    timestamp: datetime = datetime.now()
    admin_notes: Optional[str] = None
    tags: list[str] = []

class RequestUpdate(BaseModel):
    status: Optional[str] = None
    admin_notes: Optional[str] = None
    tags: Optional[list[str]] = None