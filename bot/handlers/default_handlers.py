from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from bot_config import dp
from util.string_resources import START_ANSWER, BACK_BUTTON, HELP_ANSWER
from keyboards import main_keyboard


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)
    await message.delete()


@dp.message_handler(Command("help"))
async def help(message: types.Message):
    await message.answer(HELP_ANSWER, reply_markup=main_keyboard)
    await message.delete()


@dp.message_handler(Text(equals=BACK_BUTTON))
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=main_keyboard)