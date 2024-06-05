from sqlalchemy.orm import Mapped, mapped_column

from app.src.services.dp.models import Base


class Photos(Base):
	__tablename__ = 'photos'

	id: Mapped[int] = mapped_column(primary_key=True)
	photo: Mapped[str]
