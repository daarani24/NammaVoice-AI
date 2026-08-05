from pydantic import BaseModel

class DistrictCreate(BaseModel):
    name:str

class DistrictResponse(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes=True
        