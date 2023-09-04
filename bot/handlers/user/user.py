# import validators
from validators import url
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from handlers import back_to_main_menu
from data import add_order_link
from keyboards import make_order_keyboard, consultation_keyboard, faq_keyboard
from util import (
    MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
    FAQ_BUTTON, CALCULATE_COST_BUTTON, FAQ_ANSWER
    )
from util import BACK_BUTTON, SEND_LINK_BUTTON
from states import WaitLink


# TODO сделать обработку кнопки faq
# TODO сделать обработку кнопки calculate_cost
# TODO сделать возможность просматривать свои заказы (инлайн кнопка)


async def make_order(message: Message):
    await message.answer(MAKE_ORDER_BUTTON, reply_markup=make_order_keyboard)


async def consultation(message: Message):
    await message.answer(CONSULTATION_BUTTON, reply_markup=consultation_keyboard)
    await message.answer("Часто задаваемые вопросы", reply_markup= faq_keyboard)


async def faq_callback(call: CallbackQuery):
    await call.message.answer(FAQ_ANSWER)
    await call.answer()


async def calculate_cost(message: Message):
    """
        Функция для расчета примерной стоимости заказа
    """
    await message.answer(CALCULATE_COST_BUTTON, reply_markup=consultation_keyboard)


async def send_link(message: Message, state: FSMContext):
    """
        Функция для приема ссылок от пользователей
    """
    await state.set_state(WaitLink.waiting_for_send_link)
    await message.answer("Укажи ссылку на товар", reply_markup=make_order_keyboard)


async def process_link(message: Message, state: FSMContext, session_maker: AsyncSession):
    if message.text == BACK_BUTTON:
        await state.clear()
        await back_to_main_menu(message)
        return 
    elif url(message.text):
        # *
        await add_order_link(
            user_id=message.from_user.id,
            link=message.text,
            user_name=message.from_user.username,
            session_maker=session_maker
        )
        await message.answer('Ссылка успешно отправлена! Теперь по команде /link тебе будет доступен список твоих заказов')
        await state.clear()
        return await back_to_main_menu(message)
    else:
        await message.answer('Некорректная ссылка!')
        await state.clear()
        # return await make_order(message)