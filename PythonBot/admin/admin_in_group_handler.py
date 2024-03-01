

from aiogram import F, Bot, types, Router
from aiogram.filters import Command


from filters.admin_filters import *
admin_group_router = Router()
admin_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
admin_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))


@admin_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    print(admins_list)



