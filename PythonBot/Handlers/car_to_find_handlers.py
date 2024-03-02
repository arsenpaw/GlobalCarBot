import logging
import sqlite3
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import car_to_find_keyboard
from aiogram.fsm.context import FSMContext
from utils.states import *


from filters.admin_filters import *


router = Router()
router.message.filter(ChatTypeFilter(["private"]))
@router.message(F.text.lower() == 'авто на підбір')
async def cars_cost_to_find(message: Message, state: FSMContext):
    logging.info("cars to find info button")
    await state.set_state(BotStates.car_to_find_get_price)
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=car_to_find_keyboard.cars_to_find_price_kb)
    
@router.message(BotStates.car_to_find_get_price)
async def cars_year_to_find(message: Message ,state: FSMContext):
    await state.update_data(car_to_find_price_select = message.text)
    await state.set_state(BotStates.year_selection)
    logging.info("Year in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=car_to_find_keyboard.cars_to_find_year_kb)
    
<<<<<<< HEAD
@router.message(BotStates.year_selection)
async def cars_year_to_find(message: Message ,state: FSMContext):
    await state.update_data(car_to_find_year_select = message.text)
    print(await state.get_data())
    await state.set_state(BotStates.car_to_find_get_user_contact)
    logging.info("get info for car in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=car_to_find_keyboard.send_contact_car_to_find)
    
=======
  

async def handle_price(price:str)->list:
    logging.info('price convert to list')
    if '8 000' in price and '15 000' in price:
        return [8000,15000]
    elif '8 000' in price and '15 000' not in price:
        return [0,8000]
    elif '15 000' in price and '20 000' in price:
        return [15000,20000]
    else:
        return [20000, 10000000]
async def handle_year(year:str)->list:
    logging.info('year convert to list')
    if '2007' in year:
        return [0, 2007]
    elif '2012' in year:
        return [2008, 2012]
    elif '2018' in year:
        return [2013, 2018]
    else:
        return [2019, 3000]  
    
>>>>>>> e8ebb9d87665a065f14a9ac524e25303cd1a8759
