from util import ADMIN_ID
from load_bot import dp
from aiogram import types
from aiogram.dispatcher.filters import Command

@dp.message_handler(user_id=ADMIN_ID, commands=Command("admin"))
async def admin_menu(message: types.Message):
    await message.answer("admin_menu")