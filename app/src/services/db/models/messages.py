from sqlalchemy.orm import Mapped, mapped_column

from app.src.services.db.models import Base
from app.src.services.db.models.base import Int16, Int64


class Messages(Base):

	__tablename__ = "messages"

	id: Mapped[Int16] = mapped_column(primary_key=True)
	message_text: Mapped[str]