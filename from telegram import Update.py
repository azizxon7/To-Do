# from telegram import Update
# # from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()

# import requests as r
# api="https://api.telegram.org/bot5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0"
# up=r.get(api+'/getUpdates').json()
# id=up['result'][0]['message']['from']['id']
# text='Assalomu alaykum'
# for i in range(20):
#     print(r.get(api+f'/sendMessage?chat_id={id}&text={text}').json)

# import logging
# import wikipedia as w
# from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = '5512523054:AAH6zBPIZyciqDxheJp0PcYDGR2bssWtlh0'
# w.set_lang('uz')
# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺 😀  ',
#                              reply_to_message_id=message.message_id)


# @dp.message_handler()
# async def wiki(message: types.Message):
#     try:
#         respond=w.summary(message.text)
#         await bot.send_message(message.chat.id, respond)
#     except:
#         await bot.send_message(message.chat.id, 'Bu maqola topilmadi')

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)