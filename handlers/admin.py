from aiogram.dispatcher.filters import Text

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.admin_kb import kb_admin, kb_del
from main.create_bot import dp, bot

from data_base.sqlite_db import sql_add_command, sql_read2, sql_del

#Creating a state machine for adding products
class FSM_admin(StatesGroup):
    photo = State()
    category = State()
    name = State()
    description = State()
    rating = State()
    price = State()
    link = State()

#Start function in administrator mode
async def admin_start(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Ви увійшли у режим адміністратора.\n Оберіть потрібну функцію', reply_markup=kb_admin)
    await callback.answer()

#Function to start the state machine to add the product
async def add_prod_call(callback: types.CallbackQuery):
    await FSM_admin.photo.set()
    await bot.send_message(callback.from_user.id, 'Завантаж фото продукту\n⬇️⬇️⬇️')
    await callback.answer()

#Adding a photo of the product
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_admin.next()
    await message.reply('Вкажи категорію продукту\n⬇️⬇️⬇️')

#Specifying the product category
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await FSM_admin.next()
    await message.reply('Тепер вкажи назву продукту\n⬇️⬇️⬇️')

#Setting the name of the product
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_admin.next()
    await message.reply('Тепер напиши короткий опис продукту\n⬇️⬇️⬇️')

#Adding a description of the product
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_admin.next()
    await message.reply('Вкажи рейтинг продукту\n⬇️⬇️⬇️')

#Setting a product rating
async def load_rating(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rating'] = message.text
    await FSM_admin.next()
    await message.reply('Задай ціну для продукта\n⬇️⬇️⬇️')

#Adding a price of the product
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSM_admin.next()
    await message.reply('Вкажи посилання на продукт\n⬇️⬇️⬇️')

#Setting a link to a product.
#Stopping the state machine and writing data to the database
async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
    await sql_add_command(state)
    await bot.send_message(message.from_user.id, text='Продукт додано', reply_markup=kb_admin)
    await state.finish()

#Function for exiting the state machine at any stage
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Операцію відмінено. Оберіть варіант продовження:', reply_markup=kb_admin)

#Removing the product from the database
async def del_callback_run(callback: types.CallbackQuery):
    await sql_del(callback.data.replace('del ', ''))
    await callback.message.answer(text=f"{callback.data.replace('del ', '')} видалено.", reply_markup=kb_admin)
    await callback.answer()

#Menu of products that can be removed
async def del_prod_call(callback: types.CallbackQuery):
    read = await sql_read2()
    for ret in read:
        await bot.send_photo(callback.from_user.id, ret[0], f'{ret[2]}\nОпис: {ret[3]}\nРейтинг: {ret[4]}\nЦіна: {ret[5]}')
        await bot.send_message(callback.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().
                               add(InlineKeyboardButton(f'Видалити {ret[2]}', callback_data=f'del {ret[2]}')))
    await bot.send_message(callback.from_user.id, text='Оберіть варіант для продовження:', reply_markup=kb_del)

#Go back 1 step in admin mode
async def back_call(callback: types.CallbackQuery):
    await admin_start(callback)
    await callback.answer()

#A function for registering admin handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, Text(equals = 'відміна', ignore_case = True), state = '*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM_admin.photo)
    dp.register_message_handler(load_category, state=FSM_admin.category)
    dp.register_message_handler(load_name, state=FSM_admin.name)
    dp.register_message_handler(load_description, state=FSM_admin.description)
    dp.register_message_handler(load_rating, state=FSM_admin.rating)
    dp.register_message_handler(load_price, state=FSM_admin.price)
    dp.register_message_handler(load_link, state=FSM_admin.link)
    dp.register_callback_query_handler(admin_start, state=None, text='admin_panel')
    dp.register_callback_query_handler(add_prod_call, text='add_prod')
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_callback_query_handler(del_prod_call, text = 'del_prod')
    dp.register_callback_query_handler(back_call, text = 'back_adm')