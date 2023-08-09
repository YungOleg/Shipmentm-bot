import validators
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession
from bot_config import dp
from util import BACK_BUTTON, SEND_LINK_BUTTON
from keyboards import make_order_keyboard
from handlers import back_to_main_menu

from data import add_order_link


class Wait_link(StatesGroup):
    waiting_for_link = State()

@dp.message_handler(state=Wait_link.waiting_for_link)
async def process_link(message: types.Message, state: FSMContext, session_maker: AsyncSession):
    link = message.text
    if link == BACK_BUTTON:
        await state.finish() 
        await back_to_main_menu(message)
        return
    if validators.url(link):
        await message.answer('Ссылка успешно отправлена!')
        await add_order_link(
            user_id=message.from_user.id,
            link=link,
            user_name=message.from_user.username,
            session_maker=session_maker
        )
        await state.finish()
    else:
        await message.answer('Некорректная ссылка! Отправьте ссылку заново')
        await Wait_link.waiting_for_link.set()

@dp.message_handler(Text(equals=SEND_LINK_BUTTON))
async def send_link(message: types.Message):
    """
        Функция для приема ссылок от пользователей
    """
    await Wait_link.waiting_for_link.set()
    await message.answer("Отправьте ссылку на товар", reply_markup=make_order_keyboard)