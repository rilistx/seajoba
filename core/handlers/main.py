from aiogram import Bot, Dispatcher

from core.database.connector.user import user_search, user_create
from core.database.engine import async_session
from core.utils.configer import bot_admin


async def jobastart(
        bot: Bot,
) -> None:
    async with async_session() as session:
        admin = await user_search(
            session=session,
            user_id=bot_admin,
        )

        if not admin:
            await user_create(
                session=session,
                user_id=bot_admin,
                role='admin',
                first_name='SeaJoba Admin',
            )

    await bot.send_message(
        chat_id=bot_admin,
        text="Start bot 👍🏻",
    )


async def jobastop(
        bot: Bot,
        dispatcher: Dispatcher,
) -> None:
    await dispatcher.storage.close()

    await bot.send_message(
        chat_id=bot_admin,
        text="Stop bot 👎🏻",
    )
