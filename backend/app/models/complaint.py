from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Complaint(Base):
    __tablename__="complaints"

    id=Column(Integer, primary_key=True, index=True)

    citizen_id=Column(Integer, ForeignKey("users.id"), nullable=False)
    officer_id=Column(Integer, ForeignKey("users.id"), nullable=True)
    category_id=Column(Integer, ForeignKey("categories.id"), nullable=False)
    department_id=Column(Integer, ForeignKey("departments.id"), nullable=False)
    district_id=Column(Integer, ForeignKey("districts.id"), nullable=False)

    title=Column(String, nullable=False)
    description=Column(String, nullable=False)
    latitude=Column(Float, nullable=True)
    longitude=Column(Float, nullable=True)
    status=Column(String, nullable=False, default="submitted")

    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), onupdate=func.now())

    citizen=relationship("User", foreign_keys=[citizen_id])
    officer_id=relationship("user", foreign_keys=[officer_id])
    category=relationship("Category")
    department=relationship("Department")
    district=relationship("District")