from aiogram import types
from aiogram.dispatcher.filters import Text
from bot import dp
from util.string_resources import START_ANSWER, HELP_ANSWER, BACK_BUTTON
from keyboards.keyboards import main_keyboard


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)
    await message.delete()

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_ANSWER)
    await message.delete()

@dp.message_handler(Text(equals=BACK_BUTTON))
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=main_keyboard)