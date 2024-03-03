import io
import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext
from admin.admin_methods import *
from utils.states import *
from typing import BinaryIO
from admin.admin_kb import *
from aiogram.types.file import File
from keyboards.start_keyboard import *
import uuid
from keyboards.start_keyboard import back_bome_kb

admin_private_router = Router()
admin_private_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())
admin_private_router.edited_message.filter(ChatTypeFilter(["private"]), IsAdmin())


@admin_private_router.message(Command("admin"))
@admin_private_router.message(F.text.lower() == 'в адмін панель')
async def private_admin_handler(message: Message,state:FSMContext):
    await state.clear()
    logging.info(f'AUTHROIZE PRIVATE ADMIN {message.from_user.full_name}')
    await message.answer(f'<b>Ви в адмін панелі, виберіть функцію.</b>', reply_markup=admin_panel_private)


@admin_private_router.message(BotStates.add_car)
@admin_private_router.message(F.text.lower() == 'додати авто')
async def add_car_method(message: Message, state: FSMContext, bot: Bot):
    logging.info(f'add_car_method')
    await message.answer("<b>Вводіть всю інформацю корректно щоб потім не їсти собі нерви</b>")
    await message.answer("<b>Вкажіть назву</b>, \nПишіть тільки марку і модель \nПриклад: Honda Acord", reply_markup=back_admin_kb)
    await state.set_state(BotStates.add_car_name)

@admin_private_router.message(BotStates.add_car_name)
async def add_name_to_car(message: Message, state: FSMContext, bot: Bot):
    logging.info(f'add_name_to_car')
    try:
        name = str(message.text)
        await state.update_data(name = name)
        await message.answer(f'<b>Надішліть фото.</b>', reply_markup=back_admin_kb)
        await state.set_state(BotStates.add_car_photo)

    except Exception as ex:
        await state.set_state(BotStates.add_car_name)
        await message.answer(f'<b>Помилка при введені інфи,спробуйте ще раз.</b>')
        logging.warning(f'WRONG INPUT PHOTO:{ex}')

@admin_private_router.message(BotStates.add_car_photo)
async def add_photo_to_car(message: Message, state: FSMContext, bot: Bot):
    logging.info(f'add_photo_to_car')
    try:
        file_id = message.photo[-1].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        filename = str(uuid.uuid4())
        final_path = f"database/CarPhotos/{filename}.jpg"
        await bot.download_file(file_path, final_path)
        await state.update_data(path_to_photo=final_path)
        await state.set_state(BotStates.add_car_price)
        await message.answer("<b>Вкажіть ціну</b>, \n Пишіть тільки суму в долларах США і нічого іншого \nПриклад: 9000", reply_markup=back_admin_kb)
    except Exception as ex:
        await state.set_state(BotStates.add_car_photo)
        await message.answer(f'<b>Помилка збереження. \nНадішліть зображення ще раз або спробуйте інше .</b>')
        logging.warning(f'WRONG INPUT PHOTO:{ex}')


@admin_private_router.message(BotStates.add_car_price)
async def add_price_to_car(message: Message, state: FSMContext, bot: Bot):
    logging.info('add_price_to_car')
    logging.info(await state.get_data())
    try:
        price = int(message.text)
        await state.update_data(price=price)
        await state.set_state(BotStates.add_car_year)
        await message.answer('Введіть рік, вказуюючи тільки цифру \n Наприклад: 2009',reply_markup=back_admin_kb)
    except Exception as ex:
        logging.warning(f'WRONG INPUT, NEED ONLY NUMS {ex}')
        await message.answer('Введіть суму, вказуюючи тільки цифри !!!. ')
        await state.set_state(BotStates.add_car_price)

@admin_private_router.message(BotStates.add_car_year)
async def add_year_to_car(message: Message, state: FSMContext, bot: Bot):
    logging.info('add_year_to_car')
    logging.info(await state.get_data())
    try:
        year = int(message.text)
        await state.update_data(year=year)
        await state.set_state(BotStates.add_car_desctiption)
        await message.answer('<b>Введіть опис</b> \nПриклад: Крута машина.',reply_markup=back_admin_kb)
    except Exception as ex:
        logging.warning(f'WRONG INPUT, NEED ONLY NUMS {ex}')
        await message.answer('Введіть рік, вказуюючи тільки цифру !!!. \n Наприклад: 2009')
        await state.set_state(BotStates.add_car_year)

@admin_private_router.message(BotStates.add_car_desctiption)
async def add_description_to_car(message: Message, state: FSMContext, bot: Bot):
    logging.info('add_description_to_car')
    logging.info(await state.get_data())
    try:
        description = str(message.text)
        await state.update_data(description=description)
        await sent_admin_car_to_db(message,state)
    except Exception as ex:
        logging.warning(f'WRONG INPUT, NEED ONLY NUMS {ex}')
        await message.answer('Просто введіть текст' )
        await state.set_state(BotStates.add_car_desctiption)

async def sent_admin_car_to_db(message: Message, state: FSMContext):
    logging.info('sent_admin_car_to_db')
    dict_info = await state.get_data()
    logging.info(dict_info)
    photo_path = dict_info['path_to_photo']
    price = dict_info['price']
    year = dict_info['year']
    description = dict_info['description']
    name = dict_info['name']
    try:
        with sqlite3.connect("database/clients.db") as db:
            cur = db.cursor()
            query = (""" INSERT INTO CarShop
                   (car_photo,car_year,car_cost,car_name,car_description)
                   VALUES (?, ?, ?,?,?)
                   """)
            values = (photo_path,year,price,name,description)
            cur.execute(query, values)
            db.commit()
    except Exception as ex:
        logging.error(f'ERROR IN ADMIN PRIVATE BUTTON  DB, {ex}')
    finally:
        result = await is_object_added(cur)
        if result is True:
            await message.answer('Товар успішно доданий',reply_markup=back_admin_kb)
        else:
            await message.answer('Ойойо щось не так спройбуте пізніше',reply_markup=back_admin_kb)

