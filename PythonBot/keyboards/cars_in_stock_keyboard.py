from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from utils.callback_data import *


def car_ikb(short_info: str):
    builder = InlineKeyboardBuilder()

    builder.button(text='Докладніше', callback_data=UserInfoCallback(foo="user_info", user_info=short_info))
    return builder.as_markup(resize_keyboard=True)


cars_cost_in_stock_kb = ReplyKeyboardMarkup(
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
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

cars_year_in_stock_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='до 2007'),
            KeyboardButton(text='2008-2012')
        ],
        [
            KeyboardButton(text='2013-2018'),
            KeyboardButton(text='2019 + ')
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отримати інформацію', request_contact=True),
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
