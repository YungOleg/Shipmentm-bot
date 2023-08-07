from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util.string_resources import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
                  FAQ_BUTTON, CALCULATE_COST_BUTTON, 
                  SEND_LINK_BUTTON, BACK_BUTTON)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
make_order_button = KeyboardButton(MAKE_ORDER_BUTTON)
consultation_button = KeyboardButton(CONSULTATION_BUTTON)

main_keyboard.add(make_order_button)
main_keyboard.add(consultation_button)

back_button = KeyboardButton(BACK_BUTTON)

make_order_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
send_link_button = KeyboardButton(SEND_LINK_BUTTON)

make_order_keyboard.add(send_link_button)
make_order_keyboard.add(back_button)

consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
faq_button = KeyboardButton(FAQ_BUTTON)
calculate_cost_button = KeyboardButton(CALCULATE_COST_BUTTON)

consultation_keyboard.add(faq_button)
consultation_keyboard.add(calculate_cost_button)
consultation_keyboard.add(back_button)

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# Кнопки: 
# 1. посмотреть статистику(все заказы)
# 2. посмотреть оплаченные заказы
# 3. посмотреть неоплаченные заказы

calculate_cost_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
from_dollars_to_rubles_button = KeyboardButton("Перевести из долларов в рубли")
from_euro_to_rubles_button = KeyboardButton("Перевести из евро в рубли")

calculate_cost_keyboard.add(from_dollars_to_rubles_button)
calculate_cost_keyboard.add(from_euro_to_rubles_button)