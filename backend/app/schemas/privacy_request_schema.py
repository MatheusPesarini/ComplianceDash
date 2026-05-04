from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.privacy_request_model import RequestType, RequestStatus

class PrivacyRequestBase(BaseModel):
    request_type: RequestType
    details: Optional[str] = None

class PrivacyRequestCreate(PrivacyRequestBase):
    pass

class PrivacyRequestUpdate(BaseModel):
    status: Optional[RequestStatus] = None
    admin_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None

class PrivacyRequest(PrivacyRequestBase):
    id: int
    status: RequestStatus
    admin_notes: Optional[str] = None
    created_at: datetime
    resolved_at: Optional[datetime] = None
    user_id: int

    class Config:
        from_attributes = True
