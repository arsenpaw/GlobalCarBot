from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

carfax_start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отримати CarFax'),
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

aproove_carfax_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Підтвердити отримання CarFax', request_contact=True),
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
