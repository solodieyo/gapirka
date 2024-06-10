import asyncio
import logging

from aiogram import Bot, Dispatcher
from dishka.integrations.aiogram import setup_dishka

from app.src.config.config import AppConfig
from app.src.config.laod_config import load_config
from app.src.main.setups.main_factory import create_dishka
from app.src.main.setups.setup_log import setup_logging


async def main() -> None:

	setup_logging()
	config = load_config(AppConfig)
	dishka = create_dishka(config)
	bot: Bot = await dishka.get(Bot)
	dp: Dispatcher = await dishka.get(Dispatcher)

	try:
		setup_dishka(router=dp, auto_inject=True, container=dishka)
		await bot.delete_webhook(drop_pending_updates=True)
		await dp.start_polling(bot)
	finally:
		await dishka.close()


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		logging.info("Bot stopped!")
