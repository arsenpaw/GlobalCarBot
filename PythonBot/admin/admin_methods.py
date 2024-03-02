import logging

from aiogram import F, Bot, types, Router
from aiogram.filters import Command
import sqlite3
from  admin.admin_kb import *
from utils.callback_data import *
from filters.admin_filters import *
admin_group_router = Router()
admin_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
admin_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))
from database.database_methods import *
from utils.states import Status
from  admin.admin_in_group_handler import MESSAGE_OVERLOAD

class LastMessageSend:
    id = int()
async def auto_request_to_db(bot:Bot):
    logging.info('send_aplies_to_admin')
    cur_chat_id = bot.chat_to_send
    if cur_chat_id == 0:
        logging.info('AUTORN DIDNT WORK')
        return
    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = (""" SELECT * FROM CertainCar WHERE status = 'unhandled' AND id > ?;
               """)
        values = (LastMessageSend.id,)
        cur.execute(query, values)
        rows = cur.fetchall()
        logging.info(f"SQL RESPONCE {rows}")
        if len(rows) == 0:
            return
        LastMessageSend.id = rows[-1][0]
        if len(rows) > MESSAGE_OVERLOAD:
            rows = rows[:MESSAGE_OVERLOAD]
            await bot.send_message(chat_id=cur_chat_id,text=f'⚠️Увага!⚠️\n Дуже багато заявок, обробіть спочатку найстаріші')
        for person in rows:
            id = person[0]
            name = person[2]
            request = person[3]
            phone_number = person[4]
            phone_number =f'+ {phone_number}' if '+' not in phone_number else phone_number
            await bot.send_message(chat_id=cur_chat_id,text =f'Імя: {name}\n'
                           f'Номер телефону  {phone_number}\n'
                           f'Запит: {request}\n'
                            f'Статус: ❌Не оброблено❌', reply_markup=admin_message_ikb(id))