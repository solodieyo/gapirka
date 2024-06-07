from dataclasses import dataclass

from sqlalchemy import URL


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


