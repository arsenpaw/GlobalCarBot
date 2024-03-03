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

consult_and_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Звязок з менеджером', request_contact=True),
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
detail_info_and_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отримати детальну інформацію', request_contact=True),
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

back_bome_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
