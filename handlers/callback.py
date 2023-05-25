from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1' )
async def quiz_2(call: types.CallbackQuery):
    murkup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    murkup.add(button_call_2)
    question = 'By whom invented Python'
    answer = [
        'Harry Potter',
        'Putin?',
        'Guido Van Rossum',
        'Voldemort',
        'Griffin',
        'Linus Torvalds',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='it`s easy',
        open_period=10,
        reply_markup=murkup
    )


# @dp.callback_query_handler(lambda call: call.data == 'button_call_2' )
async def quiz_3(call: types.CallbackQuery):
    question = 'SOLVE:'
    answer = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]
    photo = open('media/photo1.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='it`s easy',
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == 'button_call_2')
