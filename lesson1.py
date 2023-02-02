from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
     await message.answer(f"Привет, {message.from_user.first_name}, я простой бот")

#@dp.message_handler()
#async def echo(message: types.Message):
    #await message.reply(message.text.upper())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)