from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util import (
    VIEW_ALL_ORDERS_BUTTON, 
    VIEW_PAID_ORDERS_BUTTON, 
    VIEW_UNPAID_ORDERS_BUTTON, 
    BACK_BUTTON
    )

view_all_orders_button = KeyboardButton(text=VIEW_ALL_ORDERS_BUTTON)
view_paid_orders_button = KeyboardButton(text=VIEW_PAID_ORDERS_BUTTON)
view_unpaid_orders_button = KeyboardButton(text=VIEW_UNPAID_ORDERS_BUTTON)
back_button = KeyboardButton(text=BACK_BUTTON)

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [view_all_orders_button],
        [view_paid_orders_button],
        [view_unpaid_orders_button], 
        [back_button]
    ],
    resize_keyboard=True
    )