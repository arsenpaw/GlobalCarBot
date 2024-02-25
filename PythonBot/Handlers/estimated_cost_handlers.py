import logging

from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import *
from aiogram.fsm.context import FSMContext
from  utils.states import *

router = Router()


@router.message(F.text.lower() == 'вартість під ключ')
async def estimated_cost_handler(message: Message,state:FSMContext) -> None:
    logging.info("/estimated cose")
    await state.set_state(BotStates.get_estimnated_cost)
    await message.answer(f"Ми зробимо для вас індивідуальний прорахуноквартості під ключ в Україні \n "
                         f"Вкажіть, який автомобіль вас цікавить\n \n "
                         f"- марка, модель та рік\n \n"
                         f"- посилання на лот на аукціоні\n \n"
                         f"- тощо",
                         reply_markup=estimated_cost_keyboards.individual_cost_kb)

@router.message(F.text.lower() == 'вартість під ключ')
async def estimated_cost_handler(message: Message,state:FSMContext) -> None:
    logging.info("/estimated cose")
    await state.set_state(BotStates.get_estimnated_cost)
    await message.answer(f"Ми зробимо для вас індивідуальний прорахуноквартості під ключ в Україні \n "
                         f"Вкажіть, який автомобіль вас цікавить\n \n "
                         f"- марка, модель та рік\n \n"
                         f"- посилання на лот на аукціоні\n \n"
                         f"- тощо",
                         reply_markup=estimated_cost_keyboards.individual_cost_kb)

@router.message(BotStates.get_estimnated_cost)
async def wait_data_input(message: Message,state:FSMContext) -> None:
    logging.info("User input")
    print(message.text)


