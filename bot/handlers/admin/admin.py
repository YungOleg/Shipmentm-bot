from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from keyboards import admin_keyboard
from util import AdminCD
from data import (
    get_unpaid_orders, 
    get_paid_orders, select_all, 
    delete_order_by_id, change_is_paid
    )


# TODO сделать смену статуса оплаты(для уведомления пользователя)
# TODO сделать возможность менять статус покупки у конкретного пользователя
# TODO сделать возможность смены статуса покупки (is_paid) поле
# TODO сделать возможность удаления заказа(в случае некорректного)


async def admin_menu(message: Message):
    await message.answer("Меню админа", reply_markup=admin_keyboard)


async def get_unpaid_order_to_admin(call: CallbackQuery, session_maker: AsyncSession):
    list_of_orders = await get_unpaid_orders(session_maker=session_maker)
    if list_of_orders:
        formated_list_of_orders = await _format_order(list_of_orders)
        await call.message.answer(formated_list_of_orders)
        await call.answer()
        return
    await call.answer(show_alert=True, text="У вас нет неоплаченных заказов")


async def get_paid_order_to_admin(call: CallbackQuery, session_maker: AsyncSession):
    list_of_orders = await get_paid_orders(session_maker=session_maker)
    if list_of_orders:
        formated_list_of_orders = await _format_order(list_of_orders)
        await call.message.answer(formated_list_of_orders)
        await call.answer()
        return
    await call.answer(show_alert=True, text="У вас нет оплаченных заказов")


async def change_is_paid(call: CallbackQuery, session_maker: AsyncSession):
    ...


async def delete_order_by_id(call: CallbackQuery, session_maker: AsyncSession):
    ...


async def select_all(call: CallbackQuery, session_maker: AsyncSession):
    ...


async def close_admin(call: CallbackQuery):
    await call.message.delete()
    await call.answer()


async def _format_order(list_of_orders) -> str:
    formated_list_of_orders = [
        f"@{order[1]} - {order[2]}\r\n{order[0]}" 
        for order in list_of_orders
        ]
    formated_string = '\n\n'.join(formated_list_of_orders)
    return formated_string