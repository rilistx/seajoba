from sqlalchemy.ext.asyncio import AsyncSession


async def main_processor(
        *,
        session: AsyncSession,
        user_id: int | None = None,
        level: int | None = None,
):
    if level == 0:
        pass
    elif level == 1:
        pass
