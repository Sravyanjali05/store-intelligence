from pydantic import BaseModel

class Event(BaseModel):
    event_id: str
    store_id: str
    visitor_id: str