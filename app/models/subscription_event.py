from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String
from datetime import datetime
from typing import Optional

class SubscriptionEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id")
    stripe_customer_id: str = Field(sa_column=Column("stripe_customer_id", String))
    stripe_event_type: str = Field(sa_column=Column("stripe_event_type", String))
    raw_payload: str = Field(sa_column=Column("raw_payload", String))
    received_at: datetime = Field(default_factory=datetime.utcnow)
