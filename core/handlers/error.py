from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.query.user import user_search
from core.handlers.start import start
from core.keyboards.error import error_button


error_router = Router()


@error_router.message()
async def error(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    user = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    if not user:
        text = 'Error bot, not user!'
        reply_markup = ReplyKeyboardRemove()

        await message.answer(
            text=text,
            reply_markup=reply_markup,
        )

        return await start(
            message=message,
            session=session,
            state=state,
        )

    text = 'Error bot!'
    reply_markup = error_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )
