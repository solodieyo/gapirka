from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from dishka import FromDishka

from app.src.services.di.api import HeroesData
from app.src.services.dota_api.get_pugach_text import get_dota_stats_text

router = Router()


@router.message(Command('find'))
async def find(message: Message, command: CommandObject, heroes: FromDishka[HeroesData]):
	message_text = await get_dota_stats_text(steam_id32=int(command.args), heroes=heroes)
	await message.reply(text=message_text)
