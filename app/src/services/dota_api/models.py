from dataclasses import dataclass
from typing import Union, Optional


@dataclass
class User:
	personaname: str
	avatarfull: str
	gameextrainfo: str | None = ""


@dataclass
class UserSearchResult:
	players: list[User]


@dataclass
class Game:
	appid: int
	name: str
	playtime_2weeks: int


@dataclass
class RecentlyPlayedGames:
	games: list[Game]


@dataclass
class ResponseSteam:
	response: Union[UserSearchResult, RecentlyPlayedGames]


@dataclass
class WL:
	win: int
	lose: int


@dataclass
class Match:
	match_id: int
	duration: int
	hero_id: int
	kills: int
	deaths: int
	assists: int
	radiant_win: bool
	player_slot: int = 0
	party_size: Optional[int] = None
	side = "radiant" if player_slot < 128 else "dire"

	@property
	def win(self) -> str:
		match self.side:
			case "radiant":
				return 'Win' if self.radiant_win else "Loss"
			case "dire":
				return 'Win' if not self.radiant_win else "Loss"


@dataclass
class Profile:
	account_id: int
	personaname: str
	plus: bool
	cheese: int
	steamid: str
	avatar: str
	avatarmedium: str
	avatarfull: str
	profileurl: str
	fh_unavailable: bool
	is_contributor: bool
	is_subscriber: bool | None
	name: str | None = None
	last_login: str | None = None
	loccountrycode: str | None = None
	status: str | None = None
	leaderboard_rank: str | int | None = None


@dataclass
class ResponseProfile:
	profile: Profile
