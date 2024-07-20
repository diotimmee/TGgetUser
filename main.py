import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.filters.command import CommandStart
from db import Database

load_dotenv()

db = Database(os.getenv("DB_URL"))

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f"Xush Kelibsiz ! {msg.from_user.full_name}")
    db.add(msg.from_user.id, msg.from_user.full_name)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
