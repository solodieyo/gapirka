from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.src.services.dp.models.base import TimestampMixin, Base, Int16, Int64


class User(Base, TimestampMixin):

	__tablename__ = "users"

	id: Mapped[Int16] = mapped_column(primary_key=True)
	user_id: Mapped[Int64]
	archive: Mapped[bool] = mapped_column(default=False)
	username: Mapped[Optional[str]]
	message_count: Mapped[Int16] = mapped_column(default=0)
