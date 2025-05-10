from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer
from datetime import datetime
from typing import Optional

class TokenUsageLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id")
    itinerary_id: Optional[int] = Field(foreign_key="itinerary.id")
    tokens_used: int
    model: str = Field(sa_column=Column("model", String), default="gpt-4o")
    created_at: datetime = Field(default_factory=datetime.utcnow)
