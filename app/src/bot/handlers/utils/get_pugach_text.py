import aiohttp

from app.src.config.config import AppConfig


async def get_pugach_menu_text(config: AppConfig) -> str:

	text: str = '<b>PUGACH</b>\n\n'

	async with aiohttp.ClientSession() as session:
		async with session.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
							   f'?key={config.steam.steam_api_key.get_secret_value()}&steamids='
							   f'{config.steam.pugach_steam_id}') as response:

			data = await response.json()
			data = data['response']['players'][0]

			text += f"<a href='{data['avatarfull']}'>Avatar</a>\n"
			text += f"<b>Username:</b> {data['personaname']}\n"

			game_playing = data.get('gameextrainfo', '')
			text += f"<b>Game playing:</b> {game_playing}\n\n" if game_playing else ''

		async with session.get(f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key='
							   f'{config.steam.steam_api_key.get_secret_value()}'
							   f'&steamid={config.steam.pugach_steam_id}&format=json') as response:

			data = await response.json()

			for game in data['response']['games']:
				text += (f'<a href="https://store.steampowered.com/app/{game["appid"]}">{game["name"]}</a>:'
						 f' <b>{round(int(game['playtime_2weeks']) / 60, 2)} hours</b>\n')
	return text


async def get_dota_stats_text(steam_id32: int) -> str:

	text: str = ''

	async with aiohttp.ClientSession() as session:
		async with session.get(f'https://api.opendota.com/api/players/{steam_id32}') as response:
			data = await response.json()
			text += (f"<a href='https://steamcommunity.com/profiles/{data['profile']['steamid']}/'>"
					 f"{data['profile']['personaname']}:</a>\n\n")
			text += f"<b>Dota2 rang</b>: {data['leaderboard_rank']}\n"

		async with session.get(f"https://api.opendota.com/api/players/{steam_id32}/wl") as response:
			data = await response.json()
			text += f"<b>W/L</b>: {data['win']}/{data['lose']}\n"

		async with session.get(f"https://api.opendota.com/api/players/{steam_id32}/matches?limit=1") as response:
			data = await response.json()
			side = "radiant" if data[0]['player_slot'] < 128 else "dire"
			if side == 'radiant' and data[0]['radiant_win']:
				match_won = 'Win'
			elif side == 'dire' and data[0]['radiant_win']:
				match_won = 'Lose'
			elif side == 'dire' and not data[0]['radiant_win']:
				match_won = 'Win'
			else:
				match_won = 'Lose'
			text += f"\n\n<b>Last match</b>: <b>{match_won}</b>\n"
			text += f"<b>Duration:</b> {round(int(data[0]['duration']) / 60, 2)}\n"
			text += f"<b>KDA</b> {data[0]['kills']}/{data[0]['deaths']}/{data[0]['assists']}\n"

	return text