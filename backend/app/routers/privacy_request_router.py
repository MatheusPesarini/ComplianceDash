from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.privacy_request_schema import PrivacyRequest, PrivacyRequestCreate, PrivacyRequestUpdate
from app.services.privacy_request_service import PrivacyRequestService
from app.core.token_jwt import get_current_user

router = APIRouter(prefix="/privacy-requests", tags=["Privacy Requests"])

@router.post("/", response_model=PrivacyRequest, status_code=status.HTTP_201_CREATED)
def create_request(
    request_in: PrivacyRequestCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    return service.create_request(request_in, current_user.id)

@router.get("/me", response_model=List[PrivacyRequest])
def read_my_requests(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    return service.get_user_requests(current_user.id)

@router.get("/", response_model=List[PrivacyRequest])
def read_all_requests(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    return service.get_all_requests()

@router.get("/{request_id}", response_model=PrivacyRequest)
def read_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    return service.get_request_by_id(request_id)

@router.patch("/{request_id}", response_model=PrivacyRequest)
def update_request(
    request_id: int,
    request_in: PrivacyRequestUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    return service.update_request(request_id, request_in)

@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PrivacyRequestService(db)
    service.delete_request(request_id)
