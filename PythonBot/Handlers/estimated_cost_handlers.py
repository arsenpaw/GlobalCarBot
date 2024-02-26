import logging,os
import sqlite3

from aiogram.types import *
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import *
from aiogram.fsm.context import FSMContext
from utils.states import *
from database.database_methods import *
from  methods.user_filter_to_db import *

router = Router()


db = sqlite3.connect("database/clients.db")
cur = db.cursor()


@router.message(F.text.lower() == 'вартість під ключ')
async def estimated_cost_handler(message: Message,state:FSMContext) -> None:
    logging.info("/estimated cose")
    await state.set_state(BotStates.user_car_info)
    await message.answer(f"Ми зробимо для вас індивідуальний прорахуноквартості під ключ в Україні \n "
                         f"<b>Вкажіть, який автомобіль вас цікавить</b>\n \n "
                         f"- марка, модель та рік\n \n"
                         f"- посилання на лот на аукціоні\n \n"
                         f"- тощо",
                         reply_markup = start_keyboard.consult_and_main_kb)


@router.message(BotStates.user_car_info)
async def wait_data_input(message: Message,state:FSMContext) -> None:
    logging.info("User input")
    await state.update_data(user_car_info = message.text)
    logging.info(message.text)
    await message.answer(f"Інформацію збережено.")
    await state.set_state(BotStates.contact_to_user_about_info)
    await message.answer(f"Щоб отрмати детальнішу інформацію по даному автомобілю "
                          f"\n натисніть 'Отримати прорахунок' aбо звяжіться з менеджером",
                         reply_markup=estimated_cost_keyboards.individual_cost_kb)

@router.message(BotStates.contact_to_user_about_info)
async def after_data_provided(message: Message,state:FSMContext) -> None:
    logging.info('after_data_provided')
    try:
        dict_car = await state.get_data()
        car = ''.join(str(value) for value in dict_car.values())
        logging.info(f'Selected car {car}')
        dict_user_info = await get_basic_info(message)
    except Exception as ex:
        logging.error(f'ERROR IN PARSING 1 BUTTON, {ex}')
    try:
        query = (""" INSERT INTO CertainCar
            (client_id,client_name,car_to_find,client_phone,time)
            VALUES (?, ?, ?,?,?)
            """)
        values = (dict_user_info['user_id'],dict_user_info['user_name'], car,dict_user_info['phone_number'],dict_user_info['time'])
        cur.execute(query, values)
        db.commit()
    except Exception as ex:
        logging.error(f'ERROR IN FIRST BUTTON  DB, {ex}')
    finally:
        result = await is_object_added(cur)
        await send_status_to_user(message,result)
        db.close()
