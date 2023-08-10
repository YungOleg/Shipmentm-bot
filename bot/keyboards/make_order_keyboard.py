from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (SEND_LINK_BUTTON, BACK_BUTTON)

send_link_button = KeyboardButton(text=SEND_LINK_BUTTON)
back_button = KeyboardButton(text=BACK_BUTTON)

make_order_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [send_link_button],
        [back_button]
        ],
    resize_keyboard=True
    )