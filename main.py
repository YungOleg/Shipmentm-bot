import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from util import HELP_ANSWER, START_ANSWER, TOKEN



bot = Bot(TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def on_startup(_):
    log.info("Bot is running")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
        Обрабатывает /start команду
    """
    await message.answer(START_ANSWER)
    await message.delete()

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    """
        Обрабатывает /help команду
    """
    await message.answer(HELP_ANSWER)

@dp.message_handler()
async def unknow_data(message: types.Message):
    """
        Обрабатывает неизвестные команды
    """
    await message.reply("Я не знаю такую команду!")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)