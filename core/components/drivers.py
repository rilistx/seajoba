from aiogram.filters.callback_data import CallbackData


class Branch(CallbackData, prefix="branch"):
    user_id: int | None = None
