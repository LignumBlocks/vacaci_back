from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserRead(BaseModel):
    id: int
    supabase_uid: str
    email: str
    role: str
    plan: str
    tokens_used: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
