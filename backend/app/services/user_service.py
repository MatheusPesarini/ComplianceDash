from sqlalchemy.orm import Session

from app.core.password_hash import generate_hashed_password, verify_password
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserLogin

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_user(self, user_data: UserCreate) -> User:
        hashed_password = generate_hashed_password(user_data.password)
        
        new_user = User(name=user_data.name, phone=user_data.phone, email=user_data.email, hashed_password=hashed_password)
        
        return self.repository.create_user(new_user)
    
    def get_user(self, user_id: int) -> User:
        user = self.repository.get_user_by_id(user_id)
        
        if not user:
            raise ValueError(f"usere com ID {user_id} não encontrado")
        
        return user
    
    def login_user(self, user_data: UserLogin) -> User:
        user = self.repository.get_user_by_email(user_data.email)
        
        if not user:
            raise ValueError("Credenciais inválidas")
        
        if not verify_password(user_data.password, user.hashed_password):
            raise ValueError("Credenciais inválidas")
        
        return user
