from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.equipament_model import Equipament

class EquipamentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_equipaments_by_user_id(self, user_id: int) -> List[Equipament]:
        stmt = select(Equipament).where(Equipament.user_id == user_id)
        return list(self.db.scalars(stmt).all())
    
    def create_equipament(self, equipament: Equipament, user_id: int) -> Equipament:
        equipament.user_id = user_id
        self.db.add(equipament)
        self.db.commit()
        self.db.refresh(equipament)
        return equipament
    
    def get_equipament_by_id(self, equipament_id: int) -> Equipament | None:
        stmt = select(Equipament).where(Equipament.id == equipament_id)
        return self.db.scalar(stmt)
    
    def update_equipament(self, equipament: Equipament) -> Equipament:
        self.db.add(equipament)
        self.db.commit()
        self.db.refresh(equipament)
        return equipament
