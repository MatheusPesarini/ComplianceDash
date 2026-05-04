from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.privacy_request_repository import PrivacyRequestRepository
from app.schemas.privacy_request_schema import PrivacyRequestCreate, PrivacyRequestUpdate
from app.models.privacy_request_model import PrivacyRequest, RequestStatus
from datetime import datetime, UTC

class PrivacyRequestService:
    def __init__(self, db: Session):
        self.repository = PrivacyRequestRepository(db)

    def create_request(self, request_in: PrivacyRequestCreate, user_id: int) -> PrivacyRequest:
        return self.repository.create(request_in, user_id)

    def get_user_requests(self, user_id: int) -> List[PrivacyRequest]:
        return self.repository.get_by_user_id(user_id)

    def get_all_requests(self) -> List[PrivacyRequest]:
        return self.repository.get_all()

    def get_request_by_id(self, request_id: int) -> PrivacyRequest:
        db_obj = self.repository.get_by_id(request_id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Privacy Request not found")
        return db_obj

    def update_request(self, request_id: int, request_in: PrivacyRequestUpdate) -> PrivacyRequest:
        db_obj = self.get_request_by_id(request_id)
        
        if request_in.status in [RequestStatus.RESOLVED, RequestStatus.REJECTED] and request_in.resolved_at is None:
            request_in.resolved_at = datetime.now(UTC).replace(tzinfo=None)
            
        return self.repository.update(db_obj, request_in)

    def delete_request(self, request_id: int) -> None:
        db_obj = self.get_request_by_id(request_id)
        self.repository.delete(db_obj)
