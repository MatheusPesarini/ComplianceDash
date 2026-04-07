import enum

from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Enum, Float, ForeignKey, String, Text, func
from app.core.database import Base

class ServiceStatus(enum.Enum):
    PENDING = "Pendente"
    ESTIMATING = "Em Orçamento"
    APPROVED = "Aprovado"
    IN_PROGRESS = "Em Andamento"
    DONE = "Concluído"
    DELIVERED = "Entregue"

class Client(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    telephone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    equipaments: Mapped[List["Equipament"]] = relationship(back_populates="proprietary")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    
    def __repr__(self) -> str:
        return f"<Client id={self.id} name='{self.name}' email='{self.email}' telephone='{self.telephone}'>"
    
class Equipament(Base):
    __tablename__ = "equipaments"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    brand: Mapped[str] = mapped_column(String(100), nullable=False)
    
    service: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[ServiceStatus] = mapped_column(Enum(ServiceStatus), default=ServiceStatus.PENDING)
    
    price: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    entry_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    expected_delivery_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    delivery_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    proprietary: Mapped["Client"] = relationship(back_populates="equipaments")
    
    def __repr__(self) -> str:
        return f"<Equipament id={self.id} category='{self.category}' model='{self.model}' brand='{self.brand}' service='{self.service}'>"