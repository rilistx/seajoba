from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.requestor.user import user_search
from core.keyboards.error import error_button
from core.keyboards.start import role_button
from core.states.start import StartState


error_router = Router()


@error_router.message()
async def error(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    user: bool = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    if user:
        text = (
            '<b>⛔️ Error</b>\n\n'
            'There is something wrong with your request.\n\n'
            '<i>If you are sure that you have done everything correctly, '
            'please write to technical support and we will try to fix this error.</i>'
        )

        reply_markup = error_button()

        await message.answer(
            text=text,
            reply_markup=reply_markup,
        )
    else:
        text = (
            '<b>⚠️ Warning</b>\n\n'
            'There is something wrong with your request.'
        )

        reply_markup = role_button()

        await message.answer(
            text=text,
            reply_markup=reply_markup,
        )

        await state.set_state(StartState.ROLE)
