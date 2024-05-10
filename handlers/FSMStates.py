from aiogram.fsm.state import StatesGroup, State


class FSMMain(StatesGroup):
    # main branch
    settings: State
    
    # settings branch
    # - add location branch
    add_location: State
    add_name: State
    
    # - delete location branch
    del_location: State
