# import asyncio
# import aioschedule
# from aiogram import types, Dispatcher
# from config import bot
#
#
# async def get_chat_id(message: types.Message):
#     global chat_id
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id=chat_id, text="ok!")
#
#
# async def go_to_sleep():
#     await bot.send_message(chat_id=chat_id, text="Пошел ты спать!")
#
#
# async def wake_up():
#     video = open("media/video.mp4", "rb")
#     await bot.send_video(chat_id=chat_id, video=video, caption="Вставай")
#
#
# async def scheduler():
#     aioschedule.every().day.at("17:58").do(go_to_sleep)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(2)
#
#
# def register_handlers_notification(dp: Dispatcher):
#     dp.register_message_handler(get_chat_id,
#                                 lambda word: 'напомни' in word.text)
