from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from sqlalchemy import Integer, String

class Document(Base):
    __tablename__ = "documents"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    filename:Mapped[str]
