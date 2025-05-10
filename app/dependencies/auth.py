from fastapi import Depends, Header, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.core.firebase import verify_firebase_token
from app.models.user import User

def get_current_user(authorization: str = Header(...), session: Session = Depends(get_session)) -> User:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization token requerido")

    token = authorization.split(" ")[1]
    decoded = verify_firebase_token(token)
    uid = decoded.get("uid")
    email = decoded.get("email")

    user = session.exec(select(User).where(User.firebase_uid == uid)).first()
    if not user:
        user = User(firebase_uid=uid, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)

    return user
