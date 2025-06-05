from pydantic import BaseModel


class CommentRequest(BaseModel):
    author_id: str
    text: str
