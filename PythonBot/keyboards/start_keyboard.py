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
        ],
        [
         KeyboardButton(text='В головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
