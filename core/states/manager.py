from aiogram.fsm.state import StatesGroup, State


class ManagerState(StatesGroup):
    NAME = State()
    PHONE = State()
    WHATSAPP = State()
    EMAIL = State()
    COMPANY = State()
    CONFIRM = State()

    change = None
