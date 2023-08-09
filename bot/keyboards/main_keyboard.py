from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON)


main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

make_order_button = KeyboardButton(MAKE_ORDER_BUTTON)
consultation_button = KeyboardButton(CONSULTATION_BUTTON)

main_keyboard.add(make_order_button)
main_keyboard.add(consultation_button)