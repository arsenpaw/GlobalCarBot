from aiogram.filters.callback_data import *


class UserInfoCallback(CallbackData, prefix="my"):
    foo: str
    user_info: str


class AdminSelectCallback(CallbackData, prefix="adm"):
    foo: str
    id_selected: int
