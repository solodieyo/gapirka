from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
	create_async_engine,
	AsyncEngine,
	AsyncSession,
	async_sessionmaker
)


def create_pool(dsn: str | URL, echo: bool = False) -> async_sessionmaker[AsyncSession]:
	engine: AsyncEngine = create_async_engine(dsn, echo=echo)
	return async_sessionmaker(engine, expire_on_commit=False)
