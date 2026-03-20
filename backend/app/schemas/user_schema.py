from pydantic import BaseModel, ConfigDict
from typing import Optional

# Address
class AddressCreate(BaseModel):
    email_address: str
    
class AddressResponse(BaseModel):
    id: int
    email_address: str
    user_id: int
    
    model_config = ConfigDict(from_attributes=True)
    
# User
class UserCreate(BaseModel):
    name: str
    fullname: Optional[str] = None
    
class UserResponse(BaseModel):
    id: int
    name: str
    fullname: Optional[str] = None
    address: Optional[AddressResponse] = None
    
    model_config = ConfigDict(from_attributes=True)