from io import BytesIO

from aiogram import Bot
from freeGPT import AsyncClient
from PIL import Image

from app.src.config.config import AppConfig


async def prodia_request(prompt: str, bot: Bot, config: AppConfig) -> str:
	try:
		response = await AsyncClient.create_generation(
			model="prodia",
			prompt=prompt
		)
		Image.open(BytesIO(response)).save("./gtp_photos/image.png")

	# преобразовать фото

	except Exception as e:
		await bot.send_message(
			chat_id=config.tg.log_channel_id,
			text=(f"<b>PRODIA error:</b>\n\n"
				 f"{e}"),
		)
