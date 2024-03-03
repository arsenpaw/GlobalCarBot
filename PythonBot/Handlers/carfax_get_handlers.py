import logging
import sqlite3

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router

import database.database_methods
from keyboards import carfax_keyboard
from utils.states import *
from aiogram.fsm.context import FSMContext
from database.database_methods import *
from methods.others import *
from methods.user_filter_to_db import *

from filters.admin_filters import *

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


@router.message(F.text.lower() == 'отримати carfax')
async def cars_cost_in_stock(message: Message, state: FSMContext):
    logging.info("Carfax Button")
    await state.set_state(BotStates.carfax_get_info)
    await message.answer(
        "Щоб отримати звіт по авто, <b> залиште нижче VIN код або посилання на лот на аукціоні</b> та підтвердіть отриання Carfax",
        reply_markup=start_keyboard.back_bome_kb)


@router.message(BotStates.carfax_get_info)
async def handle_vin_user_input(message: Message, state: FSMContext):
    logging.info("handle_vin_user_input")
    unchecked_masg = message.text
    bool_msg_valid = await is_vin_valid(unchecked_masg)
    logging.info(f'{bool_msg_valid}')
    if bool_msg_valid is True:
        await state.update_data(carfax_get_info=unchecked_masg)
        await state.set_state(BotStates.send_vin_to_manager)
        await message.answer('Щоб підтвердити отримання, натисніть "Підтвердити отримання CarFax" ',
                             reply_markup=carfax_keyboard.aproove_carfax_keyboard)
    else:
        await state.set_state(BotStates.carfax_get_info)
        await message.answer('Ви ввели некоректний VIN aбо некоректне посилання.\nВведіть інформацію ще раз',
                             reply_markup=start_keyboard.back_bome_kb)


@router.message(BotStates.send_vin_to_manager)
async def handle_msg_to_manger(message: Message, state: FSMContext):
    logging.info('handle_vin_user_input')
    try:
        dict_vin = await state.get_data()
        vin = ''.join(str(value) for value in dict_vin.values())
        vin_request = f'CarFax: {str(vin)}'
        dict_user_info = await get_basic_info(message)
    except Exception as ex:
        logging.error(f'ERROR IN PARSING 4 BUTTON, {ex}')
    try:
        with sqlite3.connect("database/clients.db") as db:
            cur = db.cursor()
            query = (""" INSERT INTO CertainCar
                (client_id,client_name,car_to_find,client_phone,time)
                VALUES (?, ?, ?,?,?)
                """)
            values = (
                dict_user_info['user_id'], dict_user_info['user_name'], vin_request, dict_user_info['phone_number'],
                dict_user_info['time'])
            cur.execute(query, values)
            db.commit()
    except Exception as ex:
        logging.error(f'ERROR IN 4 BUTTON  DB, {ex}')
    finally:
        result = await is_object_added(cur)
        await send_status_to_user(message, result)
        await message.answer(text='Верніться в головне меню', reply_markup=start_keyboard.back_bome_kb)
