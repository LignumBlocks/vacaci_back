from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Boolean, Integer
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firebase_uid: str = Field(sa_column=Column("firebase_uid", String, unique=True, index=True))
    email: str = Field(sa_column=Column("email", String, unique=True, index=True))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    role: str = Field(sa_column=Column("role", String), default="user")
    plan: str = Field(sa_column=Column("plan", String), default="free")
    tokens_used: int = Field(default=0)
    is_active: bool = Field(default=True)
