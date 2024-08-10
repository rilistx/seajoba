from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core.keyboards.error import error_button


error_router = Router()


@error_router.message()
async def error(
        message: Message,
        state: FSMContext,
):
    await state.clear()

    ReplyKeyboardRemove()

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
