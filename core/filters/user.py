from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.query.user import user_search


class UserMessageFilter(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user = await user_search(
            session=session,
            user_id=message.from_user.id,
        )

        if user:
            return True

        return False


class UserCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery, session: AsyncSession) -> bool:
        user = await user_search(
            session=session,
            user_id=callback.from_user.id,
        )

        if user:
            return True

        return False
