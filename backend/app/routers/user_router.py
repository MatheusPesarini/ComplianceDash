from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user_schema import AddressCreate, AddressResponse, UserCreate, UserResponse
from app.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user_in)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/{user_id}/address", response_model=AddressResponse)
def create_address(user_id: int, address_in: AddressCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user_address(address_in, user_id)
    
@router.get("{user_id}/address", response_model=AddressResponse)
def get_address(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        address = service.get_user_address(user_id)
        return address
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
