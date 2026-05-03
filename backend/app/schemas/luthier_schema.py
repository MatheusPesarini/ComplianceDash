from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from app.models.luthier_model import ServiceStatus

# Equipament
class EquipamentCreate(BaseModel):
    category: str
    model: str
    brand: str
    service: str
    client_id: int
    status: Optional[ServiceStatus] = ServiceStatus.PENDING
    price: Optional[float] = None
    notes: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None
    
class EquipamentResponse(BaseModel):
    id: int
    category: str
    model: str
    brand: str
    service: str
    client_id: int
    status: Optional[ServiceStatus] = ServiceStatus.PENDING
    price: Optional[float] = None
    notes: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
    entry_date: datetime

    model_config = ConfigDict(from_attributes=True)
    
class EquipamentUpdate(BaseModel):
    status: Optional[ServiceStatus] = None
    price: Optional[float] = None
    notes: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None
    
# User
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
    error_message: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
