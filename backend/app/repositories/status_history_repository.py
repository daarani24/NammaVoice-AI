from app.models.complaint_status_history import ComplaintStatusHistory

def add_status_entry(db, complaint_id, status, changed_by, remarks: str=None):
    entry = ComplaintStatusHistory(
        complaint_id=complaint_id, status=status, changed_by=changed_by, remarks=remarks
    )
    db.add(entry)
    db.commit()