from aiogram.types import Message
from aiogram.filters import BaseFilter

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.queryset import user_search


class RoleUserFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.text == '👨‍✈️ Sailor' or message.text == '👩‍💼 Manager':
            return True

        return False


class CheckUserFilter(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user = await user_search(
            session=session,
            user_id=message.from_user.id,
        )

        if user:
            if not user.blocked:
                return True

        return False


class BlockUserFilter(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user = await user_search(
            session=session,
            user_id=message.from_user.id,
        )

        if user.blocked:
            return True

        return False
