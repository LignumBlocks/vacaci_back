from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, String, JSON
from sqlmodel import SQLModel, Field, Relationship

class Hack(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    destination_id: int = Field(foreign_key="destination.id")
    user_id: Optional[int] = Field(foreign_key="user.id", default=None)
    snippet: str = Field(sa_column=Column("snippet", String, index=True))  # "La mejor vista es..."
    source_review_ids: Optional[List[int]] = Field(sa_column=Column("source_review_ids", JSON), default=None)
    upvotes: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    destination: "Destination" = Relationship(back_populates="hacks")