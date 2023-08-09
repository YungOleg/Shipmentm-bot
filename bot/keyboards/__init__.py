__all__ = [
    "main_keyboard", 
    "make_order_keyboard", "consultation_keyboard", 
    "admin_keyboard", "calculate_cost_keyboard"
    ]

# from .keyboards import (
#     main_keyboard, make_order_keyboard, 
#     consultation_keyboard, admin_keyboard, calculate_cost_keyboard
#     )

from .main_keyboard import main_keyboard
from .consultation_keyboard import consultation_keyboard
from .make_order_keyboard import make_order_keyboard

# TODO: доделать клавиатуры 
from .admin_keyboard import admin_keyboard
from .calculate_cost_keyboard import calculate_cost_keyboard
