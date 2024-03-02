import logging

import sqlite3

from aiogram.filters import CommandStart
from Handlers.callback_user_chose_car import CallbackDataHolder
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import start_keyboard
from aiogram.fsm.context import FSMContext
from database.database_methods import *
from methods.user_filter_to_db import *
from filters.admin_filters import *



router = Router()
router.message.filter(ChatTypeFilter(["private"]))




@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    logging.info("/command start")
    await message.answer(f"<b>Привіт {message.from_user.first_name} !</b>\n"
                         f"Це чат-бот компанії Global Car 🚘🇺🇸 \n"
                         f"Ми займаємось доставкою автомобілів в будь-яку точку України 🇺🇦\n"
                         f"⬇️ Виберіть послугу ⬇️",
                         reply_markup=start_keyboard.start_kb)

@router.message(BotStates.main_menu)
@router.message(F.text.lower() == 'головне меню')
async def back_to_menu(message: Message,state:FSMContext):
    await state.clear()
    logging.info("/main menu command")
    await message.answer('⬇️Ви в головному меню, виберіть послугу.⬇️', reply_markup=start_keyboard.start_kb)

@router.message(BotStates.contact_with_manager)
@router.message(F.text.lower() == 'звязок з менеджером')
async def connect_to_manager(message: Message,state:FSMContext):
    logging.info("connect_to_manager")
    await state.clear()
    await state.set_state(BotStates.contact_with_manager)
    try:
        dict_user_info = await get_basic_info(message)
    except Exception as ex:
        logging.error(f'ERROR IN PARSING 1 BUTTON, {ex}')
    try:
        with sqlite3.connect("database/clients.db") as db:
            cur = db.cursor()
            query = (""" INSERT INTO CertainCar
                    (client_id,client_name,car_to_find,client_phone,time)
                    VALUES (?, ?, ?,?,?)
                    """)
            await state.update_data(contact_with_manager = message.text)
            dict_data = await state.get_data()
            if CallbackDataHolder.get_callback_data() is not None:
                values = (dict_user_info['user_id'], dict_user_info['user_name'], CallbackDataHolder.get_callback_data(),
                          dict_user_info['phone_number'],
                          dict_user_info['time'])

            else:
              values = (dict_user_info['user_id'], dict_user_info['user_name'], 'Звяжіться зі мною', dict_user_info['phone_number'],
                          dict_user_info['time'])
            cur.execute(query, values)
            db.commit()
    except Exception as ex:
        logging.error(f'ERROR IN FIRST BUTTON  DB, {ex}')
    finally:
        CallbackDataHolder.clear_callback_data()
        result = await is_object_added(cur)
        await send_status_to_user(message, result)
        await message.answer("Верніться в головне меню", reply_markup=start_keyboard.back_bome_kb)

