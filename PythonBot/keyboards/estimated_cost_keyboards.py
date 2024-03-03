from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

individual_cost_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Звязок з менеджером', request_contact=True),
            KeyboardButton(text='Отрмати прорахунок', request_contact=True)
        ],
        [
            KeyboardButton(text='Головне меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
