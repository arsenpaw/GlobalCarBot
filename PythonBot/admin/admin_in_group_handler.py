from aiogram import Router

from filters import IsAdmin

admin_router = Router()
admin_router.message.filter(IsAdmin())