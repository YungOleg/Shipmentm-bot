from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# TODO перенести текст в string resources + продумать использование этой клавиатуры
calculate_cost_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

from_dollars_to_rubles_button = KeyboardButton("Перевести из долларов в рубли")
from_euro_to_rubles_button = KeyboardButton("Перевести из евро в рубли")

calculate_cost_keyboard.add(from_dollars_to_rubles_button)
calculate_cost_keyboard.add(from_euro_to_rubles_button)