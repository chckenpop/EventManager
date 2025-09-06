
def fetch_events(user_id: str):
    events = db.events.find({"user_id": user_id})
    return list(events)