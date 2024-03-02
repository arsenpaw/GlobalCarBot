import logging
import asyncio



from config_reader import config
from aiogram import Bot, Dispatcher
from Handlers import  *
from Handlers import carfax_get_handlers
from Handlers import car_to_find_handlers
from admin import admin_methods,admin_in_group_handler
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
    bot.my_admins_list = []
    logging.info(f'Server is: {bot.session.api.base}')
    dp = Dispatcher(bot=bot)
    dp.include_routers(base_handlers.router, estimated_cost_handlers.router, cars_in_stock_handlers.router,callback_user_chose_car.router,
                       carfax_get_handlers.router, car_to_find_handlers.router,admin_in_group_handler.admin_group_router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())