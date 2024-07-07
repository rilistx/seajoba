from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.query.user import user_create, user_search
from core.filters.role import RoleFilter
from core.handlers.menu import menu
from core.keyboards.start import role_button
from core.states.start import StartState


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    user = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    if user:
        text = 'User exist!'
        reply_markup = ReplyKeyboardRemove()

        await message.answer(
            text=text,
            reply_markup=reply_markup,
        )

        return await menu(
            message=message,
            session=session,
            state=state,
        )

    text = 'Hello!'
    reply_markup = role_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(StartState.START)


@start_router.message(StartState.START, RoleFilter())
async def registration(message: Message, session: AsyncSession, state: FSMContext):
    role = 'sailor' if message.text == '👨‍✈️ Sailor' else 'manager'

    await user_create(
        session=session,
        user_id=message.from_user.id,
        role=role,
    )

    text = f'OK! You {role}'
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


@start_router.message(StartState.START)
async def start_error(message: Message) -> None:
    text = 'Error!'
    reply_markup = role_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )
