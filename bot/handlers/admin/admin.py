from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from keyboards import admin_keyboard
from data import get_unpaid_orders, get_paid_orders

# TODO сделать обработку текста из admin_keyboard
# TODO сделать смену статуса оплаты(для уведомления пользователя)
# TODO сделать возможность менять статус покупки у конкретного пользователя


async def admin_menu(message: Message):
    await message.answer("Меню админа", reply_markup=admin_keyboard)


async def get_paid_order_to_admin(message: Message, session_maker: AsyncSession):
    list_of_orders = await get_paid_orders(session_maker=session_maker)
    await message.answer(f"Список оплаченных заказов:\n {list_of_orders}")


async def _format_order():
    ...