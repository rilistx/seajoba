from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.queryset import user_create, user_search
from core.filters.user import RoleUserFilter
from core.handlers.menu import menu
from core.keyboards.start import role_button
from core.states.start import StartState


start_router = Router()


@start_router.message(
    CommandStart(),
)
async def start(
        message: Message,
        session: AsyncSession,
        state: FSMContext,
):
    await state.clear()

    ReplyKeyboardRemove()

    user = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    if user:
        text = (
            f'<b>⚠️ Warning</b>\n\n'
            f'You are already registered in the system as a {user.role}.'
        )

        await message.answer(
            text=text,
        )

        return await menu(
            message=message,
            session=session,
            state=state,
        )

    text = (
        f'<b>👋🏻 Hello {message.from_user.first_name}</b>\n\n'
    )

    reply_markup = role_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(StartState.ROLE)


@start_router.message(
    StartState.ROLE,
    RoleUserFilter(),
)
async def registration(
        message: Message,
        session: AsyncSession,
        state: FSMContext,
):
    role = 'sailor' if message.text == '👨‍✈️ Sailor' else 'manager'

    await user_create(
        session=session,
        user_id=message.from_user.id,
        role=role,
    )

    text = (
        f'<b>✅ Success</b>\n\n'
        f'You became part of the team as a {role}.'
    )

    reply_markup = ReplyKeyboardRemove()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.clear()

    return await menu(
        message=message,
        session=session,
        state=state,
    )


@start_router.message(
    StartState.ROLE,
)
async def error(
        message: Message,
) -> None:
    text = (
        '<b>⛔️ Error</b>\n\n'
        'There is something wrong with your request.\n\n'
        '<i>If you are sure that you have done everything correctly, '
        'please write to technical support and we will try to fix this error.</i>'
    )

    reply_markup = role_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )
