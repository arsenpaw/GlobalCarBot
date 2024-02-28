import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router,types
from keyboards import cars_in_stock_keyboard
from aiogram.types.callback_query import *
from aiogram.fsm.context import FSMContext
from utils.states import *
from keyboards.start_keyboard import *

router = Router()


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

@router.callback_query()
async def callback_query(callback_query: types.CallbackQuery,state:FSMContext):
    logging.info('callback_query')
    callback_data = callback_query.data
    logging.info(f'CALL BACK {callback_data}')
    CallbackDataHolder.set_callback_data(f'З магазину GlobalCar: {callback_query.data}')
    await state.set_state(BotStates.contact_with_manager)
    await callback_query.message.answer('Класний вибір, натисніть Звязатись з менеджером та отримайте докладнішу інформацію', reply_markup=consult_and_main_kb)
