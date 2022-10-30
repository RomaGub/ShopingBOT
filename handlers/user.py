from aiogram import types, Dispatcher

from data_base.sqlite_db import sql_phone, sql_tablet, sql_laptop, sql_other
from keyboards.admin_kb import kb_ch_panel
from keyboards.user_kb import kb_user, kb_contacts, kb_categories
from main.create_bot import bot, dp, ADMIN_ID

#The initial function that executes after calling the "/start" command
async def command_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await bot.send_message(message.from_user.id,
f'''Вітаю <b>{message.from_user.first_name}</b>.
Оберіть варіант продовження''', reply_markup=kb_ch_panel)
        await message.delete()
    else:
        await bot.send_message(message.from_user.id,
'''Вітаємо вас у телеграм боті ShopBot!
За допомогою цього бота ви зможете переглянути цікаві товари,та підібрати щось для себе''', reply_markup=kb_user)
        await message.delete()

#A function that sends you to user mode if you are an administrator.
#An ordinary user enters this mode automatically after verification
async def user_panel_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer('<b>Панель користувача</b>', reply_markup=kb_user)
    await callback.answer()

#The function sends contact data to the chat
async def contacts_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer(f'''<b>ПІБ адміністратора боту:</b> Губійчук Р. О.\n
<b>☎ Контактна інформація для зв'язку:</b>
<i>Email:</i> roma2003gub@gmail.com
<i>Tel. number:</i> +380687514705
<i>Telegram:</i> @GUF1_R''', reply_markup=kb_contacts)
    await callback.answer()

#The function sends buttons to select product categories
async def products_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(callback.from_user.id, text='Оберіть категорію', reply_markup=kb_categories)
    await callback.answer()

#Functions send products from the selected category to the chat
async def phone_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await sql_phone(callback)
    await callback.answer()


async def tablet_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await sql_tablet(callback)
    await callback.answer()


async def laptop_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await sql_laptop(callback)
    await callback.answer()


async def other_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await sql_other(callback)
    await callback.answer()

#Functions takes the user back 1 step
async def back_call(callback: types.CallbackQuery):
    await products_call(callback)
    await callback.answer()

#Return to the main menu
async def menu_call(callback: types.CallbackQuery):
    try:
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    except:
        pass
    if callback.from_user.id == ADMIN_ID:
        await callback.message.answer('<b>Головне меню</b>', reply_markup=kb_ch_panel)
        await callback.answer()
    else:
        await callback.message.answer('<b>Головне меню</b>', reply_markup=kb_user)
        await callback.answer()

#A function for registering user handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(user_panel_call, text='user_panel')
    dp.register_callback_query_handler(contacts_call, text='contacts')
    dp.register_callback_query_handler(products_call, text='products')
    dp.register_callback_query_handler(phone_call, text='phone')
    dp.register_callback_query_handler(tablet_call,  text="tablet")
    dp.register_callback_query_handler(laptop_call,  text='laptop')
    dp.register_callback_query_handler(other_call,  text='other')
    dp.register_callback_query_handler(back_call,  text='back')
    dp.register_callback_query_handler(menu_call,  text='menu')