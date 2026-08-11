from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.district import District
from app.models.department import Department
from app.models.category import Category
from app.schemas.district import DistrictCreate, DistrictResponse
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/reference", tags=["reference"])

@router.post("/districts", response_model=DistrictResponse)
def create_district(data: DistrictCreate, db: Session = Depends(get_db)):
    obj = District(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.post("/departments", response_model=DepartmentResponse)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    obj = Department(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.post("/categories", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    obj = Category(name=data.name, department_id=data.department_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj