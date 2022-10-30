import sqlite3 as sq

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.user_kb import kb_prod
from main.create_bot import bot

#Database connection
def sql_start():
    global base, cur
    base = sq.connect('bot_products.db')
    cur = base.cursor()
    if base:
        print('Базу даних підключено')
    base.execute("CREATE TABLE IF NOT EXISTS products(img TEXT, category TEXT, name TEXT PRIMARY KEY, description TEXT, rating TEXT, price TEXT, link TEXT)")
    base.commit()

#The function of recording data about the product in the database
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

#A function for reading all data in the database
async def sql_read2():
    return cur.execute('SELECT * FROM products').fetchall()

#The function of deleting data from the database
async def sql_del(data):
    cur.execute('DELETE FROM products WHERE name == ?', (data,))
    base.commit()

#Product search function from the category "phones"
async def sql_phone(callback):
    data = 'phone'
    await bot.send_message(callback.from_user.id, '<b>📱 Смартфони</b>')
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    for ret in cur.execute('SELECT * FROM products WHERE category == ?', (data,)).fetchall():
        await bot.send_photo(callback.from_user.id, ret[0], f'<b>{ret[2]}</b>\n<b><i>Опис:</i></b> {ret[3]}\n<b><i>Рейтинг:</i></b> {ret[4]}\n<b><i>Ціна:</i></b> {ret[5]}',
                             reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Перейти до товару', url=f'{ret[6]}')))
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    await bot.send_message(callback.from_user.id, text='<b>Оберіть опцію для продовження</b>', reply_markup=kb_prod)

#Product search function from the category "tablets"
async def sql_tablet(callback):
    data = 'tablet'
    await bot.send_message(callback.from_user.id, '<b>Планшети</b>')
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    for ret in cur.execute('SELECT * FROM products WHERE category == ?', (data,)).fetchall():
        await bot.send_photo(callback.from_user.id, ret[0], f'<b>{ret[2]}</b>\n<b><i>Опис:</i></b> {ret[3]}\n<b><i>Рейтинг:</i></b> {ret[4]}\n<b><i>Ціна:</i></b> {ret[5]}',
                             reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Перейти до товару', url=f'{ret[6]}')))
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    await bot.send_message(callback.from_user.id, text='<b>Оберіть опцію для продовження</b>', reply_markup=kb_prod)

#Product search function from the category "laptops"
async def sql_laptop(callback):
    data = 'laptop'
    await bot.send_message(callback.from_user.id, '<b>💻 Ноутбуки</b>')
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    for ret in cur.execute('SELECT * FROM products WHERE category == ?', (data,)).fetchall():
        await bot.send_photo(callback.from_user.id, ret[0], f'<b>{ret[2]}</b>\n<b><i>Опис:</i></b> {ret[3]}\n<b><i>Рейтинг:</i></b> {ret[4]}\n<b><i>Ціна:</i></b> {ret[5]}',
                             reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Перейти до товару', url=f'{ret[6]}')))
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    await bot.send_message(callback.from_user.id, text='<b>Оберіть опцію для продовження</b>', reply_markup=kb_prod)

#Product search function from the category "other"
async def sql_other(callback):
    data = 'other'
    await bot.send_message(callback.from_user.id, '<b>Інші товари</b>')
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    for ret in cur.execute('SELECT * FROM products WHERE category == ?', (data,)).fetchall():
        await bot.send_photo(callback.from_user.id, ret[0], f'<b>{ret[2]}</b>\n<b><i>Опис:</i></b> {ret[3]}\n<b><i>Рейтинг:</i></b> {ret[4]}\n<b><i>Ціна:</i></b> {ret[5]}',
                             reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Перейти до товару', url=f'{ret[6]}')))
    await bot.send_message(callback.from_user.id, '◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤')
    await bot.send_message(callback.from_user.id, text='<b>Оберіть опцію для продовження</b>', reply_markup=kb_prod)