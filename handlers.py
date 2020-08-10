from app import bot, dp

from aiogram.types import Message
from botconfig import admin

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin, text='Бот запущен')

@dp.message_handler()
async def echo(message: Message):
    text = message.text
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await message.answer(text=text)