from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.db.scalar(stmt)
        
    def get_user_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return self.db.scalar(stmt)
    
    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
