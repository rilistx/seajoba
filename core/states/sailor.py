from aiogram.fsm.state import StatesGroup, State


class SailorState(StatesGroup):
    NAME = State()
    PHONE = State()
    WHATSAPP = State()
    EMAIL = State()
    BIRTH = State()
    NATIONALITY = State()
    POSITION = State()
    RANK = State()
    EXPERIENCE = State()
    FLEET = State()
    PURPOSE = State()
    VESSEL = State()
    APPLICATION = State()
    CONFIRM = State()

    change = None
