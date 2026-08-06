import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60*24

def hash_password(password):
    return bcrypt.hashpw(password.enode(), bcrypt.gensalt()).decode()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def create_access_token(data):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp:expire"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)

def decode_access_token(token):
    return jwt.decode(token, settings.secret_key, algorithm=[ALGORITHM])

