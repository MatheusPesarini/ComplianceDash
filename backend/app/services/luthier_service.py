from sqlalchemy.orm import Session

from app.models.luthier_model import Address, User
from app.repositories.luthier_repository import UserRepository
from app.schemas.luthier_schema import AddressCreate, UserCreate

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_user(self, user_data: UserCreate) -> User:
        new_user = User(name=user_data.name, fullname=user_data.fullname)
        return self.repository.create(new_user)
    
    def get_user(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"Usuário com ID {user_id} não encontrado")
        return user
    
    def create_user_address(self, address_data: AddressCreate, user_id: int) -> Address:
        self.get_user(user_id)
        
        existing_address = self.repository.get_address_by_user_id(user_id)
        if existing_address:
            raise ValueError(f"O usuário com ID {user_id} já tem endereço de email")
        
        new_address = Address(email_address=address_data.email_address)
        return self.repository.create_address(new_address, user_id)

    def get_user_address(self, user_id: int) -> Address:
        self.get_user(user_id)
        
        existing_address = self.repository.get_address_by_user_id(user_id)
        if not existing_address:
            raise ValueError(f"O usuário com ID {user_id} não tem endereço de email")
        
        return existing_address