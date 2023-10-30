from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.dispatcher.fsm.context import FSMContext
from keyboards import admin_keyboard
from util import AdminCD
from data import (
    get_unpaid_orders, 
    get_paid_orders, select_all, 
    delete_order_by_username, change_is_paid
    )
from states import WaitUsernameForDelete, WaitUsernameForChange

# TODO сделать возможность смены статуса покупки (is_paid) поле
# TODO сделать возможность удаления заказа(в случае некорректного)


async def admin_menu(message: Message):
    await message.answer("Выбери действие⚙️", reply_markup=admin_keyboard)


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


async def wait_id_for_delete(call: CallbackQuery, state: FSMContext):
    await state.set_state(WaitUsernameForDelete.waiting_for_send_username)
    await call.message.answer("Отправь id заказа, чтобы его удалить")
    await call.answer()


async def wait_username_for_change(call: CallbackQuery, state: FSMContext):
    await state.set_state(WaitUsernameForChange.waiting_for_send_username)
    await call.message.answer("Отправь username пользователя\r\n Удаляться все заказы пользователя с этим username")
    await call.answer()


async def admin_change_is_paid(message: Message, state: FSMContext, session_maker: AsyncSession):
    ...


async def admin_delete_order_by_id(message: Message, state: FSMContext, session_maker: AsyncSession):
    user_name = message.text.strip()
    if "@" in user_name:
        user_name = user_name[1:]
    if user_name == "Отмена":
        # TODO сделать отмену ввода юзернейма
        ...
    print(user_name)
    await delete_order_by_username(session_maker=session_maker, user_name=user_name)
    await message.answer("Заказ пользователя удален")


async def view_all_orders(call: CallbackQuery, session_maker: AsyncSession):
    list_of_orders = await select_all(session_maker=session_maker)
    if list_of_orders:
        formated_list_of_orders = await _format_select_all_order(list_of_orders)
        await call.message.answer(formated_list_of_orders)
        await call.answer()
        return
    await call.answer(show_alert=True, text="На данный момент у вас нет заказов")


async def close_admin(call: CallbackQuery):
    await call.message.delete()
    await call.answer()


async def _format_order(list_of_orders) -> str:
    formated_list_of_orders = [
        f"@{order[1]} - {order[2]}\r\n{order[0]}\r\nНомер заказа: {str(order[3])}" 
        for order in list_of_orders
        ]
    formated_string = '\n\n'.join(formated_list_of_orders)
    return formated_string


async def _format_select_all_order(list_of_orders) -> str:
    formated_list_of_orders = [
        f"@{order[4]} - id: {order[3]}\r\n{order[2]} - {order[1]}\r\n{order[0]}\r\nНомер заказа: {str(order[5])}"
        for order in list_of_orders
    ]
    formated_string = '\n\n'.join(formated_list_of_orders)
    return formated_string