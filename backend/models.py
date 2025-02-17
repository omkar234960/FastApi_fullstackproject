from .database import Base
from sqlalchemy import Column, Integer, String, Float,DateTime,Boolean,DATETIME,Date
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    add=Column(Boolean)
    Quantity=Column(Integer)
    price=Column(Float)
    date_added = Column(DateTime, default=datetime.utcnow)
