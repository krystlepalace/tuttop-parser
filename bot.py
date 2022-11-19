from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from parsing import get_updates
import asyncio
from datetime import datetime


bot = Bot(token='')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def send_updates(message: Message):
    while True:
        now = datetime.now()
        MSG = '\n'.join(f'{name} — {link}' for name, link in get_updates().items())
        await bot.send_message(chat_id=message.from_user.id, text=MSG)
        sleeping_time = (3600 * (24 - (now.hour - 6))) if now.hour >= 6 else (6 - now.hour)
        await asyncio.sleep(delay=sleeping_time)

if __name__ == '__main__':
    executor.start_polling(dp)
