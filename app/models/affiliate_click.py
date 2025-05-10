from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String
from datetime import datetime
from typing import Optional

class AffiliateClick(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id", index=True)
    itinerary_id: Optional[int] = Field(foreign_key="itinerary.id", index=True)
    type: str = Field(sa_column=Column("type", String))
    provider: str = Field(sa_column=Column("provider", String))
    affiliate_url: str = Field(sa_column=Column("affiliate_url", String))
    clicked_at: datetime = Field(default_factory=datetime.utcnow)
