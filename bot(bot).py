import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,  BotCommand, BotCommandScopeDefault
from aiohttp import ContentTypeError
from telegram import Location
api = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.answer(f"Assalomu alaykum {name} ◻️◻️◻️!\nMen 🦾'Bot'🦾man!\n👨Azizxon👨 tomonidan yasalganman.")
@dp.message_handler(commands=['game'])
async def send_start(message: types.Message):
    btn1=InlineKeyboardButton('◻️', callback_data='1')
    btn2=InlineKeyboardButton('◻️', callback_data='2')
    btn3=InlineKeyboardButton('◻️', callback_data='3')
    btn4=InlineKeyboardButton('◻️', callback_data='4')
    btn5=InlineKeyboardButton('◻️', callback_data='5')
    btn6=InlineKeyboardButton('◻️', callback_data='6')
    btn7=InlineKeyboardButton('◻️', callback_data='7')
    btn8=InlineKeyboardButton('◻️', callback_data='8')
    btn9=InlineKeyboardButton('◻️', callback_data='9')
    buttons=InlineKeyboardMarkup().add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    await message.reply('X and O', reply_markup=buttons)
@dp.callback_query_handler(text=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
async def a(call: types.CallbackQuery):
    if call.data=='five':
        await call.message.answer(random.randint(0, 5))
    if call.data=='ten':
        await call.message.answer(random.randint(5, 10))
    if call.data=='fifty':
        await call.message.answer(random.randint(10, 50))            
    if call.data=='hund':
        await call.message.answer(random.randint(50, 100))
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    