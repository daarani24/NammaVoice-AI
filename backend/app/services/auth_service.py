from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import user_repository
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db:Session, data):
    existing=user_repository.get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")

    hashed=hash_password(data.password)
    user=user_repository.create_user(
        db, name=data.name, email=data.email, password_hash=hashed,
        role=data.role, phone=data.phone,
        district_id=data.district_id, department_id=data.department_id,
    )
    return user

def login_user(db: Session, data):
    user=user_repository.get_user_by_email(db, data.email)
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token=create_access_token({"sub": str(user.id), "role": user.role})
    return {"access_token": token, "token_type": "bearer"}