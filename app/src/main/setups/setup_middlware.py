from aiogram import Dispatcher

from app.src.bot.middleware.repository_middleware import RepositoryMiddleware
from app.src.config.config import AppConfig
from app.src.services.dp.base import create_pool


def _setup_outer_middleware(dispatcher: Dispatcher, config: AppConfig) -> None:
	# pool = dispatcher['session_pool'] = create_pool(config.postgres.build_dsn())
	# dispatcher.update.outer_middleware(RepositoryMiddleware(session_pool=pool))
	pass

def _setup_inner_middleware(dispatcher: Dispatcher, config: AppConfig) -> None:
	pass