from util import admin
from aiogram import types
from keyboards import admin_keyboard

# TODO сделать обработку текста из admin_keyboard


@admin
async def admin_menu(message: types.Message):
    await message.answer("Меню админа", reply_markup=admin_keyboard)