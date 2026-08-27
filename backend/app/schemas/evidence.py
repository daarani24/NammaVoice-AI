from pydantic import BaseModel
from datetime import datetime

class EvidenceResponse(BaseModel):
    id: int
    complaint_id: int
    image_url: str
    evidence_type: str
    created_at: datetime

    class Config:
        from_attributes=True