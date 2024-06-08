from sqlalchemy import select, func

from app.src.services.db.models import Photos
from app.src.services.db.reposirories import BaseRepository


class PhotoRepository(BaseRepository):

	async def add_photo(self, photo: str) -> None:
		photo = Photos(
			photo=photo
		)
		self.session.add(photo)
		await self.session.commit()

	async def get_photo(self) -> str:
		result = await self.session.scalar(select(Photos.photo).order_by(func.random()).limit(1))
		return result