from aiogram.dispatcher.filters.state import State, StatesGroup


class WaitIdForChange(StatesGroup):
    waiting_for_send_id = State()