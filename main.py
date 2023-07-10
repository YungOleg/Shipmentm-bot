from aiogram import executor, types
from load_bot import dp
from logger import log
from currency_parser import parse_rub
from handlers import *

async def on_startup(_):
    log.info("Bot is running")

# ! Функция для теста обращения к апи
@dp.message_handler(commands=['getdata'])
async def test_parser(message: types.Message):
    test = await parse_rub()
    await message.answer(f"test: {test}")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)