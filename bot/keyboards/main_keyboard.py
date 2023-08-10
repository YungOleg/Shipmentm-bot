from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON)

make_order_button = KeyboardButton(text=MAKE_ORDER_BUTTON)
consultation_button = KeyboardButton(text=CONSULTATION_BUTTON)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [make_order_button],
        [consultation_button]
    ],
    resize_keyboard=True
    )