from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserCreateResponse, UserLogin, UserLoginResponse
from app.services.user_service import UserService
from app.core.token_jwt import create_acess_token, verify_token


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
        token = create_acess_token()
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
