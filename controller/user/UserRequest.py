from pydantic import BaseModel


class UserRequest(BaseModel):
    user_first_name: str
    user_last_name: str
