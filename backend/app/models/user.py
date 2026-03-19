from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import Optional
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    fullname: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    addresses: Mapped["Address"] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"<User id={self.id} name='{self.name}' fullname='{self.fullname}'>"
    
class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    
    user: Mapped["User"] = relationship(back_populates="addresses")
    
    def __repr__(self) -> str:
        return f"<Address id={self.id} email_address='{self.email_address}'>"