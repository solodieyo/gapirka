from app.src.services.dp.models import Messages
from app.src.services.dp.reposirories import BaseRepository


class MessageRepository(BaseRepository):

	async def add_message(self, text: str):
		message = Messages(
			message_text=text
		)
		self.session.add(message)
		await self.session.commit()