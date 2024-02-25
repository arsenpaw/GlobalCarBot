import logging
import asyncio
from config_reader import config
from aiogram import Bot, Dispatcher
from  Handlers import  base_handlers
from aiogram.client.session.aiohttp import AiohttpSession


async def main():
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
    logging.info('Program Started !!!')
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    logging.info(f'Server is: {bot.session.api.base}')
    dp = Dispatcher(bot=bot)
    dp.include_routers(base_handlers.router)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
