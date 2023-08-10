from aiogram import types
from util import START_ANSWER, HELP_ANSWER
from keyboards import main_keyboard


async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)


async def help(message: types.Message):
    await message.answer(HELP_ANSWER, reply_markup=main_keyboard)


async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=main_keyboard)