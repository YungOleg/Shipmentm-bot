from aiogram.dispatcher.filters.state import State, StatesGroup


class WaitIdForDelete(StatesGroup):
    waiting_for_send_id = State()