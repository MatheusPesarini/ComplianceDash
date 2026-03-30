from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.luthier_model import Client, Equipament

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_client_by_id(self, client_id: int) -> Client | None:
        stmt = select(Client).where(Client.id == client_id)
        return self.db.scalar(stmt)
    
    def create_client(self, client: Client) -> Client:
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    def get_equipaments_by_user_id(self, client_id: int) -> List[Equipament]:
        stmt = select(Equipament).where(Equipament.client_id == client_id)
        return list(self.db.scalars(stmt).all())
    
    def create_equipament(self, equipament: Equipament, client_id: int) -> Equipament:
        equipament.client_id = client_id
        self.db.add(equipament)
        self.db.commit()
        self.db.refresh(equipament)
        return equipament
        