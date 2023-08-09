from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# TODO сделать admin keyboard

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# Кнопки: 
# 1. посмотреть статистику(все заказы)
# 2. посмотреть оплаченные заказы
# 3. посмотреть неоплаченные заказы