from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Раздел помощь.')


@router.message(F.text == 'У меня все хорошо.')
async def nice(message: Message):
    await message.answer('Я очень рад.')
