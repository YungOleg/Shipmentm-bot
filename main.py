from aiogram import executor, types
from load_bot import dp
from logger import log
from util import HELP_ANSWER, START_ANSWER, UNKNOW_DATA_ANSWER
from currency_parser import parse_rub

async def on_startup(_):
    log.info("Bot is running")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_ANSWER + "p")
    await message.delete()

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_ANSWER + "p")

# ! Функция для теста обращения к апи
@dp.message_handler(commands=['getdata'])
async def test_parser(message: types.Message):
    test = await parse_rub()
    await message.answer(f"test: {test}")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)