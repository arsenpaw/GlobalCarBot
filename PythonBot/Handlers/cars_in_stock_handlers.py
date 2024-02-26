import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard

from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.lower() == 'авто в наявності')
<<<<<<< HEAD
async def cars_cost_in_stock(message: Message):
=======
async def back_to_menu(message: Message):
>>>>>>> 411c817dc7c4d468c0bd2a4aff543edc9b97fb0a
    logging.info("cars in stock button")
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=cars_in_stock_keyboard.cars_cost_in_stock_kb)
    

