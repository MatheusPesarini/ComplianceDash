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
    
# Client
class ClientCreate(BaseModel):
    name: str
    telephone: str
    email: str
    password: str
    
class ClientLogin(BaseModel):
    email: str
    password: str
    
class ClientCreateResponse(BaseModel):
    id: int
    created_at: datetime
    equipaments: List[EquipamentResponse] = []
    
    model_config = ConfigDict(from_attributes=True)
    
