from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import User


# ###############################   USER   ###############################

async def user_create(
        *,
        session: AsyncSession,
        user_id: int,
        role: str,
        first_name: str | None = None,
) -> None:
    session.add(
        User(
            id=user_id,
            role=role,
            first_name=first_name,
        )
    )

    await session.commit()


async def user_search(
        *,
        session: AsyncSession,
        user_id: int,
):
    query = await session.execute(
        select(
            User,
        ).where(
            User.id == user_id,
        )
    )

    return query.scalars().one_or_none()
