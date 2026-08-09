from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.api.deps import get_current_user
from app.schemas.complaint import ComplaintResponse, ComplaintStatusUpdate
from app.services import complaint_service

router=APIRouter(prefix="/officer", tags=["officer"])

@router.get("/pool", response_model=List[ComplaintResponse])
def department_pool(db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    return complaint_service.get_department_pool(db, current_user)

@router.post("/{complaint_id}/accept", response_model=ComplaintResponse)
def accept(complaint_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return complaint_service.accept_complaint(db, current_user, complaint_id)

@router.patch("/{complaint_id}/status", response_model=ComplaintResponse)
def update_status(complaint_id: int, data: ComplaintStatusUpdate,
                   db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return complaint_service.change_status(db, current_user, complaint_id, data.status, data.remarks)