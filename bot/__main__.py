import asyncio
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from util import COMMANDS_DESCRIPRION, TOKEN, POSTGRESQL_URL
from middleware import DBSessionMiddleware

from handlers import register_handlers
from data import BaseModel, create_async_engine, processed_schemas, get_session_maker
from log_config import log


async def start_bot() -> None:
    storage = MemoryStorage()
    bot = Bot(TOKEN)
    dp = Dispatcher(storage=storage)
    
    # * Регистрация подсказок с командами
    cmd_description = [
        BotCommand(command=cmd[0], description=cmd[1]) for cmd in COMMANDS_DESCRIPRION
        ]
    await bot.set_my_commands(commands=cmd_description)
    
    dp.message.middleware(DBSessionMiddleware())
    register_handlers(dp)
    
    async_engine = create_async_engine(POSTGRESQL_URL)
    session_maker = get_session_maker(async_engine)
    # * await processed_schemas(async_engine, BaseModel.metadata)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session_maker=session_maker)


def main() -> None:
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        pass
    except Exception as e:
        log.exception(f"Exception: {e}")


if __name__ == "__main__":
    # python bot/__main__.py
    main()