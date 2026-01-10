from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from jose import jwt, JWTError
from passlib.context import CryptContext

from .config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def create_access_token(subject: str) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    payload = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int(exp.timestamp()),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)


def decode_token(token: str) -> Optional[Dict[str, Any]]:
    try:
        return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
    except JWTError:
        return None
