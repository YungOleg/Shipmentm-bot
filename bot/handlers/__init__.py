from aiogram import Router

__all__ = [
    "start", "help", 
    "back_to_main_menu", "admin_menu", 
    "make_order", "calculate_cost", "faq", 
    "process_link", "send_link", "consultation"
    ]

from .default_handlers import start, help, back_to_main_menu
from .admin import admin_menu
from .user import make_order, calculate_cost, faq, process_link, send_link, consultation

def register_handlers(router: Router):
    router.message.register()