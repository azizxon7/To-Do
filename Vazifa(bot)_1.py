import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import pyqrcode
api = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)

pictures=['rasm_0.jpg', 'rasm_1.jpg', 'rasm_2.jpg', 'rasm_3.jpg', 'rasm_4.jpg', 'rasm_5.jpg',
          'rasm_6.jpg', 'rasm_7.jpg', 'rasm_8.jpg', 'rasm_9.jpg']                            
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name}!\nMen 'EkoBot'man!\nAzizxon tomonidan yasalganman.")
@dp.message_handler(commands=['picture'])
async def send_picture(message: types.Message):
    for i in pictures:
        await message.answer_photo(photo=open(i, 'rb'))
@dp.message_handler(commands=['menu'])
async def menu(message: types.message):
    btn1=KeyboardButton('Taomlar')
    btn2=KeyboardButton('To\'lov turi')
    btn3=KeyboardButton('Goelokatsiyani ulashish')
    btn4=KeyboardButton('Kontakni ulashish')
    btn5=KeyboardButton('To\'lovlar tarixi')
    buttons=ReplyKeyboardMarkup(one_time_keyboard=True).add(btn1).add(btn2).add(btn3).add(btn4).add(btn5)
    await message.answer('Menudan istaganingnizni tanlang', reply_markup=buttons)
bttns=['Kontakni ulashish', 'To\'lovlar tarixi', 'Goelokatsiyani ulashish', 'Kontakni ulashish', 'To\'lovlar tarixi']
foods=['BURGER', 'HOT-DOG', 'LAVASH', 'SHAURMA', 'NON KABOB', 'SHASHLIK']
@dp.message_handler()
async def bolim(message: types.message):
    if message.text in bttns:
        await message.reply(f"{message.text} bo'limiga xush kelibsiz")
    if message.text=='Taomlar':
        btn1=KeyboardButton('BURGER')
        btn2=KeyboardButton('HOT-DOG')
        btn3=KeyboardButton('LAVASH')
        btn4=KeyboardButton('SHAURMA')
        btn5=KeyboardButton('NON KABOB')
        btn6=KeyboardButton('SHASHLIK')
        buttons=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1).add(btn2).add(btn3).add(btn4).add(btn5).add(btn6)
        await message.reply("Taomlar bo'limiga xush kelibsiz")
        await message.answer('Taomlardan istaganingnizni tanlang', reply_markup=buttons)
    elif message.text=='To\'lov turi':
        await message.reply(f"{message.text} bo'limiga xush kelibsiz")
        btn1=KeyboardButton('NAQD')
        btn2=KeyboardButton('PLASTIK KARTOCHKA')
        buttons=ReplyKeyboardMarkup(one_time_keyboard=True).add(btn1).add(btn2)
        await message.answer(reply_markup=buttons)
    elif message.text=='Goelokatsiyani ulashish':
        await message.reply("Farg'ona vil. Farg'ona shah. ZED IT Academy binosi")
        await message.answer('Geolekatsiya uzatildi')
    if message.text in foods:
        await message.reply("Buyurtmangiz qabul qilindi, Tez orada yetkazib beriladi.")
    else:
        a=pyqrcode.create(f'https://www.youtube.com/results?search_query={message.text}')
        a.png('codel.png', scale=10)
        await message.answer_photo(photo=open("codel.png", 'rb'))
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)