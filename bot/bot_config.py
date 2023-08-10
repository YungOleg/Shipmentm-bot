from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from util import TOKEN


storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(storage=storage)