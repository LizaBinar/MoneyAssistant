from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, Float
from core.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_name = Column(Text(55), unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date_added = Column(DateTime)
    balans = Column(Float)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)