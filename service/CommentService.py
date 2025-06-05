from typing import Optional

from domain.comment.AuthorId import AuthorId
from domain.comment.Comment import Comment
from domain.comment.CommentId import CommentId
from domain.comment.CommentText import CommentText
from repository.comment import CommentRepository as repository


def get_all() -> list[Comment]:
    return repository.get_all_comments()


def get_one(comment_id: str) -> Optional[Comment]:
    return repository.get_comment(CommentId(comment_id))


def add_comment(author_id: str, text: str) -> Comment:
    comment = Comment.new(AuthorId(author_id), CommentText(text))
    repository.create_comment(comment)
    return repository.get_comment(comment.comment_id)


def delete(comment_id: str) -> None:
    repository.delete_comment(CommentId(comment_id))
