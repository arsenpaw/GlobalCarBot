import logging

from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import *

router = Router()


@router.message(F.text.lower() == 'вартість під ключ')
async def estimated_cost_handler(message: Message) -> None:
    logging.info("/estimated cose")
    await message.answer(f"Ми зробимо для вас індивідуальний прорахуноквартості під ключ в Україні \n "
                         f"Вкажіть, який автомобіль вас цікавить\n \n "
                         f"- марка, модель та рік\n \n"
                         f"- посилання на лот на аукціоні\n \n"
                         f"- тощо",
                         reply_markup=estimated_cost_keyboards.individual_cost_kb)