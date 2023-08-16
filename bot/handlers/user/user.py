# import validators
from validators import url
from aiogram.types import Message
from aiogram.dispatcher.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from handlers import back_to_main_menu
from data import add_order_link
from keyboards import make_order_keyboard, consultation_keyboard
from util import (MAKE_ORDER_BUTTON, CONSULTATION_BUTTON, 
                  FAQ_BUTTON, CALCULATE_COST_BUTTON)
from util import BACK_BUTTON, SEND_LINK_BUTTON
from states import WaitLink

# TODO сделать обработку кнопки faq
# TODO сделать обработку кнопки calculate_cost
# TODO сделать возможность просматривать свои заказы (инлайн кнопка)


async def make_order(message: Message):
    await message.answer(MAKE_ORDER_BUTTON, reply_markup=make_order_keyboard)


async def consultation(message: Message):
    await message.answer(CONSULTATION_BUTTON, reply_markup=consultation_keyboard)


async def faq(message: Message):
    """
        Функция для отправки сообщения админу с вопросом
    """
    await message.answer(FAQ_BUTTON, reply_markup=consultation_keyboard)


async def calculate_cost(message: Message):
    """
        Функция для расчета примерной стоимости заказа
    """
    await message.answer(CALCULATE_COST_BUTTON, reply_markup=consultation_keyboard)


# TODO сделать обработку ссылки
async def send_link(message: Message, state: FSMContext):
    """
        Функция для приема ссылок от пользователей
    """
    await state.set_state(WaitLink.process_for_link)
    await message.answer("Укажи ссылку на товар", reply_markup=make_order_keyboard)


async def process_link(message: Message, state: FSMContext, session_maker: AsyncSession):
    link = message.text
    match link:
        case "Назад":
            await state.clear()
            return await back_to_main_menu(message)
        case url(link):
            await message.answer('Ссылка успешно отправлена!')
            await add_order_link(
                user_id=message.from_user.id,
                link=link,
                user_name=message.from_user.username,
                session_maker=session_maker
            )
            await state.clear()
        case _:
            await message.answer('Некорректная ссылка! Отправьте ссылку заново')
            await state.set_state(WaitLink.waiting_for_link)
    
    # if link == BACK_BUTTON:
    #     await state.clear()
    #     return await back_to_main_menu(message)
    # if validators.url(link):
    #     await message.answer('Ссылка успешно отправлена!')
    #     await add_order_link(
    #         user_id=message.from_user.id,
    #         link=link,
    #         user_name=message.from_user.username,
    #         session_maker=session_maker
    #     )
    #     await state.clear()
    # else:
    #     await message.answer('Некорректная ссылка! Отправьте ссылку заново')
    #     await state.set_state(WaitLink.waiting_for_link)

