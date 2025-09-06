#event routes 
from fastapi import APIRouter

router = APIRouter()


#create event
@router.post("/events")

#update single event
@router.put("/events/{event_id}")

#delete single event
@router.DELETE("/events/{event_id}")

#fetch single event
@router.get("/events/{event_id}")
