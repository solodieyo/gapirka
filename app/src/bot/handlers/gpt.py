from contextlib import suppress
from os import remove

from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, FSInputFile
from dishka import FromDishka

from app.src.config.config import AppConfig
from app.src.services.ai.gpt_request import gtp_request
from app.src.services.ai.prodia_request import prodia_request

router = Router()


@router.message(Command("gpt"))
async def gpt_prompt_handler(message: Message, bot: Bot, config: FromDishka[AppConfig], command: CommandObject):
	try:
		response = await gtp_request(
			prompt=command.args,
		)
		await message.reply(response)
	except Exception as e:
		await bot.send_message(
			chat_id=config.tg.log_channel_id,
			text=(f"<b>GPT error:</b>\n\n"
				  f"{e}"),
		)


@router.message(Command("photo"))
async def prodia_prompt_handler(message: Message, bot: Bot, config: FromDishka[AppConfig], command: CommandObject):
	try:
		await prodia_request(
			prompt=command.args,
		)
		photo = FSInputFile('image.jpeg')
		await message.reply_photo(photo=photo)
	except Exception as e:
		await bot.send_message(
			chat_id=config.tg.log_channel_id,
			text=(f"<b>PRODIA error:</b>\n\n"
				  f"{e}"),
		)
	finally:
		with suppress(FileNotFoundError):
			remove('image.png')
