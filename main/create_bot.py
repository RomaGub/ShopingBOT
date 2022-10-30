from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#Administrator ID registration
ADMIN_ID = 738728494

#Creation of temporary memory to save data about the added product
storage = MemoryStorage()

#Inicialisation BOT and DISPATCHER
bot = Bot(token='5334880821:AAE7eXBx-JNJA8kCZph0Gb9DcEFcA_10RE4', parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)