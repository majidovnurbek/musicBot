import asyncio
import logging
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message,CallbackQuery
from aiogram.filters.command import Command
from config import Token
from button import *
from web import audio
from web2 import audio_turk
from web3 import audio_ru
from  web4 import audio_xorazm

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"hello{message.from_user.first_name} choose music type",reply_markup=catalog)

@dp.message(Command("poll"))
async def cmd_poll(message: Message):
    await message.bot.send_poll(chat_id=message.from_user.id,question="nima gaplar",options=["ha","yoq"],is_anonymous=False)

@dp.callback_query(F.data=="uzbek")
async def callback_query(call: CallbackQuery):
    for x in audio:
        await  call.message.answer_audio(audio=x)

@dp.callback_query(F.data=="turk")
async def callback_query(call: CallbackQuery):
    for x in audio_turk:
        await call.message.answer_audio(audio=x)


@dp.callback_query(F.data=="rus")
async def callback_query(call: CallbackQuery):
    for x in audio_ru:
        await call.message.answer_audio(audio=x)

@dp.callback_query(F.data=="xorazm")
async def callback_query(call: CallbackQuery):
    for x in audio_xorazm:
        await call.message.answer_audio(audio=x)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
