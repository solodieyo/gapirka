from typing import AsyncIterable

from dishka import Provider, Scope, provide, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.src.config.config import AppConfig
from app.src.services.db.base import create_pool
from app.src.services.db.reposirories import GeneralRepository


class DbProvider(Provider):
	scope = Scope.APP

	config = from_context(scope=Scope.APP, provides=AppConfig)

	@provide
	def get_pool(self, config: AppConfig) -> async_sessionmaker:
		return create_pool(dsn=config.postgres.build_dsn())

	@provide(scope=Scope.REQUEST)
	async def get_session(self, pool: async_sessionmaker) -> AsyncIterable[AsyncSession]:
		async with pool() as session_pool:
			yield session_pool

	@provide(scope=Scope.REQUEST)
	async def get_db(self, session: AsyncSession) -> GeneralRepository:
		return GeneralRepository(session=session)
