from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.api.deps import get_current_user
from app.schemas.user import UserResponse
from app.services import admin_service

router=APIRouter(prefix="/admin", tags=["admin"])

def require_admin(current_user=Depends(get_current_user)):
    if current_user.role!="admin":
        raise HTTPException(status_code=403, detail="Admin access only")
    return current_user

@router.get("/users", response_model=List[UserResponse])
def list_users(db: Session=Depends(get_db), current_user=Depends(require_admin)):
    return admin_service.list_all_users(db)