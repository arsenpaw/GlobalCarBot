import logging
import sqlite3
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import car_to_find_keyboard
from aiogram.fsm.context import FSMContext
from methods import user_filter_to_db
from utils.states import *
from filters.admin_filters import *
from methods.user_filter_to_db import *


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
    await state.set_state(BotStates.car_to_find_get_year)
    logging.info("Year in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=car_to_find_keyboard.cars_to_find_year_kb)
    
@router.message(BotStates.car_to_find_get_year)
async def cars_year_to_find(message: Message ,state: FSMContext):
    logging.info("get info for car in stock button")
    await state.update_data(car_to_find_year_select = message.text)
    await state.set_state(BotStates.car_to_find_sent_contact)
    await message.answer('Щоб отримати детальнішу інформацію, натисніть Отримати інформацію', reply_markup=car_to_find_keyboard.send_contact_car_to_find)

        
@router.message(BotStates.car_to_find_sent_contact)
async def contact_to_manager_to_find_car(message: Message,state:FSMContext) -> None:
    logging.info('after_data_provided')
    try:

        user_data_dict = await state.get_data()
        car = ','.join(user_data_dict.values())
        car = f'Авто на підбір: {car}'
        dict_user_info = await user_filter_to_db.get_basic_info(message)
    except Exception as ex:
        logging.error(f'ERROR IN PARSING CAR_TO_FIND BUTTON, {ex}')

        dict_user_info = await get_basic_info(message)
        car = ', '.join(dict_user_info.values())
        dict_user_info = await user_filter_to_db.get_basic_info(message)
    except Exception as ex:
        logging.error(f'ERROR IN PARSING 2 BUTTON, {ex}')

    try:
        with sqlite3.connect("database/clients.db") as db:
            cur = db.cursor()
            query = (""" INSERT INTO CertainCar
                (client_id,client_name,car_to_find,client_phone,time)
                VALUES (?, ?, ?,?,?)
                """)
            values = (dict_user_info['user_id'],dict_user_info['user_name'], car, dict_user_info['phone_number'],dict_user_info['time'])
            cur.execute(query, values)
            db.commit()
    except Exception as ex:
        logging.error(f'ERROR IN CAR_TO_FIND BUTTON  DB, {ex}')
    finally:
        result = await is_object_added(cur)
        await send_status_to_user(message,result)
        await message.answer(text='Верніться в головне меню', reply_markup=start_keyboard.back_bome_kb)

