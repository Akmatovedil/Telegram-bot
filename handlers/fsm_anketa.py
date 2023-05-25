from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import cancel_markup, gender_markup
from database import bot_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    gender = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f'Салам {message.from_user.full_name}'
                             f'скинь фотку...',
                             reply_markup=cancel_markup)

    else:
        await message.reply('Пиши в личку!')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Как звать ?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Какого года ?')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 1950 or int(message.text) > 2015:
            await message.answer('Доступ воспрещен!')
        else:
            async with state.proxy() as data:
                data['age'] = 2023 - int(message.text)
            await FSMAdmin.next()
            await message.answer('Какой пол ?', reply_markup=gender_markup)
    except:
        await message.answer('Пиши числа!')


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer('Откуда будешь ?')


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Name: {data['name']}\n"
                                     f"Age: {data['age']}\n"
                                     f"Gender: {data['gender']}\n"
                                     f"Region: {data['region']}\n"
                                     f"{data['username']}")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer('Все свободен')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Ну и пошел ты!')


async def delete_data(message: types.Message):
    users = await bot_db.sql_command_all()
    for user in users:
        await bot.send_photo(message.from_user.id, user[2],
                             caption=f"Name: {user[3]}\n"
                                     f"Age: {user[4]}\n"
                                     f"Gender: {user[5]}\n"
                                     f"Region: {user[6]}\n"
                                     f"{user[1]}",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f"delete {user[3]}",
                                     callback_data=f"delete {user[0]}"
                                 )
                             ))


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Стерт из БД", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands="cancel")
    dp.register_message_handler(fsm_start, commands=["reg"])
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender
                                , state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )
