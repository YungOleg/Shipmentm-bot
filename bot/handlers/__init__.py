from aiogram import Router
from aiogram import F
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.fsm.state import any_state
from util import (
    BACK_BUTTON, MAKE_ORDER_BUTTON,
    CONSULTATION_BUTTON, FAQ_BUTTON, 
    CALCULATE_COST_BUTTON, SEND_LINK_BUTTON, ADMIN_ID, 
    AdminCD, AdminCDAction
)

from states import WaitLink
from .default_handlers import start, help, back_to_main_menu
from .admin import (
    admin_menu, get_paid_order_to_admin, 
    get_unpaid_order_to_admin, change_is_paid, 
    delete_order_by_id, select_all, close_admin
    )
from .user import (
    make_order, calculate_cost, 
    faq, consultation, process_link, send_link
    )

__all__ = ["register_handlers"]

def register_handlers(router: Router):
    # * default commands
    router.message.register(start, Command(commands=["start"]))
    router.message.register(help, Command(commands=["help"]))
    router.message.register(back_to_main_menu, Text(text=BACK_BUTTON), any_state)
    # * user commands
    router.message.register(make_order, Text(text=MAKE_ORDER_BUTTON), any_state)
    router.message.register(calculate_cost, Text(text=CALCULATE_COST_BUTTON))
    router.message.register(faq, Text(text=FAQ_BUTTON))
    router.message.register(consultation, Text(text=CONSULTATION_BUTTON))
    # * register fsm commands
    router.message.register(process_link, WaitLink.waiting_for_send_link)
    router.message.register(send_link, Text(text=SEND_LINK_BUTTON))
    # * admin commands
    router.message.register(admin_menu, Command(commands=["admin"]), F.from_user.id == int(ADMIN_ID))
    # * admin callbacks
    router.callback_query.register(
        get_paid_order_to_admin, 
        AdminCD.filter(F.action == AdminCDAction.VIEW_PAID_ORDERS), 
        F.from_user.id == int(ADMIN_ID)
        )
    router.callback_query.register(
        get_unpaid_order_to_admin, 
        AdminCD.filter(F.action == AdminCDAction.VIEW_UNPAID_ORDERS), 
        F.from_user.id == int(ADMIN_ID)
        )
    # router.callback_query.register(
    #     select_all, 
    #     AdminCD.filter(F.action == AdminCDAction.VIEW_ALL_ORDERS), 
    #     F.from_user.id == int(ADMIN_ID)
    #     )
    router.callback_query.register(
        close_admin, 
        AdminCD.filter(F.action == AdminCDAction.CLOSE),
        F.from_user.id == int(ADMIN_ID)
        )
    # router.callback_query.register(
    #     change_is_paid, 
    #     AdminCD.filter(F.action == AdminCDAction.CHANGE_IS_PAID), 
    #     F.from_user.id == int(ADMIN_ID)
    #     ) #! need fsm
    # router.callback_query.register(
    #     delete_order_by_id, 
    #     AdminCD.filter(F.action == AdminCDAction.DELETE_ORDER), 
    #     F.from_user.id == int(ADMIN_ID)
    #     ) #! need fsm