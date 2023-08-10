__all__ = ["make_order", "calculate_cost", "faq", "process_link", "send_link", "consultation"]


from .user import make_order, calculate_cost, faq, consultation
from .url_reciver import process_link, send_link