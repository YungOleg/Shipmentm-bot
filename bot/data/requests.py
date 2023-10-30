from .models import OrderLinks
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
# from log_config import log

# TODO сделать функцию удаления заказа

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
                # log.info(e)
                ...


async def get_unpaid_orders(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(OrderLinks.link, OrderLinks.user_name, OrderLinks.order_time, OrderLinks.id)
                    .where(OrderLinks.is_paid == False)
            )
            full_result = [(link, user_name, order_time.strftime('%d.%m.%Y'), id) for link, user_name, order_time, id in result.all()]
            return full_result


async def get_paid_orders(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(OrderLinks.link, OrderLinks.user_name, OrderLinks.order_time, OrderLinks.id)
                    .where(OrderLinks.is_paid == True)
            )
            full_result = [(link, user_name, order_time.strftime('%d.%m.%Y'), id) for link, user_name, order_time, id in result.all()]
            return full_result


async def select_all(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(OrderLinks.link, OrderLinks.is_paid, OrderLinks.order_time, OrderLinks.user_id, OrderLinks.user_name, OrderLinks.id)
            )
            full_result = [
                (link, "Paid" if is_paid else "Unpaid", order_time.strftime('%d.%m.%Y %H:%M:%S'), user_id, user_name, id)
                for link, is_paid, order_time, user_id, user_name, id in result.all()
            ]
            return full_result


async def delete_order_by_username(session_maker: sessionmaker, user_name: str):
    """Удаляет все заказы 1 пользователя"""
    async with session_maker() as session:
        async with session.begin():
            try:
                orders_to_delete = await session.execute(
                    select(OrderLinks).filter_by(user_name=user_name)
                )
                for order in orders_to_delete.scalars():
                    await session.delete(order)
                await session.commit()
            except Exception as e:
                pass


async def delete_order_by_id(session_maker: sessionmaker, id: int):
    """Удаляет заказ по id"""
    ...


async def change_is_paid(session_maker: sessionmaker, user_name: str):
    ...