from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Create Inline Buttons for main menu
products = InlineKeyboardButton('🛒 Товари', callback_data='products')
go_to_site = InlineKeyboardButton('🌐 Перейти на сайт', url='https://rozetka.com.ua/ua/')
contacts = InlineKeyboardButton('☎ Контактні дані', callback_data='contacts')

kb_user = InlineKeyboardMarkup()
kb_user.add(products).add(go_to_site).insert(contacts)

#Create Button for back to main menu
main_menu = InlineKeyboardButton('Головне меню', callback_data='menu')

kb_contacts = InlineKeyboardMarkup()
kb_contacts.row(products, go_to_site).add(main_menu)

#Create Inline Butons for chousing category of products
phones = InlineKeyboardButton('Смартфони', callback_data='phone')
tablets = InlineKeyboardButton('Планшети', callback_data='tablet')
laptops = InlineKeyboardButton('Ноутбуки', callback_data='laptop')
other = InlineKeyboardButton('Інше', callback_data='other')

kb_categories = InlineKeyboardMarkup()
kb_categories.row(phones, tablets).row(laptops, other).add(main_menu)

#Create Button BACK on one step
back = InlineKeyboardButton('До категорій', callback_data='back')

kb_prod = InlineKeyboardMarkup()
kb_prod.add(back).add(main_menu)


