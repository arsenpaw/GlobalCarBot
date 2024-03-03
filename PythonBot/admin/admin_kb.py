from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callback_data import *
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

def admin_message_ikb(id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text='Обробити', callback_data=AdminSelectCallback(foo="selected_item", id_selected=id))
    return builder.as_markup(resize_keyboard=True)


admin_panel_private = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Додати авто'),
            KeyboardButton(text='Редагувати автомобілі')
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

show_more_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показати ще')
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
