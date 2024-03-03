import logging
import asyncio

from admin.admin_methods import *
from config_reader import config
from aiogram import Bot, Dispatcher
from Handlers import  *
from Handlers import carfax_get_handlers, unhandled_message
from Handlers import car_to_find_handlers
from admin.admin_in_group_handler import *
async def run_function_every_two_minutes(bot:Bot):
    while True:
        logging.info('AUTOREQUEST')
        await auto_request_to_db(bot=bot)
        await asyncio.sleep(60)

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
    bot.chat_to_send = int()
    logging.info(f'Server is: {bot.session.api.base}')
    dp = Dispatcher(bot=bot)
    dp.include_routers(base_handlers.router, estimated_cost_handlers.router, cars_in_stock_handlers.router, callback_user_chose_car.router,
                       carfax_get_handlers.router, car_to_find_handlers.router, admin_group_router,
                       unhandled_message.all_router)
    #unhandled_message.all_router is alwaise last !!!!
    #await asyncio.create_task(run_function_every_two_minutes(bot))
   # await dp.start_polling(bot, skip_updates=True)
    task1 = asyncio.create_task(run_function_every_two_minutes(bot))
    task2 = asyncio.create_task(dp.start_polling(bot, skip_updates=True))
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())