from aiogram import Dispatcher
from dishka import AsyncContainer

from app.src.bot.middleware.user_middleware import UserMiddleware
from app.src.config.config import AppConfig
from app.src.services.db.base import create_pool


def _setup_outer_middleware(dispatcher: Dispatcher, dishka: AsyncContainer) -> None:
	dispatcher.message.outer_middleware(UserMiddleware(dishka=dishka))


def _setup_inner_middleware(dispatcher: Dispatcher, config: AppConfig) -> None:
	pass