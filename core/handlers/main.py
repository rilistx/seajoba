from aiogram import Bot, Dispatcher

from core.utils.checker import creator
from core.utils.configer import admin_id


async def jobastart(bot: Bot) -> None:
    await creator()

    await bot.send_message(
        chat_id=admin_id,
        text="Start bot 👍🏻",
    )


async def jobastop(bot: Bot, dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()

    await bot.send_message(
        chat_id=admin_id,
        text="Stop bot 👎🏻",
    )
