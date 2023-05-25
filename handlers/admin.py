from aiogram import types, Dispatcher
from config import bot, ADMIN
from database.bot_db import sql_command_all_id


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if not message.from_user.id in ADMIN:
            await message.reply('Ты не мой Босс!!!')
        elif message.reply_to_message:
            await message.reply('Команда должна быть ответом на сообщение')
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} братан'
                                 f'кикнул пользователя {message.reply_to_message.from_user.full_name}')
    else:
        await message.reply('Пиши в групе!!!')


async def distribution(message: types.Message):
    if not message.from_user.id in ADMIN:
        await message.reply('Ты не мой Босс!!!')
    else:
        result = await sql_command_all_id()
        for id in result:
            await bot.send_message(id[0], message.text[3:])

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(distribution, commands=['R'])
