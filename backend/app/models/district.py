from sqlalchemy import Column, Integer, String
from app.core.database import Base

class District(Base):
    __tablename__="districts"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False, unique=True)
    