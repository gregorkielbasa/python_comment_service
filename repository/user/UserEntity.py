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

    def __repr__(self):
        return "UserEntity(id={}, first_name={} last_name={})".format(self.id, self.firs_tname, self.last_tname)
