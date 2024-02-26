import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import carfax_keyboard
from utils.states import *
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(F.text.lower() == 'отримати carfax')
async def cars_cost_in_stock(message: Message, state: FSMContext):
    logging.info("Carfax Button")
    await state.set_state(BotStates.carfax_get_info)
    await message.answer("Щоб отримати звіт по авто, залиште нижче VIN код або посилання на лот на аукціоні та натисніть на кнопку Отримати Carfax для підтвердження", reply_markup=carfax_keyboard.carfax_start_keyboard)
    