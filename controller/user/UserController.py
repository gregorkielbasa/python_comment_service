from typing import Optional

from fastapi import APIRouter, HTTPException

from controller.user.UserRequest import UserRequest
from controller.user.UserResponse import UserResponse
from domain.user.User import User
from service import UserService as user_service

router: APIRouter = APIRouter(prefix="/users")


@router.get("")
def get_all() -> list[UserResponse]:
    result: list[User] = user_service.get_all()
    return response_of_list(result)


@router.get("/{user_id}")
def get_by_id(user_id: str) -> UserResponse:
    result: Optional[User] = user_service.get_one(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return response_of_one(result)


@router.post("")
def create_user(neu_user: UserRequest) -> UserResponse:
    result: User = user_service.add_user(neu_user.user_first_name, neu_user.user_last_name)
    return response_of_one(result)


@router.delete("/{user_id}")
def delete_by_id(user_id: str) -> None:
    user_service.delete(user_id)


def response_of_one(user: User) -> UserResponse:
    user_id = str(user.user_id.value)
    user_name = user.username.first_name + " " + user.username.last_name
    user_email = user.email.value
    return UserResponse(user_id=user_id, user_name=user_name, user_email=user_email)


def response_of_list(users: list[User]) -> list[UserResponse]:
    result = []
    for user in users:
        result.append(response_of_one(user))
    return result
