from aiogram.dispatcher.filters.state import State, StatesGroup

# TODO добавить состояния для админа

class WaitLink(StatesGroup):
    waiting_for_send_link = State()