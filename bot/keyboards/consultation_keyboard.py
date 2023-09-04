from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (CALCULATE_COST_BUTTON, BACK_BUTTON)


calculate_cost_button = KeyboardButton(text=CALCULATE_COST_BUTTON)
back_button = KeyboardButton(text=BACK_BUTTON)

consultation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [calculate_cost_button],
        [back_button]  
    ],
    resize_keyboard=True
    )