from app.repositories import complaint_repository

def get_dashboard(db, current_user):
    stats=complaint_repository.get_district_stats(db, current_user.district_id)
    complaints=complaint_repository.get_all_by_district(db, current_user.district_id)
    return {"stats": stats, "complaints": complaints}