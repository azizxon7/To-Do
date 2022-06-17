import logging
from pyexpat.errors import messages
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, BotCommand, BotCommandScopeDefault


api='5592113515:AAHqFURsrAPp-hlfljxkfxxgXrrHMnj291w'
logging.basicConfig(level=logging.INFO)
l={}
bot = Bot(token=api)
dp = Dispatcher(bot)
b1=KeyboardButton("📞 Kontaktimni yubor ", request_contact=True)
buttons=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(b1)
b2=KeyboardButton("🌏 Lokatsiyamni yubor ", request_location=True)
buttons2=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(b2)
btn1=KeyboardButton("📝 Kategoriya ")
btn2=KeyboardButton("💲 Keshbek ")
btn3=KeyboardButton("🗂️ Buyurtmalar tarixi ")
btns2=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1).add(btn2).add(btn3)
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.answer(f"Assalomu alaykum {name} 👋👋👋!\nMen 🦾'BOMBA BURGER_bot'🦾man!\n👨Azizxon👨 tomonidan yasalganman. \nIltimos bizga 📞 kontaktingizni yuboring!", reply_markup=buttons)
@dp.message_handler(content_types=[ContentType.CONTACT])
async def init_contact(msg: types.Contact):
    print(msg.values['contact'].phone_number)
    await msg.reply('📌 Lokatsiyangizni  yuboring \n(ammo avval telefoningizda \'Location\' (📍) funksiyasi yoniq ekanligiga ishonch hosil qiling)', reply_markup=buttons2)
@dp.message_handler(content_types=[ContentType.LOCATION])
async def init_location(msg: types.Location):
    print(msg.values['location'].latitude, msg.values['location'].longitude)
    await msg.answer('Bomba Burgerga xush kelibsiz', reply_markup=btns2)
foods=['🍜 Ko\'cha', '🥘 Tovuq sho\'rva', '🍲 Oddiy sho\'rva', '🍛 Mastava', '🍚 Osh', '🥣 Bosma', '🍱 Bishteks', 
'🍔 Bomba Burger', '🌭 Hot-Dog', '🌯 Lavash',  '🌮 Shaurma', '🥪 Chizburger']
l={}
@dp.message_handler()
async def b(message: types.message):
    if message.text=='📝 Kategoriya':
        btn1='🍜 Suyuq ovqatlar'
        btn2='🍝 Qo\'yiq ovqatlar'
        btn3='🍔 Fast-Food'
        btn6='🔚 Asosiy bo\'lim'
        btns3=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1, btn2).add(btn3).add(btn6)
        await message.answer(message.text, reply_markup=btns3)
    if message.text=='🍜 Suyuq ovqatlar':       
        butn1='🍜 Ko\'cha'
        butn2='🥘 Tovuq sho\'rva'
        butn3='🍲 Oddiy sho\'rva'
        butn4='🍛 Mastava'
        btn5='📝 Kategoriyaga qaytish'
        btn6='🔚 Asosiy bo\'lim'
        btns4=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(butn1,butn2,butn3,butn4).add(btn5, btn6)
        await message.answer(message.text, reply_markup=btns4)   
    if message.text=='🍝 Qo\'yiq ovqatlar':       
        butn1='🍚 Osh'
        butn2='🥣 Bosma'
        butn3='🍱 Bishteks'
        btn5='📝 Kategoriyaga qaytish'
        btn6='🔚 Asosiy bo\'lim'
        btns5=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(butn1,butn2,butn3).add(btn5, btn6)
        await message.answer(message.text, reply_markup=btns5)   
    if message.text=='🍔 Fast-Food':       
        butn1='🍔 Bomba Burger'
        butn2='🌭 Hot-Dog'
        butn3='🌯 Lavash'
        butn4='🌮 Shaurma'
        butn5='🥪 Chizburger'
        btn5='📝 Kategoriyaga qaytish'
        btn6='🔚 Asosiy bo\'lim'
        btns5=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(butn1,butn2,butn3,butn4,butn5).add(btn5, btn6)
        await message.answer(message.text, reply_markup=btns5)   
    if message.text=='📝 Kategoriyaga qaytish':       
        btn1='🍜 Suyuq ovqatlar'
        btn2='🍝 Qo\'yiq ovqatlar'
        btn3='🍔 Fast-Food'
        btn6='🔚 Asosiy bo\'lim'
        btns3=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1,btn2).add(btn3).add(btn6)
        await message.answer(message.text, reply_markup=btns3)  
    if message.text=='🔚 Asosiy bo\'lim':
        btn1=KeyboardButton("📝 Kategoriya ")
        btn2=KeyboardButton("💲 Keshbek ")
        btn3=KeyboardButton("🗂️ Buyurtmalar tarixi ")
        btns2=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1).add(btn2).add(btn3)
        await message.answer(message.text, reply_markup=btns2)  
    if message.text in foods:
        msg=message.text
        id=message.from_user.id
        try:
            print(l[id])
        except:
            l[id]=[]
        l[id].append(msg)
        await message.reply('Buyurtma \'Buyurtmalar tarixi\' bo\'limiga qo\'shildi')
    if message.text=="🗂️ Buyurtmalar tarixi ":
        await message.answer(f'Buyurtmalaringiz - {l[id]}')   
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    