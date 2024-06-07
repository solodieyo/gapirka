from dataclass_rest import get
from dataclass_rest.http.aiohttp import ClientSession

from .base import AiohttpClient
from .models import ResponseSteam, WL, ResponseProfile, Match


class SteamClient(AiohttpClient):
	def __init__(
		self,
		session: ClientSession,
		token: str,
		steam_id: int,
	):
		super().__init__(
			query_params={'key': token, 'steamids': steam_id, "steamid": steam_id},
			base_url='http://api.steampowered.com',
			session=session
		)

	@get("/ISteamUser/GetPlayerSummaries/v0002/")
	async def get_profile(self) -> ResponseSteam:
		pass

	@get("/IPlayerService/GetRecentlyPlayedGames/v0001/")
	async def get_recently_played_games(self) -> ResponseSteam:
		pass


class DotaClient(AiohttpClient):
	def __init__(
		self,
		session: ClientSession,
	):
		super().__init__(
			base_url='https://api.opendota.com/api/players/',
			session=session
		)

	@get('{steam_id32}')
	async def get_player(self, steam_id32: int) -> ResponseProfile:
		pass

	@get("{steam_id32}/wl")
	async def get_wl(self, steam_id32: int) -> WL:
		pass

	@get("{steam_id32}/matches?limit=1")
	async def get_last_match(self, steam_id32: int) -> list[Match]:
		pass