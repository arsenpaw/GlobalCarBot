import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard

from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.lower() == 'авто в наявності')
async def cars_cost_in_stock(message: Message):
    logging.info("cars in stock button")
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=cars_in_stock_keyboard.cars_cost_in_stock_kb)
    print(F.text.lower())
    

@router.message(F.text.lower() == 'До 8 000$' 
                or F.text.lower() == '8 000$ - 15 000$' 
                or F.text.lower() == '15 000$ - 20 000$'
                or F.text.lower() == '20 000$ +'
                )
async def cars_year_in_stock(message: Message):
    logging.info("cars in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=cars_in_stock_keyboard.cars_year_in_stock_kb)
    car_cost = F.text.lower()