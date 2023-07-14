from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from util import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
                  MESSAGE_TO_ADMIN_BUTTON, CALCULATE_COST_BUTTON, 
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
message_to_admin_button = KeyboardButton(MESSAGE_TO_ADMIN_BUTTON)
calculate_cost_button = KeyboardButton(CALCULATE_COST_BUTTON)
consultation_keyboard.add(message_to_admin_button)
consultation_keyboard.add(calculate_cost_button)
consultation_keyboard.add(back_button)

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# Кнопки: 
# 1. посмотреть статистику(все заказы)
# 2. посмотреть оплаченные заказы
# 3. посмотреть неоплаченные заказы