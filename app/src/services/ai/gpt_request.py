from aiogram import Bot
from freeGPT import AsyncClient

from app.src.config.config import AppConfig


async def gtp_request(prompt: str) -> str:
	response = await AsyncClient.create_completion(
		model="gpt3",
		prompt=prompt
	)
	return response
