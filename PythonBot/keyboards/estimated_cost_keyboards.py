from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

individual_cost_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='Звязок з менеджером'),
         KeyboardButton(text='Отрмати прорахунок')
        ],
        [
         KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)