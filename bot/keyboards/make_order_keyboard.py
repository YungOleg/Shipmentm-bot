from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (SEND_LINK_BUTTON, BACK_BUTTON)

# TODO: добавить комментарий к заказу(размер или что то другое)

poizon_button = KeyboardButton(text="Заказать с Poizon")
tradeinn_button = KeyboardButton(text="Заказать с Tradeinn")
other_button = KeyboardButton(text="Заказать из другого места")
back_button = KeyboardButton(text=BACK_BUTTON)

make_order_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [poizon_button],
        [tradeinn_button],
        [other_button],
        [back_button]
        ],
    resize_keyboard=True
    )