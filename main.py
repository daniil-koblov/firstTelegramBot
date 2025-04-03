import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from tokens import TBOTTOKEN


async def main():
    bot = Bot(token=TBOTTOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')
