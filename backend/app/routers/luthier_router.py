from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.luthier_schema import ClientCreate, ClientResponse, EquipamentCreate, EquipamentResponse
from app.services.luthier_service import UserService


router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientResponse, status_code=201)
def create_client(client_in: ClientCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_client(client_in)

@router.get("/{client_id}", response_model=ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.get_client(client_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{client_id}/equipaments", response_model=EquipamentResponse, status_code=201)
def create_equipament(client_id: int, equipament_in: EquipamentCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_equipament(equipament_in, client_id)

@router.get("/{client_id}/equipaments", response_model=EquipamentResponse)
def get_equipaments(client_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        equipaments = service.get_client_equipaments(client_id)
        return equipaments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
