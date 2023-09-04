__all__ = [
    "main_keyboard", 
    "make_order_keyboard", "consultation_keyboard", 
    "admin_keyboard", "calculate_cost_keyboard", "faq_keyboard"
    ]

from .main_keyboard import main_keyboard
from .consultation_keyboard import consultation_keyboard
from .make_order_keyboard import make_order_keyboard
from .admin_keyboard import admin_keyboard
from .faq_keyboard import faq_keyboard

# TODO переделать клавиатуру
from .calculate_cost_keyboard import calculate_cost_keyboard
