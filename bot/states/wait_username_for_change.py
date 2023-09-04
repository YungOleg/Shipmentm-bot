from aiogram.dispatcher.filters.state import State, StatesGroup


class WaitUsernameForChange(StatesGroup):
    waiting_for_send_username = State()