from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.query.user import user_search
from core.handlers.menu import menu
from core.handlers.start import start


restart_router = Router()


@restart_router.message(Command(commands='restart'))
async def restart(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    text = 'Restart bot!'
    reply_markup = ReplyKeyboardRemove()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    user = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    if user:
        return await menu(
            message=message,
            session=session,
            state=state,
        )

    return await start(
        message=message,
        session=session,
        state=state,
    )
