from aiogram import Router

from .start import router as start_router
from .gpt import router as gpt_router
from .default import default_router
from .get_player import router as get_player_router
from .pugach import router as pugach_router
from .demotivator_create import router as demotivator_create_router


def setup_routers():
	router = Router()
	router.include_router(start_router)
	router.include_router(gpt_router)
	router.include_router(pugach_router)
	router.include_router(get_player_router)
	router.include_router(demotivator_create_router)
	router.include_router(default_router)
	return router
