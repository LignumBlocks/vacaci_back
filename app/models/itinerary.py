from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Float, Integer
from datetime import datetime
from typing import Optional

class Itinerary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id", index=True)
    title: str = Field(sa_column=Column("title", String))
    origin: str = Field(sa_column=Column("origin", String))
    destination: str = Field(sa_column=Column("destination", String))
    start_date: datetime
    end_date: datetime
    budget: Optional[float]
    travelers: Optional[int]
    interests: Optional[str] = Field(sa_column=Column("interests", String), default=None)
    currency: str = Field(sa_column=Column("currency", String), default="MXN")
    language: str = Field(sa_column=Column("language", String), default="es")
    content_json: str = Field(sa_column=Column("content_json", String))
    created_at: datetime = Field(default_factory=datetime.utcnow)
