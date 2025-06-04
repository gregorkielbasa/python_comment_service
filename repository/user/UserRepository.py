import uuid
from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from domain.user.User import User
from domain.user.UserId import UserId
from domain.user.UserName import UserName
from repository.user.UserEntity import UserEntity

__engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/haeger_db", echo=False)


def get_all_users() -> list[User]:
    session = Session(__engine)
    statement = select(UserEntity)
    result: list[User] = map_list_to_domain(session.scalars(statement))
    session.close()
    return result


def get_user(user_id: UserId) -> Optional[User]:
    session = Session(__engine)
    statement = select(UserEntity).where(UserEntity.id == str(user_id.value))
    result: User = map_one_to_domain(session.scalar(statement))
    session.close()
    return result


def create_user(domain: User) -> None:
    session = Session(__engine)
    session.add(map_to_entity(domain))
    session.commit()
    session.close()


def delete_user(user_id: UserId) -> None:
    session = Session(__engine)
    statement = select(UserEntity).where(UserEntity.id == str(user_id.value))
    entity: Optional[User] = session.scalar(statement)
    if entity is not None:
        session.delete(entity)
        session.commit()
    session.close()


def map_one_to_domain(entity: Optional[UserEntity]) -> Optional[User]:
    if entity is None:
        return None
    user_id = UserId(uuid.UUID(entity.id))
    user_name = UserName(entity.first_name, entity.last_name)
    return User(user_id, user_name)


def map_list_to_domain(entities) -> list[User]:
    result: list[User] = []
    for entity in entities:
        result.append(map_one_to_domain(entity))
    return result


def map_to_entity(domain: User) -> UserEntity:
    user_id = str(domain.user_id.value)
    user_first_name = domain.username.first_name
    user_last_name = domain.username.last_name
    return UserEntity(id=user_id, first_name=user_first_name, last_name=user_last_name)
