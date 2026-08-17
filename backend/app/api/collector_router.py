from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_user
from app.services import collector_service

router=APIRouter(prefix="/collector", tags=["collector"])

@router.get("/dashboard")
def dashboard(db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    return collector_service.get_dashboard(db, current_user)