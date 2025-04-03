from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Раздел помощь.')


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара',
                         reply_markup=kb.catalog)


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию.')
    await callback.message.answer('Вы выбрали категорию с футболками.')
