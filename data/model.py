from .base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.sql import func

class OrderLinks(BaseModel):
    __tablename__ = 'order_links'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    link = Column(String(1023), nullable=False)
    is_paid = Column(Boolean, default=False)
    order_time = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    user_id = Column(Integer, nullable=False)
    user_name = Column(String(255), nullable=False)
    
    def __str__(self) -> str:
        return f"User: {self.id}, username: {self.user_name}"