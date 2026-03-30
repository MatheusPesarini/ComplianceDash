from typing import List
from sqlalchemy.orm import Session

from app.models.luthier_model import Client, Equipament
from app.repositories.luthier_repository import UserRepository
from app.schemas.luthier_schema import ClientCreate, EquipamentCreate 

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_client(self, client_data: ClientCreate) -> Client:
        new_client = Client(name=client_data.name, telephone=client_data.telephone, email=client_data.email)
        return self.repository.create_client(new_client)
    
    def get_client(self, client_id: int) -> Client:
        client = self.repository.get_client_by_id(client_id)
        if not client:
            raise ValueError(f"Cliente com ID {client_id} não encontrado")
        return client
    
    def create_equipament(self, equipament_data: EquipamentCreate, client_id: int) -> Equipament:
        self.get_client(client_id)
        
        existing_equipament = self.repository.get_equipaments_by_user_id(client_id)
        if existing_equipament:
            raise ValueError(f"O cliente com ID {client_id} já tem um equipamento registrado")
        
        new_equipament = Equipament(category=equipament_data.category, brand=equipament_data.brand, model=equipament_data.model, service=equipament_data.service)
        return self.repository.create_equipament(new_equipament, client_id)

    def get_client_equipaments(self, client_id: int) -> List[Equipament]:
        self.get_client(client_id)
        return self.repository.get_equipaments_by_user_id(client_id)