from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ComplaintEvidence(Base):
    __tablename__="complaint_evidence"

    id=Column(Integer, primary_key=True, index=True)
    complaint_id=Column(Integer, ForeignKey("complaints.id"), nullable=False)
    image_url=Column(String, nullable=False)
    evidence_type=Column(String, nullable=False)
    uploaded_by=Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    complaint=relationship("Complaint")
    uploaded_by_user=relationship("User",foreign_keys=[uploaded_by])