from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

view_all_orders_button = KeyboardButton("Посмотреть все заказы")
view_paid_orders_button = KeyboardButton("Посмотреть оплаченные заказы")
view_unpaid_orders_button = KeyboardButton("Посмотреть неоплаченные заказы")

admin_keyboard.add(view_all_orders_button)
admin_keyboard.add(view_paid_orders_button)
admin_keyboard.add(view_unpaid_orders_button)