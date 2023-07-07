import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from util.constants import HELP_ANSWER, START_ANSWER

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_ANSWER)
    

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_ANSWER)


@dp.message_handler()
async def unknow_data(message: types.Message):
    """
        Функция для обработки неивестных команд
    """
    await message.reply("Я не знаю такую команду!")
    

if __name__ == "__main__":
    executor.start_polling(dp)