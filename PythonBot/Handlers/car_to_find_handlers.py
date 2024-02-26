import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import car_to_find_keyboard
from aiogram.fsm.context import FSMContext
from utils.states import *

router = Router()

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
    
@router.message(BotStates.car_to_find_get_year)
async def cars_year_to_find(message: Message ,state: FSMContext):
    await state.update_data(car_to_find_year_select = message.text)
    await state.set_state(BotStates.car_to_find_get_user_contact)
    logging.info("get info for car in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=car_to_find_keyboard.send_contact_car_to_find)
    