import logging

from aiogram import F, Bot, types, Router
from aiogram.filters import Command
import sqlite3
from admin.admin_kb import *
from utils.callback_data import *
from filters.admin_filters import *
from database.database_methods import *
from utils.states import Status
from admin.admin_methods import *
from admin.constants import *

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
    logging.info(f'ADMINS{admins_list}')
    bot.chat_to_send = chat_id
    logging.info(f'CHAT ID: {bot.chat_to_send}')
    if message.from_user.id in admins_list and chat_id == bot.chat_to_send:
        await message.delete()
        await message.answer('✅Синхронізація пройшла успішно✅')
    logging.info(bot.my_admins_list)


@admin_group_router.message(Command("autorun"))
async def get_admins(message: types.Message):
    chat_id = message.chat.id
    await write_into_txt(chat_id)
    checked_id = await get_from_txt()
    logging.info(f'Chat id is {checked_id}')
    if chat_id == checked_id:
        await message.delete()
        await message.answer('✅Chat_Id доданий✅')


@admin_group_router.message(Command("update"))
async def get_aplies(message: types.Message):
    logging.info('send_aplies_to_admin')

    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = (""" SELECT * FROM CertainCar WHERE status = 'unhandled';
               """)
        cur.execute(query)
        rows = cur.fetchall()
        logging.info(f"SQL RESPONCE {rows}")
        if len(rows) == 0:
            await message.answer(f'Всі заявки оброблені 🎉.')
            logging.info('no data to handle')
            return
        elif len(rows) > MESSAGE_OVERLOAD:
            rows = rows[:MESSAGE_OVERLOAD]
            await message.answer(f'⚠️Увага!⚠️\n Дуже багато заявок, обробіть спочатку найстаріші')
        LastMessageSend.set_id_data(rows[-1][0])
        for person in rows:
            id = person[0]
            name = person[2]
            request = person[3]
            phone_number = person[4]
            await message.answer(f'Імя: {name}\n'
                                 f'Номер телефону  {phone_number}\n'
                                 f'Запит: {request}\n'
                                 f'Статус: ❌Не оброблено❌', reply_markup=admin_message_ikb(id))


@admin_group_router.callback_query(AdminSelectCallback.filter(F.foo == "selected_item"))
async def callback_query(callback_query: CallbackQuery, callback_data: UserInfoCallback):
    logging.info('callback_query_admin_group')
    selected_id = callback_data.id_selected
    logging.info(selected_id)
    with sqlite3.connect("database/clients.db") as db:
        cur = db.cursor()
        query = """
            UPDATE CertainCar
            SET status = ?
            WHERE id = ?
        """

        cur.execute(query, (Status.HANDLED.value, selected_id))
    if cur.rowcount > 0:
        logging.info("Status updated successfully.")
        logging.info(callback_query.message.text)
        final_msg = await replace_last_two_words(callback_query.message.text, f'✅{callback_query.from_user.full_name}'
                                                                              f', обробленно✅')
        await callback_query.message.edit_text(final_msg)

    else:
        logging.error(
            "No rows were updated. The specified ID might not exist or the status is already set to the desired value.")
        await callback_query.message.answer('ЙОЙОЙОЙ помилка при введені в БД')
