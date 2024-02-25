import logging

from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
from keyboards import start_keyboard
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    logging.info("/command start")
    await message.answer(f"<b>Привіт {message.from_user.full_name} !</b>\n Ми ітд ітп/help",
                         reply_markup=start_keyboard.start_kb)


@router.message(F.text.lower() == 'в головне меню')
async def back_to_menu(message: Message):
    logging.info("/main menu command")
    await message.answer('Ви в головному меню', reply_markup=start_keyboard.start_kb)

<<<<<<< HEAD
@router.message(F.text.lower() == 'авто в наявності')
async def command_start_handler(message: Message) -> None:
    logging.info("/command start")
    await message.answer(f"Який ваш бюджет для купівлі авто?",
                         reply_markup=start_keyboard.auto_cost_in_stock_kb)

=======
@router.message(F.text.lower() == 'звязок з менеджером')
async def connect_to_manager(message: Message,state:FSMContext):
    await state.clear()
    logging.info("connect_to_manager")
    await message.answer('ТУТ БУДЕ ЗВЯЗОК З МЕНЕДЖЕРОМ', reply_markup=start_keyboard.back_bome_kb)
>>>>>>> 020e6800a06dcdf629c0d1766ce8ea8a5737d7cc
