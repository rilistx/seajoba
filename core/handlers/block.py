from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core.filters.user import BlockUserFilter
from core.keyboards.error import error_button


block_router = Router()


@block_router.message(
    BlockUserFilter()
)
async def block(
        message: Message,
        state: FSMContext,
):
    await state.clear()

    ReplyKeyboardRemove()

    text = (
        '<b>⛔️ Block account</b>\n\n'
        'There is something wrong with your request.\n\n'
        '<i>If you are sure that you have done everything correctly, '
        'please write to technical support and we will try to fix this error.</i>'
    )

    reply_markup = error_button()

    await message.answer(
        text=text,
        reply_markup=reply_markup,
    )
