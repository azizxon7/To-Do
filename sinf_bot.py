import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
api='5454640638:AAGlBvW4CVVd-HUVmcFC5z5z1uerA_A97is'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name} 👋👋👋!\nMen 🦾'Bot'🦾man!\n👨Azizxon👨 tomonidan yasalganman.")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 

