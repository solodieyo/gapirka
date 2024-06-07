from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from app.src.services.dota_api.get_pugach_text import get_dota_stats_text

router = Router()


@router.message(Command('find'))
async def find(message: Message, command: CommandObject):
	message_text = await get_dota_stats_text(steam_id32=int(command.args))
	await message.reply(text=message_text)
