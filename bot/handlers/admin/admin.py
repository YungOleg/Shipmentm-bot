from util import admin
from bot_config import dp
from aiogram import types
from keyboards import admin_keyboard

# TODO сделать обработку текста из admin_keyboard

@dp.message_handler(commands=["admin"])
@admin
async def admin_menu(message: types.Message):
    await message.answer("Меню админа", reply_markup=admin_keyboard)