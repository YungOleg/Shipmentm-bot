from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (FAQ_BUTTON, CALCULATE_COST_BUTTON, BACK_BUTTON)


consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

faq_button = KeyboardButton(FAQ_BUTTON)
calculate_cost_button = KeyboardButton(CALCULATE_COST_BUTTON)
back_button = KeyboardButton(BACK_BUTTON)

consultation_keyboard.add(faq_button)
consultation_keyboard.add(calculate_cost_button)
consultation_keyboard.add(back_button)