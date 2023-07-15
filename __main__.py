import asyncio
from aiogram import executor, types
from bot import dp, bot
from logger import log
from currency_parser.currency_parser import parse_rub #? переместить в user(calculate cost)
from handlers import *


async def on_startup(_):
    log.info("Bot is running")

# ! Функция для теста обращения к апи
@dp.message_handler(commands=['getdata'])
async def test_parser(message: types.Message):
    test = await parse_rub()
    await message.answer(f"test: {test}")

# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    # asyncio.run(main())