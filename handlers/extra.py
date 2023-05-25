from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler()
async def echo(message: types.Message):
    bad_words = ['бля', 'сука', 'пидор', 'гондон', 'сучка', 'лох', 'уебок']
    username = f"@{message.from_user.username}" if message.from_user.username is not None else ""
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(message.chat.id,
                                   f'Не матерись {message.from_user.full_name}, '
                                   f'Сам ты {word} {username}')
            await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith("."):
        await bot.pin_chat_message(message.chat.id, message.message_id)


    if message.text == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
