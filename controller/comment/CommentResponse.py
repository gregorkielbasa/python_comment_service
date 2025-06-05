from pydantic import BaseModel


class CommentResponse(BaseModel):
    comment_id: str
    author_id: str
    text: str
