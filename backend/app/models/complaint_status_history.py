from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ComplaintStatusHistory(Base):
    __tablename__="complaint_status_history"

    id=Column(Integer, primary_key=True, index=True)
    complaint_id=Column(Integer, ForeignKey("complaints.id"), nullable=False)
    status=Column(String, nullable=False)
    changed_by=Column(Integer, ForeignKey("users.id"), nullable=False)
    remarks=Column(String, nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    complaint=relationship("Complaint")
    changed_by_user=relationship("User", foreign_keys=[changed_by])
