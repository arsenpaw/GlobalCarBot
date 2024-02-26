from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

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