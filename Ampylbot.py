import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Text

TOKEN = "8409070749:AAGcTSutRzjq4RQ_QDN-zOa07YtR9339CDw"
STICKER_ID = "CAACAgIAAxkBAAEBk3Jov_QeYTgHvRBgsjPw4AxyuHAi7AACjjkAAp9wGEltZKyNLQOPqDYE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Логируем всё, что бот видит
@dp.message()
async def log_message(message: types.Message):
    print(f"📩 Получено сообщение: {message.text}")

# Реакция на "да"
@dp.message(Text(contains="да", ignore_case=True))
async def send_sticker(message: types.Message):
    await message.reply_sticker(STICKER_ID)

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
