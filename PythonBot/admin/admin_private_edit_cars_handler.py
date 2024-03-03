import io
import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext
import os

import admin.admin_kb
import keyboards.start_keyboard
from admin.admin_methods import *
from utils.states import *
from typing import BinaryIO
from admin.admin_kb import *
from aiogram.types.file import File
from keyboards.start_keyboard import *
import uuid
from admin.constants import *

admin_private_router = Router()
admin_private_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())
admin_private_router.edited_message.filter(ChatTypeFilter(["private"]), IsAdmin())


class ShowedItem():
    count = int()
    all_list = list()


async def get_reversed_rows_from_CarShop() -> list:
    logging.info('reversed query from CarShop')
    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = """ SELECT * FROM CarShop """
        cur.execute(query)
        rows = cur.fetchall()
        rows.reverse()
        logging.info(f"SQL RESPONCE {rows}")
        return rows


async def sent_car_items_limited(short_rows: list, message: Message, bot: Bot):
    for row in short_rows:
        id = row[0]
        path_to_photo = row[1]
        logging.info(path_to_photo)
        photo = FSInputFile(f"{path_to_photo}")
        year = row[2]
        price = row[3]
        car_name = row[4]
        car_description = row[5]
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=photo,reply_markup=admin_car_ikb(id),
                                 caption=f"{car_name}\n"
                                         f"Рік {year}р \n"
                                         f"Ціна {price}$\n"
                                         f"Опис {car_description}")
        except Exception as ex:
            logging.warning(f'PICTURE DIDNT FOUND{ex}')
            photo = FSInputFile(r"database\CarPhotos\unknown.jpg")
            await bot.send_photo(chat_id=message.chat.id, photo=photo,reply_markup=admin_car_ikb(id),
                                 caption=f"{car_name}\n"
                                         f"Рік {year}р \n"
                                         f"Ціна {price}$\n"
                                         f"Опис {car_description}")


@admin_private_router.message(F.text.lower() == 'редагувати автомобілі')
async def edti_cars(message: Message, state: FSMContext, bot: Bot):
    logging.info(f'add_car_method')
    await message.answer("<b>Ось всі ваші машини</b>")
    rows = await get_reversed_rows_from_CarShop()
    ShowedItem.all_list = rows
    if len(rows) == 0:
        await message.answer('На жаль у вас немає машин, додайте їх спершу')
        return
    elif len(rows) > MESSAGE_OVERLOAD:
        await message.answer(f'У вас бато машин, тому будем показувати їх по {MESSAGE_OVERLOAD}')
        short_rows = rows[:MESSAGE_OVERLOAD]
    else:
        short_rows = rows
    ShowedItem.count = MESSAGE_OVERLOAD
    await sent_car_items_limited(short_rows, message, bot)
    if len(rows) > MESSAGE_OVERLOAD:
        await message.answer('Це не всі машини, показати ще ?', reply_markup=show_more_kb)
        await state.set_state(BotStates.show_more_cars)
    else:
        await message.answer('Це всі машини,', reply_markup=keyboards.start_keyboard.back_bome_kb)


@admin_private_router.message(BotStates.show_more_cars)
async def show_more_cars(message: Message, state: FSMContext, bot: Bot):
    low_border = ShowedItem.count
    high_border = ShowedItem.count + MESSAGE_OVERLOAD
    if high_border >= len(ShowedItem.all_list):
        ShowedItem.count = len(ShowedItem.all_list)
        showed_list = ShowedItem.all_list[low_border:len(ShowedItem.all_list)]
    else:
        ShowedItem.count = high_border
        showed_list = ShowedItem.all_list[low_border:high_border]
    await sent_car_items_limited(showed_list, message, bot)
    if len(ShowedItem.all_list) > high_border:
        await message.answer('Це не всі машини, показати ще ?', reply_markup=show_more_kb)
        await state.set_state(BotStates.show_more_cars)
    else:
        await message.answer('Це всі машини', reply_markup=admin_panel_private)


@admin_private_router.callback_query(AdminSelectCallback.filter(F.foo == "admin_deleted"))
async def callback_query_private(callback_query: CallbackQuery, callback_data: UserInfoCallback):
    logging.info('callback_query_private')
    selected_id = callback_data.id_selected
    logging.info(selected_id)
    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = """
            SELECT car_photo   
            FROM CarShop
            WHERE id = ?
        """
        cur.execute(query, (selected_id,))
        result = cur.fetchone()
        car_photo_path = result[0]
        logging.info(f'CAR PATH TO DELETE {car_photo_path}')
        if result is not None:
            query_delete = """
                       DELETE FROM CarShop
                        WHERE id = ?
                   """
            cur.execute(query_delete, (selected_id,))
            db.commit()
            result_after = cur.fetchone()
            if result_after is None:
                await callback_query.message.delete()
                try:
                    os.remove(car_photo_path)
                    await callback_query.message.answer('✅Машину видалено✅', reply_markup=show_more_kb)
                except Exception as ex:
                    logging.error(f'CAN NOT DELETE LOCAL FILE: {ex}')
                    await callback_query.message.answer('✅Машину видалено✅',
                                                        reply_markup=show_more_kb)
            else:
                await callback_query.message.answer('❌Машину НЕ видалено❌')
                logging.warning('CAR NOT DELETED FROM DB')

        else:
           logging.info('car not found when deleting from db')
           await callback_query.message.answer('⚠️Машину не знайдено⚠️')
