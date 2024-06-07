import os
import tomllib
from pathlib import Path
from typing import TypeVar
from dataclasses import dataclass

from adaptix import Retort
from sqlalchemy import URL

T = TypeVar("T")
DEFAULT_CONFIG_PATH = r"C:\Users\SOLO\2to3\gapirka\app\config.toml"


def read_toml(path: Path) -> dict:
	with Path.open(path, "rb") as f:
		return tomllib.load(f)


@dataclass
class Tg:
	token: str
	admin_id: int
	log_channel_id: int


@dataclass
class Steam:
	pugach_steam_id: int
	pugach_steam_id32: int
	steam_api_key: str


@dataclass
class Postgres:
	database: str
	user: str
	password: str
	host: str
	port: int

	def build_dsn(self) -> URL:
		return URL.create(
			drivername="postgresql+asyncpg",
			username=self.user,
			password=self.password,
			host=self.host,
			port=self.port,
			database=self.database,
		)


@dataclass
class Redis:
	host: str
	port: int


@dataclass
class AppConfig:
	tg: Tg
	postgres: Postgres
	steam: Steam
	redis: Redis


def load_config(
	config_type: type[T],
	config_scope: str | None = None,
	path: Path | None = None,
) -> T:
	if path is None:
		path = Path(os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH))

	data = read_toml(path)

	if config_scope is not None:
		data = data[config_scope]

	dcf = Retort()
	return dcf.load(data, config_type)


if __name__ == "__main__":
	print(load_config(AppConfig))
