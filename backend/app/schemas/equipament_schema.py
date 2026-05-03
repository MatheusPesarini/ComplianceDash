from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.equipament_model import ServiceStatus

class EquipamentCreate(BaseModel):
    category: str
    model: str
    brand: str
    service: str
    user_id: int
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
    user_id: int
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
