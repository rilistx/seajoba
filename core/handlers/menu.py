from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.components.redirector import distributor
from core.components.transistor import MenuData
from core.filters.user import CheckUserFilter


menu_router = Router()

menu_router.message.filter(
    CheckUserFilter(),
)


@menu_router.message(
    Command(commands='menu'),
)
async def menu(
        message: Message,
        session: AsyncSession,
        state: FSMContext,
        key='menu',
        level=0,
) -> None:
    await state.clear()

    ReplyKeyboardRemove()

    text, reply_markup = await distributor(
        session=session,
        key=key,
        level=level,
        user_id=message.from_user.id,
    )

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )


@menu_router.callback_query(
    MenuData.filter(),
)
async def redirector(
        callback: CallbackQuery,
        callback_data: MenuData,
        session: AsyncSession,
) -> None:
    text, reply_markup = await distributor(
        session=session,
        key=callback_data.key,
        level=callback_data.level,
        user_id=callback.from_user.id,
        page=callback_data.page,
        object_id=callback_data.object_id,
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
