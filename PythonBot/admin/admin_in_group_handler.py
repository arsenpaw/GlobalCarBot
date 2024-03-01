import logging

from aiogram import F, Bot, types, Router
from aiogram.filters import Command
import sqlite3
from  admin.admin_kb import *

from filters.admin_filters import *
admin_group_router = Router()
admin_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
admin_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))

MESSAGE_OVERLOAD: int = 10
@admin_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    logging.info( bot.my_admins_list)

@admin_group_router.message(Command("update"))
async def get_aplies(message: types.Message, bot: Bot):
    logging.info('send_aplies_to_admin')

    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = (""" SELECT * FROM CertainCar WHERE status = 'unhandled';
               """)

        cur.execute(query)
        rows = cur.fetchall()
        logging.info(f"SQL RESPONCE {rows}")
        if len(rows) > MESSAGE_OVERLOAD:
            rows = rows[:MESSAGE_OVERLOAD]
            await message.answer(f'Дуже багато заявок, обрібіть спочатку найстаріші')

        for person in rows:
            id = person[0]
            name = person[2]
            request = person[3]
            phone_number = person[4]
            phone_number =f'+ {phone_number}' if '+' not in phone_number else phone_number
            await message.answer(f'Імя: {name}\n'
                           f'Номер телефону  {phone_number}\n'
                           f'Запит: {request}\n'
                            f'Статус: Не оброблено', reply_markup=admin_message_ikb(id))

@admin_group_router.callback_query()
async def callback_query(callback_query: types.CallbackQuery):
    logging.info('callback_query_admin_group')
    callback_data = callback_query.data
    logging.info(f'CALL BACK {callback_data}')




