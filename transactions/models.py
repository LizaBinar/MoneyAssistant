from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    value = Column(Float)
    date_added = Column(DateTime)
    category = Column(Text)
    user = Column(Integer, ForeignKey("users.id"))
    user_id = relationship("User")