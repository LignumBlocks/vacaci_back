from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItineraryRequest(BaseModel):
    title: str
    origin: str
    destination: str
    start_date: datetime
    end_date: datetime
    budget: Optional[float] = None
    travelers: Optional[int] = 1
    interests: Optional[str] = None
    currency: str = "MXN"
    language: str = "es"

class ItineraryResponse(BaseModel):
    id: int
    title: str
    origin: str
    destination: str
    content_json: str
    created_at: datetime

    class Config:
        orm_mode = True
