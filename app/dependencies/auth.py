from fastapi import Depends, Header, HTTPException
from sqlmodel import Session, select
from jose import jwt
import os
from app.db.session import get_session
from app.models.user import User
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

def verify_supabase_token(token: str):
    try:
        decoded = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token inválido: {str(e)}")

def get_current_user(
    authorization: str = Header(...),
    session: Session = Depends(get_session)
) -> User:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token mal formado")

    token = authorization.split(" ")[1]
    decoded = verify_supabase_token(token)

    uid = decoded.get("sub")
    email = decoded.get("email")

    if not uid or not email:
        raise HTTPException(status_code=400, detail="Token incompleto")

    user = session.exec(select(User).where(User.supabase_uid == uid)).first()

    if not user:
        user = User(supabase_uid=uid, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
    else:
        from datetime import datetime
        user.last_login = datetime.utcnow()
        session.add(user)
        session.commit()

    return user
