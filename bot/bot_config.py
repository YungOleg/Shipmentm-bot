from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from util import TOKEN


storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)