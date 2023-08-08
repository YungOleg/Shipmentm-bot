import asyncio
from aiogram import executor
from util import POSTGRESQL_URL
from bot_config import dp, bot
from log_config import log
# from middleware.currency_parser import parse_rub #? переместить в user(calculate cost)
from handlers.user.commands_description import COMMANDS_DESCRIPRION
from aiogram.types import BotCommand

from handlers import *
from data import BaseModel, OrderLinks, create_async_engine, processed_schemas, get_session_maker


async def on_startup(_):
    log.info("Bot is running")

# # ! Функция для теста обращения к апи
# @dp.message_handler(commands=['getdata'])
# async def test_parser(message: types.Message):
#     test = await parse_rub()
#     await message.answer(f"test: {test}")

async def start_bot() -> None:
    cmd_description = [
        BotCommand(command=cmd[0], description=cmd[1]) for cmd in COMMANDS_DESCRIPRION
        ]
    
    await bot.set_my_commands(commands=cmd_description)
    
    async_engine = create_async_engine(POSTGRESQL_URL)
    session_maker = get_session_maker(async_engine)
    await processed_schemas(async_engine, BaseModel.metadata)
    
    await dp.start_polling(
        bot,
        # session_maker=session_maker
        )
    
    # executor.start_polling(
    #     dp, 
    #     on_startup=on_startup, 
    #     skip_updates=True,
    #     bot=bot,
    #     session_maker=session_maker
    #     )

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot was stopped")