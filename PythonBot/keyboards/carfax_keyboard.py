from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

carfax_start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='ОТРИМАТИ CARFAX'),
        ],
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)