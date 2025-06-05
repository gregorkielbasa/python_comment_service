import uuid
from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from domain.comment.AuthorId import AuthorId
from domain.comment.Comment import Comment
from domain.comment.CommentId import CommentId
from domain.comment.CommentText import CommentText
from repository.comment.CommentEntity import CommentEntity

__engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/haeger_db", echo=False)


def get_all_comments() -> list[Comment]:
    session = Session(__engine)
    statement = select(CommentEntity)
    result: list[Comment] = map_list_to_domain(session.scalars(statement))
    session.close()
    return result


def get_comment(comment_id: CommentId) -> Optional[Comment]:
    session = Session(__engine)
    statement = select(CommentEntity).where(CommentEntity.id == str(comment_id.value))
    result: Comment = map_one_to_domain(session.scalar(statement))
    session.close()
    return result


def create_comment(domain: Comment) -> None:
    session = Session(__engine)
    session.add(map_to_entity(domain))
    session.commit()
    session.close()


def delete_comment(comment_id: CommentId) -> None:
    session = Session(__engine)
    statement = select(CommentEntity).where(CommentEntity.id == str(comment_id.value))
    entity: Optional[Comment] = session.scalar(statement)
    if entity is not None:
        session.delete(entity)
        session.commit()
    session.close()


def map_one_to_domain(entity: Optional[CommentEntity]) -> Optional[Comment]:
    if entity is None:
        return None
    comment_id = CommentId(uuid.UUID(entity.id))
    author_id = AuthorId(entity.author_id)
    text = CommentText(entity.text)
    return Comment(comment_id, author_id, text)


def map_list_to_domain(entities) -> list[Comment]:
    result: list[Comment] = []
    for entity in entities:
        result.append(map_one_to_domain(entity))
    return result


def map_to_entity(domain: Comment) -> CommentEntity:
    comment_id = str(domain.comment_id.value)
    author_id = str(domain.author_id.value)
    comment_text = str(domain.text.value)
    return CommentEntity(id=comment_id, author_id=author_id, text=comment_text)
