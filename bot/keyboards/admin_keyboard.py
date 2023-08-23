from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from util import (
    VIEW_ALL_ORDERS_BUTTON,
    VIEW_PAID_ORDERS_BUTTON,
    VIEW_UNPAID_ORDERS_BUTTON,
    BACK_BUTTON
)

view_all_orders_button = InlineKeyboardButton(text=VIEW_ALL_ORDERS_BUTTON, callback_data="view_all_orders")
view_paid_orders_button = InlineKeyboardButton(text=VIEW_PAID_ORDERS_BUTTON, callback_data="view_paid_orders")
view_unpaid_orders_button = InlineKeyboardButton(text=VIEW_UNPAID_ORDERS_BUTTON, callback_data="view_unpaid_orders")
back_button = InlineKeyboardButton(text=BACK_BUTTON, callback_data="back")

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [view_all_orders_button],
        [view_paid_orders_button],
        [view_unpaid_orders_button],
        [back_button]
    ]
)
