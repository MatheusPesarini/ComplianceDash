from typing import List
from sqlalchemy.orm import Session

from app.core.security import generate_hashed_password, verify_password
from app.models.luthier_model import user, Equipament
from app.repositories.luthier_repository import UserRepository
from app.schemas.luthier_schema import userCreate, userLogin, EquipamentCreate, EquipamentUpdate 

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_user(self, user_data: userCreate) -> user:
        hashed_password = generate_hashed_password(user_data.password)
        
        new_user = user(name=user_data.name, telephone=user_data.telephone, email=user_data.email, hashed_password=hashed_password)
        
        return self.repository.create_user(new_user)
    
    def get_user(self, user_id: int) -> user:
        user = self.repository.get_user_by_id(user_id)
        
        if not user:
            raise ValueError(f"usere com ID {user_id} não encontrado")
        
        return user
    
    def login_user(self, user_data: userLogin) -> user:
        user = self.repository.get_user_by_email(user_data.email)
        
        if not user:
            raise ValueError("Credenciais inválidas")
        
        if not verify_password(user_data.password, user.hashed_password):
            raise ValueError("Credenciais inválidas")
        
        return user
    
    def create_equipament(self, equipament_data: EquipamentCreate, user_id: int) -> Equipament:
        self.get_user(user_id)
        
        existing_equipament = self.repository.get_equipaments_by_user_id(user_id)
        if existing_equipament:
            raise ValueError(f"O usere com ID {user_id} já tem um equipamento registrado")
        
        new_equipament = Equipament(category=equipament_data.category, brand=equipament_data.brand, model=equipament_data.model, 
                                    service=equipament_data.service, status=equipament_data.status, price=equipament_data.price, 
                                    notes=equipament_data.notes, expected_delivery_date=equipament_data.expected_delivery_date)
        return self.repository.create_equipament(new_equipament, user_id)

    def get_user_equipaments(self, user_id: int) -> List[Equipament]:
        self.get_user(user_id)
        return self.repository.get_equipaments_by_user_id(user_id)
    
    def update_equipament(self, equipament_id: int, update_data: EquipamentUpdate) -> Equipament:
        equipament = self.repository.get_equipament_by_id(equipament_id)
        if not equipament:
            raise ValueError(f"Equipamento com ID {equipament_id} não encontrado")
        
        if update_data.status is not None:
            equipament.status = update_data.status
            
        if update_data.price is not None:
            equipament.price = update_data.price
            
        if update_data.notes is not None:
            equipament.notes = update_data.notes
            
        if update_data.expected_delivery_date is not None:
            equipament.expected_delivery_date = update_data.expected_delivery_date
            
        return self.repository.update_equipament(equipament)