from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='Вартість під ключ'),
         KeyboardButton(text='Авто в наявності')
        ],
        [
         KeyboardButton(text='Авто на підбір'),
         KeyboardButton(text='Отримати CarFax')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

consult_and_main_kb= ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='Звязок з менеджером'),
        ],
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

back_bome_kb= ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='В головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
<<<<<<< HEAD
)


auto_cost_in_stock_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='До 8 000$'),
         KeyboardButton(text='8 000$ - 15 000$')
        ],
        [
         KeyboardButton(text='15 000$ - 20 000$'),
         KeyboardButton(text='20 000$ +')
        ],
        [
         KeyboardButton(text='В головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
=======
>>>>>>> 020e6800a06dcdf629c0d1766ce8ea8a5737d7cc
)