import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from tokens import TBOTTOKEN

bot = Bot(token=TBOTTOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')
