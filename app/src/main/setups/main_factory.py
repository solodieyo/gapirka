from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage, DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from dishka import Provider, Scope, provide, make_async_container, AsyncContainer
from redis.asyncio import Redis

from app.src.bot.handlers import setup_routers
from app.src.config.config import AppConfig
from app.src.main.setups.setup_middlware import _setup_outer_middleware
from app.src.services.di.api import HeroesDataProvider
from app.src.services.di.bot import BotProvider
from app.src.services.di.config import ConfigProvider
from app.src.services.di.db import DbProvider


def create_dishka():
	container = make_async_container(*get_providers())
	return container


def get_providers():
	return [
		ConfigProvider(),
		DpProvider(),
		DbProvider(),
		BotProvider(),
		HeroesDataProvider()
	]


class DpProvider(Provider):
	scope = Scope.APP

	@provide
	def get_dispatcher(
		self,
		dishka: AsyncContainer,
		storage: BaseStorage,
	) -> Dispatcher:
		dp = Dispatcher(
			storage=storage
		)

		dp.include_routers(setup_routers())
		_setup_outer_middleware(dispatcher=dp, dishka=dishka)

		return dp

	@provide(scope=Scope.APP)
	def get_redis(self, config: AppConfig) -> Redis:
		return Redis(host=config.redis.host, port=config.redis.port)

	@provide(scope=Scope.APP)
	def get_storage(self, redis: Redis) -> BaseStorage:
		return RedisStorage(
			redis=redis,
			key_builder=DefaultKeyBuilder(
				with_destiny=True,
				with_bot_id=True
			)
		)
