from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

Base = declarative_base()


class CommentEntity(Base):
    __tablename__ = "comments"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    author_id: Mapped[str] = mapped_column(String(36))
    text: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return ("CommentEntity(id={}, author_id={} text={})"
                .format(self.id, self.author_id, self.text))
