from aiogram import types
from aiogram.dispatcher.filters import Text
from bot import dp
from keyboards.keyboards import main_keyboard, make_order_keyboard, consultation_keyboard
from util.string_resources import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
                  MESSAGE_TO_ADMIN_BUTTON, CALCULATE_COST_BUTTON)



# ! Меню заказа
@dp.message_handler(Text(equals=MAKE_ORDER_BUTTON))
async def make_order(message: types.Message):
    await message.answer(MAKE_ORDER_BUTTON, reply_markup=make_order_keyboard)

# ! Меню консультации
@dp.message_handler(Text(equals=CONSULTATION_BUTTON))
async def consultation(message: types.Message):
    await message.answer(CONSULTATION_BUTTON, reply_markup=consultation_keyboard)

@dp.message_handler(Text(equals=MESSAGE_TO_ADMIN_BUTTON))
async def message_to_admin(message: types.Message):
    """
        Функция для отправки сообщения админу с вопросом
    """
    await message.answer(MESSAGE_TO_ADMIN_BUTTON, reply_markup=consultation_keyboard)

@dp.message_handler(Text(equals=CALCULATE_COST_BUTTON))
async def calculate_cost(message: types.Message):
    """
        Функция для расчета примерной стоимости заказа
    """
    await message.answer(CALCULATE_COST_BUTTON, reply_markup=consultation_keyboard)
