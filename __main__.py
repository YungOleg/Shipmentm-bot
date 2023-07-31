import asyncio
from aiogram import executor, types
from util import POSTGRESQL_URL
from bot_config import dp, bot
from log_config import log
# from middleware.currency_parser import parse_rub #? переместить в user(calculate cost)
from handlers import *
from data import BaseModel, OrderLinks, create_async_engine, processed_schemas, get_session_maker

# * ---------------------------------------------------------------- #
# !TODO_list:
# TODO 1. добавить базу данных
# TODO 2. добаить faq

# * ---------------------------------------------------------------- #

async def on_startup(_):
    log.info("Bot is running")

# # ! Функция для теста обращения к апи
# @dp.message_handler(commands=['getdata'])
# async def test_parser(message: types.Message):
#     test = await parse_rub()
#     await message.answer(f"test: {test}")

async def main() -> None:
    async_engine = create_async_engine(POSTGRESQL_URL)
    session_maker = get_session_maker(async_engine)
    await processed_schemas(async_engine, BaseModel.metadata)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(
        dp, 
        on_startup=on_startup, 
        skip_updates=True
        )
    
    # asyncio.run(main())