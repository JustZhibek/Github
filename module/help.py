from aiogram import types
from module.constans import HELP_TEXT

async def help_command(cb: types.CallbackQuery):
    """
    посмотреть доступные команды
    """
    await cb.bot.send_message(chat_id=cb.from_user.id,text=HELP_TEXT)