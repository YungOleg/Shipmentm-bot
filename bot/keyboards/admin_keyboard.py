from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


view_all_orders_button = KeyboardButton(text="Посмотреть все заказы")
view_paid_orders_button = KeyboardButton(text="Посмотреть оплаченные заказы")
view_unpaid_orders_button = KeyboardButton(text="Посмотреть неоплаченные заказы")


admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [view_all_orders_button],
        [view_paid_orders_button],
        [view_unpaid_orders_button]
    ],
    resize_keyboard=True
    )