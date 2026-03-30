from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import Optional
from app.core.database import Base

class Client(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    telephone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    
    
    def __repr__(self) -> str:
        return f"<Client id={self.id} name='{self.name}' email='{self.email}' telephone='{self.telephone}'>"
    
class Equipament(Base):
    __tablename__ = "equipaments"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    brand: Mapped[str] = mapped_column(String(100), nullable=False)
    service: Mapped[str] = mapped_column(String(200), nullable=False)
    
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    
    proprietary: Mapped["Client"] = relationship(back_populates="equipaments")
    
    def __repr__(self) -> str:
        return f"<Equipament id={self.id} category='{self.category}' model='{self.model}' brand='{self.brand}' service='{self.service}'>"