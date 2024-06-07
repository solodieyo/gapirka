import asyncio
import logging

from aiogram import Bot, Dispatcher


from app.src.main.setups.setup_bot import setup_bot
from app.src.main.setups.setup_dp import setup_dispatcher
from app.src.config.config import AppConfig, load_config
from app.src.main.setups.setup_log import setup_logging


async def main() -> None:
	config: AppConfig = load_config(AppConfig)

	setup_logging()
	bot: Bot = setup_bot(token=config.tg.token)
	dp: Dispatcher = setup_dispatcher(config=config)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		logging.info("Bot stopped!")