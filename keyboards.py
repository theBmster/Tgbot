from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://thebmster.github.io/Tgbot/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='შეკვეთის განთავსება', web_app=web_app)]
    ],
    resize_keyboard=True
)
