from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from parsing import get_updates
from datetime import datetime
import asyncio


bot = Bot(token='5804487703:AAExSwZGSWAQB2g1ty2ar03Qez1kdAMUSdk')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def send_updates(message: Message):
    while True:
        now = datetime.now()
        MSG = '\n\n'.join(f'{name} — {link}' for name, link in get_updates().items())
        await message.answer(text='Последние обновления:')
        await message.reply(text=MSG)

        sleeping_time = (3600 * (24 - (now.hour - 6))) if now.hour >= 6 else (3600 * (24 + (6 - now.hour)))
        await asyncio.sleep(delay=sleeping_time)

if __name__ == '__main__':
    executor.start_polling(dp)
