from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from util import (
    FAQ_BUTTON
)

faq_button = InlineKeyboardButton(
    text="FAQ", 
    callback_data='faq'
    )

faq_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [faq_button]
    ]
)