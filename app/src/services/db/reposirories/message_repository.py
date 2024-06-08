import random
from typing import Optional

from sqlalchemy import select, func, delete

from app.src.services.db.models import Messages
from app.src.services.db.reposirories import BaseRepository


class MessageRepository(BaseRepository):

	async def add_message(self, text: str) -> None:
		message = Messages(
			message_text=text
		)
		self.session.add(message)
		await self.session.commit()

	async def get_message(self) -> str:
		result: Optional[str] = await self.session.scalar(select(Messages.message_text).order_by(func.random()).limit(1))
		if result and len(result.strip()) > 30:
			words = result.split()
			text = words[random.randint(0, len(words) - 2):]
			return ' '.join(text)

		if result:
			await self.session.execute(delete(Messages).where(Messages.message_text == result))
			await self.session.commit()
			return result
		return "Гапирня, гапирочка, гапирка"