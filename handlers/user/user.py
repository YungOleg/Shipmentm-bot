from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from load_bot import dp
from util import START_ANSWER, HELP_ANSWER
from keyboards import main_keyboard, make_order_keyboard, consultation_keyboard
from util import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
                  MESSAGE_TO_ADMIN_BUTTON, CALCULATE_COST_BUTTON, 
                  SEND_LINK_BUTTON, BACK_BUTTON)

@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)
    await message.delete()

@dp.message_handler(Command("help"))
async def help(message: types.Message):
    await message.answer(HELP_ANSWER)
    await message.delete()

@dp.message_handler(Text(equals=BACK_BUTTON))
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=main_keyboard)
    
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
