from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок!',
                         reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара',
                         reply_markup=await kb.categories())


@router.message(F.text == 'Контакты')
async def catalog(message: Message):
    await message.answer('Контактная информация магазина.',
                                  reply_markup=await kb.contacts())


@router.message(F.text == 'О нас')
async def catalog(message: Message):
    await message.answer('Реквизиты магазина.')


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар из категории',
                                  reply_markup=await
                                  kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\n'
                                  f'Описание: {item_data.description}\n'
                                  f'Цена: {item_data.price}$',
                                  reply_markup=await
                                  kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('to_main'))
async def to_main(callback: CallbackQuery):
    await callback.answer('Вы вернулись в меню')
    await callback.message.answer('Добро пожаловать в магазин кроссовок!',
                                  reply_markup=kb.main)
