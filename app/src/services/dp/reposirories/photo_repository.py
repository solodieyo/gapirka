from app.src.services.dp.models import Photos
from app.src.services.dp.reposirories import BaseRepository


class PhotoRepository(BaseRepository):

	async def add_photo(self, photo: str):
		photo = Photos(
			photo=photo
		)
		self.session.add(photo)
		await self.session.commit()