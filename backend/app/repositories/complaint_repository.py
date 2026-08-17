from sqlalchemy import func
from app.models.complaint import Complaint

def create_complaint(db, citizen_id, data):
    complaint=Complaint(
        citizen_id=citizen_id,
        title=data.title,
        description=data.description,
        category_id=data.category_id,
        district_id=data.district_id,
        department_id=data.department_id,
        latitude=data.latitude,
        longitude=data.longitude,
    )
    db.add(complaint)
    db.commit()
    db.refresh(complaint)
    return complaint

def get_complaints_by_citizen(db, citizen_id):
    return db.query(Complaint).filter(Complaint.citizen_id==citizen_id).all()

def get_unassigned_by_department(db, department_id):
    return db.query(Complaint).filter(
        Complaint.department_id==department_id,
        Complaint.officer_id.is_(None)
    ).all()

def get_by_id(db, complaint_id):
    return db.query(Complaint).filter(Complaint.id==complaint_id).first()

def assign_officer(db, complaint, officer_id):
    complaint.officer_id=officer_id
    complaint.status="under_action"
    db.commit()
    db.refresh(complaint)
    return complaint

def update_status(db, complaint, new_status):
    complaint.status=new_status
    db.commit()
    db.refresh(complaint)
    return complaint

def get_district_stats(db, district_id):
    total=db.query(Complaint).filter(Complaint.district_id==district_id).count()
    pending=db.query(Complaint).filter(
        Complaint.district_id==district_id,
        Complaint.status.in_(["submitted", "under_action"])
    ).count()
    completed=db.query(Complaint).filter(
        Complaint.district_id==district_id, Complaint.status=="completed"
    ).count()
    return {"total": total, "pending": pending, "completed": completed}

def get_all_by_district(db, district_id):
    return db.query(Complaint).filter(Complaint.district_id==district_id).all()