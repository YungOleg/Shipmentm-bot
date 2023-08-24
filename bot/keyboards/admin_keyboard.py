from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from util import (
    VIEW_ALL_ORDERS_BUTTON,
    VIEW_PAID_ORDERS_BUTTON,
    VIEW_UNPAID_ORDERS_BUTTON, 
    AdminCDAction, AdminCD
)

view_all_orders_button = InlineKeyboardButton(
    text=VIEW_ALL_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_ALL_ORDERS).pack()
    )
view_paid_orders_button = InlineKeyboardButton(
    text=VIEW_PAID_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_PAID_ORDERS).pack()
    )
view_unpaid_orders_button = InlineKeyboardButton(
    text=VIEW_UNPAID_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_UNPAID_ORDERS).pack()
    )
# view_all_order_by_user = InlineKeyboardButton(text="Посмотреть заказы пользователя по юзернейму", callback_data=AdminCD(action=AdminCDAction.).pack())
close_button = InlineKeyboardButton(text="Закрыть ❌", callback_data=AdminCD(action=AdminCDAction.CLOSE).pack())


admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [view_all_orders_button],
        [view_paid_orders_button],
        [view_unpaid_orders_button],
        # [view_all_order_by_user],
        [close_button]
    ]
)