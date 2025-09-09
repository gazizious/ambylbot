import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "ТВОЙ_ТОКЕН"
STICKER_ID = "CAACAgIAAxkBAAEBk3Jov_QeYTgHvRBgsjPw4AxyuHAi7AACjjkAAp9wGEltZKyNLQOPqDYE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start просто для проверки
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот запущен! Напиши 'да' и увидишь магию :)")

# реагируем на слово "да" (в любом регистре)
@dp.message()
async def react_to_da(message: Message):
    if "да" in message.text.lower():   # проверяем наличие слова
        await message.answer_sticker(STICKER_ID)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
