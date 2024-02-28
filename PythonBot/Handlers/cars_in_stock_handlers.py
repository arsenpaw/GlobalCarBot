import logging
import sqlite3


from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard
from utils.states import *
from aiogram.fsm.context import FSMContext
from keyboards.start_keyboard import *

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
async def handle_data_to_sql(message: Message ,state: FSMContext,bot:Bot):
    await state.update_data(year_select = message.text)
    user_input: dict = await state.get_data()

    price_text = user_input['price_selection']
    price_range_list = await handle_price(price_text)
    logging.info(f'Chosen price {price_range_list}')

    year_text = user_input['year_select']
    year_range_list = await handle_year(year_text)
    logging.info(f'Chosen year {year_range_list}')
    min_year = year_range_list[0]
    max_year = year_range_list[1]
    min_price = price_range_list[0]
    max_price= price_range_list[1]
    try:
        with sqlite3.connect("database/clients.db") as db:
            cur = db.cursor()
            query = (""" SELECT * FROM CarShop
                WHERE car_cost BETWEEN ? AND ?
                AND car_year BETWEEN ? AND ?
                """)
            values = (min_price, max_price,min_year,max_year)
            cur.execute(query, values)
            rows = cur.fetchall()
            logging.info(f"SQL RESPONCE {rows}")
            if len(rows) == 0:
                await message.answer('Поки що у нас немає таких автомобілів в наявості, але ми обовязково привизем їх на замовлення.', reply_markup=consult_and_main_kb)
            else:
                await send_car_items(message,state,rows,bot)


    except Exception as ex:
        logging.error(f'ERROR FIND IN SQL WHEN SEARCH OUR CARS (CARS IN STOCK)  DB, {ex}')


async def send_car_items(message: Message ,state: FSMContext,rows,bot:Bot):
    for row in rows:
        path_to_photo = row[1]
        logging.info(path_to_photo)
        photo = FSInputFile(f"{path_to_photo}")

        year = row[2]
        price = row[3]
        car_name = row[4]
        car_description = row[5]
        await bot.send_photo(chat_id=message.chat.id ,photo=photo,caption=f"{car_name}\n"
                                                                          f"Рік {year}р \n"
                                                                          f"Ціна {price}$\n"
                                                                          f"Опис {car_description}")