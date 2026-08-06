from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComplaintCreate(BaseModel):
    title:str
    description:str
    category_id:int
    district_id:int
    department_id:int
    latitude:Optional[float]=None
    longitude:Optional[float]=None

class ComplaintResponse(BaseModel):
    id:int
    title:str
    description:str
    status:str
    citizen_id:int
    officer_id:Optional[int]
    category_id:int
    district_id:int
    department_id:int
    created_at:datetime

    class Config:
        from_attributes=True

class ComplaintStatusUpdate(BaseModel):
    status:str
    remarks:Optional[str]=None