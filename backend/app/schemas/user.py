from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str
    phone:Optional[str]=None
    role:str
    district_id:Optional[int]=None
    department_id:Optional[int]=None

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    role:str

    class Config:
        from_attributes=True