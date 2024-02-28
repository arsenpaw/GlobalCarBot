import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard
from utils.states import *
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(F.text.lower() == 'авто в наявності')
async def cars_cost_in_stock(message: Message, state: FSMContext):
    logging.info("cars in stock button")
    await state.set_state(BotStates.price_selection)
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=cars_in_stock_keyboard.cars_cost_in_stock_kb)
    
    

@router.message(BotStates.price_selection)
async def cars_year_in_stock(message: Message ,state: FSMContext):
    await state.update_data(price_selection = message.text)
    await state.set_state(BotStates.year_selection)
    logging.info("Year in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=cars_in_stock_keyboard.cars_year_in_stock_kb)

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

@router.message(BotStates.year_selection)
async def handle_data_to_sql(message: Message ,state: FSMContext):
    await state.update_data(year_select = message.text)
    user_input: dict = await state.get_data()

    price_text = user_input['price_selection']
    price_range_list = await handle_price(price_text)
    logging.info(f'Choseb price {price_range_list}')

    year_text = user_input['year_select']
    year_range_list = await handle_year(year_text)
    logging.info(f'Choseb year {year_range_list}')

    await message.answer('Дані підтверждено✅')
    await message.answer('Натисніть на кнопку Отримати підбірку , щоб чат-бот надіслав відповідні варіанти під ваш запит в Telegram👇', reply_markup=cars_in_stock_keyboard.send_contact)