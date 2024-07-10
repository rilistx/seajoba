__all__ = ['unpacking']


from aiogram import Dispatcher
from aiogram.types import BotCommandScopeDefault

from core.commands.menu import commands
from core.database.engine import async_session
from core.handlers import start, branch, error
from core.handlers.main import jobastart, jobastop
from core.middlewares.session import SessionMiddleware
from core.utils.configer import bot, storage


async def unpacking() -> None:
    dp = Dispatcher(storage=storage)

    dp.startup.register(jobastart)
    dp.shutdown.register(jobastop)

    dp.update.middleware(SessionMiddleware(session_pool=async_session))

    dp.include_router(start.start_router)
    dp.include_router(branch.branch_router)
    dp.include_router(error.error_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.delete_my_commands(scope=BotCommandScopeDefault())
        await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
