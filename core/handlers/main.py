from aiogram import Bot, Dispatcher

from core.database.query import admin
from core.settings import admin_id


async def on_startup(bot: Bot) -> None:
    await admin.checker()

    await bot.send_message(
        chat_id=admin_id,
        text="Start bot 👍🏻",
    )


async def on_shutdown(bot: Bot, dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()

    await bot.send_message(
        chat_id=admin_id,
        text="Stop bot 👎🏻",
    )
