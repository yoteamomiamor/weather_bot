from aiogram.fsm.state import State, StatesGroup


class MainFSM(StatesGroup):
    menu: State = State()
    select_weather: State = State()
    set_location: State = State()
    