import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router, types
from keyboards import cars_in_stock_keyboard
from aiogram.types.callback_query import *
from aiogram.fsm.context import FSMContext
from utils.states import *
from keyboards.start_keyboard import *
from aiogram.filters.callback_data import *
from filters.admin_filters import *
from utils.callback_data import *
from aiogram.types.callback_query import CallbackQuery

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


class CallbackDataHolder:
    __call_back_data = None

    @staticmethod
    def set_callback_data(text: str):
        CallbackDataHolder.__call_back_data = text

    @staticmethod
    def get_callback_data():
        return CallbackDataHolder.__call_back_data

    @staticmethod
    def clear_callback_data():
        CallbackDataHolder.__call_back_data = None


@router.callback_query(UserInfoCallback.filter(F.foo == "user_info"))
async def callback_query(callback_query: CallbackQuery, callback_data: UserInfoCallback, state: FSMContext):
    logging.info('callback_query')
    callback_data = callback_data.user_info
    logging.info(f'CALL BACK {callback_data}')
    CallbackDataHolder.set_callback_data(f'З магазину GlobalCar: {callback_data}')
    await state.set_state(BotStates.contact_with_manager)
    await callback_query.message.answer(
        '<b>Класний вибір 🔥</b>\nНатисніть <i>Отримати інформацію</i> і ви дізнаєтесь ще більше про це авто.',
        reply_markup=detail_info_and_main_kb)
