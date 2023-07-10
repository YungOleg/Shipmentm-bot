from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util import MAKE_ORDER_BUTTON, CONSULTATION_BUTTON

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton(MAKE_ORDER_BUTTON))
main_keyboard.add(KeyboardButton(CONSULTATION_BUTTON))

