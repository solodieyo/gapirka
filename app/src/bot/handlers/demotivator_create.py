from contextlib import suppress
from os import remove

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, File, FSInputFile
from demotivator import demotivate
from dishka import FromDishka

from app.src.config.config import AppConfig
from app.src.services.db.reposirories import GeneralRepository

router = Router()


@router.message(Command('d'))
async def d(message: Message, repo: FromDishka[GeneralRepository], bot: Bot, config: FromDishka[AppConfig]):
	try:
		message_text = await repo.messages.get_message()
		photo_id = await repo.photos.get_photo()

		file: File = await bot.get_file(file_id=photo_id)
		await bot.download_file(file.file_path, "photo.jpeg")

		demotivate(
			"photo.jpeg",
			font='Roboto-Regular.ttf',
			caption=message_text
		).save('photo.jpeg')
		file_dem: FSInputFile = FSInputFile("photo.jpeg")

		await message.reply_photo(
			photo=file_dem
		)
	except Exception as e:
		await bot.send_message(
			chat_id=config.tg.log_channel_id,
			text=str(e)
		)
	finally:
		with suppress(FileNotFoundError):
			remove('photo.jpeg')
