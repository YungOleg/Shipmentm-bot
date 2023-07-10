from aiogram import types
from load_bot import dp
from util import START_ANSWER, HELP_ANSWER
from keyboards import main_keyboard

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)
    await message.delete()

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_ANSWER)