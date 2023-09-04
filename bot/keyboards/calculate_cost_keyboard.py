from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from_dollars_to_rubles_button = KeyboardButton(text="Перевести из долларов в рубли")
from_euro_to_rubles_button = KeyboardButton(text="Перевести из евро в рубли")

# TODO перенести текст в string resources + продумать использование этой клавиатуры

calculate_cost_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [from_dollars_to_rubles_button],
        [from_euro_to_rubles_button]
    ],
    resize_keyboard=True
    )