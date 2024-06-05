from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.src.services.dp.reposirories import GeneralRepository

router = Router()


@router.message(Command('stats'))
async def stats(message: Message, repo: GeneralRepository):
	message_count = await repo.user.get_message_count(
		user_id=message.from_user.id
	)

	await message.answer(
		f'<a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>\n'
		f'<b>id:</b> {message.from_user.id}\n\n'
		f'<b>Кол-во сообщений:</b> {message_count}\n'
	)