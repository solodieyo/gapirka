from typing import Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from app.src.services.dp.models import User
from app.src.services.dp.reposirories import GeneralRepository


class UserMiddleware(BaseMiddleware):

	async def __call__(
		self,
		handler: Callable[[TelegramObject, dict[str, any]], Awaitable[Any]],
		event: Message,
		data: dict[str: Any]
	):

		repo: GeneralRepository = data['repo']
		user: User = await repo.user.get_user(user_id=event.from_user.id, username=event.from_user.username)

		data['user'] = user

		return await handler(event, data)