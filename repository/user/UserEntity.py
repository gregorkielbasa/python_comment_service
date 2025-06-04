from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

Base = declarative_base()


class UserEntity(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25))
    last_name: Mapped[str] = mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(60))

    def __repr__(self):
        return ("UserEntity(id={}, first_name={} last_name={} email={})"
                .format(self.id, self.first_name, self.last_name, self.email))
