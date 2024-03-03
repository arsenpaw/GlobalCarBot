import logging

from aiogram import F, Bot, types, Router
from aiogram.filters import Command
import sqlite3
from admin.admin_kb import *
from utils.callback_data import *
from filters.admin_filters import *

admin_group_router = Router()
admin_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
admin_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))
from database.database_methods import *
from utils.states import Status
from admin.constants import *


class LastMessageSend:
    __id = int()

    @staticmethod
    def set_id_data(id: int):
        logging.info(f'LAST ID SET:{id}')
        LastMessageSend.__id = id

    @staticmethod
    def get_id_data() -> int:
        return LastMessageSend.__id

    @staticmethod
    def clear_id_data():
        LastMessageSend.__id = int()


async def replace_last_two_words(input_string, new_words):
    lines = input_string.split('\n')
    last_line = lines.pop()
    words = last_line.split()
    removed_words = words[-2:]
    words = words[:-2]
    words.extend(new_words.split())
    new_last_line = ' '.join(words)
    lines.append(new_last_line)
    result = '\n'.join(lines)
    return result


async def write_into_txt(info: int):
    with open('admins_chat_id.txt', 'w') as f:
        info = str(info)
        f.write(info)


async def get_from_txt() -> int:
    with open('admins_chat_id.txt', 'r') as f:
        chat_id = f.read()
        try:
            chat_id = int(chat_id)
        except:
            chat_id = int()
        return chat_id


async def auto_request_to_db(bot: Bot):
    logging.info('send_AUTO_aplies_to_admin')
    cur_chat_id = await get_from_txt()
    if cur_chat_id == 0:
        logging.info('AUTORN DIDNT WORK, need command /autorun to activate')
        return
    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = (""" SELECT * FROM CertainCar WHERE status = 'unhandled' AND id > ?;
               """)
        values = (LastMessageSend.get_id_data(),)
        cur.execute(query, values)
        rows = cur.fetchall()
        logging.info(f"SQL RESPONCE {rows}")
        if len(rows) == 0:
            logging.info('No data to send in auto send')
            return
        LastMessageSend.set_id_data(rows[-1][0])
        if len(rows) > MESSAGE_OVERLOAD:
            rows = rows[:MESSAGE_OVERLOAD]
            await bot.send_message(chat_id=cur_chat_id,
                                   text=f'⚠️Увага!⚠️\n Дуже багато заявок, обробіть спочатку найстаріші')
        for person in rows:
            id = person[0]
            name = person[2]
            request = person[3]
            phone_number = person[4]
            phone_number = f'+ {phone_number}' if '+' not in phone_number else phone_number
            await bot.send_message(chat_id=cur_chat_id, text=f'Імя: {name}\n'
                                                             f'Номер телефону  {phone_number}\n'
                                                             f'Запит: {request}\n'
                                                             f'Статус: ❌Не оброблено❌',
                                   reply_markup=admin_message_ikb(id))
