from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__='users'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False, unique=True)
    password_hash=Column(String, nullable=False)
    phone=Column(String, nullable=True)
    role=Column(String, nullable=False)

    department_id=Column(Integer, ForeignKey("departments.id"), nullable=True)
    district_id=Column(Integer, ForeignKey("districts.id"), nullable=True)

    created_at=Column(DateTime(timezone=True), server_default=func.now())

    department=relationship("Department")
    district=relationship("District")