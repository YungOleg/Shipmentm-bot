from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from util import (
    VIEW_ALL_ORDERS_BUTTON,
    VIEW_PAID_ORDERS_BUTTON,
    VIEW_UNPAID_ORDERS_BUTTON, 
    AdminCDAction, AdminCD
)

view_all_orders_button = InlineKeyboardButton(
    text=VIEW_ALL_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_ALL_ORDERS).pack()
    )
view_paid_orders_button = InlineKeyboardButton(
    text=VIEW_PAID_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_PAID_ORDERS).pack()
    )
view_unpaid_orders_button = InlineKeyboardButton(
    text=VIEW_UNPAID_ORDERS_BUTTON, 
    callback_data=AdminCD(action=AdminCDAction.VIEW_UNPAID_ORDERS).pack()
    )
delete_order_button = InlineKeyboardButton(
    text="Удалить заказ", 
    callback_data=AdminCD(action=AdminCDAction.DELETE_ORDER).pack()
)
change_is_paid_button = InlineKeyboardButton(
    text="Изменить статус заказа", 
    callback_data=AdminCD(action=AdminCDAction.CHANGE_IS_PAID).pack()
)
close_button = InlineKeyboardButton(text="Закрыть ❌", callback_data=AdminCD(action=AdminCDAction.CLOSE).pack())


admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [view_all_orders_button],
        [view_paid_orders_button],
        [view_unpaid_orders_button],
        [delete_order_button],
        [change_is_paid_button],
        [close_button]
    ]
)