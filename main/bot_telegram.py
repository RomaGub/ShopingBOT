from aiogram.utils import executor

from data_base.sqlite_db import sql_start
from handlers import user, admin
from main.create_bot import dp

#If the bot started without errors, a launch message is sent to the console
async def on_startup(_):
    print('Бот працює')
    sql_start()

#Registration of administrator and user handlers
user.register_handlers(dp)
admin.register_handlers(dp)

#Launching a bot
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)