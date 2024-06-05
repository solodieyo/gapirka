from aiogram import Bot
from freeGPT import AsyncClient

from app.src.config.config import AppConfig


async def gtp_request(prompt: str, bot: Bot, config: AppConfig) -> str:
	try:
		response = await AsyncClient.create_completion(
			model="gpt3",
			prompt=prompt
		)
		return response
	except Exception as e:
		await bot.send_message(
			chat_id=config.tg.log_channel_id,
			text=(f"<b>GPT error:</b>\n\n"
				 f"{e}"),
		)
