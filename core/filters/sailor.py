from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter

from core.components.validator import is_valid_phone, is_valid_email, is_valid_date


class SailorNameFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if 2 <= len(message.text) <= 25:
            return True

        return False


class SailorChangeFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'sailor_change':
            return True

        return False


class SailorCancelFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'sailor_cancel':
            return True

        return False


class SailorReturnFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'sailor_return':
            return True

        return False


class SailorPhoneFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if is_valid_phone(message.text):
            return True

        return False


class SailorWhatsappFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'whatsapp_yes' or callback.data == 'whatsapp_not':
            return True

        return False


class SailorEmailFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if is_valid_email(message.text):
            return True

        return False


class SailorBirthFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if is_valid_date(message.text, method='less'):
            return True

        return False


class SailorNationalityNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('nationality_next_'):
            return True

        return False


class SailorNationalityConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('nationality_confirm_'):
            return True

        return False


class SailorPositionNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('position_next_'):
            return True

        return False


class SailorPositionConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('position_confirm_'):
            return True

        return False


class SailorRankNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('rank_next_'):
            return True

        return False


class SailorRankConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('rank_confirm_'):
            return True

        return False


class SailorExperienceYesFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('experience_yes'):
            return True

        return False


class SailorExperienceNotFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('experience_not'):
            return True

        return False


class SailorFleetNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('fleet_next_'):
            return True

        return False


class SailorFleetConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('fleet_confirm_'):
            return True

        return False


class SailorPurposeNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('purpose_next_'):
            return True

        return False


class SailorPurposeConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('purpose_confirm_'):
            return True

        return False


class SailorVesselNextFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('vessel_next_'):
            return True

        return False


class SailorVesselConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.startswith('vessel_confirm_'):
            return True

        return False


class SailorApplicationFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.document:
            return True

        return False


class SailorConfirmFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data == 'sailor_confirm':
            return True

        return False
