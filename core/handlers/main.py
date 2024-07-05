from aiogram import Bot, Dispatcher

from core.settings import admin


async def on_startup(bot: Bot) -> None:
    await bot.send_message(
        chat_id=admin,
        text="Run bot 👍🏻",
    )


async def on_shutdown(bot: Bot, dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
    await bot.send_message(
        chat_id=admin,
        text="Stop bot 👎🏻",
    )
