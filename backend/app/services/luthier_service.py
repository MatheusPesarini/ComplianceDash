from typing import List
from sqlalchemy.orm import Session

from app.core.security import generate_hashed_password, verify_password
from app.models.luthier_model import Client, Equipament
from app.repositories.luthier_repository import UserRepository
from app.schemas.luthier_schema import ClientCreate, ClientLogin, EquipamentCreate, EquipamentUpdate 

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_client(self, client_data: ClientCreate) -> Client:
        hashed_password = generate_hashed_password(client_data.password)
        
        new_client = Client(name=client_data.name, telephone=client_data.telephone, email=client_data.email, hashed_password=hashed_password)
        
        return self.repository.create_client(new_client)
    
    def get_client(self, client_id: int) -> Client:
        client = self.repository.get_client_by_id(client_id)
        
        if not client:
            raise ValueError(f"Cliente com ID {client_id} não encontrado")
        
        return client
    
    def login_client(self, client_data: ClientLogin) -> Client:
        client = self.repository.get_client_by_email(client_data.email)
        
        if not client:
            raise ValueError("Credenciais inválidas")
        
        if not verify_password(client_data.password, client.hashed_password):
            raise ValueError("Credenciais inválidas")
        
        return client
    
    def create_equipament(self, equipament_data: EquipamentCreate, client_id: int) -> Equipament:
        self.get_client(client_id)
        
        existing_equipament = self.repository.get_equipaments_by_user_id(client_id)
        if existing_equipament:
            raise ValueError(f"O cliente com ID {client_id} já tem um equipamento registrado")
        
        new_equipament = Equipament(category=equipament_data.category, brand=equipament_data.brand, model=equipament_data.model, 
                                    service=equipament_data.service, status=equipament_data.status, price=equipament_data.price, 
                                    notes=equipament_data.notes, expected_delivery_date=equipament_data.expected_delivery_date)
        return self.repository.create_equipament(new_equipament, client_id)

    def get_client_equipaments(self, client_id: int) -> List[Equipament]:
        self.get_client(client_id)
        return self.repository.get_equipaments_by_user_id(client_id)
    
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