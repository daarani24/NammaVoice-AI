from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email==email).first()

def create_user(db:Session, name:str, email:str, password_hash:str, role:str, phone:str=None, district_id:int=None, department_id:int=None):
    user=User(
        name=name, 
        email=email, 
        password_hash=password_hash, 
        role=role, 
        phone=phone, 
        district_id=district_id, 
        department_id=department_id,)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

