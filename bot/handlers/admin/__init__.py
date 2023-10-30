__all__ = [
    "admin_menu", "get_paid_order_to_admin",
    "get_unpaid_order_to_admin", "admin_change_is_paid", 
    "admin_delete_order_by_id", "view_all_orders", "close_admin", 
    "wait_id_for_change", "wait_id_for_delete"
    ]

from .admin import (
    admin_menu, get_paid_order_to_admin, 
    get_unpaid_order_to_admin, admin_change_is_paid, 
    admin_delete_order_by_id, view_all_orders, close_admin, 
    wait_id_for_change, wait_id_for_delete
    )