from util import ADMIN_ID
from bot import dp
from aiogram import types

@dp.message_handler(commands=["admin"], user_id=ADMIN_ID)
async def admin_menu(message: types.Message):
    await message.answer("admin_menu")