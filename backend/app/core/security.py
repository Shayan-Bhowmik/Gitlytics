from datetime import datetime
from datetime import timedelta
from datetime import timezone
from jose import jwt
from jose import JWTError
from app.core.config import settings

ACCESS_TOKEN_EXPIRE_DAYS=7

def create_access_token(user_id: str)->str:
    """Createes a JWT containing the 
    users's ID and an expiration time."""

    expiration_time=datetime.now(timezone.utc)+timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

    payload={
        "sub":str(user_id),
        "exp":expiration_time,
    }

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")

def verify_access_token(token:str)->str | None:
    """Decodes a JWT and returns
    the user_id if valid, or None if expired/invalid"""

    try:
        payload=jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        return payload.get("sub")
    except JWTError:
        return None