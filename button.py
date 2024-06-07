from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='uzbek', callback_data='uzbek'),
     InlineKeyboardButton(text='turk ', callback_data='turk'),
     InlineKeyboardButton(text="rus", callback_data='rus'),
     InlineKeyboardButton(text="xorazm", callback_data='xorazm')],

])