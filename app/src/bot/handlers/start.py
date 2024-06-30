import datetime

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka import FromDishka

from app.src.services.db.reposirories import GeneralRepository

router = Router()


@router.message(CommandStart())
async def start(message: Message, repository: FromDishka[GeneralRepository]):
	users = await repository.user.get_count_users_per_date(selected_date=datetime.date(2024, 6, 9))
	await message.answer(f'{users}')