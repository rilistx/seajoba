from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.keyboards.menu import menu_button


menu_router = Router()


@menu_router.message(Command(commands='menu'))
async def menu(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()

    text = 'Menu bot!'
    reply_markup = menu_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )


@menu_router.callback_query(F.data == 'menu')
async def redirector(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()

    text = 'Menu bot!'
    reply_markup = menu_button()

    await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )
