from typing import List
from sqlalchemy.orm import Session

from app.models.equipament_model import Equipament
from app.repositories.equipament_repository import EquipamentRepository
from app.schemas.equipament_schema import EquipamentCreate, EquipamentUpdate
from app.services.user_service import UserService

class EquipamentService:
    def __init__(self, db: Session):
        self.repository = EquipamentRepository(db)
        self.user_service = UserService(db)
        
    def create_equipament(self, equipament_data: EquipamentCreate, user_id: int) -> Equipament:
        self.user_service.get_user(user_id)
        
        existing_equipament = self.repository.get_equipaments_by_user_id(user_id)
        if existing_equipament:
            raise ValueError(f"O usere com ID {user_id} já tem um equipamento registrado")
        
        new_equipament = Equipament(category=equipament_data.category, brand=equipament_data.brand, model=equipament_data.model, 
                                    service=equipament_data.service, status=equipament_data.status, price=equipament_data.price, 
                                    notes=equipament_data.notes, expected_delivery_date=equipament_data.expected_delivery_date)
        return self.repository.create_equipament(new_equipament, user_id)

    def get_user_equipaments(self, user_id: int) -> List[Equipament]:
        self.user_service.get_user(user_id)
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
