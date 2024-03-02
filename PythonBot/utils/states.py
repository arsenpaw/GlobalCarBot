from aiogram.fsm.state import State, StatesGroup
from enum import Enum

class Status(Enum):
    HANDLED = 'handled'
    UNHANDLED = 'unhandled'
class BotStates(StatesGroup):
    user_car_info = State()
    contact_to_user_about_info = State()
    #car in stock states
    price_selection = State()
    year_selection = State()
    carfax_get_info = State()
    #car to find states
    car_to_find_get_price = State()
    car_to_find_get_year = State()
    car_to_find_get_user_contact = State()
    #to base handlers
    contact_with_manager = State() 
    send_vin_to_manager = State()
    callback_state = State()
    main_menu = State()