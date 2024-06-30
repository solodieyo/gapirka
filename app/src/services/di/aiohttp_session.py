from dishka import provide, Provider, Scope
from aiohttp import ClientSession


class AiohttpProvider(Provider):
	scope = Scope.APP

	@provide
	async def get_aiohttp_session(self) -> ClientSession:
		async with ClientSession() as session:
			return session
