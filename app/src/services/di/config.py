from dishka import provide, Scope, Provider

from app.src.config.config import AppConfig
from app.src.config.laod_config import load_config


class ConfigProvider(Provider):
	scope = Scope.APP

	@provide
	def get_config(self) -> AppConfig:
		return load_config(AppConfig)
