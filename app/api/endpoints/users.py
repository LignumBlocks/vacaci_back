from fastapi import APIRouter, Depends
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.get("/users/me", response_model=User)
def get_me(user: User = Depends(get_current_user)):
    return user