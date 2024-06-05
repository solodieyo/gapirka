import os
import tomllib
from pathlib import Path
from typing import TypeVar
from dataclasses import dataclass

from adaptix import Retort

T = TypeVar("T")
DEFAULT_CONFIG_PATH = "./config.toml"


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
