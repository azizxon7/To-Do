import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand, BotCommandScopeDefault, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import wikipedia as w
API_TOKEN = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    btn1=InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='uz')
    btn2=InlineKeyboardButton('🇷🇺 Русский язык', callback_data='ru')
    btn3 = InlineKeyboardButton('🇺🇸 English language', callback_data='us')
    buttons = InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3)
    name=message.from_user.first_name
    await message.reply(f"Assalomu-alaykum {name}\nSalom. Men sizga 'wikipedia'dagi ma'lumotlarni ko'rsatib beraman. \nBuning uchun ushbu tillardan birini tanlang\n\nПривет. Я покажу вам информацию в 'Википедии'.\n Для этого выберите один из этих языков\n\nHello there. I'll show you the information in wikipedia. \nTo do this, choose one of these languages", reply_markup=buttons)
    await bot.set_my_commands(
        commands=[
            BotCommand("start", 'Botni qayta ishga tushuring'),
            BotCommand("set_language", 'Tilni o\'zgartirish')
    ], scope=BotCommandScopeDefault)
@dp.message_handler(commands=['set_language'])
async def send_start(message: types.Message):
    btn1=InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='uz')
    btn2=InlineKeyboardButton('🇷🇺 Русский язык', callback_data='ru')
    btn3 = InlineKeyboardButton('🇺🇸 English language', callback_data='us')
    buttons = InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3)
    await message.reply(f"Iltimos, ushbu tillardan birini tanlang\n\nПривет. Я покажу вам информацию в 'Википедии'.\n Для этого выберите один из этих языков\n\nHello there. I'll show you the information in wikipedia. \nTo do this, choose one of these languages", reply_markup=buttons)
@dp.callback_query_handler(text=['uz', 'ru', 'us'])
async def a(call: types.CallbackQuery):
    if call.data=='uz':
        await call.message.answer('🇺🇿 O\'zbek tili\nYaxshi, endi menga istalgan so\'rovingizni yuboring')
        w.set_lang('uz')
    if call.data=='ru':
        await call.message.answer('🇷🇺 Русский язык\nХорошо, пришлите мне любой запрос сейчас')
        w.set_lang('ru')
    if call.data=='us':
        await call.message.answer('🇺🇸 English language\n Well, now send me your desired request')
        w.set_lang('en')
@dp.message_handler()
async def wiki(message: types.Message):
    try:
        respond=w.summary(message.text)
        await bot.send_message(message.chat.id, respond)
        res=w.search(message.text)
        await bot.send_message(message.chat.id, f"Ehtimol, siz bulardan birini qidirgandirsiz:\nВы, вероятно, искали один из них:\nMaybe you were looking for one of these:\n\n{res}")
    except:
        res=w.search(message.text)
        await bot.send_message(message.chat.id, f"Ehtimol, siz bulardan birini qidirgandirsiz:\nВы, вероятно, искали один из них:\nMaybe you were looking for one of these\n\n{res}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 