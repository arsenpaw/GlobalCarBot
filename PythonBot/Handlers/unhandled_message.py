from aiogram.types import *
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F, Router
import logging
from keyboards.start_keyboard import *
from Handlers.base_handlers import command_start_handler
from filters.admin_filters import *

all_router = Router()
all_router.message.filter(ChatTypeFilter(["private"]))


@all_router.message()
async def unhandeler_message(message: Message) -> None:
    logging.info("/command start all message")
    await command_start_handler(message)
