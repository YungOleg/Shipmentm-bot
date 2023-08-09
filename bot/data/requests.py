from .models import OrderLinks
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from log_config import log


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
                    .where(OrderLinks.is_paid == False)
            )
            return result.all()