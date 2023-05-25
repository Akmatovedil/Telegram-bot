from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards import client_kb
from database.bot_db import sql_command_random
from parser.cartoon import parser

# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Салам Алейкум {message.from_user.full_name}',
                           reply_markup=client_kb.start_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    murkup.add(button_call_1)
    question = 'Why are you gay'
    answer = [
        'Because',
        'Who say`s i`m gay ?',
        'I`m not gay',
        'I`m gay'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='this is meme',
        open_period=10,
        reply_markup=murkup
    )


# @dp.message_handler(commands=['mem'])
async def quiz_4(message: types.Message):
    photo = open('media/photo1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def cartoon_parser(message: types.Message):
    cartoons = parser()
    for cartoon in cartoons:
        await bot.send_message(
            message.from_user.id,
            f"{cartoon['link']}\n\n"
            f"{cartoon['title']}\n"
            f"{cartoon['info']}\n\n"
            f"#{cartoon['date']}\n"
            f"#{cartoon['country']}\n"
            f"#{cartoon['genre']}\n"
        )



async def show_random_user(message: types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(quiz_4, commands=['mem'])
    dp.register_message_handler(show_random_user, commands=['get'])
    dp.register_message_handler(cartoon_parser, commands=['cartoon'])