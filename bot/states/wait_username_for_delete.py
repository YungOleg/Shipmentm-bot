from aiogram.dispatcher.filters.state import State, StatesGroup


class WaitUsernameForDelete(StatesGroup):
    waiting_for_send_username = State()