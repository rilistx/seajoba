from core.database.engine import async_session
from core.database.query.user import user_search, user_create
from core.settings import admin_id


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
