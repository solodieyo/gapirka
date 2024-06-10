from typing import Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from dishka import AsyncContainer

from app.src.services.db.models import User
from app.src.services.db.reposirories import GeneralRepository


class UserMiddleware(BaseMiddleware):

	def __init__(self, dishka: AsyncContainer):
		super().__init__()
		self.dishka = dishka

	async def __call__(
		self,
		handler: Callable[[TelegramObject, dict[str, any]], Awaitable[Any]],
		event: Message,
		data: dict[str: Any]
	):
		async with self.dishka() as req_dishka:
			repo = await req_dishka.get(GeneralRepository)
			user: User = await repo.user.get_user(user_id=event.from_user.id, username=event.from_user.username)

		data['user'] = user

		return await handler(event, data)