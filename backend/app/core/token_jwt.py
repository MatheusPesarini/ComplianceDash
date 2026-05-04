import jwt
from app.core.config import settings
from datetime import datetime, timedelta

secret_key = settings.secret_key
algorithm = "HS256"
access_token_expire_minutes = 60

def create_acess_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def verify_token(token: str):
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    return payload