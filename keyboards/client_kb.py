from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("Share location", request_location=True)
info_button = KeyboardButton("share info", request_contact=True)


start_markup.add(start_button, quiz_button)
start_markup.row(location_button, info_button)

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

gender_g = KeyboardButton("Я девушка")
gender_b = KeyboardButton("Я парень")
gender_u = KeyboardButton("Я незнаю")
gender_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
gender_markup.row(gender_g, gender_b, gender_u)