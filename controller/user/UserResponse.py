from pydantic import BaseModel


class UserResponse(BaseModel):
    user_id: str
    user_name: str
