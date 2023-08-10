from aiogram import Router
from aiogram.dispatcher.filters import Command, Text
from util import (
    BACK_BUTTON, MAKE_ORDER_BUTTON,
    CONSULTATION_BUTTON, FAQ_BUTTON, 
    CALCULATE_COST_BUTTON, SEND_LINK_BUTTON
)

__all__ = [
    "start", "help", 
    "back_to_main_menu", "admin_menu", 
    "make_order", "calculate_cost", "faq", 
    "process_link", "send_link", "consultation"
    ]

from states import WaitLink
from .default_handlers import start, help, back_to_main_menu
from .admin import admin_menu
from .user import make_order, calculate_cost, faq, consultation, process_link, send_link

def register_handlers(router: Router):
    router.message.register(admin_menu, Command(commands=["admin"]))
    router.message.register(start, Command(commands=["start"]))
    router.message.register(help, Command(commands=["help"]))
    router.message.register(back_to_main_menu, Text(text=BACK_BUTTON))
    router.message.register(make_order, Text(text=MAKE_ORDER_BUTTON))
    router.message.register(calculate_cost, Text(text=CALCULATE_COST_BUTTON))
    router.message.register(faq, Text(text=FAQ_BUTTON))
    router.message.register(consultation, Text(text=CONSULTATION_BUTTON))
    router.message.register(process_link, WaitLink.waiting_for_link)
    router.message.register(send_link, Text(text=SEND_LINK_BUTTON))