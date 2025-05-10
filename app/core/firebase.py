import firebase_admin
from firebase_admin import credentials, auth
from functools import lru_cache
from fastapi import HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()

@lru_cache()
def init_firebase():
    cred_path = os.getenv("FIREBASE_CREDENTIALS", "firebase_credentials.json")
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

def verify_firebase_token(token: str):
    init_firebase()
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token  # contiene uid, email, etc.
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido o expirado: {str(e)}"
        )
