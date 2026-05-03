from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.database import get_db
from app.schemas.luthier_schema import UserCreate, UserCreateResponse, UserLogin, EquipamentCreate, EquipamentResponse, EquipamentUpdate, UserLoginResponse
from app.services.luthier_service import UserService


router = APIRouter(prefix="/api", tags=["users"])

@router.post("/register", response_model=UserCreateResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        service.create_user(user_in)
        return UserCreateResponse(successful=True)
    except IntegrityError:
        # ex: e-mail já existe [unique=True]
        db.rollback() 
        return UserCreateResponse(successful=False, error_message="Este email já está cadastrado")
    except Exception as e:
        return UserCreateResponse(successful=False, error_message=str(e))
    
@router.post("/login", response_model=UserLoginResponse, status_code=200)
def login_user(user_in: UserLogin, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        service.login_user(user_in) 
        return UserLoginResponse(successful=True)
    except ValueError as e:
        # ValueError = "Credenciais inválidas"
        return UserLoginResponse(successful=False, error_message=str(e))
    except Exception as e:
        return UserLoginResponse(successful=False, error_message=str(e))


@router.get("/user/{user_id}", response_model=UserCreateResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{user_id}/equipaments", response_model=EquipamentResponse, status_code=201)
def create_equipament(user_id: int, equipament_in: EquipamentCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_equipament(equipament_in, user_id)

@router.get("/{user_id}/equipaments", response_model=EquipamentResponse)
def get_equipaments(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    
    try:
        equipaments = service.get_user_equipaments(user_id)
        return equipaments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{user_id}/equipaments/{equipament_id}", response_model=None, status_code=201)
def update_equipament(equipament_id: int, equipament_in: EquipamentUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_equipament(equipament_id, equipament_in)
        
    
    
