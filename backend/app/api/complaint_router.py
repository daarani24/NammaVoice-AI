from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.api.deps import get_current_user
from app.schemas.complaint import ComplaintCreate, ComplaintResponse
from app.services import complaint_service

router=APIRouter(prefix="/complaints", tags=["complaints"])

@router.post("/", response_model=ComplaintResponse)
def submit_complaint(data: ComplaintCreate, db: Session=Depends(get_db),
                      current_user=Depends(get_current_user)):
    return complaint_service.submit_complaint(db, current_user, data)

@router.get("/my", response_model=List[ComplaintResponse])
def my_complaints(db: Session=Depends(get_db),
                   current_user=Depends(get_current_user)):
    return complaint_service.get_my_complaints(db, current_user)