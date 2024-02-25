import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.lower() == 'Авто в наявності')
async def back_to_menu(message: Message):
    logging.info("cars in stock button")
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=cars_in_stock_keyboard.cars_cost_in_stock_kb)
