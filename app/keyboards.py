from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True, one_time_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...'
                           )


async def contacts():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Страница владельца в "VK"',
                                      url='https://vk.com/creator_my_life'))
    keyboard.add(InlineKeyboardButton(text='Контакт владельца в "Telegram"',
                                      url='https://t.me/Hug0StiglitZ'))
    return keyboard.adjust(1).as_markup()


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,
                                          callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную',
                                      callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name,
                                          callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную',
                                      callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
