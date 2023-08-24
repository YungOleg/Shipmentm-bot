import enum
from aiogram.dispatcher.filters.callback_data import CallbackData


class AdminCDAction(enum.IntEnum):
    VIEW_ALL_ORDERS = 0
    VIEW_PAID_ORDERS = 1
    VIEW_UNPAID_ORDERS = 2
    CHANGE_IS_PAID = 3
    DELETE_ORDER = 4
    CLOSE = 5

class AdminCD(CallbackData, prefix="admin"):
    action: AdminCDAction
    # user_id: int = None