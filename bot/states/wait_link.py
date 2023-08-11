from aiogram.dispatcher.filters.state import State, StatesGroup


class WaitLink(StatesGroup):
    waiting_for_link = State()
    process_for_link = State()