from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services import auth_service

router=APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(data:UserCreate, db:Session=Depends(get_db)):
    return auth_service.register_user(db, data)

@router.post("/login")
def login(data:UserLogin, db:Session=Depends(get_db)):
    return auth_service.login_user(db, data)