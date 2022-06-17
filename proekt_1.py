from email import message
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import pyqrcode
# api = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name}!\nMen 'RasmBot'man!\nAzizxon tomonidan yasalganman.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Bu bot sizga yozganingizni qaytaradi!")

@dp.message_handler(commands=['dog'])
async def send_picture(message: types.Message):
    await message.answer_photo("https://yandex.ru/images/search?text=%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F%D1%8F%20%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0&img_url=https%3A%2F%2Fw-dog.ru%2Fwallpapers%2F6%2F6%2F550402226757356%2Fsobaka-vzglyad-drug-bigl.jpg&rpt=simage&source=qa&stype=image&lr=10335&parent-reqid=1654522944755694-10219262517637586794-vla1-4682-vla-l7-balancer-8080-BAL-295", "The domestic dog (Canis familiaris or Canis lupus familiaris) is a domesticated form of wolf.")

@dp.message_handler(commands=['cat'])
async def send_picture(message: types.Message):
    await message.answer_photo("https://yandex.ru/images/search?pos=7&from=tabbar&img_url=https%3A%2F%2Fpicfiles.alphacoders.com%2F296%2F296162.jpg&text=cat&rpt=simage", "Домашнее животное, одно из наиболее популярных «животных-компаньонов». С точки зрения научной систематики, домашняя кошка - млекопитающее семейства кошачьих отряда хищных.")

@dp.message_handler(commands=['subject'])
async def send_picture(message: types.Message):
    await message.answer_photo(photo=open('290px-Uzbekistan_location_map.svg.png', 'rb'))

# @dp.message_handler()
# async def send_picture(message: types.Message):
#     a=pyqrcode.create(f'https://google.com/search?q={message.text}')
#     a.png('codel.png', scale=10)
#     await message.answer_photo(photo=open("codel.png", 'rb'))
@dp.message_handler(commands=['menu'])
async def menu(message: types.message):
    btn1=KeyboardButton('Kartalarim')
    btn2=KeyboardButton('To\'lov')
    btn3=KeyboardButton('O\'tkazmalar')
    btn4=KeyboardButton('To\'lovlar tarixi')
    buttons=ReplyKeyboardMarkup(one_time_keyboard=True).add(btn1).add(btn2).add(btn3).add(btn4)
    await message.answer('Menudan istaganingnizni tanlang', reply_markup=buttons)
btns=['Kartalarim', 'To\'lov', 'O\'tkazmalar', 'To\'lovlar tarixi']
@dp.message_handler()
async def bolim(message: types.message):
    if message.text in btns:
        await message.reply(f"{message.text} bo'limiga xush kelibsiz")
    else:
        await message.answer(message.text)
# @dp.message_handler(commands=['start'])
# async def send_start(message: types.Message):
#     name=message.from_user.first_name
#     await message.reply(f"Assalomu alaykum {name}!\nMen 'BurgerBot'man!\nAzizxon tomonidan yasalganman.")
# @dp.message_handler(commands=['menu'])
# async def contact(message: types.message):
#      btn1=KeyboardButton('Kontaktimni ulash', request_contact=True)
#      buttons=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(btn1)
#      await message.answer('Kontakt ulashildi', reply_markup=buttons)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)