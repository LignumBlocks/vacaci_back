from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship, Column, String, Float

class Destination(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", String, index=True))
    slug: str = Field(sa_column=Column("slug", String, unique=True, index=True))
    country: str = Field(sa_column=Column("country", String(2), index=True))
    lat: Optional[float] = Field(default=None)
    lon: Optional[float] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    reviews: List["Review"] = Relationship(back_populates="destination")
    hacks: List["Hack"] = Relationship(back_populates="destination")
    