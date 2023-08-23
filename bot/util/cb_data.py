import enum
from aiogram.dispatcher.filters.callback_data import CallbackData

class AdminCD(CallbackData, prefix="amdin"):
    ...