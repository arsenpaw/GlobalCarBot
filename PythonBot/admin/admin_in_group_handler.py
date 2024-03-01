import logging

from aiogram import F, Bot, types, Router
from aiogram.filters import Command
import sqlite3

from filters.admin_filters import *
admin_group_router = Router()
admin_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
admin_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))


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
        for person in rows:
            name = person[2]
            request = person[3]

            phone_number = person[4]
            phone_number =f'+ {phone_number}' if '+' not in phone_number else phone_number
            await message.answer(f'Імя: {name}\n'
                           f'Номер телефону  {phone_number}\n'
                           f'Запит: {request}\n'
                            f'Статус: Не оброблено')




