from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from keyboards import admin_keyboard
from data import get_unpaid_orders, get_paid_orders

# TODO сделать обработку текста из admin_keyboard
# TODO сделать смену статуса оплаты(для уведомления пользователя)
# TODO сделать возможность менять статус покупки у конкретного пользователя
# TODO сделать возможность смены статуса заказа
# TODO сделать возможность смены статуса покупки (is_paid) поле
# TODO сделать возможность удаления заказа(в случае некорректного)


async def admin_menu(message: Message):
    await message.answer("Меню админа", reply_markup=admin_keyboard)


async def get_unpaid_order_to_admin(message: Message, session_maker: AsyncSession):
    list_of_orders = await get_unpaid_orders(session_maker=session_maker)
    
    formated_list_of_orders = await _format_order(list_of_orders)
    await message.answer(formated_list_of_orders)


async def get_paid_order_to_admin(message: Message, session_maker: AsyncSession):
    list_of_orders = await get_paid_orders(session_maker=session_maker)
    
    formated_list_of_orders = await _format_order(list_of_orders)
    await message.answer(formated_list_of_orders)


async def _format_order(list_of_orders) -> str:
    formated_list_of_orders = [
        f"@{order[1]} - {order[2]}\r\n{order[0]}" 
        for order in list_of_orders
        ]
    formated_string = '\n\n'.join(formated_list_of_orders)
    return formated_string