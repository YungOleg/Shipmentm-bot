from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (SEND_LINK_BUTTON, BACK_BUTTON)


make_order_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

send_link_button = KeyboardButton(SEND_LINK_BUTTON)
back_button = KeyboardButton(BACK_BUTTON)

make_order_keyboard.add(send_link_button)
make_order_keyboard.add(back_button)