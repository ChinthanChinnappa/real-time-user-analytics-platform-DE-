from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserEventBase(BaseModel):
    event_type: str
    user_id: str
    page: str
    timestamp: datetime
    value: Optional[float] = None

class UserEventCreate(UserEventBase):
    pass

class UserEvent(UserEventBase):
    id: int

    class Config:
        from_attributes = True

class AnalyticsResponse(BaseModel):
    total_events: int
    unique_users: int
    top_pages: dict
    event_types: dict