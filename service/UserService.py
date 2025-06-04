from typing import Optional

from domain.user.User import User
from domain.user.UserId import UserId
from domain.user.UserName import UserName
from repository.user import UserRepository as repository


def get_all() -> list[User]:
    return repository.get_all_users()


def get_one(user_id: str) -> Optional[User]:
    return repository.get_user(UserId(user_id))


def add_user(user_name: str) -> User:
    user = User.new(UserName(user_name))
    repository.create_user(user)
    return repository.get_user(user.user_id)


def delete(user_id: str) -> None:
    repository.delete_user(UserId(user_id))