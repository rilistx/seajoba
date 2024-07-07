from aiogram.types import Message
from aiogram.filters import BaseFilter


class RoleFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text == '👨‍✈️ Sailor' or message.text == '👩‍💼 Manager':
            return True

        return False
