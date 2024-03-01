import logging

from keyboards import *
from aiogram.fsm.context import FSMContext
from utils.states import *
from database.database_methods import *

async def get_basic_info(message: Message)-> dict:
    logging.info('get_basic_info')
    user_info_dict = message.contact
    message_date = str(message.date)
    client_phone = user_info_dict.phone_number
    if user_info_dict.last_name is None:
        full_name = str(user_info_dict.first_name)
    else:
        full_name = f'{str(user_info_dict.first_name) } {str(user_info_dict.last_name)}'
    logging.info(f'User info  {user_info_dict.user_id},{full_name},{client_phone},{message_date}')
    return {'user_id': user_info_dict.user_id,'user_name': full_name,'phone_number': user_info_dict.phone_number, 'time': message.date}