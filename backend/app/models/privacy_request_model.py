from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Enum, ForeignKey, Text, func
import enum
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user_model import User

class RequestType(enum.Enum):
    ACCESS = "access"
    DELETION = "deletion"
    CORRECTION = "correction"
    PORTABILITY = "portability"
    OPT_OUT = "opt_out"

class RequestStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    REJECTED = "rejected"

class PrivacyRequest(Base):
    __tablename__ = "privacy_requests"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    request_type: Mapped[RequestType] = mapped_column(Enum(RequestType), nullable=False)
    status: Mapped[RequestStatus] = mapped_column(Enum(RequestStatus), default=RequestStatus.PENDING)
    
    details: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    admin_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="privacy_requests")
    
    def __repr__(self) -> str:
        return f"<PrivacyRequest id={self.id} type='{self.request_type.value}' status='{self.status.value}'>"
