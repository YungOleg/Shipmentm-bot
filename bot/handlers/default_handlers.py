from aiogram import Router
from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from util import START_ANSWER, BACK_BUTTON, HELP_ANSWER
from keyboards import main_keyboard

router = Router(name="default")

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(START_ANSWER, reply_markup=main_keyboard)
    await message.delete()


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(HELP_ANSWER, reply_markup=main_keyboard)
    await message.delete()


@router.message(Text(equals=BACK_BUTTON))
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=main_keyboard)