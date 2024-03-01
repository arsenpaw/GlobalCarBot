from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from  aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
def admin_message_ikb(id:int):
    builder = InlineKeyboardBuilder()
    str_id = str(id)
    builder.button(text='Обробити',callback_data=str_id)
    return builder.as_markup(resize_keyboard=True)