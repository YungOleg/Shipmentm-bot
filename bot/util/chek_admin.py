from util import ADMIN_ID


def admin(func):
    """Декоратор для проверки пользователя на админа"""
    async def check_admin(message):
        id = message["from"]["id"]
        if str(message["from"]["id"]) != ADMIN_ID:
            return await message.answer("нет доступа к этой команде")
            # return await message.answer(f"id = {type(id)}, admin = {type(ADMIN_ID)}")
        return await func(message)
    return check_admin