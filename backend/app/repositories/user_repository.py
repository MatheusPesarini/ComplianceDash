from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User, Address

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return self.db.scalar(stmt)
    
    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_address_by_user_id(self, user_id: int) -> Address | None:
        stmt = select(Address).where(Address.user_id == user_id)
        return self.db.scalar(stmt)
    
    def create_address(self, address: Address, user_id: int) -> Address:
        address.user_id = user_id
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address
        