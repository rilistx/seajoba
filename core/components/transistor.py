from aiogram.filters.callback_data import CallbackData


class MenuData(CallbackData, prefix='menu'):
    key: str
    level: int
    page: int = 1
    object_id: int | None = None


class SailorData(CallbackData, prefix='sailor'):
    method: str
    user_id: int


class ManagerData(CallbackData, prefix='manager'):
    method: str
    user_id: int


class VacancyData(CallbackData, prefix='vacancy'):
    method: str
    user_id: int
