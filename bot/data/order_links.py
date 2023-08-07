from .base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from log_config import log

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
    
    def __repr__(self):
        return self.__str__()


async def add_order_link(user_id: int, link: str, user_name: str, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            new_order = OrderLinks(
                user_id=user_id,
                link=link,
                user_name=user_name
            )
            try:
                session.add(new_order)
            except Exception as e:
                log.info(e)


async def get_unpaid_orders(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(OrderLinks.link, OrderLinks.user_name)
                    .filter(OrderLinks.is_paid == False)
            )
            return result.all()
