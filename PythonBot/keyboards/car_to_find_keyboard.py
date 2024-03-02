from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

cars_to_find_price_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='До 10 000$'),
         KeyboardButton(text='10 000$ - 20 000$')
        ],
        [
         KeyboardButton(text='20 000$ - 30 000$'),
         KeyboardButton(text='50 000$ +')
        ],
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

cars_to_find_year_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='до 2007'),
         KeyboardButton(text='2008-2012')
        ],
        [
         KeyboardButton(text='2013-2018'),
         KeyboardButton(text='2019-2024')
        ],
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

send_contact_car_to_find = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='Поділитись контактом', request_contact = True),
        ]
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)