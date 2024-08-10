from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter

from core.components.validator import is_valid_phone, is_valid_email


class ManagerNameFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if 2 <= len(message.text) <= 25:
            return True

        return False


class ManagerChangeFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'manager_change':
            return True

        return False


class ManagerCancelFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'manager_cancel':
            return True

        return False


class ManagerReturnFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'manager_return':
            return True

        return False


class ManagerPhoneFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if is_valid_phone(message.text):
            return True

        return False


class ManagerWhatsappFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'whatsapp_yes' or callback.data == 'whatsapp_not':
            return True

        return False


class ManagerEmailFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if is_valid_email(message.text):
            return True

        return False


class ManagerCompanyNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('company_next_'):
            return True

        return False


class ManagerCompanyConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('company_confirm_'):
            return True

        return False


class ManagerConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'manager_confirm':
            return True

        return False
