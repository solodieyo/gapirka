from typing import Callable, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.src.services.dp.reposirories.general_repository import GeneralRepository


class RepositoryMiddleware(BaseMiddleware):
	pool: async_sessionmaker[AsyncSession]

	def __init__(self, session_pool: async_sessionmaker[AsyncSession]):
		self.pool = session_pool

	async def __call__(
		self,
		handler: Callable[[TelegramObject, dict[str, any]], Awaitable[Any]],
		event: TelegramObject,
		data: dict[str, Any],
	):
		async with self.pool() as session:
			data['repo'] = GeneralRepository(session=session)
			return await handler(event, data)
