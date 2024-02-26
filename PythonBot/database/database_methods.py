import logging
import sqlite3 as sqlite
from aiogram.types import *
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router

async def is_object_added(cur: sqlite.Cursor)->bool:
    logging.info(msg = 'is_object_added')

    if cur.fetchall() is True:
        logging.info(f'IS USER ADD TO TABLE: TRUE')
        return True
    else:
        logging.info(f'IS USER ADD TO TABLE: FALSE')
        return False

async  def send_status_to_user(message: Message, is_sucesfull: bool)->None:
    logging.info('send status to user from db folder')
    if is_sucesfull is True:
       await message.answer("Заявку успішно залишено. З вами звяжуться протягом найближчого часу.")
    else:
        await message.answer("Ой, щось пішло не так. Спробуйте знову")