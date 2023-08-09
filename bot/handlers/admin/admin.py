from util import admin
from bot_config import dp
from aiogram import types

@dp.message_handler(commands=["admin"])
@admin
async def admin_menu(message: types.Message):
    await message.answer("admin_menu")
    await message.answer(f"{message.from_user.id}")