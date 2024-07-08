from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.query.user import user_search
from core.filters.user import UserMessageFilter
from core.keyboards.menu import menu_admin_button, menu_user_button


menu_router = Router()


@menu_router.message(Command(commands='menu'), UserMessageFilter())
async def menu(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    user = await user_search(
        session=session,
        user_id=message.from_user.id,
    )

    text = 'Menu bot!'

    if user.role == 'admin':
        reply_markup = menu_admin_button()
    else:
        reply_markup = menu_user_button(
            role=user.role,
            premium=user.premium,
        )

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )


@menu_router.callback_query(F.data == 'menu')
async def redirector(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()

    user = await user_search(
        session=session,
        user_id=callback.from_user.id,
    )

    text = 'Menu bot!'

    if user.role == 'admin':
        reply_markup = menu_admin_button()
    else:
        reply_markup = menu_user_button(
            role=user.role,
            premium=user.premium,
        )

    await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
