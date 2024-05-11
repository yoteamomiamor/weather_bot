from aiogram.fsm.state import StatesGroup, State


class FSMMain(StatesGroup):
    add_location = State()
    select_weather = State()
