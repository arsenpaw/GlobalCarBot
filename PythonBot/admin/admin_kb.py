from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callback_data import *


def admin_message_ikb(id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text='Обробити', callback_data=AdminSelectCallback(foo="selected_item", id_selected=id))
    return builder.as_markup(resize_keyboard=True)
