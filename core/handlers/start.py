from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()

    text = 'Hello!'

    await message.answer(
        text=text,
    )
