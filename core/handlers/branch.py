from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.components.drivers import Branch
from core.filters.user import IsUserFilter
from core.processes.branch import main_processor


branch_router = Router()
branch_router.message.filter(IsUserFilter())


@branch_router.message(
    Command(commands='menu'),
)
async def menu(
        message: Message,
        session: AsyncSession,
        state: FSMContext,
) -> None:
    await state.clear()

    text, reply_markup = await main_processor(
        session=session,
    )

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )


@branch_router.callback_query(
    Branch.filter(),
)
async def redirector(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
) -> None:
    await state.clear()

    text, reply_markup = await main_processor(
        session=session,
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
