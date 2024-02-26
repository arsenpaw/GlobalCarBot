import logging

from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import cars_in_stock_keyboard
from utils.states import *
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(F.text.lower() == 'авто в наявності')
async def cars_cost_in_stock(message: Message, state: FSMContext):
    logging.info("cars in stock button")
    await state.set_state(BotStates.price_selection)
    await message.answer('Який ваш комфортний бюджет для купівлі авто?', reply_markup=cars_in_stock_keyboard.cars_cost_in_stock_kb)
    
    

@router.message(BotStates.price_selection)
async def cars_year_in_stock(message: Message ,state: FSMContext):
    await state.update_data(price_selection = message.text)
    await state.set_state(BotStates.year_selection)
    logging.info("Year in stock button")
    await message.answer('Автомобіль яких років випуску ви розглядаєте?', reply_markup=cars_in_stock_keyboard.cars_year_in_stock_kb)
    
@router.message(BotStates.year_selection)
async def cars_year_in_stock(message: Message ,state: FSMContext):
    await state.update_data(year_select = message.text)
    logging.info("contact")
    await message.answer('Дані підтверждено✅')
    await message.answer('Натисніть на кнопку Отримати підбірку , щоб чат-бот надіслав відповідні варіанти під ваш запит в Telegram👇', reply_markup=cars_in_stock_keyboard.send_contact)
    await Bot.send_contact(message.from_user.id)