from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, func
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.privacy_request_model import PrivacyRequest

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    
    privacy_requests: Mapped[List["PrivacyRequest"]] = relationship(back_populates="user")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    is_admin: Mapped[bool] = mapped_column(default=False, server_default="false")
    
    def __repr__(self) -> str:
        return f"<User id={self.id} name='{self.name}' email='{self.email}' phone='{self.phone}'>"
