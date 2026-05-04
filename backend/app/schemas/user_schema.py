from typing import Optional
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    
class UserCreateResponse(BaseModel):
    successful: bool
    error_message: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class UserLogin(BaseModel):
    email: str
    password: str
    
class UserLoginResponse(BaseModel):
    successful: bool
    user_id: str
    error_message: Optional[str] = None
    jwt_token: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
