from aiogram.fsm.state import State, StatesGroup

class BotStates(StatesGroup):
    user_car_info = State()
    contact_to_user_about_info = State()
    price_selection = State()
    year_selection = State()
    carfax_get_info = State()
