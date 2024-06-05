import os

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, FSInputFile

from app.src.config.config import AppConfig
from app.src.services.ai.gpt_request import gtp_request
from app.src.services.ai.prodia_request import prodia_request

router = Router()


@router.message(Command("gpt"))
async def gpt_prompt_handler(message: Message, bot: Bot, config: AppConfig, command: CommandObject):
	response = await gtp_request(
		prompt=command.args,
		bot=bot,
		config=config
	)
	await message.reply(response)


@router.message(Command("photo"))
async def prodia_prompt_handler(message: Message, bot: Bot, config: AppConfig):
	await prodia_request(
		prompt=message.text,
		bot=bot,
		config=config
	)

	photo = FSInputFile('./gtp_photos/image.png')
	await bot.send_photo(
		chat_id=message.chat.id,
		photo=photo
	)

	os.remove('./gtp_photos/image.png')