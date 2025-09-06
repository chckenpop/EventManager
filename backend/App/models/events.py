from pydantic import BaseModel
from datetime import date, time
class Event(BaseModel):
    id: int
    eventName: str
    eventDate: date
    eventTime: time
    eventLocation: str