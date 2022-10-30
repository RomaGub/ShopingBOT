from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Create admin Inline Butons and Markup in admin control panel
add_prod = InlineKeyboardButton('🆕 Додати продукт', callback_data='add_prod')
del_prod = InlineKeyboardButton('🗑️ Видалити продукт', callback_data='del_prod')
main_menu = InlineKeyboardButton('Головне меню', callback_data='menu')

kb_admin = InlineKeyboardMarkup()
kb_admin.row(add_prod, del_prod).add(main_menu)

#Create Buttons for admin chouse a way of countinue
admin_panel = InlineKeyboardButton('Панель адміністратора', callback_data='admin_panel')
user_panel = InlineKeyboardButton('Панель користувача', callback_data='user_panel')

kb_ch_panel = InlineKeyboardMarkup()
kb_ch_panel.row(admin_panel, user_panel)

#BACK BUTTON on 1 step(like button in user keyboards)
back = InlineKeyboardButton('Повернутися назад', callback_data='back_adm')

kb_del = InlineKeyboardMarkup()
kb_del.add(back).add(main_menu)