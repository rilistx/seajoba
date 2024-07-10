from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    ROLE = State()
