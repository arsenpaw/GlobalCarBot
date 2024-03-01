
from aiogram.filters.callback_data import  *
class UserInfoCallback(CallbackData, prefix="my"):
    foo: str
    user_info: str