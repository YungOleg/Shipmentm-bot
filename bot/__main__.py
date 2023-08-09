import asyncio
from aiogram import executor
from aiogram.types import BotCommand
from util import POSTGRESQL_URL
from bot_config import dp, bot
from log_config import log
from util.commands_description import COMMANDS_DESCRIPRION

from handlers import *
from data import BaseModel, OrderLinks, create_async_engine, processed_schemas, get_session_maker


async def on_startup(_):
    log.info("Bot is running")


async def start_bot() -> None:
    cmd_description = [
        BotCommand(command=cmd[0], description=cmd[1]) for cmd in COMMANDS_DESCRIPRION
        ]
    
    await bot.set_my_commands(commands=cmd_description)
    
    async_engine = create_async_engine(POSTGRESQL_URL)
    session_maker = get_session_maker(async_engine)
    # await processed_schemas(async_engine, BaseModel.metadata)
    
    
    await bot.delete_webhook(drop_pending_updates=True)
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