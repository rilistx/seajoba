__all__ = ['unpacking']


from aiogram import Dispatcher
from aiogram.types import BotCommandScopeDefault

from core.commands.menu import commands
from core.database.engine import async_session
from core.handlers import start, restart, menu, error
from core.handlers.main import on_startup, on_shutdown
from core.middlewares.session import SessionMiddleware
from core.settings import bot, storage


async def unpacking() -> None:
    dp = Dispatcher(storage=storage)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(SessionMiddleware(session_pool=async_session))

    dp.include_router(restart.restart_router)
    dp.include_router(start.start_router)
    dp.include_router(menu.menu_router)
    dp.include_router(error.error_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.delete_my_commands(scope=BotCommandScopeDefault())
        await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
