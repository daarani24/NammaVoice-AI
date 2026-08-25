from app.repositories import user_repository

def list_all_users(db):
    return user_repository.get_all_users(db)