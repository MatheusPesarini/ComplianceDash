from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from datetime import datetime
from app.models.privacy_request_model import PrivacyRequest
from app.schemas.privacy_request_schema import PrivacyRequestCreate, PrivacyRequestUpdate

class PrivacyRequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request_in: PrivacyRequestCreate, user_id: int) -> PrivacyRequest:
        db_obj = PrivacyRequest(
            request_type=request_in.request_type,
            details=request_in.details,
            user_id=user_id
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_by_id(self, request_id: int) -> Optional[PrivacyRequest]:
        return self.db.execute(select(PrivacyRequest).where(PrivacyRequest.id == request_id)).scalar_one_or_none()

    def get_by_user_id(self, user_id: int) -> List[PrivacyRequest]:
        return list(self.db.execute(select(PrivacyRequest).where(PrivacyRequest.user_id == user_id)).scalars().all())
    
    def get_all(self) -> List[PrivacyRequest]:
        return list(self.db.execute(select(PrivacyRequest)).scalars().all())

    def update(self, db_obj: PrivacyRequest, update_data: PrivacyRequestUpdate) -> PrivacyRequest:
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(db_obj, key, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: PrivacyRequest):
        self.db.delete(db_obj)
        self.db.commit()
