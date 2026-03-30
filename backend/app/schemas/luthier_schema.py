from pydantic import BaseModel, ConfigDict
from typing import Optional

# Client
class ClientCreate(BaseModel):
    name: str
    telephone: str
    email: str
    password: str
    
class ClientResponse(BaseModel):
    id: int
    # Talvez não precise retornar isso
    name: str
    telephone: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)
    
# Address
class EquipamentCreate(BaseModel):
    category: str
    model: str
    brand: str
    service: str
    client_id: int
    
class EquipamentResponse(BaseModel):
    id: int
    category: str
    model: str
    brand: str
    service: str
    client_id: int
    
    model_config = ConfigDict(from_attributes=True)
    