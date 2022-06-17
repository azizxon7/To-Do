import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
api = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name} 👋👋👋!\nMen 🦾'Bot'🦾man!\n👨Azizxon👨 tomonidan yasalganman.")
@dp.message_handler(commands=['number'])
async def send_start(message: types.Message):
    btn1=InlineKeyboardButton('5️⃣', callback_data='five')
    btn2=InlineKeyboardButton('1️⃣0️⃣', callback_data='ten')
    btn3=InlineKeyboardButton('5️⃣0️⃣', callback_data='fifty')
    btn4=InlineKeyboardButton('1️⃣0️⃣0️⃣', callback_data='hund')
    buttons=InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3).add(btn4)
    await message.reply('Sonlardan istaganingizni tanlang', reply_markup=buttons)
@dp.callback_query_handler(text=['five', 'ten', 'fifty', 'hund' ])
async def a(call: types.CallbackQuery):
    if call.data=='five':
        await call.message.answer(random.randint(0, 5))
    if call.data=='ten':
        await call.message.answer(random.randint(5, 10))
    if call.data=='fifty':
        await call.message.answer(random.randint(10, 50))            
    if call.data=='hund':
        await call.message.answer(random.randint(50, 100))
@dp.message_handler(commands=['menu'])
async def menu(message: types.message):
    btn1=KeyboardButton('🔢Raqamlarni tanlang🔢')
    btn2=KeyboardButton('🔣Kontakni ulash🔣', request_contact=True)
    btn3=KeyboardButton('🆎Ismingizni bilish🆎')
    btn4=KeyboardButton("🆔'ID'ni aniqlash🆔")
    btn5=KeyboardButton("🆔Geolokatsiyani ulash🆔", request_location=True)
    buttons=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1).add(btn2).add(btn3).add(btn4).add(btn5)
    await message.answer('Menudan istaganingnizni tanlang', reply_markup=buttons)
@dp.message_handler()
async def b(message: types.message):
    if message.text=='🔢Raqamlarni tanlang🔢':
        await message.answer(a)
#     if message.text=='🔣Son topish o\'yini🔣':
#         r=random.randint(5, 10)
#         await message.reply('Men 5 dan 10 gacha bo\'lgan sonlar orasidan birini o\'ylayman, siz esa topishga harakat qilasiz')
#         async def c(message: types.message):
#             if message.text==r:
#                 await message.reply('🥳Barakalla, topdingiz🥳')
#             else:
#                 await message.reply('☹️Afsus, topa olmadingiz, qaytatdan urunib ko\'ring☹️')
    if message.text=='🆎Ismingizni bilish🆎':
        name=message.from_user.first_name
        usr=message.from_user.username
        await message.reply(name)
        await message.answer(usr)
    if message.text=="🆔'ID'ni aniqlash🆔":
        id=message.from_user.id
        await message.reply(id)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)