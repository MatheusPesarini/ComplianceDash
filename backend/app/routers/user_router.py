from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

@router.get("/{user_id}")
def read_user(user_id: int):
    