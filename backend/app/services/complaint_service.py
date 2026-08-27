from app.repositories import complaint_repository
from fastapi import HTTPException
from app.repositories import complaint_repository, status_history_repository, evidence_repository
from app.core.cloud_storage import upload_image

def submit_complaint(db, current_user, data):
    return complaint_repository.create_complaint(db, current_user.id, data)

def get_my_complaints(db, current_user):
    return complaint_repository.get_complaints_by_citizen(db, current_user.id)

def get_department_pool(db, current_user):
    return complaint_repository.get_unassigned_by_department(db, current_user.department_id)

def accept_complaint(db, current_user, complaint_id):
    complaint=complaint_repository.get_by_id(db, complaint_id)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    if complaint.officer_id is not None:
        raise HTTPException(status_code=409, detail="Complaint already assigned")

    complaint=complaint_repository.assign_officer(db, complaint, current_user.id)
    status_history_repository.add_status_entry(db, complaint.id, "under_action", current_user.id)
    return complaint

def change_status(db, current_user, complaint_id, new_status, remarks: str = None):
    complaint=complaint_repository.get_by_id(db, complaint_id)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    if complaint.officer_id!=current_user.id:
        raise HTTPException(status_code=403, detail="Not your assigned complaint")

    complaint=complaint_repository.update_status(db, complaint, new_status)
    status_history_repository.add_status_entry(db, complaint.id, new_status, current_user.id, remarks)
    return complaint

def upload_complaint_evidence(db, current_user, complaint_id, file, evidence_type):
    complaint=complaint_repository.get_by_id(db, complaint_id)
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    if evidence_type=="initial" and complaint.citizen_id!=current_user.id:
        raise HTTPException(status_code=403, detail="Not your complaint")
    if evidence_type=="completion" and complaint.officer_id!=current_user.id:
        raise HTTPException(status_code=403, detail="Not your assigned complaint")

    image_url=upload_image(file)
    return evidence_repository.add_evidence(db, complaint_id, image_url, evidence_type, current_user.id)