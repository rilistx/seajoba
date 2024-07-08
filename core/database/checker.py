from core.database.engine import async_session
from core.database.query.premium import premium_search, premium_create
from core.database.query.user import user_search, user_create
from core.settings import admin_id, premium_id


async def checker() -> None:
    async with async_session() as session:
        admin = await user_search(
            session=session,
            user_id=admin_id,
        )

        if not admin:
            await user_create(
                session=session,
                user_id=admin_id,
                role='admin',
                first_name='SeaJoba Support',
                premium=True,
            )

        premium = await premium_search(
            session=session,
            premium_id=premium_id,
        )

        if not premium:
            await premium_create(
                session=session,
                premium_id=premium_id,
            )
