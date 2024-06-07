import aiohttp

from app.src.config.config import AppConfig
from app.src.services.dota_api.profile_menu import SteamClient, DotaClient


async def get_pugach_menu_text(config: AppConfig, steam_id: int) -> str:
	async with aiohttp.ClientSession() as session:
		steam_client = SteamClient(
			session=session,
			token=config.steam.steam_api_key,
			steam_id=steam_id
		)

		response = await steam_client.get_profile()

		text = (
			f"'<b>PUGACH</b>\n\n"
			f"<a href='{response.response.players[0].avatarfull}'>Avatar</a>\n"
			f"<b>Username:</b> {response.response.players[0].personaname}\n"
			f""
		)
		game_playing = response.response.players[0].gameextrainfo
		text += f"<b>Game playing:</b> {game_playing}\n\n" if game_playing else ''

	response = await steam_client.get_recently_played_games()

	if response.response is not None:
		text += f"<b>Recently played games:</b>\n\n"
		data = response.response.games

		for game in data:
			text += (f'<a href="https://store.steampowered.com/app/{game.appid}">{game.name}</a>:'
					 f' <b>{round(int(game.playtime_2weeks) / 60, 2)} hours</b>\n')

	return text


async def get_dota_stats_text(steam_id32: int) -> str:
	async with aiohttp.ClientSession() as session:

		dota_client = DotaClient(
			session=session
		)

		response_player = await dota_client.get_player(steam_id32)
		response_wl = await dota_client.get_wl(steam_id32)
		response_last_match = await dota_client.get_last_match(steam_id32)[0]

		text = (
			f"<a href='https://steamcommunity.com/profiles/{response_player.profile.steamid}/'>"
			f"{response_player.profile.personaname}:</a>\n\n"
			f"<b>Dota2 rang</b>: {response_player.profile.leaderboard_rank}\n"
			f"<b>W/L</b>: {response_wl.win}/{response_wl.lose}\n"
			f"\n\n<b>Last match</b>: <b>{response_last_match.win}</b>\n"
			f"<b>Duration:</b> {round(int(response_last_match.duration) / 60, 2)}\n"
			f"<b>KDA</b> {response_last_match.kills}/{response_last_match.deaths}/{response_last_match.assists}\n"
		)

	return text
