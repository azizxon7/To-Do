import wikipedia as w
import logging
from aiogram import Bot, Dispatcher, executor, types

api = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'



# change code

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)
l={}
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name=message.from_user.first_name
    await message.reply(f"Assalomu alaykum {name}!\nMen 'EkoBot'man!\nAzizxon tomonidan yasalganman.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu bot sizga yozganingizni qaytaradi!")


@dp.message_handler()
async def echo(message: types.Message):
    msg=message.text
    id=message.from_user.id
    try:
        print(l[id])
    except:
        l[id]=[]
    l[id].append(msg)
    await message.answer(f'{l[id]}')
@dp.message_handler()
async def send_welcome(message: types.Message):
    
    await message.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    
# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺',
#                              reply_to_message_id=message.message_id)
