from aiogram.types import Message
from aiogram.filters import BaseFilter
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.requestor.user import user_search


class IsUserFilter(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user = await user_search(
            session=session,
            user_id=message.from_user.id,
        )

        if user:
            return True

        return False
