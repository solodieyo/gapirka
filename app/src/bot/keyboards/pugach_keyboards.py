from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def pugach_menu_keyboard():
	keyboard = InlineKeyboardMarkup(
		inline_keyboard=[
			[InlineKeyboardButton(text='Dota', callback_data='pugachdoto')],
			[InlineKeyboardButton(text="Match", callback_data='match')],

		]
	)
	return keyboard


def back_pugach():
	keyboard = InlineKeyboardMarkup(
		inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='back_')]
		]
	)
	return keyboard