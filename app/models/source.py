from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship, Column, String, Integer, Boolean

class Source(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", String, unique=True, index=True))
    base_url: str = Field(sa_column=Column("base_url", String))
    auth_type: str = Field(sa_column=Column("auth_type", String), default="none")  # none|api_key|oauth
    rate_limit_per_min: int = Field(default=60)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    reviews: List["Review"] = Relationship(back_populates="source")