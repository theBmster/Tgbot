from main import bot, dp
from keyboards import keyboard
from aiogram import types
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'შეკვეთის განთავსება!',
                           reply_markup=keyboard)

PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=5000)],
    '2': [types.LabeledPrice(label='Item2', amount=10000)],
    '3': [types.LabeledPrice(label='Item3', amount=15000)],
    '4': [types.LabeledPrice(label='Item4', amount=20000)],
    '5': [types.LabeledPrice(label='Item5', amount=30000)],
    '6': [types.LabeledPrice(label='Item6', amount=40000)],
}

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='გადახდა',
                           description='აღწერა',
                           provider_token='410694247:TEST:08ca9563-c1a9-4dd1-a06b-29bb84c432b8',
                           currency='GEL',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'გადახდა წარმატებით შესრულდა!')
