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
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    proprietary: Mapped["User"] = relationship(back_populates="equipaments")
    
    def __repr__(self) -> str:
        return f"<Equipament id={self.id} category='{self.category}' model='{self.model}' brand='{self.brand}' service='{self.service}'>"
