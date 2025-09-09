import asyncio
import re
import time
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "8409070749:AAGcTSutRzjq4RQ_QDN-zOa07YtR9339CDw"
STICKER_ID = "CAACAgIAAxkBAAEBk3Jov_QeYTgHvRBgsjPw4AxyuHAi7AACjjkAAp9wGEltZKyNLQOPqDYE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Глобальная переменная для хранения времени последнего ответа
last_reply_time = 0
cooldown = 30  # сек


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Бот запущен! Напиши 'да', 'ДА', 'дааа', 'da' в конце сообщения — и получишь стикер 😉"
    )


@dp.message()
async def react_to_da(message: Message):
    global last_reply_time
    text = message.text.strip()

    # Регулярка: да/da в конце (любой регистр, растянутые буквы, знаки препинания)
    pattern = r"(?:^|\s)(д+а+|da+)[.!?…]*$"

    if re.search(pattern, text, re.IGNORECASE):
        now = time.time()
        if now - last_reply_time >= cooldown:
            await message.answer_sticker(STICKER_ID)
            last_reply_time = now


async def main():
    print("✅ Бот запущен и ждёт сообщений...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
