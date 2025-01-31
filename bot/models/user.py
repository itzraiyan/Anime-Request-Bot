from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_id: int
    username: Optional[str]
    full_name: str
    daily_requests: int = 0
    pending_requests: int = 0
    total_requests: int = 0
    blacklisted: bool = False
    last_request: Optional[datetime] = None

class UserUpdate(BaseModel):
    daily_requests: Optional[int] = None
    pending_requests: Optional[int] = None
    total_requests: Optional[int] = None
    blacklisted: Optional[bool] = None
    last_request: Optional[datetime] = None