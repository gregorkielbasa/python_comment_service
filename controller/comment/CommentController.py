from typing import Optional
from fastapi import APIRouter, HTTPException
from controller.comment.CommentRequest import CommentRequest
from controller.comment.CommentResponse import CommentResponse
from domain.comment.Comment import Comment
from service import CommentService as comment_service

router: APIRouter = APIRouter(prefix="/comments")


@router.get("")
def get_all() -> list[CommentResponse]:
    result: list[Comment] = comment_service.get_all()
    return response_of_list(result)


@router.get("/{comment_id}")
def get_by_id(comment_id: str) -> CommentResponse:
    result: Optional[Comment] = comment_service.get_one(comment_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    else:
        return response_of_one(result)


@router.post("")
def create_comment(new_comment: CommentRequest) -> CommentResponse:
    result: Comment = comment_service.add_comment(new_comment.author_id, new_comment.text)
    return response_of_one(result)


@router.delete("/{comment_id}")
def delete_by_id(comment_id: str) -> None:
    comment_service.delete(comment_id)


def response_of_one(comment: Comment) -> CommentResponse:
    comment_id = str(comment.comment_id.value)
    author_id = str(comment.author_id.value)
    text = str(comment.text.value)
    return CommentResponse(comment_id=comment_id, author_id=author_id, text=text)


def response_of_list(comments: list[Comment]) -> list[CommentResponse]:
    result = []
    for comment in comments:
        result.append(response_of_one(comment))
    return result
