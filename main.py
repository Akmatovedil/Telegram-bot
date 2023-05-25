from aiogram.utils import executor
from config import dp
import logging
from handlers import client, extra, callback, admin, fsm_anketa, notifications, inline
from database import bot_db
import asyncio

async def on_startup(_):
    # asyncio.create_task(notifications.scheduler())
    bot_db.sql_create()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsmanketa(dp)
# notifications.register_handlers_notification(dp)
# inline.register_handlers_inline(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
