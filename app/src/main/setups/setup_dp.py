from aiogram import Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from app.src.bot.handlers import setup_routers
from app.src.config.config import AppConfig
from app.src.main.setups.setup_middlware import _setup_outer_middleware, _setup_inner_middleware


def setup_dispatcher(config: AppConfig) -> Dispatcher:
	redis = Redis(
		host=config.redis.host,
		port=config.redis.port,
		decode_responses=True
	)

	storage = RedisStorage(
		redis=redis,
		key_builder=DefaultKeyBuilder(
			with_destiny=True,
			with_bot_id=True
		)
	)

	dp = Dispatcher(storage=storage)
	dp.workflow_data.update(
		config=config,
		redis=redis
	)

	dp.include_router(setup_routers())
	_setup_outer_middleware(dispatcher=dp, config=config)
	_setup_inner_middleware(dispatcher=dp, config=config)

	return dp