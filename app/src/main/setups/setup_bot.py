from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


def setup_bot(token: str) -> Bot:
	default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
	return Bot(
		token=token,
		default=default_properties
	)
