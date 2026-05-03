from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.equipament_schema import EquipamentCreate, EquipamentResponse, EquipamentUpdate
from app.services.equipament_service import EquipamentService

router = APIRouter(prefix="/api", tags=["equipaments"])

@router.post("/{user_id}/equipaments", response_model=EquipamentResponse, status_code=201)
def create_equipament(user_id: int, equipament_in: EquipamentCreate, db: Session = Depends(get_db)):
    service = EquipamentService(db)
    try:
        return service.create_equipament(equipament_in, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}/equipaments", response_model=list[EquipamentResponse])
def get_equipaments(user_id: int, db: Session = Depends(get_db)):
    service = EquipamentService(db)
    try:
        equipaments = service.get_user_equipaments(user_id)
        return equipaments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{user_id}/equipaments/{equipament_id}", response_model=None, status_code=201)
def update_equipament(equipament_id: int, equipament_in: EquipamentUpdate, db: Session = Depends(get_db)):
    service = EquipamentService(db)
    try:
        return service.update_equipament(equipament_id, equipament_in)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
