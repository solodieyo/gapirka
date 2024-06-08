from dataclasses import dataclass

from dishka import Provider, provide, Scope
from adaptix import Retort

from .heroes import heroes as data


@dataclass
class HeroesData:
	heroes: list


class HeroesDataProvider(Provider):
	scope = Scope.APP

	@provide
	def get_dota_api(self) -> HeroesData:
		retort = Retort()
		heroes: HeroesData = retort.load(data, HeroesData)
		return heroes
