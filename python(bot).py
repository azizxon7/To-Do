import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
api = '5472267427:AAF9Zrz5gV_gw2eDJzQHTBTTDckpu2-BvhA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name}!\nMen 'BurgerBot'man!\nAzizxon tomonidan yasalganman.")

@dp.message_handler(commands=['python'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Shartlar hozir siz 'BOSHLADIM' deb yozishingiz, kod yozishingiz tugaganda esa 'TUGADI' deb yozasiz.")
    if message.text=='BOSHLADIM':
        filename='add_python(bot).py'
        # with open(filename, 'a' ):
            