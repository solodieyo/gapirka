from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiohttp import ClientSession
from dishka import FromDishka
from dishka.integrations.aiohttp import inject

from app.src.services.di.api import HeroesData
from app.src.services.dota_api.get_pugach_text import get_pugach_menu_text, get_dota_stats_text
from app.src.bot.keyboards.pugach_keyboards import pugach_menu_keyboard, back_pugach
from app.src.config.config import AppConfig

router = Router()


# ТУТ ПЕРЕДЕЛАТЬ ВСЕ.


@router.message(Command('pugach'))
async def pugach_menu(message: Message, config: FromDishka[AppConfig], session: FromDishka[ClientSession]):
	message_text = await get_pugach_menu_text(config=config, steam_id=config.steam.pugach_steam_id, session=session)
	await message.answer(message_text, reply_markup=pugach_menu_keyboard(), disable_web_page_preview=True)


@router.callback_query(F.data == 'pugachdoto')
async def pugach_dota(callback: CallbackQuery, config: FromDishka[AppConfig], heroes: FromDishka[HeroesData],
					  session: FromDishka[ClientSession]):
	text = await get_dota_stats_text(steam_id32=config.steam.pugach_steam_id32, heroes=heroes, session=session)
	await callback.message.edit_text(text=text, reply_markup=back_pugach(), disable_web_page_preview=True)


@router.callback_query(F.data == "back_")
async def back_pugach_handler(callback: CallbackQuery, config: FromDishka[AppConfig],
							  session: FromDishka[ClientSession]):
	message_text = await get_pugach_menu_text(config=config, steam_id=config.steam.pugach_steam_id, session=session)
	await callback.message.edit_text(
		text=message_text,
		reply_markup=pugach_menu_keyboard(),
		disable_web_page_preview=True
	)
