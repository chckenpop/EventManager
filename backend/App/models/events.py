from pydantic import BaseModel
from datetime import date, time
from typing import Optional
class Event(BaseModel):
    id: int
    userId: int
    eventName: str
    eventDate: date
    eventTime: time
    eventLocation: Optional[str] = None