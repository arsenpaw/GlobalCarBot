import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import *
from aiogram.fsm.context import FSMContext
from  utils.states import *
from Handlers.base_handlers import connect_to_manager

router = Router()



@router.message(F.text.lower() == 'вартість під ключ')
async def estimated_cost_handler(message: Message,state:FSMContext) -> None:
    logging.info("/estimated cose")
    await state.set_state(BotStates.get_estimnated_cost)
    await message.answer(f"Ми зробимо для вас індивідуальний прорахуноквартості під ключ в Україні \n "
                         f"<b>Вкажіть, який автомобіль вас цікавить</b>\n \n "
                         f"- марка, модель та рік\n \n"
                         f"- посилання на лот на аукціоні\n \n"
                         f"- тощо",
                         reply_markup = start_keyboard.consult_and_main_kb)

@router.message(BotStates.get_estimnated_cost)
async def wait_data_input(message: Message,state:FSMContext) -> None:
    logging.info("User input")
    logging.info(message.text)
    if message.text.lower() == 'звязатись з менеджером':
        await connect_to_manager(message,state)
    else:
        await message.answer(f"Інформацію збережено.")
        await message.answer(f"Щоб отрмати детальнішу інформацію по даному автомобілю "
                          f"\n натисніть 'Отримати прорахунок' aбо звяжіться з менеджером",
                         reply_markup=estimated_cost_keyboards.individual_cost_kb)

