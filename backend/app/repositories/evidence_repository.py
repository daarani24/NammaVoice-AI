from app.models.complaint_evidence import ComplaintEvidence

def add_evidence(db, complaint_id, image_url, evidence_type, uploaded_by):
    evidence=ComplaintEvidence(
        complaint_id=complaint_id, image_url=image_url,
        evidence_type=evidence_type, uploaded_by=uploaded_by,
    )
    db.add(evidence)
    db.commit()
    db.refresh(evidence)
    return evidence

def get_by_complaint(db, complaint_id):
    return db.query(ComplaintEvidence).filter(ComplaintEvidence.complaint_id==complaint_id).all()