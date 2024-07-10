from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import Premium


async def premium_create(
        *,
        session: AsyncSession,
        premium_id: int,
        sailor: int,
        manager: int,
) -> None:
    session.add(
        Premium(
            id=premium_id,
            sailor=sailor,
            manager=manager,
        )
    )

    await session.commit()


async def premium_search(
        *,
        session: AsyncSession,
        premium_id: int,
):
    query = await session.execute(
        select(
            Premium,
        ).where(
            Premium.id == premium_id,
        )
    )

    return query.scalars().one_or_none()
