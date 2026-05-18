import jwt
from app.core.config import settings
from datetime import datetime, timedelta, UTC
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

secret_key = settings.secret_key
algorithm = "HS256"
access_token_expire_minutes = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def create_acess_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(UTC) + timedelta(minutes=access_token_expire_minutes)
    unix_expire = int(expire.timestamp()) 
    to_encode.update({"exp": unix_expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def verify_token(token: str):
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    return payload

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        class CurrentUser:
            def __init__(self, id):
                self.id = int(id)
                
        return CurrentUser(user_id)
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")